"""An original finite cloud and an exact three-point mixture; PNG in CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def main():
    vertices = np.array([[0., 0.], [4., 0.], [3., 3.], [0., 2.]])
    interior = np.array([[1., 1.], [2., 1.7], [3., .5], [1., .5]])
    p = np.array([2., 1.])
    u = np.array([1.5, 0.])
    assert np.allclose((5/12)*vertices[0]+(1/4)*vertices[1]+(1/3)*vertices[2], p)
    fig, ax = plt.subplots(figsize=(7.6, 5.6), dpi=120, facecolor="white")
    ax.add_patch(Polygon(vertices, facecolor="#e3eff4", edgecolor="#28738f", lw=2))
    ax.scatter(*interior.T, color="#222222", s=32, label="Original points", zorder=4)
    ax.scatter(*vertices.T, color="#222222", s=42, zorder=4)
    for point, label, offset in zip(vertices, ["A=(0,0)", "B=(4,0)", "C=(3,3)", "D=(0,2)"],
                                    [(-2,-23), (-27,-23), (8,4), (-2,9)]):
        ax.annotate(label, point, xytext=offset, textcoords="offset points", fontsize=11)
    ax.plot([u[0], vertices[2,0]], [u[1], vertices[2,1]], color="#a85200", ls="--", lw=1.8)
    ax.scatter(*u, color="#a85200", s=48, zorder=5)
    ax.annotate(r"$U=(3/2,0)$", u, xytext=(-40, 12), textcoords="offset points", fontsize=12)
    ax.scatter(*p, color="#a85200", marker="*", s=180, zorder=6)
    ax.annotate(r"$p=(2,1)$", p, xytext=(12,-3), textcoords="offset points", fontsize=13,
                bbox=dict(facecolor="white", edgecolor="none", alpha=.85, pad=1.5))
    ax.set(xlim=(-.55, 4.65), ylim=(-.6, 3.6), xlabel=r"$x$", ylabel=r"$y$")
    ax.set_aspect("equal")
    ax.set_xticks(range(5)); ax.set_yticks(range(4))
    ax.grid(alpha=.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper right", fontsize=11, frameon=False)
    fig.suptitle("Mixing fills a finite point cloud's convex hull", fontsize=17, weight="bold", y=.96)
    fig.text(.5, .09, r"$p=\frac{5}{12}A+\frac{1}{4}B+\frac{1}{3}C$", ha="center", fontsize=17)
    fig.text(.5, .025, "Blue region: convex hull. The orange point is a mixture, not an original sample.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.08, right=.95, top=.85, bottom=.21)
    fig.savefig(Path(__file__).stem+".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
