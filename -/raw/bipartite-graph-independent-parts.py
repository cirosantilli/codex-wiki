"""Draw one exact graph in two layouts; run from _media with Python 3.14.

Tested with matplotlib 3.10.7 and numpy 2.3.5. The output uses this script's
basename in the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

VERTICES = (1, 2, 3, 4, 5, 6, "z")
EDGES = ((1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1))
PARTS = ({1, 3, 5, "z"}, {2, 4, 6})
BLUE, ORANGE = "#1766a5", "#bd5b09"


def draw(ax, positions):
    for u, v in EDGES:
        ax.plot(*zip(positions[u], positions[v]), color="#687680", lw=2, zorder=1)
    for vertex in VERTICES:
        x, y = positions[vertex]
        ax.scatter(x, y, s=720, color=BLUE if vertex in PARTS[0] else ORANGE,
                   edgecolors="white", linewidths=1.7, zorder=2)
        ax.text(x, y, str(vertex), color="white", ha="center", va="center",
                fontsize=14, weight="bold", zorder=3)
    ax.set_aspect("equal")
    ax.axis("off")


def main():
    assert PARTS[0].isdisjoint(PARTS[1])
    assert PARTS[0] | PARTS[1] == set(VERTICES)
    assert all((u in PARTS[0]) != (v in PARTS[0]) for u, v in EDGES)
    assert all("z" not in edge for edge in EDGES)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.6), facecolor="white")
    angles = np.pi / 2 - np.arange(6) * np.pi / 3
    circle = {i + 1: (float(np.cos(a)), float(np.sin(a))) for i, a in enumerate(angles)}
    circle["z"] = (-1.55, -1.25)
    columns = {1: (-1, 1.15), 3: (-1, 0), 5: (-1, -1.15),
               "z": (-1, -2.05), 2: (1, 1.15), 4: (1, 0), 6: (1, -1.15)}
    draw(axes[0], circle)
    draw(axes[1], columns)
    axes[0].set(xlim=(-2.0, 1.65), ylim=(-2.35, 1.8))
    axes[1].set(xlim=(-1.85, 1.85), ylim=(-2.45, 1.8))
    axes[0].set_title("Cycle layout", pad=7, fontsize=15)
    axes[1].set_title("Two independent parts", pad=7, fontsize=15)
    axes[0].text(-1.15, -1.3, "isolated", color="#42515a", fontsize=11)
    axes[1].text(-1, 1.63, "X", color=BLUE, ha="center", fontsize=14, weight="bold")
    axes[1].text(1, 1.63, "Y", color=ORANGE, ha="center", fontsize=14, weight="bold")
    fig.suptitle("Same graph, same edges, two views", fontsize=18, y=0.97)
    fig.text(0.5, 0.04, "Every edge crosses the parts.  The isolated vertex z may join either part.",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.12, top=0.83, wspace=0.15)
    fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
