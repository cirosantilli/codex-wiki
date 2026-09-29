"""Draw repeated Fibonacci calls and their distinct dependencies.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def main():
    colors = {0: "#e5ecf0", 1: "#e5ecf0", 2: "#ffe0a7", 3: "#b9e5df", 4: "#c9d8f7", 5: "#d8c8ec"}
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5), dpi=100,
                             gridspec_kw={"width_ratios": [1.65, 1]})
    fig.patch.set_facecolor("white")
    nodes, edges = [], []

    def visit(n, depth):
        index = len(nodes)
        nodes.append([n, None, depth])
        if n < 2:
            nodes[index][1] = sum(node[0] < 2 for node in nodes) - 1
        else:
            left, right = visit(n - 1, depth + 1), visit(n - 2, depth + 1)
            nodes[index][1] = (nodes[left][1] + nodes[right][1]) / 2
            edges.extend([(index, left), (index, right)])
        return index

    visit(5, 0)
    assert len(nodes) == 15 and len(edges) == 14
    ax = axes[0]
    for parent, child in edges:
        x1, y1 = nodes[parent][1:]
        x2, y2 = nodes[child][1:]
        ax.plot([x1, x2], [-y1, -y2], color="#78838c", lw=1.3, zorder=1)
    for n, x, depth in nodes:
        ax.scatter(x, -depth, s=770, color=colors[n], edgecolor="#37434e", zorder=2)
        ax.text(x, -depth, rf"$F_{n}$", ha="center", va="center", fontsize=12, zorder=3)
    ax.set(xlim=(-0.6, 7.6), ylim=(-4.65, 0.55))
    ax.set_title("Repeated recursion: 15 calls", fontsize=15, pad=16)
    ax.text(3.5, -4.6, "Each occurrence is a separate call.\nRepeated labels repeat the same work.",
            ha="center", va="top", fontsize=11)

    ax = axes[1]
    positions = {5: (0, 0), 4: (0, -1), 3: (0, -2), 2: (0, -3),
                 1: (0, -4), 0: (1.4, -4)}
    dag_edges = [(n, n - d) for n in range(2, 6) for d in (1, 2)]
    assert len(dag_edges) == 8
    for n, child in dag_edges:
        bend = -0.43 if n - child == 2 and n > 2 else 0
        ax.add_patch(FancyArrowPatch(positions[n], positions[child],
                                    connectionstyle=f"arc3,rad={bend}", arrowstyle="-|>",
                                    mutation_scale=13, shrinkA=17, shrinkB=17,
                                    color="#78838c", lw=1.4, zorder=1))
    for n, (x, y) in positions.items():
        ax.scatter(x, y, s=770, color=colors[n], edgecolor="#37434e", zorder=2)
        ax.text(x, y, rf"$F_{n}$", ha="center", va="center", fontsize=12, zorder=3)
    ax.set(xlim=(-1, 2.1), ylim=(-4.65, 0.55))
    ax.set_title("Shared dependencies: 6 values", fontsize=15, pad=16)
    ax.text(0.55, -4.6, "Arrow: caller → required value.\nOne stored answer per label.",
            ha="center", va="top", fontsize=11)
    for ax in axes:
        ax.set_facecolor("white")
        ax.axis("off")
    fig.suptitle(r"$F_5=5$: one recurrence, two views of the work", fontsize=17, y=0.97)
    fig.subplots_adjust(left=0.035, right=0.965, top=0.81, bottom=0.17, wspace=0.22)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
