"""Draw two original examples separating vertex and edge coverage.

Tested with Python 3.14, matplotlib 3.10.7; run from _media.
Arrowheads indicate traversal order in undirected graphs.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


BLUE = "#1764a0"
ORANGE = "#b95b13"
GRAY = "#a7aeb5"


def edge(ax, positions, u, v, color, number=None):
    p, q = positions[u], positions[v]
    ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=2.8, zorder=1)
    start = tuple(0.58 * a + 0.42 * b for a, b in zip(p, q))
    end = tuple(0.42 * a + 0.58 * b for a, b in zip(p, q))
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=15, lw=2, color=color, zorder=2))
    if number is not None:
        x, y = (0.70 * a + 0.30 * b for a, b in zip(p, q))
        ax.text(x, y, str(number), ha="center", va="center", fontsize=11,
                color=color, bbox=dict(facecolor="white", edgecolor="none", pad=1.5),
                zorder=3)


def nodes(ax, positions):
    for name, (x, y) in positions.items():
        ax.add_patch(Circle((x, y), 0.065, facecolor="white", edgecolor="#263746",
                            lw=1.6, zorder=4))
        ax.text(x, y, name, ha="center", va="center", fontsize=13, zorder=5)
    ax.set(xlim=(-1.35, 1.35), ylim=(-1.55, 1.47), aspect="equal")
    ax.axis("off")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.3), facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.10, top=0.83, wspace=0.17)
    fig.suptitle("Visit every vertex or traverse every edge?", fontsize=18, y=0.96)
    left, right = axes
    square = dict(A=(-0.85, 0.85), B=(0.85, 0.85),
                  C=(0.85, -0.55), D=(-0.85, -0.55))
    for u, v in [("A", "C"), ("B", "D")]:
        p, q = square[u], square[v]
        left.plot([p[0], q[0]], [p[1], q[1]], color=GRAY, lw=1.8, ls="--")
    tour = ["A", "B", "C", "D", "A"]
    for u, v in zip(tour, tour[1:]):
        edge(left, square, u, v, BLUE)
    nodes(left, square)
    left.set_title(r"Complete graph $K_4$", fontsize=15, pad=10)
    left.text(0, -0.92, "A → B → C → D → A", ha="center", fontsize=13, color=BLUE)
    left.text(0, -1.19, "Hamilton cycle; omits both diagonals", ha="center", fontsize=11)
    left.text(0, -1.44, "All four degrees are 3: no Euler circuit", ha="center", fontsize=11)
    bow = dict(X=(0, 0.12), A=(-1, 0.87), B=(-1, -0.63),
               C=(1, 0.87), D=(1, -0.63))
    walk = ["X", "A", "B", "X", "C", "D", "X"]
    for i, (u, v) in enumerate(zip(walk, walk[1:]), 1):
        edge(right, bow, u, v, ORANGE, i)
    nodes(right, bow)
    right.set_title("Two triangles sharing X", fontsize=15, pad=10)
    right.text(0, -0.92, "X → A → B → X → C → D → X", ha="center", fontsize=12,
               color=ORANGE)
    right.text(0, -1.19, "Euler circuit; X occurs again midway", ha="center", fontsize=11)
    right.text(0, -1.44, "X is a cut vertex: no Hamilton cycle", ha="center", fontsize=11)
    fig.text(0.5, 0.04, "Arrows show the chosen traversal; every graph edge is undirected.",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
