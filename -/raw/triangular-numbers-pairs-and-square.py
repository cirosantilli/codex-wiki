"""Original pair-counting and square-partition diagram with exact counts.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes its matching PNG into the current directory.
"""

from itertools import combinations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    n = 5
    blue, orange = "#235d9f", "#d4782a"
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.4))
    fig.subplots_adjust(left=0.05, right=0.96, bottom=0.18, top=0.77, wspace=0.18)
    fig.suptitle("The same triangular counts organize pairs and squares", fontsize=18, y=0.97)
    fig.text(0.5, 0.885, "Exact counting examples; the drawings represent mathematical objects, not measurements", ha="center", fontsize=11)
    angles = np.pi / 2 + np.arange(n) * 2 * np.pi / n
    points = np.column_stack([np.cos(angles), np.sin(angles)])
    ax = axes[0]
    for i, j in combinations(range(n), 2):
        ax.plot(points[[i, j], 0], points[[i, j], 1], color="#8eaac4", lw=1.8, zorder=1)
    ax.scatter(points[:, 0], points[:, 1], color=blue, s=180, zorder=3)
    for label, point in zip("ABCDE", points, strict=True):
        ax.text(*(point * 1.24), label, ha="center", va="center", fontsize=14, color=blue)
    ax.set_title("Five objects: ten unordered pairs", fontsize=14, pad=14)
    ax.set(xlim=(-1.4, 1.4), ylim=(-1.2, 1.4))
    ax.text(0, -1.35, r"$\binom{5}{2}=4+3+2+1=T_4=10$", ha="center", fontsize=13)
    ax = axes[1]
    count = {"blue": 0, "orange": 0}
    for row in range(n):
        for col in range(n):
            lower = col <= row
            count["blue" if lower else "orange"] += 1
            ax.add_patch(Rectangle((col, n - row - 1), 1, 1, facecolor=blue if lower else orange, edgecolor="white", lw=2))
    assert count == {"blue": 15, "orange": 10}
    ax.set_title("Consecutive triangles fill a square", fontsize=14, pad=14)
    ax.set(xlim=(-0.2, n + 0.2), ylim=(-0.2, n + 0.2))
    ax.text(n / 2, -0.55, r"$T_5+T_4=15+10=25=5^2$", ha="center", fontsize=13)
    for ax in axes:
        ax.set_aspect("equal")
        ax.axis("off")
    fig.text(0.5, 0.05, "Left: line crossings are not extra vertices. Right: the blue triangle includes the diagonal cells.", ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
