"""Compute BFS layers and queue snapshots; write the PNG to the current directory.

Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7.
Run from the repository with make _media/breadth-first-search-layers.png.
"""

from collections import deque
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


VERTICES = "ABCDEFG"
EDGES = ("AB", "AC", "BD", "BE", "CE", "CF", "EG", "FG")
POSITIONS = dict(zip(VERTICES, np.array([
    [0, 3], [-1, 2], [1, 2], [-1.8, 1], [-0.2, 1], [1.8, 1], [0.8, 0]
])))
COLORS = ("#ddebf7", "#bde1d0", "#ffdf9c", "#e0c9eb")
DARK, BLUE = "#253746", "#24688f"


def compute_bfs():
    adjacency = {v: sorted(b if a == v else a for a, b in EDGES if v in (a, b))
                 for v in VERTICES}
    distance, parent = {"A": 0}, {"A": None}
    queue, discovery, removal, tree, snapshots = deque("A"), ["A"], [], [], []
    scans, peak = 0, 1
    while queue:
        u = queue.popleft()
        removal.append(u)
        for v in adjacency[u]:
            scans += 1
            if v not in distance:
                distance[v], parent[v] = distance[u] + 1, u
                discovery.append(v)
                tree.append(u + v)
                queue.append(v)
                peak = max(peak, len(queue))
        snapshots.append((u, tuple(queue)))
        queued_distances = [distance[v] for v in queue]
        assert queued_distances == sorted(queued_distances)
        assert not queue or max(queued_distances) - min(queued_distances) <= 1
        assert len(queue) == len(set(queue))

    # Independently relax all edges to check shortest edge-count distances.
    reference = dict.fromkeys(VERTICES, float("inf"))
    reference["A"] = 0
    for _ in range(len(VERTICES) - 1):
        for a, b in EDGES:
            reference[a] = min(reference[a], reference[b] + 1)
            reference[b] = min(reference[b], reference[a] + 1)
    assert distance == reference == dict(zip(VERTICES, [0, 1, 1, 2, 2, 2, 3]))
    assert discovery == removal == list(VERTICES)
    assert tree == ["AB", "AC", "BD", "BE", "CF", "EG"]
    assert parent == dict(zip(VERTICES, [None, "A", "A", "B", "B", "C", "E"]))
    assert dict(snapshots)["B"] == ("C", "D", "E")
    assert dict(snapshots)["C"] == ("D", "E", "F")
    assert dict(snapshots)["E"] == ("F", "G")
    assert scans == 2 * len(EDGES) == 16 and peak == 3
    return distance, tree, snapshots, scans, peak


def draw_graph(ax, distance, tree):
    highlighted = {frozenset(e) for e in tree}
    for a, b in EDGES:
        xy = np.array([POSITIONS[a], POSITIONS[b]])
        is_tree = frozenset((a, b)) in highlighted
        ax.plot(xy[:, 0], xy[:, 1], color=BLUE if is_tree else "#929ca6",
                lw=2.7 if is_tree else 1.7, ls="-" if is_tree else "--", zorder=1)
    for v, (x, y) in POSITIONS.items():
        ax.scatter(x, y, s=800, facecolors=COLORS[distance[v]],
                   edgecolors=DARK, linewidths=1.5, zorder=3)
        ax.text(x, y, v, ha="center", va="center", fontsize=14, color=DARK, zorder=4)
    for level in range(4):
        ax.text(-2.45, 3 - level, f"d = {level}", fontsize=11,
                ha="right", va="center", color=DARK)
    ax.set(xlim=(-3.15, 2.35), ylim=(-0.45, 3.5), aspect="equal")
    ax.axis("off")
    ax.set_title("Same graph; colors show distance from A", fontsize=12, pad=12)


def draw_queue(ax, u, queue, distance, row):
    y = 2.4 - row * 1.85
    ax.text(0, y + 0.85, f"After removing and processing {u}", fontsize=12,
            color=DARK, fontweight="bold")
    for index, v in enumerate(queue):
        x = index * 1.05
        ax.add_patch(Rectangle((x, y), 0.88, 0.64, facecolor=COLORS[distance[v]],
                               edgecolor=DARK, linewidth=1.5))
        ax.text(x + 0.44, y + 0.33, f"{v} ({distance[v]})", ha="center",
                va="center", fontsize=12, color=DARK)
    ax.text(0.44, y - 0.24, "front / next", ha="center", fontsize=10, color=DARK)
    ax.text((len(queue) - 1) * 1.05 + 0.44, y - 0.24, "rear", ha="center",
            fontsize=10, color=DARK)
    message = ("C (distance 1) stays ahead of D and E (distance 2)." if u == "B" else
               "E discovers G first; later F sees G already marked.")
    ax.text(0, y - 0.63, message, fontsize=10, color=DARK)


def main():
    distance, tree, snapshots, scans, peak = compute_bfs()
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.2), dpi=120,
                             facecolor="white", gridspec_kw={"width_ratios": [1, 1.15]})
    draw_graph(axes[0], distance, tree)
    ax = axes[1]
    ax.set(xlim=(-0.1, 4.45), ylim=(-0.65, 3.8))
    ax.axis("off")
    ax.set_title("FIFO queue: front → rear; label (distance)", fontsize=12, pad=12)
    for row, u in enumerate(("B", "E")):
        draw_queue(ax, u, dict(snapshots)[u], distance, row)
    fig.suptitle("Breadth-first search: first arrival has the fewest edges", fontsize=15)
    fig.text(0.5, 0.075, "Solid: discovery tree     Dashed: other graph edges     "
             "Scan neighbors alphabetically", ha="center", fontsize=10, color=DARK)
    fig.text(0.5, 0.025, "Discovery / removal: A, B, C, D, E, F, G     "
             "Unweighted edge count; unequal costs need a different algorithm",
             ha="center", fontsize=10, color=DARK)
    fig.subplots_adjust(left=0.025, right=0.985, top=0.84, bottom=0.18, wspace=0.08)
    fig.savefig(Path.cwd() / "breadth-first-search-layers.png", facecolor="white",
                transparent=False)
    plt.close(fig)
    print(f"BFS: order={VERTICES}; distances={list(distance.values())}; tree={tree}; "
          f"scans={scans}; queue_peak={peak}; enqueues=7; dequeues=7")


if __name__ == "__main__":
    main()
