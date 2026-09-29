"""Compare a tetrahedral sphere with a square quotient presentation of a torus.

Run from _media. Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""
from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def main():
    vertices = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
    faces = list(combinations(range(4), 3))
    edges = set(e for f in faces for e in combinations(f, 2))
    assert (len(vertices), len(edges), len(faces)) == (4, 6, 4)
    # Pair right with left, top with bottom: all four corners are equivalent.
    parent = list(range(4))

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i

    for u, v in [(0, 1), (3, 2), (0, 3), (1, 2)]:
        parent[find(u)] = find(v)
    assert len({find(i) for i in range(4)}) == 1
    boundary_word = [("a", 1), ("b", 1), ("a", -1), ("b", -1)]
    assert all(sum(sign for label, sign in boundary_word if label == e) == 0
               for e in ("a", "b"))
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10.4, 4.8))
    sphere = fig.add_axes([0.02, 0.25, 0.44, 0.58], projection="3d")
    sphere.add_collection3d(Poly3DCollection([vertices[list(f)] for f in faces],
                             facecolors=["#b7d8eb", "#d5e9f3", "#90bdd5", "#dcecf4"],
                             edgecolors="#234b65", linewidths=1.8, alpha=0.72))
    sphere.scatter(*vertices.T, s=35, color="#234b65", depthshade=False)
    sphere.set(xlim=(-1.3, 1.3), ylim=(-1.3, 1.3), zlim=(-1.3, 1.3))
    sphere.set_box_aspect((1, 1, 1))
    sphere.view_init(elev=18, azim=32)
    sphere.set_title("Sphere: tetrahedron boundary", pad=8)
    sphere.axis("off")
    square = fig.add_axes([0.55, 0.28, 0.40, 0.55])
    square.add_patch(Rectangle((0, 0), 1, 1, facecolor="#eaf0e4", edgecolor="none"))
    for y in (0, 1):
        square.plot([0, 1], [y, y], color="#2c749c", linewidth=2.5)
        square.annotate("", (0.7, y), (0.3, y),
                        arrowprops={"arrowstyle": "-|>", "color": "#2c749c", "lw": 2.5})
        square.text(0.5, y + (0.10 if y == 1 else -0.14), "a", ha="center", color="#2c749c")
    for x in (0, 1):
        square.plot([x, x], [0, 1], color="#ba682e", linewidth=2.5)
        square.annotate("", (x, 0.7), (x, 0.3),
                        arrowprops={"arrowstyle": "-|>", "color": "#ba682e", "lw": 2.5})
        square.text(x + (0.10 if x == 1 else -0.14), 0.5, "b", va="center", color="#ba682e")
    square.scatter([0, 1, 1, 0], [0, 0, 1, 1], color="#2d393b", s=42, zorder=5)
    for x, y in [(0, 0), (1, 0), (1, 1), (0, 1)]:
        square.text(x + (-0.12 if x == 0 else 0.08),
                    y + (-0.08 if y == 0 else 0.03), "v", fontsize=11)
    square.text(0.5, 0.54, "one open face", ha="center", fontsize=12)
    square.text(0.5, 0.36, "all corners = v", ha="center", fontsize=11)
    square.set(xlim=(-0.3, 1.3), ylim=(-0.3, 1.3), aspect="equal")
    square.set_title("Torus: identify matching arrows", pad=8)
    square.axis("off")
    for x, counts, betti in [(0.24, (4, 6, 4), (1, 0, 1)),
                              (0.75, (1, 2, 1), (1, 2, 1))]:
        v, e, f = counts
        fig.text(x, 0.22, f"V = {v}     E = {e}     F = {f}", ha="center")
        fig.text(x, 0.14, rf"$\chi={v}-{e}+{f}={v-e+f}$", ha="center", fontsize=16)
        fig.text(x, 0.065, rf"$(b_0,b_1,b_2)={betti}$", ha="center", fontsize=13)
    fig.suptitle("Cell counts and rational Betti numbers agree", fontsize=16, y=0.96)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
