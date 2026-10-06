"""Generate the compact bound illustration used in the KKT concepts notebook."""

from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({
        'font.size': 11,
        'svg.fonttype': 'none',
        'svg.hashsalt': 'kkt-concepts',
        'axes.spines.top': False,
        'axes.spines.right': False,
    })
    gray, teal, orange = '#707070', '#168578', '#e78b24'
    figure, axis = plt.subplots(figsize=(5.12, 2.9), dpi=100)
    correction = np.linspace(0.5, 2.1, 241)
    score = lambda q: 0.5 + 6 * (q - 1.5) ** 2
    axis.plot(correction, score(correction), color=gray, linewidth=2)
    allowed = np.linspace(0.5, 1, 81)
    axis.plot(allowed, score(allowed), color=teal, linewidth=3)
    axis.axvline(1, color=gray, linestyle='--', linewidth=1.2)
    axis.plot(1, score(1), 'o', color=orange, markersize=7, zorder=3)
    axis.plot(1.5, score(1.5), 'x', color=gray, markersize=7)
    axis.text(0.77, 5.6, 'Allowed', color=teal, ha='center')
    axis.text(1.54, 5.6, 'Forbidden', color=gray, ha='center')
    axis.annotate('Bound: q = 1', xy=(1, 3.8), xytext=(1.22, 4.1),
                  arrowprops={'arrowstyle': '-', 'color': gray}, color=gray)
    axis.annotate('Lower error', xy=(1.34, score(1.34)), xytext=(1.58, 2.6),
                  arrowprops={'arrowstyle': '->', 'color': gray}, color=gray,
                  ha='center')
    axis.set(xlabel='Correction q (min)', ylabel='Squared error (min²)',
             xlim=(0.48, 2.1), ylim=(0, 6.8), xticks=[0.5, 1, 1.5, 2],
             yticks=[0, 2, 4, 6])
    axis.grid(alpha=0.25)
    figure.tight_layout(pad=0.8)
    figure.savefig(Path(__file__).parent / 'clock_bound_concept.svg',
                   metadata={'Date': None})
    plt.close(figure)


if __name__ == '__main__':
    main()
