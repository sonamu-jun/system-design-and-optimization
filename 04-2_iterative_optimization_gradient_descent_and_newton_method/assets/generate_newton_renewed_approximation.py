"""Draw two local quadratic approximations on the same objective landscape."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def objective(x):
    return 0.5 * x**2 + 0.25 * x**4


def gradient(x):
    return x + x**3


def curvature(x):
    return 1 + 3 * x**2


plt.rcParams.update({
    "font.size": 18,
    "mathtext.fontset": "stix",
    "svg.fonttype": "path",
    "lines.solid_capstyle": "round",
    "savefig.facecolor": "white",
})

fig, axes = plt.subplots(1, 2, figsize=(5.5, 3.45), dpi=160)
fig.subplots_adjust(left=0.025, right=0.975, bottom=0.20, top=0.90, wspace=0.13)
current = 2.0
blue, orange, green, gray = "#1680ff", "#ff7f0e", "#00b631", "#626675"

for index, ax in enumerate(axes):
    next_decision = current - gradient(current) / curvature(current)

    def approximation(x):
        delta = x - current
        return objective(current) + gradient(current) * delta + 0.5 * curvature(current) * delta**2

    ax.set(xlim=(-1.45, 2.55), ylim=(-0.72, 7.5))
    ax.axis("off")
    for start, end in [((-1.43, -0.34), (2.51, -0.34)), ((-1.36, -0.60), (-1.36, 7.30))]:
        ax.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "->", "lw": 1.25, "color": "#252525"})
    ax.text(-1.18, 7.0, r"$f(x)$", va="bottom")
    ax.text(2.48, -0.50, r"$x$", ha="center", va="top")

    domain = np.linspace(-1.3, 2.12, 350)
    curve, = ax.plot(domain, objective(domain), color=blue, lw=2)
    curve.set_sketch_params(scale=0.25, length=120, randomness=1.2)
    ax.text(1.55, 7.0, r"$f(x)$", color=blue, ha="center", va="bottom")

    half_span = 1.03 if index == 0 else 0.94
    local_domain = np.linspace(next_decision - half_span, next_decision + half_span, 240)
    ax.plot(local_domain, approximation(local_domain), color=gray, lw=1.3, linestyle=(0, (4, 3)))
    label = r"$q_k(x)$" if index == 0 else r"$q_{k+1}(x)$"
    ax.text(-0.65 if index == 0 else -0.1, 4.5 if index == 0 else 3.6, label, color=gray)

    for decision in [current, next_decision]:
        top = max(objective(decision), approximation(decision))
        ax.plot([decision, decision], [-0.34, top], color="#777777", lw=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.plot([0, 0], [-0.34, 0], color="#777777", lw=0.9)
    ax.scatter([0], [objective(0)], color=green, s=21, zorder=6)
    ax.scatter([next_decision], [approximation(next_decision)], facecolors="white", edgecolors=gray, s=24, linewidths=1.2, zorder=7)
    ax.scatter([current, next_decision], [objective(current), objective(next_decision)], color=orange, s=24, zorder=8)
    ax.annotate("", xy=(next_decision, objective(next_decision)), xytext=(current, objective(current)), arrowprops={"arrowstyle": "->", "color": orange, "lw": 1.3, "shrinkA": 5, "shrinkB": 5}, zorder=9)

    current_label = r"$x_k$" if index == 0 else r"$x_{k+1}$"
    next_label = r"$x_{k+1}$" if index == 0 else r"$x_{k+2}$"
    for decision, label in [(0, r"$x^*$"), (next_decision, next_label), (current, current_label)]:
        label_height = -1.2 if index == 1 and decision == next_decision else -0.50
        ax.text(decision, label_height, label, ha="center", va="top", fontsize=17)
    current = next_decision

destination = Path(__file__).with_name("newton_renewed_approximation_whiteboard.svg")
fig.savefig(destination)
fig.savefig(destination.with_suffix(".png"))
plt.close(fig)
