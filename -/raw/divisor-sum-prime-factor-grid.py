"""Weighted divisor grid for 12; save the basename PNG to the current directory.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
Reproduce: make _media/divisor-sum-prime-factor-grid.png
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    values = np.array([[2**i * 3**j for i in range(3)] for j in range(2)])
    fig, ax = plt.subplots(figsize=(8, 4.8), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    blue, orange = "#245a81", "#a44e16"
    for j, row in enumerate(values):
        for i, value in enumerate(row):
            ax.add_patch(Rectangle((i - 0.5, j - 0.5), 1, 1,
                                   facecolor=("#e6f0f6", "#fff0e1")[j],
                                   edgecolor="white", linewidth=3))
            ax.text(i, j + 0.13, rf"$2^{i}\cdot3^{j}$", ha="center",
                    va="center", fontsize=15, color="#444444")
            ax.text(i, j - 0.20, str(value), ha="center", va="center",
                    fontsize=23, color=(blue, orange)[j], weight="bold")
        ax.text(2.73, j, " + ".join(map(str, row)) + f" = {sum(row)}",
                ha="left", va="center", fontsize=14, color=(blue, orange)[j])
    ax.set_xlim(-0.5, 5.0)
    ax.set_ylim(-0.5, 1.5)
    ax.set_aspect("equal")
    ax.set_xticks([0, 1, 2], [r"$i=0$", r"$i=1$", r"$i=2$"])
    ax.set_yticks([0, 1], [r"$j=0$", r"$j=1$"])
    ax.tick_params(length=0, pad=8, labelsize=13)
    ax.set_xlabel("Exponent of 2", fontsize=13, labelpad=9)
    ax.set_ylabel("Exponent of 3", fontsize=13, labelpad=9)
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.suptitle(r"Sum the divisor weights: $12=2^2\cdot3$", fontsize=18, y=0.95)
    fig.text(0.52, 0.83, "Every cell contributes its divisor value once",
             ha="center", fontsize=13)
    fig.text(0.52, 0.08, r"$\sigma(12)=(1+2+4)(1+3)=7\cdot4=28$",
             ha="center", fontsize=19, color=blue)
    fig.subplots_adjust(left=0.12, right=0.98, bottom=0.25, top=0.77)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
