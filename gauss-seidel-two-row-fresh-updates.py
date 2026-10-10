"""Draw an original two-row update schedule; emit the PNG into the CWD.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def box(ax, xy, text, color, width=0.33):
    x, y = xy
    ax.add_patch(FancyBboxPatch(
        (x - width / 2, y - 0.055), width, 0.11,
        boxstyle="round,pad=0.014", facecolor="white", edgecolor=color,
        linewidth=1.8, zorder=3,
    ))
    ax.text(x, y, text, ha="center", va="center", color=color, fontsize=13, zorder=4)


def arrow(ax, start, end, color, dashed=False):
    ax.add_patch(FancyArrowPatch(
        start, end, arrowstyle="-|>", mutation_scale=17, linewidth=2.2,
        linestyle="--" if dashed else "-", color=color, zorder=2,
    ))


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.2), dpi=110, facecolor="white")
    blue, orange, gray = "#146b88", "#b05012", "#6b7280"
    fig.suptitle("Same equations, different information flow", fontsize=18, y=0.97)
    fig.text(0.5, 0.895, r"$4x+y=1,\quad x+3y=2,\quad (x^{(0)},y^{(0)})=(0,0)$",
             ha="center", fontsize=15)
    for ax, fresh in zip(axes, (True, False)):
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis("off")
        ax.text(0.5, 0.98, "Gauss–Seidel: fresh" if fresh else "Jacobi: stale",
                ha="center", fontsize=15, weight="bold", color=blue if fresh else orange)
        box(ax, (0.26, 0.83), r"$x^{(0)}=0$", gray if fresh else orange)
        box(ax, (0.75, 0.83), r"$y^{(0)}=0$", gray)
        box(ax, (0.26, 0.53), r"$x^{(1)}=1/4$", blue)
        box(ax, (0.75, 0.23), r"$y^{(1)}=7/12$" if fresh else r"$y^{(1)}=2/3$",
            blue if fresh else orange)
        arrow(ax, (0.71, 0.76), (0.32, 0.60), gray)
        ax.text(0.74, 0.51, r"Row 1: $(1-0)/4$", ha="center", fontsize=11)
        if fresh:
            arrow(ax, (0.33, 0.46), (0.68, 0.30), blue)
            ax.text(0.61, 0.405, "reuse 1/4 now", color=blue, fontsize=12, ha="center")
            ax.text(0.52, 0.075, r"Row 2: $(2-1/4)/3=7/12$", ha="center", fontsize=13)
        else:
            # Route the stale input outside the new first-coordinate box.
            arrow(ax, (0.078, 0.83), (0.038, 0.83), orange, dashed=True)
            ax.plot([0.038, 0.038], [0.83, 0.23], color=orange, linewidth=2.2, linestyle="--")
            arrow(ax, (0.038, 0.23), (0.57, 0.23), orange, dashed=True)
            ax.text(0.005, 0.53, "keep old x = 0", color=orange, fontsize=11, rotation=90,
                    ha="center", va="center")
            ax.text(0.52, 0.075, r"Row 2: $(2-0)/3=2/3$", ha="center", fontsize=13)
    fig.subplots_adjust(left=0.035, right=0.975, bottom=0.12, top=0.82, wspace=0.16)
    fig.text(0.5, 0.035, "First sweep only • arrows identify the input actually used by each row",
             ha="center", fontsize=11, color="#374151")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
