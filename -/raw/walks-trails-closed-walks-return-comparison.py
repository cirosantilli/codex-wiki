"""Draw original closed journeys on two triangles with an attached leaf.

Run from _media with Matplotlib's Agg backend. Tested with Python 3.14.4,
NumPy 2.3.5, and Matplotlib 3.10.7. All connections are constructed examples.
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
RETURNS = (
    ("Backtracking", "AFA", "#aa3543", "AF is used twice.", "Closed walk; not a trail.", "Length 2"),
    ("Two excursions", "ABCADEA", "#187454", "All six edges are distinct.", "Closed trail; not a cycle.", "Length 6; A also occurs internally"),
    ("One cycle", "ABCA", "#2468a0", "Only the endpoints repeat.", "Closed trail and cycle.", "Length 3"),
)


def edge_key(u, v):
    return tuple(sorted((u, v)))


def draw_graph(ax, route, color):
    used = Counter(edge_key(u, v) for u, v in zip(route, route[1:]))
    assert route[0] == route[-1]
    assert set(used) <= {edge_key(*e) for e in EDGES}
    for u, v in EDGES:
        count = used[edge_key(u, v)]
        (x1, y1), (x2, y2) = POSITIONS[u], POSITIONS[v]
        ax.plot((x1, x2), (y1, y2), color=color if count else "#d4dce3", lw=3 if count else 1.5)
        if count > 1:
            ax.text((x1 + x2) / 2 + 0.16, (y1 + y2) / 2, "×2", color=color, fontsize=12,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    for name, (x, y) in POSITIONS.items():
        ax.add_patch(Circle((x, y), 0.145, facecolor="#eaf2fa" if name == "A" else "white",
                            edgecolor="#354659", lw=1.4, zorder=3))
        ax.text(x, y, name, ha="center", va="center", fontsize=13, color="#172f46", zorder=4)
    ax.set(xlim=(-1.4, 1.4), ylim=(-1.65, 1.1), aspect="equal")
    ax.axis("off")


def draw_order(ax, route, color):
    xs = [0.065 + i * 0.14 for i in range(len(route))]
    for i in range(len(route) - 1):
        ax.add_patch(FancyArrowPatch((xs[i] + 0.03, 0.5), (xs[i + 1] - 0.03, 0.5),
                                    arrowstyle="-|>", mutation_scale=10, lw=1.4, color=color))
        ax.text((xs[i] + xs[i + 1]) / 2, 0.81, str(i + 1), ha="center", fontsize=9, color=color)
    for i, (x, name) in enumerate(zip(xs, route)):
        face = "#fff0cb" if 0 < i < len(route) - 1 and name == route[0] else "#eaf2fa"
        ax.text(x, 0.5, name, ha="center", va="center", fontsize=12, color="#172f46",
                bbox={"boxstyle": "circle,pad=0.22", "facecolor": face, "edgecolor": "#64798b"})
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": "white", "axes.facecolor": "white"})
    fig = plt.figure(figsize=(11.4, 6.5), dpi=100)
    fig.text(0.04, 0.95, "A return journey need not be a cycle", fontsize=21, weight="bold", color="#172f46")
    fig.text(0.04, 0.901, "Every journey starts and ends at A on the same constructed undirected graph.", fontsize=12, color="#536a7d")
    for i, (title, route, color, reason, verdict, length) in enumerate(RETURNS):
        left = 0.03 + i * 0.326
        fig.text(left + 0.012, 0.824, title, fontsize=17, weight="bold", color=color)
        draw_graph(fig.add_axes((left, 0.39, 0.302, 0.402)), route, color)
        draw_order(fig.add_axes((left + 0.004, 0.3, 0.299, 0.085)), route, color)
        fig.text(left + 0.012, 0.254, length, fontsize=10.5, color="#536a7d")
        fig.text(left + 0.012, 0.198, reason, fontsize=12, color="#243b50")
        fig.text(left + 0.012, 0.139, verdict, fontsize=12.5, weight="bold", color=color)
    fig.text(0.04, 0.067, "Numbered arrows show travel steps, not edge orientations. Amber marks the extra internal visit to A.", fontsize=10, color="#536a7d")
    fig.text(0.04, 0.032, "Original analytical illustration: graph connections and journey order, with no measured distances.", fontsize=10, color="#536a7d")
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
