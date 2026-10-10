"""Exact enumerated square-area examples; output PNG to the working directory.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
No measured data or theorem-based representation lookup is used.
"""

from itertools import combinations_with_replacement
from math import isqrt
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def representation(n):
    """Enumerate all unordered nonnegative four-tuples; prefer large roots."""
    candidates = [tuple(reversed(t)) for t in
                  combinations_with_replacement(range(isqrt(n) + 1), 4)
                  if sum(x * x for x in t) == n]
    return max(candidates)


def main():
    examples = {n: representation(n) for n in (7, 23, 28, 31)}
    colors = ["#2378a3", "#df9431", "#52885a", "#9b6eae"]
    fig, axes = plt.subplots(2, 2, figsize=(10, 5.8), facecolor="white")
    fig.suptitle("Four square areas can add up to a number", fontsize=18, y=0.98)
    for ax, (n, roots) in zip(axes.flat, examples.items()):
        x = 0
        for root, color in zip(roots, colors):
            ax.add_patch(Rectangle((x, 0), root, root, facecolor=color,
                                   edgecolor="white", linewidth=1.5))
            for j in range(1, root):
                ax.plot([x + j, x + j], [0, root], color="white", lw=0.6)
                ax.plot([x, x + root], [j, j], color="white", lw=0.6)
            ax.text(x + root / 2, root + 0.2, rf"${root}^2$",
                    ha="center", va="bottom", fontsize=13)
            x += root + 0.45
        equation = " + ".join(f"{root}^2" for root in roots)
        ax.set_title(rf"${n} = {equation}$", fontsize=15, pad=8)
        ax.set_xlim(-0.25, 11.1)
        ax.set_ylim(-0.3, 6.0)
        ax.set_aspect("equal")
        ax.axis("off")
    fig.text(0.5, 0.035, "Each little cell has area 1. All panels use the same unit length.",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=0.035, right=0.98, top=0.86, bottom=0.10,
                        wspace=0.12, hspace=0.28)
    fig.savefig("four-square-areas.png", dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"representations": examples}, sort_keys=True))


if __name__ == "__main__":
    main()
