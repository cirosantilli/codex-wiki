"""All sixteen fixed-label trees, independently enumerated; Python 3.14.

Write the matching opaque PNG into the current working directory.
"""

from itertools import combinations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def adjacency_of(edges):
    adjacency = {v: set() for v in range(1, 5)}
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    return adjacency


def is_connected(edges):
    adjacency = adjacency_of(edges)
    visited, pending = set(), [1]
    while pending:
        v = pending.pop()
        if v not in visited:
            visited.add(v)
            pending.extend(adjacency[v] - visited)
    return len(visited) == 4


def encode(edges):
    adjacency, code = adjacency_of(edges), []
    for _ in range(2):
        leaf = min(v for v in adjacency if len(adjacency[v]) == 1)
        neighbour = next(iter(adjacency[leaf]))
        code.append(neighbour)
        adjacency[neighbour].remove(leaf)
        del adjacency[leaf]
    return tuple(code)


def layout(edges):
    adjacency = adjacency_of(edges)
    centre = next((v for v in adjacency if len(adjacency[v]) == 3), None)
    if centre is not None:
        leaves = sorted(set(adjacency) - {centre})
        return dict(zip([centre] + leaves, [(0, 0), (0, 0.9), (-0.8, -0.65), (0.8, -0.65)]))
    start = min(v for v in adjacency if len(adjacency[v]) == 1)
    order, previous, current = [], None, start
    while current is not None:
        order.append(current)
        following = adjacency[current] - ({previous} if previous is not None else set())
        previous, current = current, next(iter(following), None)
    return {v: (x, 0) for v, x in zip(order, [-1.15, -0.38, 0.38, 1.15])}


def main():
    trees = [edges for edges in combinations(list(combinations(range(1, 5), 2)), 3)
             if is_connected(edges)]
    stars = sorted((edges for edges in trees if max(map(len, adjacency_of(edges).values())) == 3),
                   key=encode)
    paths = sorted((edges for edges in trees if max(map(len, adjacency_of(edges).values())) == 2),
                   key=encode)
    assert len(trees) == 16 and len(stars) == 4 and len(paths) == 12
    assert {encode(edges) for edges in trees} == {(a, b) for a in range(1, 5) for b in range(1, 5)}
    fig, axes = plt.subplots(4, 4, figsize=(10, 8.2), dpi=120, facecolor="white")
    for i, (ax, edges) in enumerate(zip(axes.flat, stars + paths)):
        positions = layout(edges)
        colour = "#b55c1c" if i < 4 else "#226b96"
        for a, b in edges:
            ax.plot([positions[a][0], positions[b][0]], [positions[a][1], positions[b][1]],
                    color=colour, lw=2.3, zorder=1)
        for v in range(1, 5):
            ax.scatter(*positions[v], s=390, facecolor="white", edgecolor=colour, lw=1.6, zorder=2)
            ax.text(*positions[v], str(v), ha="center", va="center", fontsize=12, zorder=3)
        ax.text(0, -1.13, f"Code {encode(edges)}", ha="center", fontsize=11, color=colour)
        ax.set_xlim(-1.55, 1.55)
        ax.set_ylim(-1.45, 1.2)
        ax.set_aspect("equal")
        ax.axis("off")
    fig.suptitle("Four fixed labels: 16 trees, only 2 shapes", y=0.975, fontsize=17, color="#243746")
    fig.text(0.5, 0.927, "Top row: 4 stars (choose the centre). Lower rows: 12 paths (4! / 2).",
             ha="center", fontsize=12)
    fig.text(0.5, 0.035, "Equal-label codes give stars; unequal-label codes give paths. Each ordered pair occurs once.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.035, right=0.965, top=0.885, bottom=0.085, hspace=0.15, wspace=0.12)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
