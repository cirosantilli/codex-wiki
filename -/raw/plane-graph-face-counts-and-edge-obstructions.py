"""Compare actual plane faces with hypothetical obstruction counts.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media; write a matching PNG basename to the current directory.
"""

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def draw(ax, pos, edges, colors=None):
    for u, v in edges:
        points = np.array([pos[u], pos[v]])
        ax.plot(points[:, 0], points[:, 1], color="#42586a", lw=1.8, zorder=1)
    for v, (x, y) in pos.items():
        ax.plot(x, y, "o", ms=8, color=(colors or {}).get(v, "#17354d"), zorder=2)
    ax.set(xlim=(-1.35, 1.35), ylim=(-1.35, 1.35), aspect="equal")
    ax.axis("off")


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 4, figsize=(11.6, 5.8), dpi=100, facecolor="white")
    path = {0: (-1, 0), 1: (0, 0), 2: (1, 0)}
    draw(axes[0], path, [(0, 1), (1, 2)])
    axes[0].text(0, 0.55, "One outer face", ha="center", fontsize=11)
    axes[0].text(0, -0.55, "Boundary length 4\n(each bridge twice)", ha="center", fontsize=11)
    square = {0: (-0.8, -0.8), 1: (0.8, -0.8), 2: (0.8, 0.8), 3: (-0.8, 0.8)}
    axes[1].add_patch(Polygon(list(square.values()), color="#e3f4e5", zorder=0))
    draw(axes[1], square, [(0, 1), (1, 2), (2, 3), (3, 0)])
    axes[1].text(0, 0, "Inner", ha="center", fontsize=11)
    axes[1].text(0, 1.08, "Outer", ha="center", fontsize=11)
    pentagon = {i: (np.cos(t), np.sin(t)) for i, t in enumerate(np.pi / 2 + np.arange(5) * 2 * np.pi / 5)}
    draw(axes[2], pentagon, list(combinations(range(5), 2)))
    bipartite = {i: (-0.9 if i < 3 else 0.9, 0.9 - 0.9 * (i % 3)) for i in range(6)}
    draw(axes[3], bipartite, [(u, v) for u in range(3) for v in range(3, 6)],
         {i: "#2477a8" if i < 3 else "#a05092" for i in range(6)})
    titles = ["Three-vertex path", "Square cycle", "$K_5$", "$K_{3,3}$"]
    for ax, title in zip(axes, titles):
        ax.set_title(title, weight="bold", pad=12)
    xs = [0.14, 0.38, 0.62, 0.86]
    rows = [
        ["n = 3, m = 2", "n = 4, m = 4", "n = 5, m = 10", "n = 6, m = 9"],
        ["f = 1 (actual)", "f = 2 (actual)", "f = 7 would be needed", "f = 5 would be needed"],
        ["3 − 2 + 1 = 2", "4 − 4 + 2 = 2", "3f = 21 > 2m = 20", "4f = 20 > 2m = 18"],
        ["One plane embedding", "One plane embedding", "Impossible plane embedding", "Impossible plane embedding"],
    ]
    for row_index, row in enumerate(rows):
        for col, value in enumerate(row):
            fig.text(xs[col], 0.34 - row_index * 0.067, value, ha="center", va="center",
                     fontsize=10.5, color="#9b3b21" if col > 1 and row_index > 0 else "#263c4b")
    fig.suptitle("Euler face counts: actual examples and contradictions", fontsize=15, y=0.97)
    fig.text(0.74, 0.86, "These two drawings have crossings; their visible regions are not the claimed f.",
             ha="center", fontsize=10, color="#9b3b21")
    fig.text(0.5, 0.055, "Always include the outer face. Right-hand f values assume a plane embedding and lead to contradictions.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=0.025, right=0.985, bottom=0.43, top=0.79, wspace=0.12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
