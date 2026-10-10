"""Original one-locus Mendelian diagram; writes basename.png to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    gametes = np.array([0.5, 0.5])
    ordered = np.outer(gametes, gametes)
    genotypes = np.array([ordered[0, 0], ordered[0, 1] + ordered[1, 0],
                          ordered[1, 1]])
    colors = ["#237ca3", "#78afc3", "#e6aa47"]
    fig, (grid, bars) = plt.subplots(1, 2, figsize=(8.8, 4.6),
                                    gridspec_kw={"width_ratios": [1.05, 1]})
    fig.set_facecolor("white")
    grid.set(xlim=(-0.72, 2.03), ylim=(-0.03, 2.65), aspect="equal")
    grid.axis("off")
    labels = [["AA", "Aa"], ["aA", "aa"]]
    for row in range(2):
        for col in range(2):
            index = 0 if row == col == 0 else 2 if row == col == 1 else 1
            grid.add_patch(Rectangle((col, 1 - row), 1, 1,
                                     facecolor=colors[index], edgecolor="white", lw=3))
            grid.text(col + 0.5, 1.67 - row, labels[row][col], ha="center",
                      va="center", fontsize=19, color="#152a35")
            grid.text(col + 0.5, 1.28 - row, f"{ordered[row, col]:.2f}",
                      ha="center", va="center", fontsize=12, color="#152a35")
    for i, allele in enumerate(("A", "a")):
        grid.text(i + 0.5, 2.16, f"{allele}: 0.50", ha="center", fontsize=11)
        grid.text(-0.10, 1.5 - i, f"{allele}\n0.50", ha="right", va="center", fontsize=11)
    grid.text(1, 2.48, "Parent 2 gametes", ha="center", fontsize=11)
    grid.text(-0.64, 1, "Parent 1 gametes", rotation=90,
              ha="center", va="center", fontsize=11)
    grid.set_title("Independent transmission", fontsize=12, pad=12)
    bars.bar([0, 1, 2], genotypes, color=colors, width=0.66)
    for i, value in enumerate(genotypes):
        bars.text(i, value + 0.015, f"{value:.2f}", ha="center", fontsize=12)
    bars.set(xticks=[0, 1, 2], xticklabels=["AA", "Aa", "aa"],
             ylim=(0, 0.65), ylabel="Offspring genotype probability")
    bars.set_title("Combine Aa and aA", fontsize=12, pad=12)
    bars.spines[["top", "right"]].set_visible(False)
    bars.set_axisbelow(True)
    bars.grid(axis="y", alpha=0.18)
    bars.plot([0, 0, 1, 1], [0.565, 0.59, 0.59, 0.565], color="#333333", lw=1.2)
    bars.text(0.5, 0.60, "Dominant phenotype: 0.75*", ha="center", fontsize=10)
    fig.suptitle("One diploid locus: Aa × Aa", fontsize=15)
    fig.text(0.5, 0.085,
             "*Only under complete dominance of A and complete penetrance.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.035,
             "Fair segregation; independent gametes; no mutation or genotype-dependent survival.",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=0.06, right=0.98, bottom=0.23, top=0.79, wspace=0.35)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
