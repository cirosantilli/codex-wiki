"""Compute every deletion and DFS lowpoints for triangles joined by CD.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/matplotlib python3 ../graph-articulation-versus-bridge.py
Writes graph-articulation-versus-bridge.png in the current working directory.
"""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


VERTICES = "ABCDEF"
EDGES = ("AB", "AC", "BC", "CD", "DE", "DF", "EF")
POSITIONS = dict(zip(VERTICES, np.array([
    [-1.65, 0.9], [-1.65, -0.9], [-0.55, 0], [0.55, 0], [1.65, 0.9], [1.65, -0.9]
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


def dfs_criteria(vertices, edges):
    """For undirected simple graphs; skip the unique parent edge."""
    neighbours = adjacency(vertices, edges)
    discovery, low, parents, cuts, bridges = {}, {}, {}, set(), []

    def visit(v, parent):
        parents[v] = parent
        discovery[v] = low[v] = len(discovery) + 1
        children = 0
        for w in neighbours[v]:
            if w not in discovery:
                children += 1
                visit(w, v)
                low[v] = min(low[v], low[w])
                if parent is not None and low[w] >= discovery[v]:
                    cuts.add(v)
                if low[w] > discovery[v]:
                    bridges.append("".join(sorted((v, w))))
            elif w != parent:
                low[v] = min(low[v], discovery[w])
        if parent is None and children >= 2:
            cuts.add(v)

    for v in sorted(vertices):
        if v not in discovery:
            visit(v, None)
    return {"discovery": discovery, "low": low, "parents": parents,
            "cut_vertices": sorted(cuts), "bridges": sorted(bridges)}


def compute():
    original = components(VERTICES, EDGES)
    deletions = {v: components(VERTICES, EDGES, removed_vertex=v) for v in VERTICES}
    edge_counts = {e: len(components(VERTICES, EDGES, removed_edge=e)) for e in EDGES}
    cuts = [v for v in VERTICES if len(deletions[v]) > len(original)]
    bridges = [e for e in EDGES if edge_counts[e] > len(original)]
    dfs = dfs_criteria(VERTICES, EDGES)
    assert original == [list(VERTICES)]
    assert deletions["C"] == [list("AB"), list("DEF")]
    assert deletions["D"] == [list("ABC"), list("EF")]
    assert components(VERTICES, EDGES, removed_edge="CD") == [list("ABC"), list("DEF")]
    assert [len(deletions[v]) for v in VERTICES] == [1, 1, 2, 2, 1, 1]
    assert cuts == dfs["cut_vertices"] == ["C", "D"]
    assert bridges == dfs["bridges"] == ["CD"]
    assert list(dfs["discovery"].values()) == [1, 2, 3, 4, 5, 6]
    assert [dfs["low"][v] for v in VERTICES] == [1, 1, 1, 4, 4, 4]
    return {"adjacency": adjacency(VERTICES, EDGES), "components": original,
            "vertex_deletions": deletions, "edge_deletion_counts": edge_counts,
            "cut_vertices": cuts, "bridges": bridges, "dfs": dfs}


def draw(ax, removed_vertex=None, removed_edge=None):
    groups = components(VERTICES, EDGES, removed_vertex, removed_edge)
    colors = {v: (BLUE if i == 0 else GREEN) for i, group in enumerate(groups) for v in group}
    for a, b in EDGES:
        if removed_vertex in (a, b) or a + b == removed_edge:
            continue
        p, q = POSITIONS[a], POSITIONS[b]
        color = RED if a + b == "CD" else colors[a]
        ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=2.6, zorder=1)
    for v in VERTICES:
        if v == removed_vertex:
            continue
        x, y = POSITIONS[v]
        color = RED if removed_vertex is None and removed_edge is None and v in "CD" else colors[v]
        ax.scatter(x, y, s=800, color="white", edgecolor=color, linewidth=2.6, zorder=2)
        ax.text(x, y, v, ha="center", va="center", fontsize=14, weight="bold", color=color)
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-1.35, 1.35)
    ax.set_aspect("equal")
    ax.axis("off")
    return len(groups), sum((removed_vertex is None or removed_vertex not in e)
                            and e != removed_edge for e in EDGES)


def main():
    result = compute()
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axes = plt.subplots(2, 2, figsize=(8.4, 6.1), facecolor="white")
    fig.suptitle("One bridge; two cut vertices; different deletions", fontsize=15, color=DARK, y=0.975)
    cases = [(None, None, "Original graph"), (None, "CD", "Delete only edge CD"),
             ("C", None, "Delete vertex C and its incident edges"),
             ("D", None, "Delete vertex D and its incident edges")]
    for ax, (vertex, edge, title) in zip(axes.flat, cases):
        count, edge_count = draw(ax, vertex, edge)
        ax.set_title(title, fontsize=12, color=DARK, pad=10)
        ax.text(0.5, -0.06, f"{len(VERTICES) - bool(vertex)} vertices; {edge_count} edges; "
                f"{count} component{'s' if count != 1 else ''}",
                ha="center", color=DARK, fontsize=11, transform=ax.transAxes)
    fig.text(0.5, 0.035, "Original cut vertices: C, D       Original bridge: CD",
             ha="center", color=DARK, fontsize=12)
    fig.subplots_adjust(left=0.035, right=0.965, top=0.865, bottom=0.12, wspace=0.15, hspace=0.4)
    fig.savefig(Path.cwd() / "graph-articulation-versus-bridge.png", dpi=140, facecolor="white",
                transparent=False)
    plt.close(fig)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
