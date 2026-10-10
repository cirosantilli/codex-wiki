"""Draw the initial copy-on-write mappings; save the matching PNG to CWD.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
Arrows are mappings; reference counts count these mappings only.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 5.6), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 5.6))
    ax.axis("off")
    ink, blue, purple = "#183044", "#2166ac", "#6f479b"

    def box(x, y, w, h, text, color="#edf4fa", edge=ink):
        ax.add_patch(FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.035,rounding_size=0.08",
            linewidth=1.2, edgecolor=edge, facecolor=color, zorder=2,
        ))
        ax.text(x+w/2, y+h/2, text, ha="center", va="center",
                fontsize=11, color=ink, linespacing=1.35, zorder=3)

    ax.text(5, 5.28, "Copy-on-write: separate mappings, shared contents",
            ha="center", fontsize=16, weight="bold", color=ink)
    for x, label, color in [(1.4, "Parent A", blue), (8.6, "Child B", purple)]:
        ax.text(x, 4.8, label, ha="center", fontsize=13, weight="bold", color=color)
        ax.text(x, 4.46, "Own page table", ha="center", fontsize=11, color=ink)
    ax.text(5, 4.63, "Physical page frames", ha="center", fontsize=12, weight="bold", color=ink)
    for i, (page, value) in enumerate([("0x12", "x = 7"), ("0x13", "y = 20"), ("0x14", "z = 30")]):
        y = 3.5 - 1.05*i
        box(0.3, y, 2.2, 0.75, f"page {page} → F{i}\nRO / COW", edge=blue)
        box(7.5, y, 2.2, 0.75, f"page {page} → F{i}\nRO / COW", edge=purple)
        box(3.75, y, 2.5, 0.75, f"F{i}:  {value}\nreferences = 2", "#f1f3f5")
        for start, end, color in [((2.55, y+.375), (3.7, y+.375), blue),
                                  ((7.45, y+.375), (6.3, y+.375), purple)]:
            ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                        mutation_scale=14, color=color, linewidth=1.6))
    ax.text(5, .82, "RO = hardware read-only; COW = private writes allowed after fault handling",
            ha="center", fontsize=10.5, color=ink)
    ax.text(5, .42, "6 virtual-page mappings • 3 physical data frames • 0 data copies",
            ha="center", fontsize=12, weight="bold", color=ink)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
