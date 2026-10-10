"""Compare relative openness with interior, closure, and boundary on R.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
Run via make _media/relative-openness-and-boundary.png; save to cwd.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


BLUE = "#176b9c"
GREEN = "#21805e"
ORANGE = "#b94e13"
GREY = "#b8c1cb"


def segment(ax, y, right=1, endpoints=(True, True), color=BLUE):
    ax.plot([0, right], [y, y], color=color, lw=5, solid_capstyle="butt")
    for x, included in zip((0, right), endpoints):
        ax.scatter([x], [y], s=85, facecolors=color if included else "white",
                   edgecolors=color, linewidths=1.8, zorder=5)


def axis_line(ax, y, relative=False, half_tick=False):
    if relative:
        segment(ax, y, color=GREY)
    else:
        ax.annotate("", xy=(1.2, y), xytext=(-0.2, y), zorder=1,
                    arrowprops={"arrowstyle": "<->", "color": GREY, "lw": 1.2})
    ticks = (0, 0.5, 1) if half_tick else (0, 1)
    for x in ticks:
        ax.text(x, y - 0.13, "1/2" if x == 0.5 else str(int(x)),
                ha="center", va="top", fontsize=10)


def main():
    fig, panels = plt.subplots(3, 1, figsize=(9.8, 8.2), facecolor="white",
                               gridspec_kw={"height_ratios": [1.25, 0.95, 1.65]})
    fig.subplots_adjust(left=0.035, right=0.97, top=0.88, bottom=0.045, hspace=0.48)
    fig.suptitle("The ambient space changes the answer", fontsize=19, y=0.975)
    for ax in panels:
        ax.set(xlim=(-0.94, 1.24))
        ax.axis("off")

    ax = panels[0]
    ax.set(ylim=(-0.5, 1.65))
    ax.set_title(r"1. Ambient space $X=[0,1]$: $A=[0,1/2)$ is open in $X$", fontsize=14, loc="left")
    ax.axvspan(-0.21, -0.025, color="#f1f3f5", zorder=0)
    ax.axvspan(1.025, 1.2, color="#f1f3f5", zorder=0)
    ax.text(-0.115, 1.22, "outside\nX", ha="center", fontsize=10, color="#5a6470")
    ax.text(1.115, 1.22, "outside\nX", ha="center", fontsize=10, color="#5a6470")
    ax.text(-0.89, 0.82, r"$A=[0,1/2)$", fontsize=13, va="center")
    axis_line(ax, 0.82, relative=True, half_tick=True)
    segment(ax, 0.82, right=0.5, endpoints=(True, False))
    radius = 0.25
    ax.text(-0.89, 0.05, r"$B_X(0,r)=[0,r)$", fontsize=13, va="center")
    axis_line(ax, 0.05, relative=True)
    segment(ax, 0.05, right=radius, endpoints=(True, False), color=GREEN)
    ax.text(radius, -0.08, r"$r=1/4$", ha="center", va="top", fontsize=10, color=GREEN)
    ax.text(0.62, 0.26, "The relative ball stays in A.", ha="center", fontsize=11, color=GREEN)

    ax = panels[1]
    ax.set(ylim=(-0.6, 1.03))
    ax.set_title(r"2. Ambient space $X=[0,1]$: $X$ itself is open and closed", fontsize=14, loc="left")
    ax.text(-0.89, 0.4, r"$X=[0,1]$", fontsize=13, va="center")
    axis_line(ax, 0.4, relative=True)
    segment(ax, 0.4)
    ax.text(0.5, -0.40, r"$\operatorname{int}_X X=X$     $\operatorname{cl}_X X=X$     $\partial_X X=\varnothing$",
            ha="center", fontsize=12)

    ax = panels[2]
    ax.set(ylim=(-0.43, 3.5))
    ax.set_title(r"3. Ambient space $\mathbb{R}$: $S=[0,1)$", fontsize=14, loc="left")
    rows = np.array([2.95, 2.05, 1.15, 0.25])
    labels = (r"$S=[0,1)$", r"Interior: $(0,1)$",
              r"Closure: $[0,1]$", r"Boundary: $\{0,1\}$")
    for y, label in zip(rows, labels):
        ax.text(-0.89, y, label, fontsize=13, va="center")
        axis_line(ax, y)
    segment(ax, rows[0], endpoints=(True, False))
    segment(ax, rows[1], endpoints=(False, False), color=GREEN)
    segment(ax, rows[2], endpoints=(True, True))
    ax.scatter([0, 1], [rows[3], rows[3]], s=90, color=ORANGE, zorder=5)
    ax.text(0.5, -0.39, "Both endpoints belong to the boundary; only 0 belongs to S.",
            ha="center", fontsize=11, color=ORANGE)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", dpi=125,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
