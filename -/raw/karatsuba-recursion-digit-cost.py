"""Illustrate an ideal equal-half recurrence, not an execution-time benchmark.

Write a matching PNG in the CWD. Tested with Python 3.14,
matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, (tree, cost) = plt.subplots(1, 2, figsize=(11.5, 5.9), dpi=110,
                                    gridspec_kw={"width_ratios": [1.04, 1]})
    fig.patch.set_facecolor("white")
    ink, blue, orange = "#24364b", "#276ea3", "#bd5d18"
    fig.suptitle("Three recursive products change the growth of multiplication cost",
                 fontsize=16, weight="bold", color=ink, y=0.98)
    tree.set(xlim=(-0.55, 8.55), ylim=(-1.75, 4.05))
    tree.axis("off")
    tree.set_title("Ideal equal halves: n = 8", fontsize=13, pad=12)
    root = [4.0]
    children = [1.0, 4.0, 7.0]
    grandchildren = [0.25, 1, 1.75, 3.25, 4, 4.75, 6.25, 7, 7.75]
    for x in children:
        tree.plot([4, x], [3.5, 2.4], color="#9cabb9", lw=1.3, zorder=1)
    for i, x in enumerate(children):
        for y in grandchildren[3 * i:3 * i + 3]:
            tree.plot([x, y], [2.4, 1.3], color="#9cabb9", lw=1.3, zorder=1)
    for xs, y, label in [(root, 3.5, "8"), (children, 2.4, "4"),
                         (grandchildren, 1.3, "2")]:
        tree.scatter(xs, np.full(len(xs), y), s=450, color="#e2eff9",
                     edgecolors=blue, linewidth=1.2, zorder=2)
        for x in xs:
            tree.text(x, y, label, ha="center", va="center", fontsize=11, zorder=3)
    for i, x in enumerate(grandchildren):
        for t in (-0.22, 0, 0.22):
            tree.plot([x, x + t], [1.3, 0.45], color="#9cabb9", lw=0.8, zorder=1)
            tree.scatter([x + t], [0.45], s=30, color=orange, zorder=2)
    tree.text(4, -0.05, "27 leaves of size 1 (one unit each)",
              ha="center", fontsize=11, color=ink)
    tree.text(4, -0.62, "Level j      Calls      Size       Internal work",
              ha="center", fontsize=11, weight="bold", color=ink)
    tree.text(4, -1.04, r"$j\qquad 3^j\qquad n/2^j\qquad \alpha n(3/2)^j$",
              ha="center", fontsize=13, color=ink)
    tree.text(4, -1.54, "Internal levels: j = 0, ..., k − 1; n = 2ᵏ",
              ha="center", fontsize=11, color=ink)

    k = np.arange(15)
    n = 2 ** k
    # One leaf unit; alpha=1 times operand length for each internal call.
    modeled = 3 * 3 ** k - 2 * 2 ** k
    school_products = n ** 2
    cost.loglog(n, school_products, "s-", base=2, ms=4, lw=2, color=blue,
                label=r"Ordinary digit products: $n^2$")
    cost.loglog(n, modeled, "o-", base=2, ms=4, lw=2, color=orange,
                label=r"Model: $3\cdot3^k-2\cdot2^k$")
    cost.set_title("Stipulated counts, not machine timings", fontsize=13, pad=12)
    cost.set_xlabel("Operand length n (fixed-base digit positions)", fontsize=11)
    cost.set_ylabel("Count in the stated model (log scale)", fontsize=11)
    cost.set_xticks(2 ** np.arange(0, 15, 2))
    cost.set_xticklabels([str(2 ** i) for i in range(0, 15, 2)], fontsize=9)
    cost.grid(True, alpha=0.23, which="major")
    cost.legend(loc="upper left", fontsize=10, frameon=False)
    cost.text(0.04, 0.08, "One unit per leaf; overhead αs per internal call\n"
              "of size s, with α = 1. Sum growth is idealized.\n"
              "Crossover depends on these chosen constants.",
              transform=cost.transAxes, fontsize=10, linespacing=1.4,
              color=ink, bbox={"facecolor": "white", "edgecolor": "none", "pad": 4})
    fig.subplots_adjust(left=0.025, right=0.98, bottom=0.16, top=0.86, wspace=0.28)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
