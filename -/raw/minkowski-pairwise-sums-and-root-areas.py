"""Exact toy Minkowski sums; write the matching opaque PNG to the CWD.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


BLUE = "#2878b5"
ORANGE = "#cc7026"
GREEN = "#20845e"


def axes_style(ax, limit):
    ax.set_aspect("equal")
    ax.set_xlim(*limit)
    ax.set_ylim(*limit)
    ax.axhline(0, color="#a7afb5", lw=0.7, zorder=0)
    ax.axvline(0, color="#a7afb5", lw=0.7, zorder=0)
    ax.set_xticks(range(int(limit[0]) + 1, int(limit[1]) + 1))
    ax.set_yticks(range(int(limit[0]) + 1, int(limit[1]) + 1))
    ax.tick_params(labelsize=9, length=2)
    ax.spines[["top", "right"]].set_visible(False)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axs = plt.subplots(2, 3, figsize=(9.6, 7.4), dpi=120)
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.06, right=0.97, top=0.86, bottom=0.15,
                        wspace=0.36, hspace=0.68)
    fig.suptitle("Minkowski addition: add every pair of points", fontsize=17, y=0.97)
    fig.text(0.5, 0.925, "Exact toy geometry; outlines and arrows sample the construction",
             ha="center", color="#4d5660", fontsize=11)
    rect_specs = [(2, 1, BLUE, r"$A=[0,2]\times[0,1]$", "Area 2"),
                  (1, 2, ORANGE, r"$B=[0,1]\times[0,2]$", "Area 2"),
                  (3, 3, GREEN, r"$A+B=[0,3]\times[0,3]$", "Area 9")]
    for ax, (w, h, color, title, caption) in zip(axs[0], rect_specs):
        axes_style(ax, (-0.35, 3.4))
        ax.add_patch(Rectangle((0, 0), w, h, facecolor=color + "30",
                               edgecolor=color, lw=2))
        ax.set_title(title, fontsize=12, pad=8)
        ax.text(0.5, -0.19, caption, transform=ax.transAxes, ha="center")
    a, b = (1.6, 0.35), (0.65, 1.45)
    for ax, point, label, color in [(axs[0, 0], a, "$a$", BLUE),
                                   (axs[0, 1], b, "$b$", ORANGE)]:
        ax.scatter(*point, s=25, color=color, zorder=4)
        ax.annotate(label, point, xytext=(6, 6), textcoords="offset points", color=color)
    sum_ax = axs[0, 2]
    for shift in [(0, 0), b, (1, 2)]:
        sum_ax.add_patch(Rectangle(shift, 2, 1, fill=False, edgecolor=BLUE,
                                  ls="--", lw=0.9))
    total = (a[0] + b[0], a[1] + b[1])
    for start, end, color in [((0, 0), a, BLUE), (a, total, ORANGE)]:
        sum_ax.annotate("", end, xytext=start,
                        arrowprops={"arrowstyle": "->", "lw": 2, "color": color})
    sum_ax.scatter(*total, color=GREEN, s=26, zorder=5)
    sum_ax.annotate("$a+b$", total, xytext=(5, 7), textcoords="offset points", color=GREEN)
    disk_specs = [(1, BLUE, "$D_1$", r"Area $\pi$"),
                  (2, ORANGE, "$D_2$", r"Area $4\pi$"),
                  (3, GREEN, "$D_1+D_2=D_3$", r"Area $9\pi$")]
    for ax, (radius, color, title, caption) in zip(axs[1], disk_specs):
        axes_style(ax, (-3.45, 3.45))
        ax.add_patch(Circle((0, 0), radius, facecolor=color + "30",
                            edgecolor=color, lw=2))
        ax.plot([0, radius], [0, 0], color=color, lw=2)
        ax.text(radius / 2, 0.23, str(radius), ha="center", color=color)
        ax.set_title(title, fontsize=12, pad=8)
        ax.text(0.5, -0.19, caption, transform=ax.transAxes, ha="center")
    fig.text(0.5, 0.064, r"Rectangles: $\sqrt{9}=3>2\sqrt{2}$     |     "
             r"Disks: $\sqrt{9\pi}=\sqrt{\pi}+\sqrt{4\pi}$", ha="center", fontsize=13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
