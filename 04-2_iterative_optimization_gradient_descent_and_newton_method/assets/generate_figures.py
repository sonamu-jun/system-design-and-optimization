"""Rebuild the compact explanatory SVGs for the clock optimization example."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

DEST = Path(__file__).resolve().parent
BLUE, TEAL, ORANGE, PURPLE, GRAY = (
    "#2878b5", "#168578", "#e78b24", "#8854a5", "#707070"
)
plt.rcParams.update({
    "font.size": 10.5, "axes.labelsize": 10.5, "legend.fontsize": 10,
    "svg.fonttype": "none", "svg.hashsalt": "clock-iterative-optimization",
    "figure.facecolor": "white", "axes.spines.top": False,
    "axes.spines.right": False,
})


def save(figure, name, manual=False):
    if not manual:
        figure.tight_layout()
    figure.savefig(DEST / f"{name}.svg", metadata={"Date": None})
    plt.close(figure)


def offset_trace(alpha, steps):
    q = 0.0
    values = [q]
    for _ in range(steps):
        q -= alpha * 8 * (q - 1)
        values.append(q)
    return np.array(values)


fig, ax = plt.subplots(figsize=(5.2, 3.4))
q = np.linspace(-0.2, 2.0, 200)
ax.plot(q, 4*(q-1)**2+2, color=BLUE)
ax.scatter([0, 0.4, 1], [6, 3.44, 2], c=[BLUE, ORANGE, TEAL], zorder=4)
ax.annotate("Start: (0, 6)", (0, 6), (0.16, 6.3))
ax.annotate("After one update", (0.4, 3.44), (0.66, 4.7),
            arrowprops={"arrowstyle": "->", "color": ORANGE})
ax.annotate("Minimum: (1, 2)", (1, 2), (1.04, 2.6))
ax.annotate("", (0.4, 1.35), (0, 1.35),
            arrowprops={"arrowstyle": "->", "color": ORANGE, "lw": 2})
ax.text(0.2, 0.9, "+0.4 min", ha="center", color=ORANGE)
ax.set(xlabel="Correction q (min)", ylabel="Squared error f (min²)",
       ylim=(0.5, 8), xlim=(-0.2, 2.1))
ax.grid(alpha=0.25)
save(fig, "offset_descent")

fig, ax = plt.subplots(figsize=(5.2, 3.7))
for alpha, color, marker in [(0.05, BLUE, "o"), (0.125, TEAL, "s"),
                              (0.25, PURPLE, "^"), (0.30, ORANGE, "D")]:
    ax.plot(range(5), offset_trace(alpha, 4), marker=marker, color=color,
            label=f"alpha = {alpha:g}", markersize=4)
ax.axhline(1, color=GRAY, ls="--", lw=1, zorder=0)
ax.set(xlabel="Number of updates k", ylabel="Correction q (min)",
       xticks=range(5), ylim=(-3.5, 6))
ax.legend(loc="upper left", ncol=2, framealpha=1)
ax.grid(alpha=0.25)
save(fig, "step_size_comparison")

fig, ax = plt.subplots(figsize=(5.2, 3.3))
q = np.linspace(-0.15, 1.8, 100)
ax.plot(q, 8*(q-1), color=BLUE, label="Derivative: 8(q − 1)")
ax.axhline(0, color=GRAY, lw=1)
ax.scatter([0, 1], [-8, 0], c=[BLUE, ORANGE], zorder=4)
ax.annotate("Slope = −8", (0, -8), (0.12, -8.5))
ax.annotate("Slope = 0", (1, 0), (1.08, -2.7))
ax.annotate("", (1, -10.5), (0, -10.5),
            arrowprops={"arrowstyle": "->", "color": ORANGE, "lw": 2})
ax.text(0.5, -12.4, "Newton change: −(−8)/8 = 1", ha="center")
ax.set(xlabel="Correction q (min)", ylabel="Offset derivative (min)",
       ylim=(-14, 8), xlim=(-0.15, 1.8))
ax.legend(loc="upper left")
ax.grid(alpha=0.25)
save(fig, "newton_slope")

fig, ax = plt.subplots(figsize=(5.2, 3.9))
q, r = np.meshgrid(np.linspace(-0.15, 2.25, 180), np.linspace(-0.85, 0.75, 180))
errors = np.array([-2., -1., -1., 0.])
times = np.arange(4.)
scores = sum((error + q + time*r)**2 for error, time in zip(errors, times))
contours = ax.contour(q, r, scores, levels=[0.3, 0.6, 1, 2, 4, 6, 10],
                      colors=GRAY, linewidths=0.8, alpha=0.5)
ax.clabel(contours, levels=[0.6, 2, 6], fontsize=10, fmt="%g")
decision = np.zeros(2)
path = [decision.copy()]
for _ in range(18):
    response = errors + decision[0] + decision[1]*times
    decision -= 0.05 * 2 * np.array([response.sum(), times @ response])
    path.append(decision.copy())
path = np.array(path)
ax.plot(path[:, 0], path[:, 1], "o-", color=BLUE, markersize=3,
        label="Gradient descent: 18 updates")
ax.plot([0, 1.9], [0, -0.6], "o-", color=ORANGE, markersize=4,
        label="Newton: 1 update", zorder=3)
ax.annotate("", (1.1, -0.6*1.1/1.9), (0.85, -0.6*0.85/1.9),
            arrowprops={"arrowstyle": "->", "color": ORANGE, "lw": 2})
ax.scatter([1.9], [-0.6], color=TEAL, marker="D", s=40, zorder=5)
ax.annotate("Start", (0, 0), (0.05, -0.18))
ax.annotate("(1.9, −0.6)", (1.9, -0.6), (1.22, -0.78))
ax.set(xlabel="Initial correction q (min)", ylabel="Rate correction r (min/h)",
       xlim=(-0.15, 2.25), ylim=(-0.85, 0.75))
ax.legend(loc="upper right", framealpha=1)
ax.grid(alpha=0.25)
save(fig, "clock_update_paths")

fig, ax = plt.subplots(figsize=(5.2, 3.9))
contours = ax.contour(q, r, scores, levels=[0.3, 0.6, 1, 2, 4, 6, 10],
                     colors=GRAY, linewidths=0.8, alpha=0.5)
ax.clabel(contours, levels=[0.6, 2, 6], fontsize=10, fmt="%g")
ax.plot(path[:, 0], path[:, 1], "o-", color=BLUE, markersize=3,
        label="Gradient descent: 18 updates")
ax.scatter([1.9], [-0.6], color=TEAL, marker="D", s=40, zorder=5)
ax.annotate("Start", (0, 0), (0.05, -0.18))
ax.annotate("First update: (0.4, 0.3)", (0.4, 0.3), (0.58, 0.48),
            arrowprops={"arrowstyle": "->", "color": BLUE})
ax.annotate("(1.9, −0.6)", (1.9, -0.6), (1.22, -0.78))
ax.set(xlabel="Initial correction q (min)", ylabel="Rate correction r (min/h)",
       xlim=(-0.15, 2.25), ylim=(-0.85, 0.75))
ax.legend(loc="upper right", framealpha=1)
ax.grid(alpha=0.25)
save(fig, "gradient_update_path")

fig, ax = plt.subplots(figsize=(5.2, 2.9))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
rows = [
    (0.71, TEAL, "Small gradient", "Tolerance reached", "‖gradient‖ ≤ 10⁻⁶"),
    (0.39, PURPLE, "Tiny step size", "Still far from stationary", "alpha = 10⁻¹²; ‖gradient‖ ≈ 10"),
    (0.07, ORANGE, "Two updates", "Budget exhausted", "‖gradient‖ ≈ 5.48"),
]
for y, color, left, right, value in rows:
    ax.add_patch(FancyBboxPatch((0.025, y), 0.95, 0.235,
                 boxstyle="round,pad=0.015", facecolor="white", edgecolor=color))
    ax.text(0.055, y+0.15, left, color=color, va="center")
    ax.text(0.43, y+0.15, right, va="center")
    ax.text(0.055, y+0.055, value, va="center")
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
save(fig, "stopping_conditions", manual=True)

print("Generated six compact clock figures in", DEST)
