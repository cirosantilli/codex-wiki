"""Draw two access orders over an unchanged row-major array.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; outputs this script's PNG basename to the current directory.
Each coloured row is one physical 16-byte cache block of four 4-byte items.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    colours = ["#dceaf8", "#fce4cc", "#ddedda", "#ebe0f4"]
    addresses = 4 * np.arange(16).reshape(4, 4)
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.9), dpi=120)
    fig.patch.set_facecolor("white")
    fig.suptitle("Same storage, different traversal", fontsize=19, fontweight="bold", y=0.96)
    fig.text(0.5, 0.885, "4 × 4 row-major array • 4 bytes per item • 16 bytes per cache line • aligned base 0",
             ha="center", fontsize=11)
    orders = [[(i, j) for i in range(4) for j in range(4)],
              [(i, j) for j in range(4) for i in range(4)]]
    for ax, order, title in zip(axes, orders, ["By rows: column j varies fastest", "By columns: row i varies fastest"]):
        for i in range(4):
            for j in range(4):
                ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1,
                                       facecolor=colours[i], edgecolor="white", linewidth=2))
                ax.text(j, i + 0.28, f"addr {addresses[i, j]}", ha="center", va="center", fontsize=9, color="#333333",
                        bbox={"facecolor": colours[i], "edgecolor": "none", "pad": 0.1}, zorder=5)
            ax.text(3.67, i, f"line {i}", va="center", fontsize=10)
        for step, (i, j) in enumerate(order, start=1):
            ax.text(j, i - 0.18, str(step), ha="center", va="center", fontweight="bold", fontsize=13,
                    bbox={"boxstyle": "circle,pad=0.14", "facecolor": "white", "edgecolor": "#233e55"}, zorder=4)
        for (i, j), (next_i, next_j) in zip(order[:-1], order[1:]):
            reset = (next_j < j) if title.startswith("By rows") else (next_i < i)
            ax.annotate("", xy=(next_j, next_i - 0.18), xytext=(j, i - 0.18),
                        arrowprops={"arrowstyle": "->", "color": "#233e55", "lw": 1.6 if not reset else 1.1,
                                    "linestyle": "--" if reset else "-", "shrinkA": 15, "shrinkB": 15,
                                    "connectionstyle": "arc3,rad=0"}, zorder=3)
        ax.set(xlim=(-0.6, 4.2), ylim=(3.6, -0.65), aspect="equal", xticks=range(4), yticks=range(4),
               xlabel="Column j", ylabel="Row i")
        ax.set_title(title, fontsize=12, pad=12, fontweight="bold")
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.tick_params(length=0)
    fig.text(0.5, 0.04, "Circled numbers = access steps 1–16; arrows follow time (dashed = next row / column).\n"
             "Row colours identify physical cache lines in BOTH panels; storage never moves.",
             ha="center", fontsize=11, linespacing=1.7)
    fig.subplots_adjust(left=0.06, right=0.99, top=0.80, bottom=0.24, wspace=0.15)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
