"""Draw original optimal edge colourings; run from _media with Python 3.14.

Tested with matplotlib 3.10.7 and numpy 2.3.5 (root pyproject.toml).
"""

from pathlib import Path

import matplotlib.pyplot as plt


COLORS = {1: "#0072B2", 2: "#D55E00", 3: "#7B4397"}


def draw_graph(ax, positions, colored_edges, title, conclusion):
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.55, 1.55)
    ax.set_ylim(-1.55, 1.6)
    ax.set_title(title, fontsize=16, pad=12)
    for u, v, color in colored_edges:
        x1, y1 = positions[u]
        x2, y2 = positions[v]
        ax.plot([x1, x2], [y1, y2], color=COLORS[color], lw=5, zorder=1)
        ax.text(
            (x1 + x2) / 2,
            (y1 + y2) / 2,
            str(color),
            ha="center",
            va="center",
            fontsize=13,
            fontweight="bold",
            bbox={"boxstyle": "round,pad=0.2", "facecolor": "white", "edgecolor": COLORS[color]},
            zorder=3,
        )
    for vertex, (x, y) in positions.items():
        ax.plot(x, y, "o", ms=11, color="#26323B", zorder=4)
        ax.text(x * 1.22, y * 1.22, vertex, ha="center", va="center", fontsize=14)
    ax.text(0, -1.52, conclusion, ha="center", va="center", fontsize=13)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.4), dpi=120, facecolor="white")
    fig.suptitle("Colour the edges: shared endpoints need different labels", fontsize=16, y=0.97)
    draw_graph(
        axes[0],
        {"a": (0, 1), "b": (-1, -0.7), "c": (1, -0.7)},
        [("a", "b", 1), ("b", "c", 2), ("c", "a", 3)],
        "Triangle: every pair of edges conflicts",
        r"$\Delta=2$, but $\chi^{\prime}=3$",
    )
    draw_graph(
        axes[1],
        {"a": (-1, 0.9), "b": (1, 0.9), "c": (1, -0.9), "d": (-1, -0.9)},
        [("a", "b", 1), ("b", "c", 2), ("c", "d", 1), ("d", "a", 2)],
        "Even cycle: opposite edges can share",
        r"$\Delta=2$ and $\chi^{\prime}=2$",
    )
    fig.subplots_adjust(left=0.03, right=0.97, top=0.79, bottom=0.10, wspace=0.30)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
