"""Plot the true R^3 input and R^2 output of an exact rectangular map.

Run from _media using Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig = plt.figure(figsize=(10, 5.5), facecolor="white")
    ax = fig.add_axes((0.005, 0.19, 0.54, 0.66), projection="3d")
    out = fig.add_axes((0.69, 0.24, 0.26, 0.53))
    blue, orange = "#2464a0", "#c26416"
    v = np.array([-2., 1., -1.])
    u0 = np.array([3., 0., 2.])
    t = np.linspace(-0.6, 2.4, 101)
    fibre = u0[:, None] + v[:, None] * t
    kernel = v[:, None] * np.linspace(-1.6, 2.3, 101)
    ax.plot(*kernel, color=blue, lw=2.3, label=r"kernel: $tv$")
    ax.plot(*fibre, color=orange, lw=2.8, label=r"solution fibre: $u_0+tv$")
    ax.scatter(0, 0, 0, color=blue, s=35)
    for i in range(3):
        u = u0 + i * v
        ax.scatter(*u, color=orange, s=45, depthshade=False)
        ax.text(*(u + np.array([0.1, 0.06, 0.20])), rf"$u_{i}$", color=orange)
    ax.quiver(*u0, *v, color="#482e17", linewidth=2.3, arrow_length_ratio=0.15)
    ax.set(xlabel="$x$", ylabel="$y$", zlabel="$z$", xlim=(-5, 5),
           ylim=(-2, 3), zlim=(-3, 4), title=r"Input: $\mathbb{R}^3$ (three axes)")
    ax.set_box_aspect((10, 5, 7))
    ax.view_init(elev=23, azim=-65)
    ax.legend(loc="upper left", fontsize=9)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.fill = False
    out.axhline(0, color="0.65", lw=0.8)
    out.axvline(0, color="0.65", lw=0.8)
    out.scatter(0, 0, color=blue, s=65, zorder=5)
    out.scatter(3, 2, color=orange, s=75, zorder=5)
    out.annotate("kernel gives $(0,0)$", (0, 0), xytext=(0.25, -0.55),
                 color=blue, fontsize=10)
    out.annotate(r"$Au_0=Au_1=Au_2=(3,2)$", (3, 2), xytext=(0.25, 3.2),
                 color=orange, fontsize=10, arrowprops={"arrowstyle": "->", "color": orange})
    out.set(xlim=(-1, 5), ylim=(-1, 4), xlabel="$b_1=x+2y$", ylabel="$b_2=y+z$",
            title=r"Output: $\mathbb{R}^2$ (two axes)")
    out.set_aspect("equal")
    out.grid(alpha=0.18)
    fig.add_artist(FancyArrowPatch((0.54, 0.52), (0.62, 0.52), transform=fig.transFigure,
                                  arrowstyle="->", mutation_scale=20, lw=1.8, color="0.3"))
    fig.text(0.58, 0.56, "$A$", ha="center", fontsize=14)
    fig.suptitle(r"$A(x,y,z)=(x+2y,\ y+z)$: rank 2, nullity 1", y=0.97, fontsize=14)
    fig.text(0.5, 0.13, r"$u_0=(3,0,2),\quad u_1=(1,1,1),\quad u_2=(-1,2,0)$", ha="center")
    fig.text(0.5, 0.065, r"Arrow: $u_1-u_0=v=(-2,1,-1)$, an invisible input displacement ($Av=0$).", ha="center")
    fig.text(0.5, 0.015, "Lines extend beyond the plotted segments; the 3D view is a perspective drawing.",
             ha="center", fontsize=10, color="0.35")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
