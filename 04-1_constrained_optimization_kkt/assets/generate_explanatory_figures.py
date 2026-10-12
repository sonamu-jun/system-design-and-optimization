"""Build complementary KKT figures without repeating the interactive score curve."""

from html import escape
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DEST = Path(__file__).resolve().parent
BLUE, TEAL, GRAY, INK = "#2878b5", "#168578", "#707070", "#243344"
plt.rcParams.update({
    "font.size": 10.5, "svg.fonttype": "none",
    "svg.hashsalt": "kkt-explanations", "axes.spines.top": False,
    "axes.spines.right": False,
})


class Diagram:
    """Use CSS-sized SVG text so labels stay readable at a 520 px display width."""

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

    def arrow(self, x1, y, x2, color):
        self.line(x1, y, x2, y, color, 3)
        tail = x2 - 8 if x2 > x1 else x2 + 8
        self.parts.append(f'<path d="M {tail},{y-5} L {x2},{y} L {tail},{y+5}" '
                          f'fill="none" stroke="{color}" stroke-width="2"/>')

    def save(self, name):
        (DEST / name).write_text("\n".join(self.parts + ["</g></svg>"]) + "\n")


def feasible_settings():
    fig, ax = plt.subplots(figsize=(5.2, 3.3))
    ax.axvspan(-0.05, 1, color=TEAL, alpha=0.07)
    q = np.linspace(-0.05, 2.05, 200)
    ax.plot(q, 1-q, color=GRAY, lw=2, ls="--")
    allowed = q[q <= 1]
    ax.plot(allowed, 1-allowed, color=TEAL, lw=3)
    ax.axvline(1, color=GRAY, ls=":", lw=1.5)
    ax.scatter([0.5, 1], [0.5, 0], c=[BLUE, TEAL], s=38, zorder=4)
    ax.scatter([1.5], [-0.5], color=GRAY, marker="x", s=45, zorder=4)
    ax.annotate("q + r = 1", (0.4, 0.6), (0.04, 0.97),
                arrowprops={"arrowstyle": "-", "color": GRAY})
    ax.text(1.07, 0.97, "Bound: q = 1", color=GRAY)
    ax.annotate("Best: (1, 0)", (1, 0), (1.2, 0.32),
                arrowprops={"arrowstyle": "-", "color": TEAL}, color=TEAL)
    ax.text(0.04, -0.66, "q ≤ 1", color=TEAL)
    ax.text(1.26, -0.85, "Rejected", color=GRAY)
    ax.set(xlabel="Initial correction q (min)", ylabel="Rate correction r (min/h)",
           xlim=(-0.05, 2.05), ylim=(-1.05, 1.2),
           xticks=[0, 0.5, 1, 1.5, 2], yticks=[-1, -0.5, 0, 0.5, 1])
    ax.grid(alpha=0.25)
    fig.tight_layout(pad=0.8)
    path = DEST / "calibration_feasible_set.svg"
    fig.savefig(path, metadata={"Date": None})
    path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines()) + "\n")
    plt.close(fig)


def activity_and_slack():
    drawing = Diagram(304, "Active bounds can have positive or zero multipliers; slack makes the multiplier zero.")
    position = lambda q: 104 + 176*q
    for row, (limit, best, multiplier) in enumerate([(1, 1, 6), (1.5, 1.5, 0), (2, 1.5, 0)]):
        top = 24 + row*88
        active = best == limit
        drawing.text(16, top, f'{"Active" if active else "Inactive"}: μ = {multiplier}', TEAL)
        drawing.text(496, top, f"Limit = {limit:g}", GRAY, "end")
        y = top + 24
        drawing.line(100, y, 488, y, "#d7dfe7", 4)
        drawing.line(104, y, position(limit), y, TEAL, 4)
        drawing.arrow(112, y, 98, TEAL)
        drawing.line(position(limit), y-9, position(limit), y+9, GRAY, 2)
        x = position(best)
        drawing.parts.append(f'<path d="M {x},{y-6} l 6,6 -6,6 -6,-6 Z" '
                             f'fill="{TEAL}" stroke="white" stroke-width="1"/>')
        drawing.text(x, y+29, f"q* = {best:g}", TEAL, "middle")
        if not active:
            drawing.line(x+6, y-12, position(limit)-2, y-12, GRAY)
            drawing.text((x+position(limit))/2, y-20, "0.5", GRAY, "middle")
    drawing.text(16, 290, "◆ best allowed", TEAL)
    drawing.text(496, 290, "Correction q (min)", GRAY, "end")
    drawing.save("bound_slack_cases.svg")


def stationarity_balance():
    drawing = Diagram(146, "At q equals 1, the slope term minus 6 and bound term plus 6 cancel.")
    drawing.text(116, 30, "Slope p′(1) = −6", BLUE, "middle")
    drawing.text(399, 30, "Bound μ = +6", TEAL, "middle")
    drawing.line(72, 70, 448, 70, "#d7dfe7")
    drawing.line(260, 49, 260, 88, GRAY, 1, 'stroke-dasharray="3 3"')
    drawing.arrow(256, 70, 84, BLUE)
    drawing.arrow(264, 70, 436, TEAL)
    drawing.text(260, 111, "−6 + 6 = 0", INK, "middle")
    drawing.text(260, 135, "Stationarity: the two terms cancel", GRAY, "middle")
    drawing.save("stationarity_balance.svg")


if __name__ == "__main__":
    feasible_settings()
    activity_and_slack()
    stationarity_balance()
    print("Generated three complementary KKT figures.")
