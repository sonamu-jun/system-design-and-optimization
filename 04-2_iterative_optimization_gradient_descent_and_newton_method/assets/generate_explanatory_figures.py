"""Build focused diagrams beside the GD steps and Newton comparisons."""

from html import escape
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DEST = Path(__file__).resolve().parent
BLUE, TEAL, ORANGE, PURPLE, GRAY, INK = (
    "#2878b5", "#168578", "#d47a20", "#8854a5", "#707070", "#243344"
)
plt.rcParams.update({
    "font.size": 10.5, "axes.labelsize": 10.5, "svg.fonttype": "none",
    "svg.hashsalt": "iterative-explanations", "axes.spines.top": False,
    "axes.spines.right": False,
})


def save_plot(figure, name):
    path = DEST / name
    figure.savefig(path, metadata={"Date": None})
    path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines()) + "\n")
    plt.close(figure)


class Diagram:
    """Keep diagram lettering at the surrounding Markdown's approximate size."""

    def __init__(self, height, description):
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="520" height="{height}" '
            f'viewBox="0 0 520 {height}" role="img">',
            f'<title>{escape(description)}</title>',
            '<rect width="100%" height="100%" fill="white"/>',
            f'<g font-family="DejaVu Sans, sans-serif" font-size="14" fill="{INK}">',
        ]

    def text(self, x, y, value, color=INK, anchor="start"):
        self.parts.append(f'<text x="{x}" y="{y}" fill="{color}" '
                          f'text-anchor="{anchor}">{escape(value)}</text>')

    def line(self, x1, y1, x2, y2, color=GRAY, width=1.5, extra=""):
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                          f'stroke="{color}" stroke-width="{width}" {extra}/>')

    def box(self, x, y, width, height, color=GRAY, fill="white"):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
                          f'rx="7" stroke="{color}" fill="{fill}"/>')

    def arrow(self, x1, y1, x2, y2, color=GRAY):
        self.line(x1, y1, x2, y2, color, 1.8)
        dx, dy = x2-x1, y2-y1
        length = (dx*dx+dy*dy)**0.5
        ux, uy = dx/length, dy/length
        a = (x2-7*ux+4*uy, y2-7*uy-4*ux)
        b = (x2-7*ux-4*uy, y2-7*uy+4*ux)
        self.parts.append(f'<path d="M {a[0]},{a[1]} L {x2},{y2} L {b[0]},{b[1]}" '
                          f'fill="none" stroke="{color}" stroke-width="1.8"/>')

    def dot(self, x, y, color):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="4.5" fill="{color}"/>')

    def save(self, name):
        (DEST / name).write_text("\n".join(self.parts + ["</g></svg>"]) + "\n")


def errors_to_score():
    drawing = Diagram(218, "At correction zero, four signed errors are squared and added to give score 6.")
    drawing.text(16, 26, "q = 0 min", ORANGE)
    for i, error in enumerate([-2, -1, -1, 0]):
        x = 154 + i*89
        drawing.text(x+34, 26, f"i = {i+1}", GRAY, "middle")
        drawing.box(x, 44, 68, 38, "#d7dfe7", "#f5f7fa")
        drawing.text(x+34, 68, str(error).replace("-", "−"), INK, "middle")
        drawing.arrow(x+34, 87, x+34, 112)
        drawing.box(x, 119, 68, 38, BLUE, "#f2f7fb")
        drawing.text(x+34, 143, str(error**2), BLUE, "middle")
    drawing.text(16, 68, "Errors (min)")
    drawing.text(16, 104, "Square each", GRAY)
    drawing.text(16, 143, "Squared (min²)")
    drawing.text(16, 197, "Add all four", GRAY)
    drawing.text(326, 197, "4 + 1 + 1 + 0 = 6 min²", INK, "middle")
    drawing.save("errors_to_score.svg")


def gd_loop():
    drawing = Diagram(354, "GD evaluates and records, checks slope and update limit, then updates q and advances the iteration counter.")
    drawing.box(62, 8, 296, 34, BLUE, "#f2f7fb")
    drawing.text(210, 30, "q = start; k = 0", BLUE, "middle")
    drawing.arrow(210, 42, 210, 64)
    drawing.box(62, 64, 296, 58)
    drawing.text(210, 87, "Calculate score and slope", INK, "middle")
    drawing.text(210, 109, "Record k, q, score, slope", GRAY, "middle")
    drawing.arrow(210, 122, 210, 146)
    for y, check, reason in [(146, "Small slope?", "small slope"), (204, "Update limit?", "update limit")]:
        drawing.box(62, y, 296, 34, PURPLE, "#faf6fc")
        drawing.text(210, y+22, check, PURPLE, "middle")
        drawing.arrow(358, y+17, 395, y+17)
        drawing.text(377, y+8, "yes", GRAY, "middle")
        drawing.box(397, y-4, 112, 46, TEAL)
        drawing.text(453, y+15, "Stop", TEAL, "middle")
        drawing.text(453, y+33, reason, GRAY, "middle")
        drawing.arrow(210, y+34, 210, y+58)
        drawing.text(225, y+51, "no", GRAY)
    drawing.box(62, 262, 296, 60, BLUE, "#f2f7fb")
    drawing.text(210, 287, "q ← q − step_size × slope", BLUE, "middle")
    drawing.text(210, 309, "k ← k + 1", BLUE, "middle")
    drawing.line(62, 292, 20, 292, BLUE)
    drawing.line(20, 292, 20, 93, BLUE)
    drawing.arrow(20, 93, 62, 93, BLUE)
    drawing.text(210, 347, "Repeat with the updated q", GRAY, "middle")
    drawing.save("gd_loop_flow.svg")


