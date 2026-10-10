"""Draw eigenvector-geometry.png in cwd; Python 3.14, NumPy, Matplotlib."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


BLUE = "#1765a8"
PURPLE = "#9a357a"
ORANGE = "#bd5d00"


def arrow(ax, vector, color, dashed=False):
    ax.annotate(
        "",
        xy=vector,
        xytext=(0, 0),
        arrowprops={
            "arrowstyle": "->",
            "color": color,
            "lw": 2.5 if not dashed else 1.7,
            "linestyle": "--" if dashed else "-",
            "mutation_scale": 16,
            "shrinkA": 0,
            "shrinkB": 0,
        },
        zorder=4 if dashed else 3,
    )


def setup(ax, limit, ticks):
    ax.set_aspect("equal")
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.grid(color="#e5e8eb", lw=0.7)
    ax.axhline(0, color="#a2aab2", lw=0.9)
    ax.axvline(0, color="#a2aab2", lw=0.9)
    ax.set_xlabel("x", labelpad=1)
    ax.set_ylabel("y", rotation=0, labelpad=6)
    for spine in ax.spines.values():
        spine.set_visible(False)


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 3, figsize=(11, 4.8), facecolor="white")
    fig.subplots_adjust(left=0.055, right=0.98, bottom=0.17, top=0.77, wspace=0.30)
    fig.suptitle("Eigenvectors follow a line; other vectors can turn", y=0.97, fontsize=16)
    fig.legend(
        handles=[
            Line2D([0], [0], color="#4a5056", ls="--", lw=2, label="Input vector"),
            Line2D([0], [0], color="#4a5056", lw=2.5, label="Image of that vector"),
        ],
        loc="upper center",
        bbox_to_anchor=(0.5, 0.91),
        ncol=2,
        frameon=False,
    )

    ax = axes[0]
    setup(ax, 3.6, [-3, 0, 3])
    ax.set_title("Symmetric stretch\nA(x, y) = (2x + y, x + 2y)")
    a = np.array([[2, 1], [1, 2]])
    diagonal = np.array([-3.6, 3.6])
    ax.plot(diagonal, diagonal, color=BLUE, alpha=0.25, lw=2)
    ax.plot(diagonal, -diagonal, color=PURPLE, alpha=0.25, lw=2)
    for v, color in [(np.array([1, 1]), BLUE), (np.array([1, -1]), PURPLE), (np.array([1, 0]), ORANGE)]:
        arrow(ax, a @ v, color)
        arrow(ax, v, color, dashed=True)
    ax.text(2.15, 3.12, r"$Av_3=3v_3$", color=BLUE, fontsize=11)
    ax.text(0.9, -1.65, r"$Av_1=v_1$", color=PURPLE, fontsize=11)
    ax.text(2.05, 0.55, "(2, 1)", color=ORANGE, fontsize=10)
    ax.text(0.02, 1.3, "(1, 1)", color=BLUE, fontsize=10)
    ax.text(0.5, -0.53, "(1, 0)", color=ORANGE, fontsize=10)

    ax = axes[1]
    setup(ax, 1.7, [-1, 0, 1])
    ax.set_title("Quarter-turn rotation\nR(x, y) = (−y, x)")
    rotation = np.array([[0, -1], [1, 0]])
    for v, color in [(np.array([1.0, 0]), BLUE), (np.array([0.8, 0.8]), ORANGE)]:
        arrow(ax, rotation @ v, color)
        arrow(ax, v, color, dashed=True)
    ax.text(1.02, -0.27, "v", color=BLUE)
    ax.text(0.13, 1.05, "Rv", color=BLUE)
    ax.text(-1.12, 1.02, "Rw", color=ORANGE)
    ax.text(0.92, 0.87, "w", color=ORANGE)
    ax.text(0.20, 0.21, "90°", color=BLUE, fontsize=10)

    ax = axes[2]
    setup(ax, 1.7, [-1, 0, 1])
    ax.set_title("Shear\nS(x, y) = (x + y, y)")
    shear = np.array([[1, 1], [0, 1]])
    ax.axhline(0, color=BLUE, alpha=0.25, lw=3)
    e1, e2 = np.eye(2)
    arrow(ax, shear @ e1, BLUE)
    arrow(ax, e1, BLUE, dashed=True)
    arrow(ax, shear @ e2, ORANGE)
    arrow(ax, e2, ORANGE, dashed=True)
    ax.text(0.54, -0.35, r"$Se_1=e_1$", color=BLUE)
    ax.text(-0.45, 1.10, r"$e_2$", color=ORANGE)
    ax.text(1.02, 1.02, r"$Se_2$", color=ORANGE)

    for ax, caption in zip(axes, ["Two independent eigendirections", "No real eigendirection", "Only one eigendirection: y = 0"]):
        ax.text(0.5, -0.24, caption, transform=ax.transAxes, ha="center", fontsize=11)
    fig.savefig(Path.cwd() / "eigenvector-geometry.png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
