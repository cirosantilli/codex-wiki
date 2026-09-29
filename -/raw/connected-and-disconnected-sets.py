"""Write connected-and-disconnected-sets.png to the current directory.

Tested with Python 3.14.4, Matplotlib 3.10.7, and NumPy 2.3.5.
Run from _media to generate the repository image.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def closed_interval(ax, left, right, color):
    ax.plot([left, right], [0, 0], color=color, lw=7, solid_capstyle="butt")
    ax.scatter([left, right], [0, 0], color=color, s=70, zorder=4)


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(10, 6), facecolor="white")
    blue, orange = "#246a93", "#a9571c"
    closed_interval(top, 0, 1, blue)
    parameters = np.array([0, 0.5, 1])
    positions = 0.25 + parameters / 2
    top.scatter(positions, np.zeros_like(positions), color="#146b46", s=65, zorder=5)
    for x, label in zip(positions, [r"$a=1/4$", r"$\gamma(1/2)=1/2$", r"$b=3/4$"]):
        top.text(x, 0.25, label, ha="center", color="#146b46")
    top.set_title(r"Connected and path-connected: $I=[0,1]$", pad=14)
    top.text(0.5, -0.5, r"A path between any $a,b\in I$: $\gamma(t)=(1-t)a+tb$",
             ha="center", fontsize=12)
    top.set(xlim=(-0.15, 1.15), ylim=(-0.7, 0.7), xticks=[0, 0.25, 0.5, 0.75, 1],
            xticklabels=["0", "1/4", "1/2", "3/4", "1"])

    bottom.axvspan(-3, 0, color=blue, alpha=0.08)
    bottom.axvspan(0, 3, color=orange, alpha=0.08)
    closed_interval(bottom, -2, -1, blue)
    closed_interval(bottom, 1, 2, orange)
    bottom.text(-1.5, 0.32, r"$U=D\cap(-3,0)$", ha="center", color=blue)
    bottom.text(1.5, 0.32, r"$V=D\cap(0,3)$", ha="center", color=orange)
    bottom.scatter([0], [0], s=65, facecolors="white", edgecolors="#7c3434", zorder=5)
    bottom.text(0, -0.31, r"$0\notin D$", ha="center", color="#7c3434")
    bottom.text(0, -0.64, "Both pieces are open relative to D; their intersection is empty.",
                ha="center", fontsize=12)
    bottom.set_title(r"Disconnected: $D=[-2,-1]\cup[1,2]$", pad=14)
    bottom.set(xlim=(-2.7, 2.7), ylim=(-0.85, 0.8), xticks=[-2, -1, 0, 1, 2])
    for ax in (top, bottom):
        ax.set_facecolor("white")
        ax.set_yticks([])
        ax.set_xlabel("Position on the real line")
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.spines["bottom"].set_color("#909090")
    fig.subplots_adjust(left=0.06, right=0.97, bottom=0.1, top=0.9, hspace=0.75)
    fig.savefig("connected-and-disconnected-sets.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
