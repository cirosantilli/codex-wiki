"""Group polynomial product terms by total contribution; write PNG to cwd.

Uses the repository's NumPy and Matplotlib dependencies, Python 3.14.4.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    colours = ["#426c91", "#bd6f26", "#338773", "#805b9b"]
    counts = np.convolve([1, 1, 1], [1, 1])
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.5), dpi=120)
    fig.patch.set_facecolor("white")
    ax = axes[0]
    for i in range(3):
        for j in range(2):
            total = i + j
            ax.add_patch(Rectangle((i - 0.46, j - 0.43), 0.92, 0.86,
                                   facecolor=colours[total], edgecolor="white"))
            ax.text(i, j + 0.14, f"({i}, {j})", ha="center", va="center",
                    fontsize=14, color="white")
            ax.text(i, j - 0.19, f"total {total}", ha="center", va="center",
                    fontsize=11, color="white")
    ax.set(xlim=(-0.6, 2.6), ylim=(-0.55, 1.55), xticks=range(3), yticks=range(2),
           xlabel="First contribution i", ylabel="Second contribution j")
    ax.set_aspect("equal")
    ax.set_title("Six ordered choices", fontsize=13, pad=14)
    ax.tick_params(length=0, labelsize=11)
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax = axes[1]
    ax.bar(range(4), counts, width=0.62, color=colours)
    for total, count in enumerate(counts):
        ax.text(total, count + 0.08, str(count), ha="center", fontsize=14)
    ax.set(xlim=(-0.65, 3.65), ylim=(0, 2.6), xticks=range(4), yticks=[0, 1, 2],
           xlabel="Total contribution n = i + j", ylabel="Number of choices")
    ax.set_title("Coefficients group equal totals", fontsize=13, pad=14)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=11)
    fig.suptitle(r"$(1+x+x^2)(1+x)=1+2x+2x^2+x^3$", fontsize=17, y=0.98)
    fig.text(0.5, 0.035, "Matching colours connect choices to the coefficient they contribute.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.19, top=0.78, wspace=0.34)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