def step_sizes():
    fig, axes = plt.subplots(2, 2, figsize=(5.2, 4.25), sharex=True, sharey=True)
    for ax, (alpha, behavior) in zip(axes.flat, [(0.05, "Closer"), (0.20, "Crosses"),
                                               (0.25, "Repeats"), (0.30, "Grows")]):
        q, values = 0., [0.]
        for _ in range(3):
            q -= alpha*8*(q-1)
            values.append(q)
        ax.axhline(1, color=TEAL, ls="--", lw=1)
        ax.plot(range(4), values, "o-", color=BLUE, ms=4)
        ax.set_title(f"α = {alpha:.2f} · {behavior}", fontsize=10.5, color=PURPLE, pad=7)
        ax.set(xticks=range(4), yticks=[-1, 0, 1, 2, 3, 4], ylim=(-1.2, 4.2))
        ax.grid(alpha=0.25)
    fig.supxlabel("Update k", fontsize=10.5)
    fig.supylabel("Correction q (min)", fontsize=10.5)
    fig.tight_layout(pad=0.7, h_pad=1.0, w_pad=1.2)
    save_plot(fig, "gd_step_size_panels.svg")


def newton_moves():
    drawing = Diagram(290, "From the same zero correction, GD moves 0.4, full Newton 1, and half Newton 0.5.")
    origin, scale = 219, 256
    drawing.line(origin, 24, origin, 226, "#d7dfe7", 1, 'stroke-dasharray="3 3"')
    drawing.line(origin+scale, 24, origin+scale, 226, TEAL, 1, 'stroke-dasharray="3 3"')
    for i, (name, rule, q, score) in enumerate([
        ("GD", "α = 0.05", 0.4, 3.44),
        ("Full Newton", "fraction = 1", 1., 2.),
        ("Damped Newton", "fraction = 0.5", 0.5, 3.),
    ]):
        y = 48 + 78*i
        drawing.text(16, y-2, name)
        drawing.text(16, y+20, rule, PURPLE)
        drawing.line(origin, y, origin+scale, y, "#d7dfe7")
        drawing.arrow(origin+5, y, origin+scale*q-6, y, BLUE)
        drawing.dot(origin, y, BLUE)
        drawing.dot(origin+scale*q, y, ORANGE)
        drawing.text(origin+scale*q, y-12, f"q = {q:g}", ORANGE, "middle")
        drawing.text(origin+scale*q, y+24, f"f = {score:g}", GRAY, "middle")
    drawing.text(origin, 251, "Start: 0", BLUE, "middle")
    drawing.text(origin+scale, 251, "Minimum: 1", TEAL, "middle")
    drawing.text(348, 274, "Correction q (min)", GRAY, "middle")
    drawing.save("newton_step_lengths.svg")


def stopping_slope():
    fig, ax = plt.subplots(figsize=(5.2, 3.2))
    q = np.linspace(-0.15, 1.55, 200)
    ax.plot(q, 4*(q-1)**2+2, color=BLUE, lw=2)
    short_q = 1e-6
    near_start = np.array([-0.10, 0.28])
    ax.plot(near_start, 4*(short_q-1)**2+2 + 8*(short_q-1)*(near_start-short_q),
            color=ORANGE, lw=1.5, ls="--")
    ax.plot([0.76, 1.25], [2, 2], color=TEAL, lw=2)
    ax.scatter([short_q, 1], [4*(short_q-1)**2+2, 2], c=[ORANGE, TEAL], s=38, zorder=4)
    ax.annotate("Tiny move\nslope ≈ −8", (short_q, 4*(short_q-1)**2+2), (0.52, 6.2),
                arrowprops={"arrowstyle": "->", "color": ORANGE}, color=ORANGE)
    ax.annotate("Full step\nslope = 0", (1, 2), (1.06, 3.65),
                arrowprops={"arrowstyle": "->", "color": TEAL}, color=TEAL)
    ax.set(xlabel="Correction q (min)", ylabel="Squared error f (min²)",
           xlim=(-0.15, 1.6), ylim=(1.3, 7.3), xticks=[0, 0.5, 1, 1.5])
    ax.grid(alpha=0.25)
    fig.tight_layout(pad=0.8)
    save_plot(fig, "newton_stopping_slope.svg")


if __name__ == "__main__":
    errors_to_score()
    gd_loop()
    step_sizes()
    newton_moves()
    stopping_slope()
    print("Generated three GD figures and two Newton figures.")
