"""Draw disk contraction and circle winding; write the PNG basename to cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-mpl python ../disk-circle-loop-obstruction.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    blue, orange, purple = "#16679c", "#b34e16", "#76529c"
    fig = plt.figure(figsize=(9.6, 6.4), facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=[1.05, 1], hspace=0.72)
    disk, circle = fig.add_subplot(grid[0, 0]), fig.add_subplot(grid[0, 1])
    winding = fig.add_subplot(grid[1, :])
    fig.subplots_adjust(left=0.09, right=0.96, top=0.89, bottom=0.10)
    fig.suptitle("A filling permits contraction; a circle retains winding", fontsize=16)
    theta = np.linspace(0, 2 * np.pi, 801)
    for ax in [disk, circle]:
        ax.set_aspect("equal")
        ax.set(xlim=(-1.2, 1.2), ylim=(-1.16, 1.2))
        ax.axis("off")

    disk.add_patch(Circle((0, 0), 1, facecolor="#eaf3f9", edgecolor=blue, lw=2))
    for radius, color in [(1, blue), (0.5, orange), (0.25, purple)]:
        disk.plot(radius * np.cos(theta), radius * np.sin(theta), color=color, lw=2)
    start = np.array([0.6, 0.8])
    disk.annotate("", xy=(0, 0), xytext=start,
                  arrowprops={"arrowstyle": "->", "color": "#333333"})
    for t in [0, 0.5, 1]:
        point = (1 - t) * start
        disk.scatter(*point, s=28, color="#333333", zorder=5)
    disk.text(0.04, -0.16, r"$t=1$", fontsize=10)
    disk.text(0.38, 0.36, r"$t=1/2$", fontsize=10)
    disk.text(0.66, 0.83, r"$t=0$", fontsize=10)
    disk.set_title(r"Filled disk $D^2$: $H(x,t)=(1-t)x$")
    disk.text(0.5, -0.11, r"All intermediate loops stay in $D^2$; $\pi_1(D^2)=0$",
              transform=disk.transAxes, ha="center", fontsize=10)

    circle.plot(np.cos(theta), np.sin(theta), color=blue, lw=3)
    circle.plot(0.5 * np.cos(theta), 0.5 * np.sin(theta), color=orange, lw=2, ls="--")
    circle.scatter([0], [0], s=30, marker="x", color=orange)
    circle.text(0.5, -0.04, r"Candidate at $t=1/2$: radius $1/2$ is outside $S^1$",
                transform=circle.transAxes, ha="center", color=orange, fontsize=10)
    circle.set_title(r"Circle $S^1$: only the blue boundary belongs")
    circle.text(0.5, -0.11, r"Winding prevents contraction in $S^1$; $\pi_1(S^1)=\mathbb{Z}$",
                transform=circle.transAxes, ha="center", fontsize=10)

    s = np.linspace(0, 1, 801)
    for n, color in [(2, blue), (1, purple), (0, "#777777"), (-1, orange)]:
        winding.plot(s, n * s, color=color, lw=2, label=rf"$\gamma_{{{n}}}$: {n} turns")
    turns = np.where(s <= 0.5, 4 * s, 3 - 2 * s)
    winding.plot(s, turns, color="#202020", lw=2, ls="--",
                 label=r"$\gamma_2 * \gamma_{-1}$: net 1 turn")
    winding.scatter([1], [1], color="#202020", zorder=5)
    winding.set(xlim=(0, 1.02), ylim=(-1.12, 2.18), xlabel=r"Loop parameter $s$",
                ylabel=r"Unwrapped angle / $2\pi$",
                title=r"$\gamma_n(s)=e^{2\pi i n s}$: nonzero windings share the same circular image")
    winding.set_yticks([-1, 0, 1, 2])
    winding.grid(alpha=0.2)
    winding.legend(loc="upper left", fontsize=9, ncol=2, framealpha=1)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
