"""Original positive and signed affine weights; output matching PNG to cwd."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def transform(points):
    return np.asarray(points) @ np.array([[2., 0.], [1., 1.]]) + [1., -2.]


def main():
    vertices = np.array([[0., 0.], [2., 0.], [0., 2.]])
    weights = [np.array([.25,.5,.25]), np.array([-.5,1.5,0.])]
    points = np.array([w @ vertices for w in weights])
    assert np.array_equal(points, [[1.,.5],[3.,0.]])
    for w, point in zip(weights, points):
        assert w.sum() == 1
        assert np.array_equal(w @ transform(vertices), transform(point))
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 5.3), dpi=100, facecolor="white")
    fig.suptitle("Affine weights survive a transformation", fontsize=17)
    for ax, mapped in zip(axes, [False, True]):
        v = transform(vertices) if mapped else vertices
        p = transform(points) if mapped else points
        closed = np.vstack([v,v[0]])
        ax.fill(v[:,0], v[:,1], color="#e0e8ef")
        ax.plot(closed[:,0], closed[:,1], "o-", color="#486779", lw=2)
        ax.plot([v[1,0],p[1,0]], [v[1,1],p[1,1]], "--", color="#bf671c", lw=2)
        for label, point, offset in zip(["A","B","C"], v, [(-17,-20),(-5,-20),(-17,10)]):
            ax.annotate(label+("′" if mapped else ""), point, xytext=offset, textcoords="offset points", fontsize=12, weight="bold")
        for label, point, color, offset in zip(["P","R"], p, ["#238354","#bf671c"], [(10,12),(8,12)]):
            ax.scatter(*point, color=color, s=60, zorder=4)
            ax.annotate(label+("′" if mapped else "")+f" = ({point[0]:g}, {point[1]:g})", point, xytext=offset, textcoords="offset points", color=color, fontsize=11)
        ax.set_aspect("equal", adjustable="box")
        ax.set(xlim=((.1,8.8) if mapped else (-.6,4.6)), ylim=((-2.8,1.3) if mapped else (-.8,2.5)))
        ax.set_xlabel("x′" if mapped else "x", fontsize=12)
        ax.set_ylabel("y′" if mapped else "y", fontsize=12)
        ax.set_title("After T: identical weights" if mapped else "Before T: interpolation and extrapolation", fontsize=12, pad=12)
        ax.grid(alpha=.22)
        ax.spines[["top","right"]].set_visible(False)
    fig.text(.5,.045,"P: (¼, ½, ¼)   ·   R: (−½, 3/2, 0)   ·   Both weight sums equal 1", ha="center", fontsize=12)
    fig.subplots_adjust(left=.07, right=.975, bottom=.2, top=.83, wspace=.3)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
