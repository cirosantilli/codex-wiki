"""Original AB/ab two-locus toy diagram; save a basename PNG to cwd.

Tested with Python 3.14.4, Matplotlib 3.10.7 (+dfsg1), NumPy 2.3.5.
Assumptions: fair segregation and equal reciprocal gamete probabilities.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../linked-locus-gamete-probabilities.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def main():
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 4.5), sharey=True, facecolor="white")
    parental, recombinant = "#246c94", "#c06923"
    for ax, r, subtitle in zip(axes, (0, 0.2, 0.5),
                               ("Complete linkage", "Partial linkage", "Independent assortment")):
        probabilities = ((1 - r) / 2, (1 - r) / 2, r / 2, r / 2)
        ax.set_facecolor("white")
        ax.bar(range(4), probabilities, color=(parental, parental, recombinant, recombinant),
               width=0.68, zorder=3)
        for x, probability in enumerate(probabilities):
            ax.text(x, probability + 0.014, f"{probability:g}", ha="center", fontsize=12)
        ax.set_xticks(range(4), ("AB", "ab", "Ab", "aB"), fontsize=12)
        ax.set_title(f"r = {r:g}\n{subtitle}", fontsize=12)
        ax.set_ylim(0, 0.57)
        ax.set_yticks((0, 0.1, 0.2, 0.3, 0.4, 0.5))
        ax.grid(axis="y", color="#dddddd", zorder=0)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_xlabel("Gamete haplotype", fontsize=11)
    axes[0].set_ylabel("Probability per transmitted gamete", fontsize=11)
    fig.suptitle("Two linked loci: parental phase AB/ab", fontsize=17, y=0.97)
    fig.legend(handles=(Patch(color=parental, label="Parental: AB, ab"),
                        Patch(color=recombinant, label="Recombinant: Ab, aB")),
               loc="lower center", bbox_to_anchor=(0.5, 0.065), ncol=2, frameon=False, fontsize=11)
    fig.text(0.5, 0.035, "Fair segregation; equal reciprocal gamete probabilities. r is the total recombinant probability.",
             ha="center", fontsize=10, color="#444444")
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.25, top=0.76, wspace=0.15)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
