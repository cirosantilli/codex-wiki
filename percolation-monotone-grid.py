"""A seeded monotone coupling on one finite nearest-neighbor square box."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np


def root_cluster(edges, opened, root):
    neighbors = {}
    for (a, b), keep in zip(edges, opened):
        if keep:
            neighbors.setdefault(a, []).append(b)
            neighbors.setdefault(b, []).append(a)
    reached, stack = {root}, [root]
    while stack:
        for neighbor in neighbors.get(stack.pop(), []):
            if neighbor not in reached:
                reached.add(neighbor)
                stack.append(neighbor)
    return reached


def main():
    size = 17
    edges = []
    for x in range(size):
        for y in range(size):
            if x+1 < size:
                edges.append(((x, y), (x+1, y)))
            if y+1 < size:
                edges.append(((x, y), (x, y+1)))
    labels = np.random.default_rng(20261011).uniform(size=len(edges))
    root = (size//2, size//2)
    previous = {root}
    color = "#b55d20"
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.4), dpi=120)
    for ax, p in zip(axes, [.3, .5, .7]):
        opened = labels <= p
        cluster = root_cluster(edges, opened, root)
        assert previous.issubset(cluster)
        previous = cluster
        assert opened.sum() >= len(cluster)-1
        ax.add_collection(LineCollection([edge for edge, keep in zip(edges, opened) if keep],
                                        colors="#c3cdd4", linewidths=1.4))
        cluster_edges = [edge for edge, keep in zip(edges, opened)
                         if keep and edge[0] in cluster]
        ax.add_collection(LineCollection(cluster_edges, colors=color, linewidths=1.8))
        points = np.array(sorted(cluster))
        ax.scatter(points[:, 0], points[:, 1], s=9, color=color, zorder=3)
        ax.scatter(*root, marker="*", s=140, color="#243746", edgecolor="white",
                   linewidth=.8, zorder=4)
        ax.set(xlim=(-.7, size-.3), ylim=(-.7, size-.3))
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(f"p = {p:.1f}\nRoot cluster: {len(cluster)} of {size**2} vertices",
                     fontsize=12)
    fig.suptitle("Raise the threshold; keep the same random edge labels", fontsize=15)
    fig.text(.5, .045, "Orange: connected to the root ★    Gray: other open edges    "
             "Finite box; no inference of infinite percolation", ha="center", fontsize=10)
    fig.subplots_adjust(left=.025, right=.975, bottom=.12, top=.77, wspace=.12)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
