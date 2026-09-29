"""Minimum positive square counts from direct tuple enumeration, not a formula.

Output PNG to CWD; run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
These are exact finite arithmetic counts, not measured data or an infinite proof.
"""

from itertools import product
from math import isqrt
from collections import Counter
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.patches import Patch
import numpy as np


def minimum_counts(limit):
    squares = tuple(x * x for x in range(isqrt(limit) + 1))
    minima = {0: 0}
    for k in range(1, 5):
        for terms in product(squares, repeat=k):
            n = sum(terms)
            if n <= limit and n not in minima:
                minima[n] = k
    assert len(minima) == limit + 1
    return minima


def main():
    minima = minimum_counts(100)
    values = np.array([minima[n] for n in range(1, 101)]).reshape(10, 10)
    colors = ["#d0e8f5", "#b8dfb4", "#f9df9e", "#e3c3ea"]
    fig, ax = plt.subplots(figsize=(8.8, 6.5), facecolor="white")
    ax.imshow(values, cmap=ListedColormap(colors),
              norm=BoundaryNorm([0.5, 1.5, 2.5, 3.5, 4.5], 4), aspect="auto")
    for i in range(10):
        for j in range(10):
            ax.text(j, i, str(10 * i + j + 1), ha="center", va="center",
                    fontsize=13, color="#222222")
    ax.set_xticks(np.arange(-0.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 10, 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=2)
    ax.tick_params(which="both", bottom=False, left=False,
                   labelbottom=False, labelleft=False)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title("How many nonzero squares are needed?\nIntegers 1–100, enumerated exactly",
                 fontsize=17, pad=17)
    ax.legend(handles=[Patch(facecolor=c, label=f"{k} square" + ("s" if k > 1 else ""))
                       for k, c in enumerate(colors, 1)],
              loc="upper center", bbox_to_anchor=(0.5, -0.035), ncol=4,
              frameon=False, fontsize=12)
    fig.text(0.5, 0.026, "Zero needs 0 nonzero squares. Add zero terms to make four slots.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.04, right=0.96, top=0.86, bottom=0.15)
    fig.savefig("four-square-minima.png", dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"counts_1_to_100": dict(sorted(Counter(minima[n] for n in range(1, 101)).items())),
                      "need_four": [n for n in range(1, 101) if minima[n] == 4]}, sort_keys=True))


if __name__ == "__main__":
    main()
