"""Generate continuous-square-compact-image-open-cover.png in the CWD.

Tested with Python 3.14.4, Matplotlib 3.10.7, and NumPy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def interval(ax, left, right, row, color, closed):
    ax.plot([left, right], [row, row], color=color, lw=6,
            solid_capstyle="butt")
    for endpoint, included in zip((left, right), closed):
        ax.scatter(endpoint, row, s=70, facecolor=color if included else "white",
                   edgecolor=color, linewidth=2, zorder=3)


def main():
    blue, orange, ink = "#2269a4", "#c25d12", "#263746"
    fig = plt.figure(figsize=(9, 6), dpi=120, facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=[1.1, 1], hspace=.45, wspace=.28)
    graph = fig.add_subplot(grid[0, :])
    x = np.linspace(0, 1, 401)
    graph.plot(x, x*x, color=ink, lw=2.5)
    graph.scatter([0, 1], [0, 1], color=ink, s=35, zorder=3)
    for a, color in [(3/5, orange), (4/5, blue)]:
        graph.plot([a, a], [0, a*a], ls="--", color=color, lw=1.5)
        graph.plot([0, a], [a*a, a*a], ls="--", color=color, lw=1.5)
    graph.set(xlim=(-.02, 1.02), ylim=(-.03, 1.03), xlabel="Domain coordinate x",
              ylabel="Image coordinate y", title=r"Continuous map $f(x)=x^2$ on $[0,1]$")
    graph.set_xticks([0, .6, .8, 1], ["0", "3/5", "4/5", "1"])
    graph.set_yticks([0, .36, .64, 1], ["0", "9/25", "16/25", "1"])
    graph.spines[["top", "right"]].set_visible(False)
    for col, title, domain in [(0, "Open cover of the image", False),
                               (1, "Preimages cover the domain", True)]:
        ax = fig.add_subplot(grid[1, col])
        ax.set_title(title, pad=12)
        interval(ax, 0, 1, 2, ink, (True, True))
        if domain:
            interval(ax, 0, .8, 1, blue, (True, False))
            interval(ax, .6, 1, 0, orange, (False, True))
            labels = [r"$f^{-1}(V_2)=(3/5,1]$", r"$f^{-1}(V_1)=[0,4/5)$", r"$X=[0,1]$"]
        else:
            interval(ax, -.1, .64, 1, blue, (False, False))
            interval(ax, .36, 1.1, 0, orange, (False, False))
            labels = [r"$V_2=(9/25,11/10)$", r"$V_1=(-1/10,16/25)$", r"$f(X)=[0,1]$"]
        for row, label in enumerate(labels):
            ax.text(.5, row+.24, label, ha="center", fontsize=11, color=ink)
        ax.set(xlim=(-.16, 1.16), ylim=(-.3, 2.7))
        ax.set_xticks([0, 1])
        ax.set_yticks([])
        ax.spines[["left", "top", "right"]].set_visible(False)
    fig.suptitle("Pull an open cover back, then select finitely many sets", fontsize=14, y=.98)
    fig.subplots_adjust(left=.09, right=.97, bottom=.08, top=.86)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
