"""An original linear-objective maximum and an outside-point certificate."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle
import numpy as np


def main():
    vertices = np.array([[0., 0.], [4., 0.], [3., 3.], [0., 2.]])
    interior = np.array([[1., 1.], [2., 1.7], [3., .5], [1., .5]])
    q = np.array([3.8, 2.5])
    assert np.max(vertices.sum(axis=1))==6 and q.sum()>6
    fig, ax = plt.subplots(figsize=(7.6, 5.6), dpi=120, facecolor="white")
    ax.add_patch(Rectangle((0,0), 4, 3, fill=False, edgecolor="#999999", lw=1, ls=":"))
    ax.add_patch(Polygon(vertices, facecolor="#e3eff4", edgecolor="#28738f", lw=2))
    x = np.linspace(-.55, 4.65, 501)
    for level in [2, 4]:
        ax.plot(x, level-x, color="#aaaaaa", lw=1, ls="--")
        ax.text(-.35, level+.35, rf"$x+y={level}$", fontsize=10, color="#666666", clip_on=True)
    ax.plot(x, 6-x, color="#a85200", lw=2, label=r"Supporting line $x+y=6$")
    ax.scatter(*interior.T, color="#222222", s=28, zorder=4)
    ax.scatter(*vertices.T, color="#222222", s=36, zorder=4)
    ax.scatter(*vertices[2], color="#a85200", marker="*", s=180, zorder=5)
    ax.annotate(r"$C=(3,3)$: maximum $6$", vertices[2], xytext=(-160, 19), textcoords="offset points",
                fontsize=12, arrowprops=dict(arrowstyle="->", color="#a85200"))
    ax.scatter(*q, color="#b42a35", marker="X", s=85, zorder=6)
    ax.annotate(r"$q=(3.8,2.5)$"+"\n"+r"$x+y=6.3>6$", q, xytext=(-9,-55), textcoords="offset points",
                fontsize=12, color="#a01c2a", ha="right",
                arrowprops=dict(arrowstyle="->", color="#a01c2a"),
                bbox=dict(facecolor="white", edgecolor="none", alpha=.85, pad=2))
    ax.annotate("Increasing objective", xy=(1.1, 2.4), xytext=(.2, 1.5), fontsize=11,
                arrowprops=dict(arrowstyle="->", color="#a85200", lw=2), color="#a85200")
    ax.set(xlim=(-.55, 4.65), ylim=(-.6, 3.65), xlabel=r"$x$", ylabel=r"$y$")
    ax.set_aspect("equal")
    ax.set_xticks(range(5)); ax.set_yticks(range(4))
    ax.grid(alpha=.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="lower left", fontsize=11, frameon=False)
    fig.suptitle("A linear objective cannot improve by mixing", fontsize=17, weight="bold", y=.96)
    fig.text(.5, .08, r"For every mixture, $x+y\leq6$.  The red point fails this necessary condition.",
             ha="center", fontsize=11.5)
    fig.text(.5, .025, "Dotted box: coordinate-wise ranges. They contain q, but the convex hull does not.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.08, right=.95, top=.84, bottom=.19)
    fig.savefig(Path(__file__).stem+".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
