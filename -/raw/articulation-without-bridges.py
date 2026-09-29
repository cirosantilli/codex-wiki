"""Two triangles share a cut vertex, but have no bridges.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/matplotlib python3 ../articulation-without-bridges.py
Writes articulation-without-bridges.png in the current working directory.
"""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


VERTICES = "ABCDE"
EDGES = ("AB", "AC", "BC", "AD", "AE", "DE")
POSITIONS = dict(zip(VERTICES, np.array([
    [0, 0], [-1.55, 0.95], [-1.55, -0.95], [1.55, 0.95], [1.55, -0.95]
])))
DARK, BLUE, GREEN, RED = "#263747", "#326f9c", "#25846a", "#bd3f43"


def adjacency(vertices, edges):
    return {v: sorted(b if a == v else a for a, b in edges if v in (a, b))
            for v in vertices}


def components(vertices, edges, removed_vertex=None, removed_edge=None):
    remaining = set(vertices) - {removed_vertex}
    kept = [e for e in edges if (removed_vertex is None or removed_vertex not in e)
            and frozenset(e) != frozenset(removed_edge or ())]
    neighbours = adjacency(sorted(remaining), kept)
    groups = []
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        pending, group = [start], []
        while pending:
            v = pending.pop()
            group.append(v)
            for w in neighbours[v]:
                if w in remaining:
                    remaining.remove(w)
                    pending.append(w)
        groups.append(sorted(group))
    return groups


def compute():
    original = components(VERTICES, EDGES)
    deletions = {v: components(VERTICES, EDGES, removed_vertex=v) for v in VERTICES}
    edge_counts = {e: len(components(VERTICES, EDGES, removed_edge=e)) for e in EDGES}
    cut_vertices = [v for v in VERTICES if len(deletions[v]) > len(original)]
    bridges = [e for e in EDGES if edge_counts[e] > len(original)]
    assert original == [list(VERTICES)]
    assert deletions["A"] == [list("BC"), list("DE")]
    assert [len(deletions[v]) for v in VERTICES] == [2, 1, 1, 1, 1]
    assert cut_vertices == ["A"] and bridges == []
    # Isolated vertices count, including the empty-graph boundary case.
    assert len(components(VERTICES + "Z", EDGES)) == 2
    assert len(components(VERTICES + "Z", EDGES, removed_vertex="A")) == 3
    assert len(components(VERTICES + "Z", EDGES, removed_vertex="Z")) == 1
    assert components("Z", (), removed_vertex="Z") == []
    return {"adjacency": adjacency(VERTICES, EDGES), "components": original,
            "vertex_deletions": deletions, "edge_deletion_counts": edge_counts,
            "cut_vertices": cut_vertices, "bridges": bridges}


def draw(ax, deleted, title):
    groups = components(VERTICES, EDGES, removed_vertex=deleted)
    colors = {v: (BLUE if i == 0 else GREEN) for i, group in enumerate(groups) for v in group}
    for a, b in EDGES:
        if deleted not in (a, b):
            p, q = POSITIONS[a], POSITIONS[b]
            ax.plot([p[0], q[0]], [p[1], q[1]], color=colors[a], lw=2.6, zorder=1)
    for v in VERTICES:
        if v == deleted:
            continue
        x, y = POSITIONS[v]
        color = RED if v == "A" else colors[v]
        ax.scatter(x, y, s=980, color="white", edgecolor=color, linewidth=2.8, zorder=2)
        ax.text(x, y, v, ha="center", va="center", fontsize=15, weight="bold", color=color)
    if deleted:
        ax.text(0, 0, "A removed", ha="center", va="center", fontsize=11, color=RED)
    ax.set_title(title, fontsize=13, color=DARK, pad=14)
    ax.set_xlim(-2.05, 2.05)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")


def main():
    result = compute()
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.65), facecolor="white")
    fig.suptitle("A vulnerable vertex, despite an alternative route around every edge",
                 fontsize=14, color=DARK, y=0.97)
    draw(axes[0], None, "Original: 1 connected component")
    draw(axes[1], "A", "Delete vertex A: 2 connected components")
    fig.text(0.25, 0.09, "Cut vertices: A     Bridges: none", ha="center", color=DARK)
    fig.text(0.75, 0.09, "Surviving components: {B, C} and {D, E}", ha="center", color=DARK)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.79, bottom=0.18, wspace=0.13)
    fig.savefig(Path.cwd() / "articulation-without-bridges.png", dpi=140, facecolor="white",
                transparent=False)
    plt.close(fig)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
