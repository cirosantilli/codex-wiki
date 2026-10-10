"""Original dot-counting illustration; all counts are exact, not measured data.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes its matching PNG into the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    n = 6
    blue, orange = "#235d9f", "#d4782a"
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.2))
    fig.subplots_adjust(left=0.05, right=0.97, bottom=0.19, top=0.77, wspace=0.18)
    fig.suptitle("Triangular numbers: pair the rows to see the formula", fontsize=18, y=0.97)
    fig.text(0.5, 0.885, r"Here $n=6$: six growing rows contain $T_6=1+2+3+4+5+6=21$ dots", ha="center")
    ax = axes[0]
    for row in range(n):
        xx = np.arange(row + 1) - row / 2
        ax.scatter(xx, np.full(row + 1, -row * np.sqrt(3) / 2), color=blue, s=105)
        ax.text(3.2, -row * np.sqrt(3) / 2, str(row + 1), ha="left", va="center", color=blue)
    ax.set_title("One growing triangle: 21 dots", fontsize=14, pad=14)
    ax.set(xlim=(-3.2, 4.1), ylim=(-4.8, 0.6))
    ax = axes[1]
    for row in range(n):
        for col in range(n + 1):
            ax.scatter(col, n - 1 - row, color=blue if col <= row else orange, s=105)
        ax.text(n + 0.55, n - 1 - row, f"{row + 1} + {n - row} = {n + 1}", va="center", fontsize=11)
    ax.plot([-0.45, n + 0.45, n + 0.45, -0.45, -0.45], [-0.45, -0.45, n - 0.55, n - 0.55, -0.45], color="#8695a3", lw=1.2)
    ax.set_title("Two triangles: 6 rows × 7 dots", fontsize=14, pad=14)
    ax.set(xlim=(-0.8, n + 3.2), ylim=(-0.8, n - 0.1))
    for ax in axes:
        ax.set_aspect("equal")
        ax.axis("off")
    fig.text(0.5, 0.09, r"Each row has $n+1$ dots after pairing: $2T_n=n(n+1)$, so $T_n=n(n+1)/2$.", ha="center", fontsize=13)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
