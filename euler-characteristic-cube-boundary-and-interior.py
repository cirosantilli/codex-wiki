"""Compare original cubical cell counts for a boundary and its filled solid; emit to CWD."""
from itertools import combinations, product
from pathlib import Path

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


def main():
    vertices = np.array(list(product([-1, 1], repeat=3)))
    edges = [(a, b) for a, b in combinations(range(8), 2) if np.count_nonzero(vertices[a] != vertices[b]) == 1]
    faces = []
    for axis in range(3):
        for value in [-1, 1]:
            fixed = np.array([p for p in vertices if p[axis] == value])
            other = [a for a in range(3) if a != axis]
            center = np.mean(fixed, axis=0)
            order = np.argsort(np.arctan2(fixed[:, other[1]] - center[other[1]], fixed[:, other[0]] - center[other[0]]))
            faces.append(fixed[order])
    assert (len(vertices), len(edges), len(faces)) == (8, 12, 6)
    fig = plt.figure(figsize=(10, 5.6), dpi=120, facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=[1.7, 1])
    for col, (filled, color) in enumerate([(False, "#5798c9"), (True, "#e49c48")]):
        ax = fig.add_subplot(grid[0, col], projection="3d")
        ax.add_collection3d(Poly3DCollection(faces, facecolors=color, edgecolors="none", alpha=0.12 if not filled else 0.45))
        for a, b in edges:
            ax.plot(*vertices[[a, b]].T, color="#183c58", lw=1.5)
        ax.scatter(*vertices.T, color="#183c58", s=15)
        ax.set(xlim=(-1.15, 1.15), ylim=(-1.15, 1.15), zlim=(-1.15, 1.15))
        ax.set_box_aspect((1, 1, 1))
        ax.view_init(elev=20, azim=29)
        ax.set_axis_off()
        ax.set_title("Filled cube: include the interior" if filled else "Boundary only: exclude the interior", fontsize=12)
        ax.text(0, 0, 0, "One open\n3-cell" if filled else "No\n3-cell", ha="center", va="center", color="#542a0f" if filled else "#183c58", fontsize=12)
        ax = fig.add_subplot(grid[1, col])
        counts = np.array([8, 12, 6, int(filled)])
        signed = counts * np.array([1, -1, 1, -1])
        assert sum(signed) == (1 if filled else 2)
        ax.bar(range(4), signed, color=["#3679b3", "#b95745", "#3679b3", "#b95745"])
        ax.axhline(0, color="#555555", lw=0.8)
        ax.set(xticks=range(4), xticklabels=["0-cells", "1-cells", "2-cells", "3-cells"], ylim=(-14, 11), ylabel="Signed contribution")
        for i, value in enumerate(signed):
            ax.text(i, value + (0.45 if value >= 0 else -0.45), f"{value:+d}", ha="center", va="bottom" if value >= 0 else "top")
        ax.set_title(r"$\chi=8-12+6-1=1$" if filled else r"$\chi=8-12+6=2$", fontsize=13)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("The three-dimensional interior changes what space is being counted", fontsize=14)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
