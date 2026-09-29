"""Draw private page divergence after a write; save the matching PNG to CWD.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
The original frame's remaining mapping stays protected until a later fault.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 6.4), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.4))
    ax.axis("off")
    ink, blue, purple, green = "#183044", "#2166ac", "#6f479b", "#27734d"

    def box(x, y, w, h, text, color="#edf4fa", edge=ink):
        ax.add_patch(FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.035,rounding_size=0.08",
            linewidth=1.2, edgecolor=edge, facecolor=color, zorder=2,
        ))
        ax.text(x+w/2, y+h/2, text, ha="center", va="center",
                fontsize=11, color=ink, linespacing=1.35, zorder=3)

    def arrow(start, end, color, style="-|>", dashed=False):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                    mutation_scale=14, color=color, linewidth=1.6,
                                    linestyle="--" if dashed else "-", zorder=1))

    ax.text(5, 6.08, "After child B writes x = 42: one private copy",
            ha="center", fontsize=16, weight="bold", color=ink)
    for x, label, color in [(1.4, "Parent A", blue), (8.6, "Child B", purple)]:
        ax.text(x, 5.6, label, ha="center", fontsize=13, weight="bold", color=color)
        ax.text(x, 5.27, "Own page table", ha="center", fontsize=11, color=ink)
    ax.text(5, 5.6, "Physical page frames", ha="center", fontsize=12, weight="bold", color=ink)
    box(.3, 4.24, 2.2, .75, "page 0x12 → F0\nRO / COW", edge=blue)
    box(7.5, 3.26, 2.2, .75, "page 0x12 → F3\nread / write", "#e9f5ec", green)
    box(3.75, 4.24, 2.5, .75, "F0:  x = 7\nreferences = 1", "#f1f3f5")
    box(3.75, 3.26, 2.5, .75, "F3:  x = 42\nreferences = 1", "#e9f5ec", green)
    arrow((2.55, 4.615), (3.7, 4.615), blue)
    arrow((7.45, 3.635), (6.3, 3.635), purple)
    arrow((5, 4.2), (5, 4.05), green, dashed=True)
    ax.text(8.6, 4.49, "Fault → copy F0 → F3\nremap → retry write", ha="center", va="center",
            fontsize=10.8, color=green)
    ax.text(2.18, 3.65, "A still reads 7", ha="center", fontsize=11, color=blue)
    for i, (page, value) in enumerate([("0x13", "y = 20"), ("0x14", "z = 30")], start=1):
        y = 2.16 - 1.05*(i-1)
        box(.3, y, 2.2, .75, f"page {page} → F{i}\nRO / COW", edge=blue)
        box(7.5, y, 2.2, .75, f"page {page} → F{i}\nRO / COW", edge=purple)
        box(3.75, y, 2.5, .75, f"F{i}:  {value}\nreferences = 2", "#f1f3f5")
        arrow((2.55, y+.375), (3.7, y+.375), blue)
        arrow((7.45, y+.375), (6.3, y+.375), purple)
    ax.text(5, .66, "F0 is now exclusive; its remaining mapping is still protected in this model",
            ha="center", fontsize=10.5, color=ink)
    ax.text(5, .27, "6 virtual-page mappings • 4 physical data frames • 1 whole-page copy",
            ha="center", fontsize=12, weight="bold", color=ink)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
