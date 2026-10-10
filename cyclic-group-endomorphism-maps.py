"""Draw two additive self-maps of C6; write an opaque PNG to the CWD.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 5.4), dpi=100)
    blue, orange, gray = "#2166a5", "#b65b13", "#6b7280"
    rows = np.arange(5, -1, -1)
    for ax, multiplier in zip(axes, (2, 5), strict=True):
        outputs = multiplier * np.arange(6) % 6
        kernel = set(np.flatnonzero(outputs == 0).tolist())
        image = set(outputs.tolist())
        for k, output in enumerate(outputs):
            ax.add_patch(FancyArrowPatch(
                (0, rows[k]), (2.1, rows[output]), shrinkA=13, shrinkB=13,
                arrowstyle="-|>", mutation_scale=14, linewidth=1.7,
                color=orange if k in kernel else blue, alpha=0.9, zorder=1,
            ))
        for k in range(6):
            for x, color in ((0, orange if k in kernel else blue),
                             (2.1, blue if k in image else gray)):
                ax.add_patch(Circle((x, rows[k]), 0.16, edgecolor=color,
                                    facecolor="white", linewidth=2, zorder=2))
                ax.text(x, rows[k], str(k), ha="center", va="center",
                        color=color, weight="bold", zorder=3)
        ax.text(0, 5.55, "Input", ha="center", weight="bold")
        ax.text(2.1, 5.55, "Output", ha="center", weight="bold")
        ax.set_title(rf"$f_{multiplier}(k)={multiplier}k\;\mathrm{{mod}}\;6$",
                     fontsize=17, pad=12)
        summary = ("Outputs: 0, 2, 4, 0, 2, 4\nKernel: {0, 3}; image: {0, 2, 4}\n"
                   "Pairs collapse: no inverse" if multiplier == 2 else
                   "Outputs: 0, 5, 4, 3, 2, 1\nKernel: {0}; image: all six elements\n"
                   "A permutation; its own inverse")
        ax.text(1.05, -0.65, summary, ha="center", va="top", fontsize=11,
                linespacing=1.5)
        ax.set(xlim=(-0.45, 2.55), ylim=(-2, 5.9))
        ax.axis("off")
    fig.suptitle("Both maps preserve addition; only one is reversible",
                 fontsize=16, weight="bold", y=0.965)
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.05, top=0.80, wspace=0.25)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
