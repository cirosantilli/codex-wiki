"""Enumerate affine maps over F_5 and draw their output pairs at 0 and 1.

Generate with: make _media/affine-hash-pair-grid.png
Writes an opaque white PNG with this basename to the current directory.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from collections import Counter
from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def main():
    q = 5
    coefficients = list(product(range(q), repeat=2))
    restricted = [(a, b) for a, b in coefficients if a != 0]

    def outputs(a, b):
        return tuple((a * x + b) % q for x in range(q))

    assert len(coefficients) == 25 and len(restricted) == 20
    assert len({outputs(a, b) for a, b in coefficients}) == 25
    assert all(len(set(outputs(a, b))) == q for a, b in restricted)
    for x in range(q):
        marginal = Counter((a * x + b) % q for a, b in coefficients)
        restricted_marginal = Counter((a * x + b) % q for a, b in restricted)
        assert marginal == Counter({u: 5 for u in range(q)})
        assert restricted_marginal == Counter({u: 4 for u in range(q)})
        for y in range(q):
            if x == y:
                continue
            pairs = Counter(((a * x + b) % q, (a * y + b) % q)
                            for a, b in coefficients)
            reduced_pairs = Counter(((a * x + b) % q, (a * y + b) % q)
                                    for a, b in restricted)
            assert pairs == Counter({(u, v): 1 for u, v in product(range(q), repeat=2)})
            assert reduced_pairs == Counter({(u, v): 1 for u, v in product(range(q), repeat=2)
                                             if u != v})
            assert sum(pairs[u, u] for u in range(q)) == 5

    grid = {(b, (a + b) % q): (a, b) for a, b in coefficients}
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 5.7), dpi=120)
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.30, top=0.77, wspace=0.30)
    fig.suptitle(r"Affine hashing over $\mathbb{F}_5$: $h_{a,b}(x)=ax+b$",
                 fontsize=16, y=0.97)
    fig.text(0.5, 0.89, "Cells show the coefficient pair (a, b) producing each output pair",
             ha="center", fontsize=11)
    palette = ListedColormap(["#e6f0f7", "#f7dfcf", "#f1f1f1"])
    for panel, ax in enumerate(axes):
        values = np.zeros((q, q), dtype=int)
        np.fill_diagonal(values, 1 if panel == 0 else 2)
        ax.imshow(values, cmap=palette, vmin=0, vmax=2, origin="lower",
                  interpolation="nearest")
        for u, v in product(range(q), repeat=2):
            a, b = grid[u, v]
            excluded = panel == 1 and a == 0
            ax.text(v, u, "excluded" if excluded else f"({a}, {b})",
                    ha="center", va="center", fontsize=9 if excluded else 11,
                    color="#6a6a6a" if excluded else "#163e5a")
        ax.set_xticks(range(q))
        ax.set_yticks(range(q))
        ax.set_xticks(np.arange(-0.5, q, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, q, 1), minor=True)
        ax.grid(which="minor", color="white", linewidth=2)
        ax.tick_params(which="minor", bottom=False, left=False)
        ax.set_xlabel(r"$v=h(1)$")
        ax.set_ylabel(r"$u=h(0)$")
        ax.set_title("All a, b: 25 functions" if panel == 0 else "Nonzero a: 20 permutations",
                     fontsize=12, pad=12)
        for spine in ax.spines.values():
            spine.set_visible(False)

    fig.text(0.28, 0.115, "Every cell: 1/25\nCollision: 5/25 = 1/5", ha="center")
    fig.text(0.75, 0.115, "Allowed cells: 1/20; collision: 0\nGiven u, four possible v, each 1/4",
             ha="center")
    fig.text(0.5, 0.035, "Both families have uniform individual outputs (1/5); only the full family has independent pairs.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / "affine-hash-pair-grid.png", transparent=False)
    plt.close(fig)
    print("All 20 ordered distinct input pairs checked: 25 output pairs once each; "
          "5 collisions / 25 functions. Nonzero a: 20 off-diagonal pairs once each, "
          "0 collisions; marginals 4/20 and conditional probabilities 1/4.")


if __name__ == "__main__":
    main()
