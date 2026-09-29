"""Draw membership for four open/closed cases in the usual real line.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
Run via make _media/open-and-closed-sets-on-line.png; save to cwd.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


BLUE = "#176b9c"
GREY = "#bdc6ce"


def number_line(ax, y):
    ax.annotate("", xy=(1.42, y), xytext=(-0.42, y), zorder=1,
                arrowprops={"arrowstyle": "<->", "color": GREY, "lw": 1.4})
    for x in (0, 1):
        ax.plot([x, x], [y - 0.045, y + 0.045], color=GREY, lw=1)
        ax.text(x, y - 0.21, str(x), ha="center", va="top", fontsize=11)


def interval(ax, y, closed_left, closed_right):
    ax.plot([0, 1], [y, y], color=BLUE, lw=5, solid_capstyle="butt")
    for x, included in ((0, closed_left), (1, closed_right)):
        ax.scatter([x], [y], s=95, facecolors=BLUE if included else "white",
                   edgecolors=BLUE, linewidths=2, zorder=4)


def main():
    fig, ax = plt.subplots(figsize=(9.6, 5.7), facecolor="white")
    fig.subplots_adjust(left=0.04, right=0.98, top=0.88, bottom=0.09)
    ax.set(xlim=(-1.52, 1.65), ylim=(-0.46, 4.92))
    ax.axis("off")
    fig.suptitle("Open and closed: four possibilities", fontsize=19, y=0.97)
    ax.text(0.5, 4.77, "Ambient space: the real line with its usual topology",
            ha="center", fontsize=12)
    rows = np.array([4.08, 3.06, 2.04, 0.98])
    for y, label, expression, endpoints in zip(
        rows,
        ("Open only", "Closed only", "Neither", "Both (clopen)"),
        (r"$(0,1)$", r"$[0,1]$", r"$[0,1)$", r"$\varnothing$ and $\mathbb{R}$"),
        ((False, False), (True, True), (True, False), None),
    ):
        ax.text(-1.45, y + 0.07, label, fontsize=14, va="bottom")
        ax.text(-1.45, y - 0.22, expression, fontsize=14, va="top")
        if endpoints is not None:
            number_line(ax, y)
            interval(ax, y, *endpoints)
        else:
            number_line(ax, y + 0.22)
            ax.text(1.49, y + 0.22, r"$\varnothing$", fontsize=14, va="center")
            ax.text(0.5, y + 0.44, "No points included", ha="center", fontsize=11)
            number_line(ax, y - 0.40)
            ax.annotate("", xy=(1.42, y - 0.40), xytext=(-0.42, y - 0.40),
                        arrowprops={"arrowstyle": "<->", "color": BLUE,
                                    "lw": 4, "mutation_scale": 17})
            ax.text(1.49, y - 0.40, r"$\mathbb{R}$", fontsize=14, va="center")
    fig.text(0.5, 0.025, "Filled circle: included endpoint   |   Hollow circle: excluded endpoint",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", dpi=125,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
