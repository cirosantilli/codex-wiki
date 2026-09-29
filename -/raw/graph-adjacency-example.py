"""Draw graph-adjacency-example.png in cwd; Python 3.14, NumPy, Matplotlib."""

from collections import deque
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


LABELS = "ABCDEF"
EDGES = ("AB", "AC", "BC", "CD", "DE", "DF", "EF")
BLUE = "#1765a8"
ORANGE = "#b85b00"


def adjacency(edges):
    matrix = np.zeros((6, 6), dtype=int)
    for u, v in edges:
        i, j = LABELS.index(u), LABELS.index(v)
        matrix[i, j] += 1
        matrix[j, i] += 1
    return matrix


def distances(matrix, start=0):
    result = {start: 0}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in np.flatnonzero(matrix[u]):
            v = int(v)
            if v not in result:
                result[v] = result[u] + 1
                queue.append(v)
    return result


def paths(matrix, start, end, visited=()):
    visited = (*visited, start)
    if start == end:
        yield visited
    else:
        for v in np.flatnonzero(matrix[start]):
            if v not in visited:
                yield from paths(matrix, int(v), end, visited)


def check_examples(matrix):
    degrees = matrix.sum(axis=1)
    assert degrees.tolist() == [2, 2, 3, 3, 2, 2]
    assert int(degrees.sum()) == 2 * len(EDGES) == 14
    assert np.array_equal(matrix, matrix.T)
    assert not matrix.diagonal().any()
    assert matrix[2].tolist() == [1, 1, 0, 1, 0, 0]
    parallel = adjacency([*EDGES, "CD"])
    assert parallel.sum(axis=1).tolist() == [2, 2, 4, 4, 2, 2]
    assert np.array_equal(parallel > 0, matrix > 0)
    loop = adjacency([*EDGES, "AA"])
    assert loop.sum(axis=1).tolist() == [4, 2, 3, 3, 2, 2]
    assert distances(matrix) == {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 3}
    assert sorted(len(p) - 1 for p in paths(matrix, 0, 5)) == [3, 4, 4, 5]

    edge_set = {frozenset(e) for e in EDGES}
    walk = "ABACDF"
    walk_edges = [frozenset(e) for e in zip(walk, walk[1:])]
    assert len(walk_edges) == 5 and set(walk_edges) <= edge_set
    assert len(set(walk_edges)) == 4
    euler = "CABCDEFD"
    euler_edges = [frozenset(e) for e in zip(euler, euler[1:])]
    assert len(euler_edges) == len(edge_set) == len(set(euler_edges))
    assert set(euler_edges) == edge_set
    hamilton = "ABCDEF"
    assert set(hamilton) == set(LABELS) and len(set(hamilton)) == len(hamilton)
    assert all(frozenset(e) in edge_set for e in zip(hamilton, hamilton[1:]))

    bridges = [e for e in EDGES if len(distances(adjacency([f for f in EDGES if f != e]))) < 6]
    assert bridges == ["CD"]
    cut = adjacency([e for e in EDGES if e != "CD"])
    assert set(distances(cut)) == {0, 1, 2}
    assert set(distances(cut, 3)) == {3, 4, 5}

    tree_edges = [e for e in EDGES if e not in ("BC", "EF")]
    tree = adjacency(tree_edges)
    assert len(tree_edges) == 6 - 1 and len(distances(tree)) == 6
    assert list(paths(tree, 0, 5)) == [(0, 2, 3, 5)]
    for i in range(6):
        for j in range(i + 1, 6):
            assert len(list(paths(tree, i, j))) == 1
    assert all(len(distances(adjacency([f for f in tree_edges if f != e]))) < 6 for e in tree_edges)
    assert len(list(paths(adjacency([*tree_edges, "BC"]), 1, 2))) == 2
    print("Verified degrees, handshake sum, matrix, BFS layers, four A–F paths, Euler trail,")
    print("Hamiltonian path, bridge deletion, two components, and unique paths in the spanning tree.")


def draw_graph(ax, coordinates, title):
    for u, v in EDGES:
        x, y = zip(coordinates[u], coordinates[v])
        ax.plot(x, y, color=ORANGE if u + v == "CD" else BLUE, lw=2.6, zorder=1)
    for label, (x, y) in coordinates.items():
        ax.scatter(x, y, s=620, color="white", edgecolor=BLUE, linewidth=2, zorder=3)
        ax.text(x, y, label, ha="center", va="center", fontsize=13, color="#172b3b", zorder=4)
    ax.set_title(title, fontsize=13, pad=16)
    ax.set_aspect("equal")
    ax.margins(0.21)
    ax.axis("off")


def main():
    matrix = adjacency(EDGES)
    check_examples(matrix)
    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.4), facecolor="white")
    fig.subplots_adjust(left=0.035, right=0.945, top=0.77, bottom=0.23, wspace=0.37)
    fig.suptitle("A graph retains adjacency, not the lengths in its drawing", fontsize=16, y=0.97)
    first = {"A": (0, 1), "B": (0, -1), "C": (1.55, 0), "D": (3, 0), "E": (4.55, 1), "F": (4.55, -1)}
    draw_graph(axes[0], first, "Two triangles joined by CD")
    order = "ADBECF"
    angles = np.linspace(0, 2 * np.pi, 6, endpoint=False) + np.pi / 2
    second = {label: (np.cos(a), np.sin(a)) for label, a in zip(order, angles)}
    draw_graph(axes[1], second, "Same edges, different drawing")
    axes[1].text(0.5, -0.03, "Crossings add no vertices", transform=axes[1].transAxes, ha="center", fontsize=11)

    ax = axes[2]
    ax.imshow(matrix, cmap=ListedColormap(["#ffffff", "#dcebf6"]), vmin=0, vmax=1)
    ax.set_title("Adjacency matrix M", fontsize=13, pad=16)
    ax.set_xticks(range(6), LABELS)
    ax.set_yticks(range(6), LABELS)
    ax.xaxis.tick_top()
    ax.tick_params(which="both", length=0)
    ax.set_xticks(np.arange(-0.5, 6, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 6, 1), minor=True)
    ax.grid(which="minor", color="#b9c8d3", linewidth=0.7)
    for i in range(6):
        for j in range(6):
            ax.text(j, i, str(matrix[i, j]), ha="center", va="center", color=BLUE if matrix[i, j] else "#64717b")
        ax.text(6.0, i, str(matrix[i].sum()), ha="center", va="center", color="#172b3b", clip_on=False)
    ax.text(6.0, -1.05, "degree", ha="center", va="center", fontsize=10, clip_on=False)
    for spine in ax.spines.values():
        spine.set_edgecolor("#b9c8d3")
    fig.text(0.5, 0.115, "Degrees in A, B, C, D, E, F order:  (2, 2, 3, 3, 2, 2)", ha="center", fontsize=13)
    fig.text(0.5, 0.045, "Sum of degrees = 14 = 2 × 7 edges     •     Orange CD is the only bridge", ha="center", fontsize=12)
    output = Path.cwd() / f"{Path(__file__).stem}.png"
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Saved {output}")


if __name__ == "__main__":
    main()
