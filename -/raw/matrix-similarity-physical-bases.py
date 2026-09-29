"""Draw one physical linear map in two bases; emit PNG into the current directory.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


BLUE = "#1769a4"
ORANGE = "#bc5318"
GREEN = "#287451"
INK = "#243444"


def arrow(ax, start, end, color, width=2.4, style="-"):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", color=color, lw=width,
                                linestyle=style, mutation_scale=14), zorder=4)


def main():
    plt.rcParams.update({"font.size": 12, "text.color": INK,
                         "axes.titlecolor": INK, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 6.5), dpi=100)
    fig.patch.set_facecolor("white")
    fig.suptitle("Same physical map: double horizontal, multiply vertical by five",
                 fontsize=16, y=0.965)
    bases = [np.eye(2), np.array([[1., 1.], [0., 1.]])]
    titles = ["Old basis: horizontal and vertical", "New basis: horizontal and diagonal"]
    for index, (ax, basis, title) in enumerate(zip(axes, bases, titles)):
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xlim(-1.6, 5.6)
        ax.set_ylim(-0.9, 6.0)
        ax.set_title(title, fontsize=13, pad=16)
        for i in range(-7, 8):
            for fixed, variable in [(0, 1), (1, 0)]:
                coords = np.zeros((2, 2))
                coords[fixed] = i
                coords[variable] = [-10, 10]
                line = basis @ coords
                ax.plot(line[0], line[1], color="#e3e7eb", lw=0.8, zorder=0)
        ax.axhline(0, color="#a3adb6", lw=1)
        ax.axvline(0, color="#a3adb6", lw=1)
        for j in range(2):
            arrow(ax, (0, 0), basis[:, j], GREEN, 2)
            label = ("$e_1$", "$e_2$")[j] if index == 0 else ("$b_1$", "$b_2$")[j]
            pos = basis[:, j] + ([0.05, -0.34] if j == 0 else [-0.40, 0.12])
            ax.text(*pos, label, color=GREEN, fontsize=13)
        p, tp = np.array([2., 1.]), np.array([4., 5.])
        for vector, color in [(p, BLUE), (tp, ORANGE)]:
            coefficients = np.linalg.solve(basis, vector)
            elbow = coefficients[0] * basis[:, 0]
            ax.plot([0, elbow[0], vector[0]], [0, elbow[1], vector[1]],
                    linestyle=(0, (2, 3)), color=color, lw=1.8, zorder=2)
            ax.scatter(*elbow, s=18, color=color, zorder=3)
            arrow(ax, (0, 0), vector, color)
        ax.text(2.12, 0.85, "$p$", color=BLUE, fontsize=14)
        ax.text(4.08, 5.06, "$T(p)$", color=ORANGE, fontsize=14)
        ax.set_xticks(range(-1, 6))
        ax.set_yticks(range(0, 6))
        ax.tick_params(length=0, labelsize=10, colors="#667582")
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.text(0.02, 0.98, "Physical plane (same scale)", transform=ax.transAxes,
                va="top", fontsize=10, color="#667582")
        ax.set_xlabel("Physical horizontal direction", fontsize=11)
    fig.text(0.26, 0.13, "$x=(2,1)^T$    $Ax=(4,5)^T$", ha="center", fontsize=14)
    fig.text(0.76, 0.13, "$y=(1,1)^T$    $By=(-1,5)^T$", ha="center", fontsize=14)
    fig.text(0.5, 0.055, "$4e_1+5e_2=-b_1+5b_2$   —   identical output vector",
             ha="center", fontsize=14)
    fig.subplots_adjust(left=0.045, right=0.97, bottom=0.23, top=0.86, wspace=0.15)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
