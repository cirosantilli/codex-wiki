"""Draw an original six-vertex graph and its adjacency lists.

Run from _media; writes adjacency-list-six-vertex-graph.png to the CWD.
Tested with Python 3.14, matplotlib 3.10.7; no external image assets.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle


VERTICES = tuple("ABCDEF")
EDGES = ("AB", "AC", "BC", "CD", "DE", "DF", "EF")
BLUE = "#24639b"
TEAL = "#087f83"
INK = "#243543"


def main():
    lists = {v: [] for v in VERTICES}
    for u, v in EDGES:
        lists[u].append(v)
        lists[v].append(u)
    assert len(EDGES) == 7 and sum(map(len, lists.values())) == 14
    plt.rcParams.update({"font.size": 13, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11.2, 5.5), dpi=100, facecolor="white")
    graph_ax = fig.add_axes((0.025, 0.18, 0.49, 0.64))
    list_ax = fig.add_axes((0.57, 0.15, 0.40, 0.69))
    fig.suptitle("One undirected graph, seven edges", y=0.96, fontsize=20, color=INK)
    graph_ax.set_title("Each edge is traversable from either endpoint", fontsize=12, pad=22)
    positions = {"A": (0, 1.8), "B": (0, 0), "C": (1.7, 0.9),
                 "D": (3.35, 0.9), "E": (5.05, 1.8), "F": (5.05, 0)}
    for u, v in EDGES:
        a, b = positions[u], positions[v]
        color = TEAL if "C" in (u, v) else BLUE
        graph_ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-", color=color,
                                          linewidth=2.6, zorder=1))
    for v, pos in positions.items():
        graph_ax.add_patch(Circle(pos, 0.23, facecolor=TEAL if v == "C" else "white",
                                  edgecolor=TEAL if v == "C" else BLUE, linewidth=2.3, zorder=2))
        graph_ax.text(*pos, v, ha="center", va="center", fontsize=17,
                      color="white" if v == "C" else INK, zorder=3)
    graph_ax.set(xlim=(-0.5, 5.55), ylim=(-0.55, 2.35), aspect="equal")
    graph_ax.axis("off")
    list_ax.set_title("Outgoing destinations: Adj[v]", fontsize=15, pad=13)
    for row, v in enumerate(VERTICES):
        y = 5 - row
        color = TEAL if v == "C" else BLUE
        if v == "C":
            list_ax.add_patch(Rectangle((-0.63, y - 0.40), 4.52, 0.8,
                                        facecolor="#e6f4f3", edgecolor="none", zorder=0))
        list_ax.text(-0.33, y, v, ha="center", va="center", color=color, weight="bold", fontsize=16)
        list_ax.add_patch(FancyArrowPatch((-0.06, y), (0.38, y), arrowstyle="->",
                                         mutation_scale=12, linewidth=1.4, color=color))
        for col, neighbour in enumerate(lists[v]):
            x = 0.5 + col * 0.92
            list_ax.add_patch(Rectangle((x, y - 0.30), 0.75, 0.60,
                                        facecolor="white", edgecolor=color, linewidth=1.6))
            list_ax.text(x + 0.375, y, neighbour, ha="center", va="center", color=INK, fontsize=16)
    list_ax.set(xlim=(-0.7, 4), ylim=(-0.8, 5.8))
    list_ax.axis("off")
    fig.text(0.26, 0.115, "From C: A, B, D", ha="center", color=TEAL, fontsize=15, weight="bold")
    fig.text(0.77, 0.07, "6 lists · 14 neighbour entries", ha="center", color=INK, fontsize=14)
    fig.text(0.50, 0.018, "CD is stored as D in C's list and as C in D's list.  Display order is not required.",
             ha="center", color=INK, fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
