"""Draw K4 twice. Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; the PNG is written to the current working directory.
"""

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.6), dpi=100, facecolor="white")
    positions = [
        {"A": (-1, -1), "B": (1, -1), "C": (1, 1), "D": (-1, 1)},
        {"A": (-1.1, -0.8), "B": (1.1, -0.8), "C": (0, 1.1), "D": (0, -0.1)},
    ]
    edges = list(combinations("ABCD", 2))
    for index, (ax, pos) in enumerate(zip(axes, positions)):
        if index == 1:
            for triangle, color in zip(["ABD", "BCD", "CAD"], ["#dff0fb", "#e3f4e5", "#fff0ce"]):
                ax.add_patch(Polygon([pos[v] for v in triangle], color=color, zorder=0))
        for a, b in edges:
            xy = np.array([pos[a], pos[b]])
            color = "#bb5a14" if index == 0 and (a + b) in ["AC", "BD"] else "#34495e"
            ax.plot(xy[:, 0], xy[:, 1], color=color, lw=2.2, zorder=1)
        for vertex, (x, y) in pos.items():
            ax.plot(x, y, "o", ms=8, color="#17354d", zorder=3)
            dx, dy = (0.14, 0.02) if vertex == "D" and index == 1 else (0, 0.17 if y > 0 else -0.2)
            ax.text(x + dx, y + dy, vertex, ha="center", va="center", weight="bold")
        ax.set(xlim=(-1.55, 1.65), ylim=(-1.55, 1.6), aspect="equal")
        ax.axis("off")
    axes[0].set_title("A crossing in this drawing", weight="bold", pad=12)
    axes[0].annotate("Crossing, not a vertex", xy=(0, 0), xytext=(0, 1.45),
                     ha="center", fontsize=11, color="#a34b12",
                     arrowprops={"arrowstyle": "->", "color": "#a34b12", "connectionstyle": "arc3,rad=.18"})
    axes[1].set_title("A plane embedding of the same graph", weight="bold", pad=12, fontsize=12)
    for label, xy in [("1", (-0.35, 0.15)), ("2", (0.35, 0.15)), ("3", (0, -0.55)), ("4: outer", (1.05, 0.7))]:
        axes[1].text(*xy, label, ha="center", va="center", fontsize=12, color="#37474f")
    fig.text(0.25, 0.12, "4 vertices · 6 edges\nThe crossing does not prove nonplanarity.", ha="center", fontsize=11)
    fig.text(0.75, 0.12, "4 vertices · 6 edges · 4 faces\n4 − 6 + 4 = 2", ha="center", fontsize=11)
    fig.suptitle("K₄: connections stay the same when vertices move", y=0.98, fontsize=15)
    fig.subplots_adjust(left=0.025, right=0.985, bottom=0.21, top=0.82, wspace=0.22)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
