"""Two spanning trees of one cyclic graph; PNG goes to cwd (Python 3.14)."""

from collections import deque
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


TREE = ((1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7))
GRAPH = TREE + ((5, 7),)
EXCHANGED = tuple(e for e in GRAPH if e != (1, 3))
POSITIONS = {1: (0, 2), 2: (-1, 1), 3: (1, 1),
             4: (-1.6, 0), 5: (-0.4, 0), 6: (1, 0), 7: (1, -1)}
BLUE, ORANGE, DARK = "#176997", "#c05422", "#273746"


def distances(edges, source):
    result, todo = {source: 0}, deque([source])
    while todo:
        v = todo.popleft()
        for a, b in edges:
            w = b if a == v else a if b == v else None
            if w is not None and w not in result:
                result[w] = result[v] + 1
                todo.append(w)
    return result


def draw(ax, edges, highlighted):
    highlighted = {frozenset(e) for e in highlighted}
    for a, b in edges:
        color = ORANGE if frozenset((a, b)) in highlighted else BLUE
        ax.plot([POSITIONS[a][0], POSITIONS[b][0]],
                [POSITIONS[a][1], POSITIONS[b][1]], color=color, lw=3, zorder=1)
    for v, (x, y) in POSITIONS.items():
        ax.scatter(x, y, s=580, color="white", edgecolors=BLUE,
                   linewidths=2.2, zorder=3)
        ax.text(x, y, str(v), color=DARK, ha="center", va="center",
                fontsize=13, zorder=4)
    ax.set(xlim=(-1.95, 1.65), ylim=(-1.45, 2.55), aspect="equal")
    ax.axis("off")


def main():
    for edges in (TREE, EXCHANGED):
        assert len(edges) == 6 and len(distances(edges, 1)) == 7
    assert distances(GRAPH, 5)[7] == distances(EXCHANGED, 5)[7] == 1
    assert distances(TREE, 5)[7] == 5
    assert distances(GRAPH, 1)[3] == distances(TREE, 1)[3] == 1
    assert distances(EXCHANGED, 1)[3] == 5
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.7), dpi=120,
                             facecolor="white")
    draw(axes[0], GRAPH, ((5, 7), (1, 3)))
    draw(axes[1], TREE, ((5, 2), (2, 1), (1, 3), (3, 6), (6, 7)))
    draw(axes[2], EXCHANGED, ((1, 2), (2, 5), (5, 7), (7, 6), (6, 3)))
    titles = ("Connected cyclic graph G: 7 edges", "Tree T: omit 5–7 (6 edges)",
              "Tree T′: omit 1–3 (6 edges)")
    captions = ("d(5, 7) = 1     d(1, 3) = 1", "d(5, 7) = 5     d(1, 3) = 1",
                "d(5, 7) = 1     d(1, 3) = 5")
    for ax, title, caption in zip(axes, titles, captions):
        ax.set_title(title, fontsize=11, pad=10)
        ax.text(0.5, -0.055, caption, transform=ax.transAxes, ha="center",
                fontsize=11, color=DARK)
    fig.suptitle("Spanning trees preserve reachability, but can lengthen routes", fontsize=14)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.86, bottom=0.15, wspace=0.08)
    fig.savefig(Path.cwd() / "spanning-tree-cycle-exchange.png", facecolor="white",
                transparent=False)
    plt.close(fig)
    print("Verified distances (5,7)/(1,3): G=1/1, T=5/1, T′=1/5.")


if __name__ == "__main__":
    main()
