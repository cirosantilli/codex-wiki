"""Draw K_3,3 at the Mantel bound and the three triangles from one extra edge.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def draw_graph(ax, extra_edge=False):
    blue, orange, red = "#176c9d", "#af650d", "#bd263c"
    left = [(0, y) for y in (2, 1, 0)]
    right = [(2.4, y) for y in (2, 1, 0)]
    for i, a in enumerate(left):
        for b in right:
            highlight = extra_edge and i < 2
            ax.plot([a[0], b[0]], [a[1], b[1]],
                    color=red if highlight else "#9babb7",
                    alpha=0.7 if highlight else 0.8,
                    lw=1.9 if highlight else 1.4, zorder=1)
    if extra_edge:
        ax.add_patch(FancyArrowPatch(left[0], left[1],
                     connectionstyle="arc3,rad=0.42", arrowstyle="-",
                     color=red, lw=3.4, zorder=2))
        ax.text(-0.4, 1.5, "+1", ha="right", va="center", color=red,
                fontsize=14, fontweight="bold")
    for points, name, color, dx in ((left, "a", blue, -0.24),
                                     (right, "b", orange, 0.24)):
        for i, (x, y) in enumerate(points, 1):
            ax.scatter(x, y, s=220, color=color, edgecolor="white",
                       linewidth=1.5, zorder=4)
            ax.text(x + dx, y, rf"${name}_{i}$", ha="right" if dx < 0 else "left",
                    va="center", fontsize=14, color=color)
    ax.text(0, 2.5, "A: 3 vertices", ha="center", color=blue, fontsize=12)
    ax.text(2.4, 2.5, "B: 3 vertices", ha="center", color=orange, fontsize=12)
    ax.set(xlim=(-0.95, 3.05), ylim=(-1.1, 3.0), aspect="equal")
    ax.axis("off")
    ax.set_title(r"$K_{3,3}$ + one internal edge" if extra_edge else r"$K_{3,3}$: sharp triangle-free bound",
                 fontsize=14, pad=10)
    ax.text(1.2, -0.45, "10 edges; exactly 3 triangles" if extra_edge else "9 edges; no triangles",
            ha="center", fontsize=14, fontweight="bold")
    ax.text(1.2, -0.82, r"Each $b_j$ completes $a_1a_2b_j$" if extra_edge else r"All $3\times3$ cross edges; none inside A or B",
            ha="center", fontsize=11)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.7), dpi=120)
    draw_graph(axes[0])
    draw_graph(axes[1], extra_edge=True)
    fig.suptitle("One edge beyond the Mantel bound forces triangles", fontsize=17, y=0.96)
    fig.text(0.5, 0.045, "Only the six labelled dots are vertices; line crossings are not vertices.",
             ha="center", fontsize=11, color="#495765")
    fig.subplots_adjust(left=0.03, right=0.98, top=0.82, bottom=0.13, wspace=0.16)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
