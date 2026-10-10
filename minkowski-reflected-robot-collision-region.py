"""Show why a translating robot's forbidden reference positions use -R.

Write the matching opaque PNG to the CWD; run from _media with
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib. Exact toy geometry, no measured data.
Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


BLUE = "#2878b5"
ORANGE = "#b85720"
GREEN = "#20845e"
RED = "#bd3b48"


def rect(ax, corner, width, height, color, *, dashed=False, filled=True):
    ax.add_patch(Rectangle(corner, width, height,
                           facecolor=color + "25" if filled else "none",
                           edgecolor=color, lw=2, ls="--" if dashed else "-"))


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axs = plt.subplots(1, 2, figsize=(10, 5.8), dpi=120)
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.05, right=0.97, top=0.80, bottom=0.17, wspace=0.18)
    fig.suptitle("Collision positions: reflect the robot before adding", fontsize=17, y=0.97)
    fig.text(0.5, 0.91, r"Toy robot $R=[0,2]\times[0,1]$; obstacle "
             r"$O=[4,6]\times[2,4]$; touching counts as collision", ha="center")
    for ax in axs:
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xlim(-2.6, 8.6)
        ax.set_ylim(-1.7, 5.9)
        ax.axhline(0, color="#abb2b9", lw=0.8)
        ax.axvline(0, color="#abb2b9", lw=0.8)
        ax.set_xticks([-2, 0, 2, 4, 6, 8])
        ax.set_yticks([-1, 0, 1, 2, 3, 4, 5])
        ax.tick_params(labelsize=10, length=2)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_xlabel("Reference x coordinate / toy units")
    left, right = axs
    left.set_title("Physical shapes and a collision", pad=12, fontsize=13)
    rect(left, (4, 2), 2, 2, ORANGE)
    left.text(5, 3.1, "$O$", color=ORANGE, ha="center", fontsize=14)
    rect(left, (0, 0), 2, 1, BLUE)
    left.text(1, 0.45, "$R$", ha="center", color=BLUE, fontsize=14)
    rect(left, (-2, -1), 2, 1, BLUE, dashed=True, filled=False)
    left.text(-1, -0.6, "$-R$", ha="center", color=BLUE)
    left.scatter(0, 0, color=BLUE, s=28, zorder=5)
    left.annotate("reference origin", (0, 0), xytext=(-2.2, 1.6),
                  arrowprops={"arrowstyle": "->", "color": BLUE}, color=BLUE, fontsize=10)
    q = (3, 1.5)
    rect(left, q, 2, 1, GREEN)
    left.text(3.9, 1.75, "$q+R$", color=GREEN, ha="center", fontsize=11)
    left.add_patch(Rectangle((4, 2), 1, 0.5, facecolor="#bd3b4870", edgecolor=RED,
                             hatch="////", lw=1))
    left.scatter(*q, s=35, color=GREEN, zorder=6)
    left.annotate("$q=(3,1.5)$", q, xytext=(2.3, 0.4),
                  arrowprops={"arrowstyle": "->", "color": GREEN}, color=GREEN, fontsize=11)
    left.text(0.5, -0.20, "Red overlap area = 1/2", transform=left.transAxes,
              ha="center", color=RED)
    right.set_title("Forbidden reference positions", pad=12, fontsize=13)
    rect(right, (2, 1), 4, 3, GREEN)
    rect(right, (4, 2), 4, 3, RED, dashed=True, filled=False)
    rect(right, (4, 2), 2, 2, ORANGE, filled=False)
    right.text(3.55, 3.4, "$O+(-R)$", color=GREEN, ha="center", fontsize=13)
    right.text(5.05, 2.75, "$O$", color=ORANGE, ha="center", fontsize=13)
    right.text(6.15, 5.35, "Wrong sign: $O+R$", color=RED, ha="center", fontsize=11)
    right.scatter(*q, s=35, color=GREEN, zorder=6)
    right.annotate("$q$: collision", q, xytext=(-1.6, 2.5),
                   arrowprops={"arrowstyle": "->", "color": GREEN}, color=GREEN)
    right.scatter(2, 1, s=28, facecolor="white", edgecolor=GREEN, zorder=6)
    right.annotate("corner contact", (2, 1), xytext=(-1.6, -0.85),
                   arrowprops={"arrowstyle": "->", "color": GREEN}, color=GREEN, fontsize=10)
    right.text(0.5, -0.20, r"$[2,6]\times[1,4]$: area $4\cdot3=12$",
               transform=right.transAxes, ha="center", color=GREEN)
    fig.text(0.5, 0.035, r"$q+r=o\ \Longrightarrow\ q=o-r$     |     "
             "The reference point is at a corner, so the sign matters.", ha="center", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
