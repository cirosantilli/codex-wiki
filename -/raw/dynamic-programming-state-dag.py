"""Draw knapsack dependencies in cwd; Python 3.14.4 and Matplotlib.

Subset enumeration and dependency checks use only the standard library.
Output: dynamic-programming-state-dag.png, normally in _media via Make.
"""

from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


WEIGHTS = (2, 3, 4)
VALUES = (3, 4, 5)
CAPACITY = 5
ORANGE = "#b75516"
BLUE = "#6496b8"
INK = "#172b3b"


def example():
    rows = [[0] * (CAPACITY + 1)]
    edges = []
    for i, (weight, value) in enumerate(zip(WEIGHTS, VALUES), start=1):
        previous = rows[-1]
        row = []
        for w in range(CAPACITY + 1):
            skip = previous[w]
            edges.append(((i, w), (i - 1, w), 0, "skip"))
            if w >= weight:
                take = value + previous[w - weight]
                edges.append(((i, w), (i - 1, w - weight), value, "take"))
                row.append(max(skip, take))
            else:
                row.append(skip)
        rows.append(row)
    path = []
    i, w = len(WEIGHTS), CAPACITY
    while i:
        if rows[i][w] == rows[i - 1][w]:
            next_state, reward, action = (i - 1, w), 0, "skip"
        else:
            next_state = (i - 1, w - WEIGHTS[i - 1])
            reward, action = VALUES[i - 1], "take"
        path.append(((i, w), next_state, reward, action))
        i, w = next_state
    return rows, edges, path


def check_example(rows, edges, path):
    for i, row in enumerate(rows):
        for w, value in enumerate(row):
            feasible = [bits for bits in product((0, 1), repeat=i)
                        if sum(b * weight for b, weight in zip(bits, WEIGHTS[:i])) <= w]
            assert value == max(sum(b * v for b, v in zip(bits, VALUES[:i]))
                                for bits in feasible)
            if i:
                dependencies = [edge for edge in edges if edge[0] == (i, w)]
                assert value == max(reward + rows[j][capacity]
                                    for _, (j, capacity), reward, _ in dependencies)
    assert len(edges) == 18 + 4 + 3 + 2 == 27
    assert all(start[0] == end[0] + 1 and end[1] >= 0 for start, end, _, _ in edges)
    assert path == [((3, 5), (2, 5), 0, "skip"),
                    ((2, 5), (1, 2), 4, "take"),
                    ((1, 2), (0, 0), 3, "take")]
    assert all(edge in edges for edge in path)
    assert sum(reward for _, _, reward, _ in path) == rows[3][5] == 7
    assert sum(start[1] - end[1] for start, end, _, _ in path) == 5
    assert all(rows[i][w] == reward + rows[j][capacity]
               for (i, w), (j, capacity), reward, _ in path)
    print("Verified 24 values by subset enumeration; 27 acyclic dependencies;")
    print("reconstructed (3,5) -> (2,5) -> (1,2) -> (0,0), weight 5, reward 7.")


def coordinates(state):
    i, w = state
    return (3 - i) * 3.1, w


def draw_edge(ax, edge, selected=False):
    start, end, _, action = edge
    ax.add_patch(FancyArrowPatch(coordinates(start), coordinates(end),
                                 arrowstyle="-|>", mutation_scale=15 if selected else 11,
                                 shrinkA=36, shrinkB=36,
                                 color=ORANGE if selected else (BLUE if action == "take" else "#b6bfc5"),
                                 linewidth=2.9 if selected else 1.15,
                                 linestyle="solid" if selected or action == "take" else "dashed",
                                 zorder=3 if selected else 1))


def main():
    rows, edges, path = example()
    check_example(rows, edges, path)
    plt.rcParams.update({"font.size": 12, "text.color": INK})
    fig, ax = plt.subplots(figsize=(10.6, 6.8), dpi=110, facecolor="white")
    fig.subplots_adjust(left=0.045, right=0.98, top=0.86, bottom=0.15)
    fig.suptitle("Dependencies point to smaller knapsack subproblems", fontsize=17, y=0.96)
    fig.text(0.5, 0.905, "Node: (i, W), optimal value V     Orange arrows: one optimal selection",
             ha="center", fontsize=12)
    for edge in edges:
        draw_edge(ax, edge)
    for edge in path:
        draw_edge(ax, edge, selected=True)
    path_nodes = {state for edge in path for state in edge[:2]}
    for i in range(4):
        x, _ = coordinates((i, 0))
        ax.text(x, 5.75, rf"$i={i}$" if i else r"$i=0$: base", ha="center", fontsize=14)
        for w in range(CAPACITY + 1):
            x, y = coordinates((i, w))
            selected = (i, w) in path_nodes
            ax.add_patch(FancyBboxPatch((x - 0.49, y - 0.24), 0.98, 0.48,
                                        boxstyle="round,pad=0.025", zorder=4,
                                        facecolor="#fff0e5" if selected else "white",
                                        edgecolor=ORANGE if selected else "#899eac",
                                        linewidth=2 if selected else 1))
            ax.text(x, y, f"({i}, {w})\nV = {rows[i][w]}", ha="center", va="center",
                    fontsize=10.5, linespacing=1.1, color=ORANGE if selected else INK, zorder=5)
    for i, label in ((3, "Skip item 3: +0"), (2, "Take item 2: +4"), (1, "Take item 1: +3")):
        x, _ = coordinates((i, 0))
        ax.text(x + 1.55, 5.40, label, ha="center", color=ORANGE, fontsize=11)
    ax.set(xlim=(-0.7, 10.05), ylim=(-0.45, 6.10))
    ax.axis("off")
    fig.text(0.5, 0.095, "Dashed gray: skip (+0)     Blue: take (+item value)     Orange: optimal choices",
             ha="center", fontsize=11)
    fig.text(0.5, 0.045, "Compute right to left from the base; reconstruct left to right. Total reward: 0 + 4 + 3 = 7.",
             ha="center", fontsize=11)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}: 1166 x 748 pixels, opaque white background.")


if __name__ == "__main__":
    main()
