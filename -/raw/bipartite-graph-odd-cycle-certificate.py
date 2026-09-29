"""Draw an exact BFS conflict and its odd-cycle certificate, with no random data.

Run from _media with Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Save the
matching basename to the current working directory on an opaque white canvas.
"""

from collections import deque
from pathlib import Path

import matplotlib.pyplot as plt

VERTICES = ("s", "w", "a", "b", "u", "v")
EDGES = (("s", "w"), ("w", "a"), ("w", "b"), ("a", "u"), ("b", "v"), ("u", "v"))
CYCLE = ("w", "a", "u", "v", "b", "w")
BLUE, ORANGE, RED = "#1766a5", "#bd5b09", "#b32632"


def distances():
    adjacency = {v: [] for v in VERTICES}
    for u, v in EDGES:
        adjacency[u].append(v)
        adjacency[v].append(u)
    depth = {"s": 0}
    queue = deque(["s"])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if v not in depth:
                depth[v] = depth[u] + 1
                queue.append(v)
    return depth


def main():
    depth = distances()
    assert depth == {"s": 0, "w": 1, "a": 2, "b": 2, "u": 3, "v": 3}
    edge_sets = {frozenset(e) for e in EDGES}
    assert CYCLE[0] == CYCLE[-1] and len(set(CYCLE[:-1])) == len(CYCLE) - 1
    assert all(frozenset(e) in edge_sets for e in zip(CYCLE, CYCLE[1:]))
    assert (len(CYCLE) - 1) % 2 == 1
    assert "s" not in CYCLE and depth["u"] == depth["v"]
    positions = {"s": (0, 3), "w": (0, 2), "a": (-1.2, 1),
                 "b": (1.2, 1), "u": (-1.2, 0), "v": (1.2, 0)}
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(8.6, 5.6), facecolor="white")
    for u, v in EDGES:
        common = {u, v} == {"s", "w"}
        conflict = {u, v} == {"u", "v"}
        ax.plot(*zip(positions[u], positions[v]), color="#849098" if common else RED,
                lw=2 if common else 3, ls="--" if common else "-", zorder=1)
        if conflict:
            ax.text(0, -0.28, "conflict edge: equal colours", color=RED,
                    ha="center", fontsize=12, weight="bold")
    for vertex, (x, y) in positions.items():
        ax.scatter(x, y, s=850, color=BLUE if depth[vertex] % 2 == 0 else ORANGE,
                   edgecolors="white", linewidths=1.7, zorder=2)
        ax.text(x, y, vertex, ha="center", va="center", color="white",
                fontsize=15, weight="bold", zorder=3)
    for d in range(4):
        ax.text(-2.5, 3 - d, f"distance {d}", ha="left", va="center", color="#42515a")
    ax.text(0.3, 2.52, "Shared root path\nexcluded", va="center", fontsize=12, color="#42515a")
    ax.text(1.62, 2, "w: common ancestor", va="center", fontsize=12, color="#42515a")
    ax.text(0, -0.85, "Certificate: w → a → u → v → b → w\n5 distinct cycle vertices, 5 edges",
            ha="center", va="center", fontsize=14, color=RED)
    ax.set(xlim=(-2.7, 3.5), ylim=(-1.23, 3.5), aspect="equal")
    ax.axis("off")
    fig.suptitle("An odd cycle obstructs two-colouring", fontsize=18, y=0.96)
    fig.subplots_adjust(left=0.03, right=0.98, top=0.88, bottom=0.04)
    fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
