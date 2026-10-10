"""Draw original schematic routes; run from _media with Matplotlib's Agg backend.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
No external image assets or measured data are used.
"""

from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


POSITIONS = {
    "A": (0, 0), "B": (-1, 0.75), "C": (-1, -0.75),
    "D": (1, 0.75), "E": (1, -0.75), "F": (0, -1.35),
}
EDGES = ("AB", "BC", "CA", "AD", "DE", "EA", "AF")
ROUTES = (
    ("Walk: edges may repeat", "BCABCAF", "#596b89", "Not a trail: BC and CA each occur twice."),
    ("Trail: no repeated edges", "BCADEAF", "#187454", "Not a path: the junction A occurs twice."),
    ("Path: no repeated vertices", "BCAF", "#2468a0", "All four vertices, and all three edges, are distinct."),
)


def edge_key(u, v):
    """The two travel directions identify the same undirected edge."""
    return tuple(sorted((u, v)))


def draw_graph(ax, route, color):
    used = Counter(edge_key(u, v) for u, v in zip(route, route[1:]))
    assert set(used) <= {edge_key(*e) for e in EDGES}
    for u, v in EDGES:
        count = used[edge_key(u, v)]
        x1, y1 = POSITIONS[u]
        x2, y2 = POSITIONS[v]
        shade = "#aa3543" if count > 1 else color if count else "#d4dce3"
        ax.plot((x1, x2), (y1, y2), color=shade, lw=3 if count else 1.5, zorder=1)
        if count > 1:
            ax.text((x1 + x2) / 2 - 0.17, (y1 + y2) / 2, f"×{count}",
                    fontsize=10, color=shade, ha="center", va="center",
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 1}, zorder=3)
    for name, (x, y) in POSITIONS.items():
        ax.add_patch(Circle((x, y), 0.14, facecolor="white", edgecolor="#354659", lw=1.4, zorder=4))
        ax.text(x, y, name, ha="center", va="center", fontsize=12, color="#172f46", zorder=5)
    ax.set(xlim=(-1.45, 1.45), ylim=(-1.65, 1.1), aspect="equal")
    ax.axis("off")


def draw_order(ax, route, color, explanation):
    counts = Counter(route)
    edge_counts = Counter(edge_key(u, v) for u, v in zip(route, route[1:]))
    xs = [0.045 + i * 0.14 for i in range(len(route))]
    for i, (u, v) in enumerate(zip(route, route[1:])):
        shade = "#aa3543" if edge_counts[edge_key(u, v)] > 1 else color
        ax.add_patch(FancyArrowPatch((xs[i] + 0.033, 0.58), (xs[i + 1] - 0.033, 0.58),
                                    arrowstyle="-|>", mutation_scale=12, lw=1.6, color=shade))
        ax.text((xs[i] + xs[i + 1]) / 2, 0.72, str(i + 1), fontsize=10, color=shade, ha="center")
    for x, name in zip(xs, route):
        face = "#fff0cb" if counts[name] > 1 else "#edf4fa"
        ax.text(x, 0.58, name, ha="center", va="center", fontsize=14, color="#172f46",
                bbox={"boxstyle": "circle,pad=0.3", "facecolor": face, "edgecolor": "#64798b"})
    ax.text(0.02, 0.31, explanation, fontsize=12, color="#243b50")
    ax.text(0.02, 0.12,
            f"Length {len(route) - 1}   •   {len(edge_counts)} distinct edges   •   {len(counts)} distinct vertices",
            fontsize=11, color="#536a7d")
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": "white", "axes.facecolor": "white"})
    fig = plt.figure(figsize=(11, 7.6), dpi=100)
    fig.text(0.045, 0.957, "Walk, trail, path: what is allowed to repeat?", fontsize=20, weight="bold", color="#172f46")
    fig.text(0.045, 0.915, "Same undirected graph in every row. Arrows in the journey record show travel order.", fontsize=11, color="#536a7d")
    for i, (title, route, color, explanation) in enumerate(ROUTES):
        top = 0.855 - i * 0.268
        fig.text(0.045, top, title, fontsize=15, weight="bold", color=color)
        draw_graph(fig.add_axes((0.035, top - 0.226, 0.26, 0.218)), route, color)
        draw_order(fig.add_axes((0.32, top - 0.218, 0.645, 0.195)), route, color, explanation)
    fig.text(0.045, 0.025, "Amber circles mark repeated vertex labels; red steps mark reused edges. Original analytical illustration.", fontsize=10, color="#536a7d")
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
