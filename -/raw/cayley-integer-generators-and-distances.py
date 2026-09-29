"""Draw finite windows of two integer Cayley graphs.

Run from _media: python ../cayley-integer-generators-and-distances.py
Writes cayley-integer-generators-and-distances.png to the current directory.
Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5 (root pyproject.toml).
"""

import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/codex-wiki-matplotlib")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


def draw_panel(ax, skips, route, heading, formula):
    vertices = list(range(-2, 8))
    highlight = {tuple(sorted(pair)) for pair in zip(route, route[1:])}
    for step in ([1, 2] if skips else [1]):
        for start in vertices:
            end = start + step
            if end not in vertices:
                continue
            selected = (start, end) in highlight
            color = "#be4b13" if selected else "#9aabb9"
            width = 3.6 if selected else 1.5
            layer = 3 if selected else 1
            if step == 1:
                ax.plot([start, end], [0, 0], color=color, lw=width, zorder=layer)
            else:
                ax.add_patch(Arc(((start + end) / 2, 0), 2, 1.25,
                                 theta1=0, theta2=180, color=color,
                                 lw=width, zorder=layer))
    ax.scatter(vertices, [0] * len(vertices), s=58, c="white",
               edgecolors="#405669", linewidths=1.6, zorder=4)
    ax.scatter(route, [0] * len(route), s=65, c="#be4b13", zorder=5)
    for n in vertices:
        ax.text(n, -0.21, str(n), ha="center", va="top", fontsize=12)
    ax.text(-2.8, 0, "…", ha="center", va="center", fontsize=18)
    ax.text(7.8, 0, "…", ha="center", va="center", fontsize=18)
    ax.set_title(heading, loc="left", fontsize=15, pad=12)
    ax.text(0.5, 0.04, formula, transform=ax.transAxes, ha="center", fontsize=13)
    ax.set_xlim(-3.2, 8.2)
    ax.set_ylim(-0.75, 0.85)
    ax.axis("off")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(2, 1, figsize=(9.6, 5.4), dpi=100)
    fig.suptitle("Same integers, different one-step moves", fontsize=18, y=0.97)
    draw_panel(axes[0], False, [0, 1, 2, 3, 4, 5],
               r"$S=\{-1,1\}$: highlighted route $0\to1\to2\to3\to4\to5$",
               r"$d_S(a,b)=|a-b|$     •     $d_S(0,5)=5$")
    draw_panel(axes[1], True, [0, 2, 4, 5],
               r"$T=\{-2,-1,1,2\}$: highlighted route $0\to2\to4\to5$",
               r"$d_T(a,b)=\lceil |a-b|/2\rceil$     •     $d_T(0,5)=3$")
    fig.text(0.5, 0.035, "Every edge costs one step. Curved edges are ±2 moves.\n"
             "Finite windows only: both graphs continue in both directions.",
             ha="center", fontsize=11, linespacing=1.5, color="#344a5e")
    fig.subplots_adjust(left=0.07, right=0.97, top=0.84, bottom=0.13, hspace=0.7)
    fig.savefig("cayley-integer-generators-and-distances.png", facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
