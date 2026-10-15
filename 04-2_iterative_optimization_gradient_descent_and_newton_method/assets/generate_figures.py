"""Rebuild compact figures for the independent iterative-method examples."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DEST = Path(__file__).resolve().parent
BLUE, TEAL, ORANGE, PURPLE, GRAY = (
    "#2878b5", "#168578", "#d47a20", "#8854a5", "#707070"
)
plt.rcParams.update({
    "font.size": 10.5, "axes.titlesize": 10.5, "axes.labelsize": 10.5,
    "svg.fonttype": "none", "svg.hashsalt": "iterative-method-concepts",
    "axes.spines.top": False, "axes.spines.right": False,
})


def delivery_fit():
    distance = np.array([0., 1., 2., 3.])
    observed_time = np.array([10., 12., 15., 17.])
    design = np.column_stack([np.ones(4), distance])
    coefficients = np.linalg.solve(design.T @ design, design.T @ observed_time)
    prediction = design @ coefficients
    fig, ax = plt.subplots(figsize=(4.8, 3.0))
    ax.plot(distance, prediction, color=BLUE, label="Fitted prediction")
    ax.scatter(distance, observed_time, color=ORANGE, s=32, zorder=3,
               label="Observed time")
    ax.vlines(distance, prediction, observed_time, color=GRAY, lw=2)
    ax.set(xlabel="Distance d (km)", ylabel="Delivery time (min)",
           xticks=distance, yticks=[10, 12, 14, 16, 18], ylim=(9, 19))
    ax.legend(loc="upper left", frameon=False)
    ax.grid(alpha=0.25)
    fig.tight_layout(pad=0.6)
    fig.savefig(DEST / "delivery_fit.svg", metadata={"Date": None})
    plt.close(fig)


def stopping_checks():
    # Native SVG lettering stays 14 px when embedded at its 480 px width.
    rows = [
        (12, TEAL, "Small gradient", "Tolerance reached"),
        (72, PURPLE, "Small move only", "Step may be too small"),
        (132, ORANGE, "Update limit", "Work stopped; check gradient"),
    ]
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="480" height="192" '
        'viewBox="0 0 480 192" role="img">',
        '<title>Three stopping situations have different meanings</title>',
        '<rect width="480" height="192" fill="white"/>',
        '<g font-family="DejaVu Sans, sans-serif" font-size="14">',
    ]
    for y, color, condition, meaning in rows:
        parts.extend([
            f'<rect x="8" y="{y}" width="464" height="46" rx="6" '
            f'fill="white" stroke="{color}"/>',
            f'<text x="20" y="{y+28}" fill="{color}">{condition}</text>',
            f'<text x="200" y="{y+28}" fill="#243344">{meaning}</text>',
        ])
    (DEST / "stopping_checks.svg").write_text("\n".join(parts + ["</g></svg>\n"]))


def iteration_flow():
    """Show why the gradient is checked again after every permitted update."""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="262"
viewBox="0 0 480 262" role="img">
<title>Check the current gradient, then stop or update and repeat</title>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5"
markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="{GRAY}"/></marker></defs>
<rect width="480" height="262" fill="white"/>
<g fill="none" stroke="{GRAY}" stroke-width="1.4" marker-end="url(#arrow)">
<path d="M 158 46 V 76"/><path d="M 158 116 V 146"/>
<path d="M 158 186 V 216"/><path d="M 286 96 H 331"/>
<path d="M 286 166 H 331"/>
<path d="M 30 236 H 9 V 26 H 29"/>
</g>
<g font-family="DejaVu Sans, sans-serif" font-size="14" text-anchor="middle">
<g fill="white" stroke="{BLUE}">
<rect x="30" y="6" width="256" height="40" rx="6"/>
<rect x="30" y="76" width="256" height="40" rx="6"/>
<rect x="30" y="146" width="256" height="40" rx="6"/>
<rect x="30" y="216" width="256" height="40" rx="6"/>
</g>
<rect x="332" y="76" width="140" height="40" rx="6" fill="white" stroke="{TEAL}"/>
<rect x="332" y="146" width="140" height="40" rx="6" fill="white" stroke="{ORANGE}"/>
<g fill="#243344">
<text x="158" y="31">Compute gradient at x</text>
<text x="158" y="101">Gradient small enough?</text>
<text x="158" y="171">Update limit reached?</text>
<text x="158" y="241">Update x; save a copy</text>
<text x="180" y="137">no</text><text x="180" y="207">no</text>
<text x="308" y="88">yes</text><text x="308" y="158">yes</text>
</g>
<text x="402" y="101" fill="{TEAL}">Small gradient</text>
<text x="402" y="171" fill="{ORANGE}">Update limit</text>
</g></svg>
'''
    (DEST / "iteration_flow.svg").write_text(svg)


if __name__ == "__main__":
    delivery_fit()
    stopping_checks()
    iteration_flow()
    print("Generated delivery_fit.svg, stopping_checks.svg, and iteration_flow.svg")
