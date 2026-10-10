"""Compare adding before and after relabeling C6; write a PNG to the CWD.

Tested with Python 3.14 and Matplotlib 3.10.7. All sums are modulo six.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def node(ax, position, text, color):
    ax.text(*position, text, ha="center", va="center", fontsize=16,
            color=color, weight="bold",
            bbox={"boxstyle": "round,pad=0.30", "facecolor": "white",
                  "edgecolor": color, "linewidth": 1.8}, zorder=3)


def arrow(ax, start, end, color):
    ax.add_patch(FancyArrowPatch(start, end, shrinkA=25, shrinkB=25,
                                arrowstyle="-|>", mutation_scale=16,
                                linewidth=2, color=color, zorder=1))


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.9), dpi=100)
    blue, orange, dark = "#2166a5", "#b65b13", "#263238"
    top, left, right = (0, 3), (-1.65, 1.7), (1.65, 1.7)
    bottom_left, bottom_right = (-1.65, 0.15), (1.65, 0.15)
    for ax, compatible in zip(axes, (True, False), strict=True):
        value = 5 if compatible else 2
        sum_then_map = 4 if compatible else 1
        map_then_sum = (value + value) % 6
        title = (r"$f_5(k)=5k\;\mathrm{mod}\;6$" if compatible else
                 r"$\pi$: exchange 1 and 2, fix the rest")
        node(ax, top, "(1, 1)", dark)
        node(ax, left, "2", blue)
        node(ax, right, f"({value}, {value})", orange)
        node(ax, bottom_left, str(sum_then_map), blue)
        node(ax, bottom_right, str(map_then_sum), orange)
        arrow(ax, top, left, blue)
        arrow(ax, top, right, orange)
        arrow(ax, left, bottom_left, blue)
        arrow(ax, right, bottom_right, orange)
        ax.text(-1.28, 2.75, "Add", color=blue, ha="center")
        ax.text(1.28, 2.75, "Relabel each", color=orange, ha="center")
        ax.text(-1.65, 0.96, "Relabel", color=blue, ha="center", va="center",
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
        ax.text(1.65, 0.96, "Add", color=orange, ha="center", va="center",
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
        ax.text(0, 0.15, "=" if compatible else r"$\ne$",
                ha="center", va="center", fontsize=26, color=dark)
        ax.text(0, -0.58, "Agrees for every input pair" if compatible else
                "One disagreement is enough to disprove it",
                ha="center", va="center", fontsize=11, weight="bold")
        ax.set_title(title, fontsize=14, pad=12)
        ax.set(xlim=(-2.5, 2.5), ylim=(-1, 3.5))
        ax.axis("off")
    fig.suptitle("Does relabeling commute with addition modulo six?",
                 fontsize=16, weight="bold", y=0.96)
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.08, top=0.78, wspace=0.20)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
