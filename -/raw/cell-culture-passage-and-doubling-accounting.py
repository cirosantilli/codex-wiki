"""Original cell-culture count ledger; Python 3.14, matplotlib 3.10.7.

Run from _media to write cell-culture-passage-and-doubling-accounting.png.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 4.6), dpi=110, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 4.6))
    ax.axis("off")
    ink, blue, green = "#203047", "#27649a", "#28734f"
    ax.text(5, 4.27, "Growth and transfer change different counters", ha="center",
            fontsize=17, color=ink, weight="bold")
    ax.text(5, 3.9, "Constructed population ledger · no measured growth curve",
            ha="center", fontsize=11, color=ink)
    boxes = [(0.15, "First seed", "300,000 cells", "Passage p"),
             (2.68, "First harvest", "1,200,000 cells", "Passage p"),
             (5.21, "Next seed", "300,000 cells", "Passage p + 1"),
             (7.74, "Next harvest", "1,200,000 cells", "Passage p + 1")]
    for x, title, count, passage in boxes:
        ax.add_patch(FancyBboxPatch((x, 2.2), 2.1, 1.25,
                                   boxstyle="round,pad=0.035", facecolor="#f4f7fb",
                                   edgecolor=blue, linewidth=1.6))
        ax.text(x + 1.05, 3.16, title, ha="center", fontsize=12, color=ink)
        ax.text(x + 1.05, 2.81, count, ha="center", fontsize=12,
                color=blue, weight="bold")
        ax.text(x + 1.05, 2.45, passage, ha="center", fontsize=11, color=ink)
    for left, label, color in [(2.27, "×4 growth", green),
                               (4.8, "keep ¼", blue),
                               (7.33, "×4 growth", green)]:
        ax.add_patch(FancyArrowPatch((left, 2.84), (left + 0.36, 2.84),
                                    arrowstyle="-|>", mutation_scale=16,
                                    linewidth=1.8, color=color))
        ax.text(left + 0.18, 1.95, label, ha="center", fontsize=11, color=color)
    for x in [2.5, 7.55]:
        ax.text(x, 1.47, "2 net doublings", ha="center", color=green, fontsize=12)
    ax.text(5, 1.07, "Transfer: 300,000 retained + 900,000 outside tracked vessel",
            ha="center", fontsize=11, color=ink)
    ax.text(5, 0.56, "Across both growth intervals: 4 net doublings · 1 intervening passage",
            ha="center", fontsize=13, color=ink, weight="bold")
    fig.subplots_adjust(left=0.015, right=0.985, top=0.985, bottom=0.015)
    fig.savefig(Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
