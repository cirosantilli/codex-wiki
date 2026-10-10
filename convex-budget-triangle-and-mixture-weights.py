"""Original continuous-budget triangle; matching opaque PNG saved in cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.6, 5.3), dpi=120, facecolor="white")
    vertices = np.array([[0, 0], [6, 0], [0, 3]])
    ax.add_patch(Polygon(vertices, facecolor="#dcecf2", edgecolor="#287a9d", lw=2))
    ax.plot(*vertices.T, "o", color="#287a9d", ms=7)
    a = np.array([1, 2])
    b = np.array([5, 0.25])
    mid = (a + b) / 2
    centroid = vertices.mean(axis=0)
    ax.plot([a[0], b[0]], [a[1], b[1]], "o-", color="#b85831", lw=2.4, ms=6)
    ax.plot(*mid, "D", color="#b85831", ms=7)
    for vertex in vertices:
        ax.plot([vertex[0], centroid[0]], [vertex[1], centroid[1]], ":", color="#3f8e72", lw=1.2)
    ax.plot(*centroid, "o", color="#3f8e72", ms=10)
    labels = [(a, "A = (1,2)", (-45, 15)), (b, "B = (5,1/4)", (-17, -32)),
              (mid, "Midpoint (3,9/8)", (17, 4)),
              (centroid, "(2,1): weights 1/3 each", (-50, -42)),
              (vertices[0], "(0,0)", (-25, -29)), (vertices[1], "(6,0)", (-20, -29)),
              (vertices[2], "(0,3)", (12, 0))]
    for point, label, offset in labels:
        ax.annotate(label, point, xytext=offset, textcoords="offset points", fontsize=11)
    ax.text(3.6, 2.25, r"$x+2y=6$", rotation=-26.6, color="#287a9d", fontsize=14)
    ax.text(0.99, 0.96, "Continuous allocations\nx ≥ 0, y ≥ 0, x + 2y ≤ 6", transform=ax.transAxes,
            ha="right", va="top", fontsize=11, bbox={"fc": "white", "ec": "#cccccc", "boxstyle": "round,pad=0.4"})
    ax.set(xlim=(-0.5, 6.5), ylim=(-0.42, 3.65), xlabel="Activity amount x", ylabel="Activity amount y", xticks=range(7), yticks=range(4))
    ax.grid(alpha=0.15)
    fig.suptitle("One feasible region: inequalities or mixtures of extreme points", fontsize=14)
    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.14, top=0.87)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
