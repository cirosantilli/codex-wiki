"""Original two-dimensional lattice-plus-motif diagram; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(11, 4.7), dpi=110)
    blue, orange, green = "#176baf", "#d76b13", "#18825c"
    a1, a2 = np.array([2., 0.]), np.array([0., 1.5])
    offset = np.array([.65, .55])
    for ax in axes:
        ax.set_aspect("equal")
        ax.set_xlim(-.5, 4.9)
        ax.set_ylim(-.5, 3.8)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)
    for ax in [axes[0], axes[2]]:
        for i in range(3):
            for j in range(3):
                p = i*a1+j*a2
                ax.plot(*p, "o", color="0.25" if ax is axes[0] else blue,
                        ms=5 if ax is axes[0] else 8, zorder=3)
                if ax is axes[2]:
                    ax.plot(*(p+offset), "o", color=orange, ms=8, zorder=3)
        ax.add_patch(Rectangle((-.22, -.22), 2, 1.5, color=green,
                               alpha=.12, zorder=1))
        ax.add_patch(Rectangle((-.22, -.22), 2, 1.5, fill=False,
                               edgecolor=green, lw=1.7, zorder=2))
    for vec, label, shift in [(a1, r"$\mathbf{a}_1=(2,0)$", (1., -.38)),
                              (a2, r"$\mathbf{a}_2=(0,1.5)$", (.08, 1.75))]:
        axes[0].annotate("", xy=vec, xytext=(0, 0),
                         arrowprops={"arrowstyle": "->", "color": green, "lw": 2})
        axes[0].text(*shift, label, ha="center", color=green)
    axes[0].set_title("1. Translation lattice", weight="bold")
    axes[1].plot(1, 1.4, "o", color=blue, ms=12)
    axes[1].plot(1.65, 1.95, "o", color=orange, ms=12)
    axes[1].annotate("A: (0, 0)", xy=(1, 1.4), xytext=(.15, .5),
                     arrowprops={"arrowstyle": "-", "color": blue}, color=blue)
    axes[1].annotate("B: (0.65, 0.55)", xy=(1.65, 1.95), xytext=(.15, 2.9),
                     arrowprops={"arrowstyle": "-", "color": orange}, color=orange)
    axes[1].set_title("2. Two-site motif", weight="bold")
    axes[2].set_title("3. Repeat both sites", weight="bold")
    captions = ["One lattice point per green cell",
                "Positions relative to a lattice point\nA and B are different species",
                "One A + one B per primitive cell\nGreen cell is shifted to avoid boundaries"]
    for ax, caption in zip(axes, captions):
        ax.text(.5, -.12, caption, transform=ax.transAxes, ha="center", va="top")
    fig.suptitle("Translations specify repetition; the motif specifies chemistry", fontsize=15)
    fig.text(.5, .035, "Chosen model coordinates, arbitrary length units; dots do not represent atomic radii.",
             ha="center", fontsize=10, color="0.3")
    fig.subplots_adjust(left=.035, right=.985, top=.85, bottom=.22, wspace=.18)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
