"""Draw the 16 reads for row/column traversal with an initially empty one-line cache.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; outputs this script's PNG basename to the current directory.
Read-only, fully associative LRU model; no prefetching or writeback costs.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    row_colours = ["#dceaf8", "#fce4cc", "#ddedda", "#ebe0f4"]
    fig, axes = plt.subplots(2, 1, figsize=(10.4, 6.0), dpi=120)
    fig.patch.set_facecolor("white")
    fig.suptitle("One resident line: use it before replacing it", fontsize=18, fontweight="bold", y=0.96)
    fig.text(0.5, 0.89, "16 array reads • empty initial cache • capacity 1 line • fully associative LRU • no prefetch / writes",
             ha="center", fontsize=10.5)
    orders = [[(i, j) for i in range(4) for j in range(4)],
              [(i, j) for j in range(4) for i in range(4)]]
    for ax, order, name in zip(axes, orders, ["By rows", "By columns"]):
        lines = np.array([(4 * (4 * i + j)) // 16 for i, j in order])
        resident = None
        hits = []
        for step, ((i, j), line) in enumerate(zip(order, lines), start=1):
            hit = resident == line
            hits.append(hit)
            resident = line
            ax.add_patch(Rectangle((step - 0.46, 1.5), 0.92, 0.82,
                                   facecolor=row_colours[line], edgecolor="white"))
            ax.text(step, 1.91, str(line), ha="center", va="center", fontweight="bold")
            ax.text(step, 2.65, f"{i},{j}", ha="center", va="center", fontsize=9)
            ax.add_patch(Rectangle((step - 0.46, 0.48), 0.92, 0.74,
                                   facecolor="#d6eee6" if hit else "#f9dfd9",
                                   edgecolor="#13765b" if hit else "#b43c25", linewidth=1.2))
            ax.text(step, 0.85, "H" if hit else "M", ha="center", va="center", fontweight="bold",
                    color="#0c5943" if hit else "#8e2818")
        count = sum(hits)
        assert count == (12 if name == "By rows" else 0)
        ax.set_title(f"{name}: {16 - count} misses, {count} hits", loc="left", fontsize=13, fontweight="bold", pad=10)
        ax.set(xlim=(0.4, 16.6), ylim=(0.1, 3), xticks=np.arange(1, 17),
               yticks=[0.85, 1.91, 2.65], yticklabels=["Outcome", "Line", "Item i,j"])
        ax.set_xlabel("Memory reference number", labelpad=7)
        ax.tick_params(length=0)
        for spine in ax.spines.values():
            spine.set_visible(False)
    fig.text(0.5, 0.048, "H = hit; M = miss. After each read, the requested line is the sole resident line.\n"
             "With capacity 4 lines, BOTH orders instead have 4 compulsory misses and 12 hits.",
             ha="center", fontsize=11, linespacing=1.6)
    fig.subplots_adjust(left=0.10, right=0.985, top=0.79, bottom=0.18, hspace=0.80)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
