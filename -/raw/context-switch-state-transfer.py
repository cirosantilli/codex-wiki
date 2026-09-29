"""Draw logical execution-state transfers, not an architecture's entry sequence.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; write the opaque matching PNG to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(10, 5.7), dpi=110, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.set_facecolor("white")
    ax.axis("off")
    ink, blue, green = "#203040", "#155d8a", "#187355"

    def box(x, y, width, height, text, color, fill):
        ax.add_patch(FancyBboxPatch((x, y), width, height,
                                   boxstyle="round,pad=0.06", linewidth=1.5,
                                   edgecolor=color, facecolor=fill))
        ax.text(x + width / 2, y + height / 2, text, ha="center",
                va="center", color=color, fontsize=12, linespacing=1.5)

    def arrow(start, end, color):
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "-|>", "lw": 2, "color": color})

    ax.text(5, 5.75, "Context switch: preserve A, resume B", ha="center",
            fontsize=17, weight="bold", color=ink)
    ax.text(5, 5.32, "Three moments on the same single CPU", ha="center", color=ink)
    box(0.25, 3.35, 2.35, 1.4, "Before: CPU runs A\nPC = p_A; SP = u_A\ndata register = 7", blue, "#eef5fa")
    box(3.35, 3.35, 3.3, 1.4, "During: CPU runs kernel\nsave A; scheduler selects B\nload B; return to B", ink, "#f2f4f6")
    box(7.4, 3.35, 2.35, 1.4, "After: CPU runs B\nPC = p_B; SP = u_B\ndata register = 42", green, "#eef7f2")
    arrow((2.68, 4.05), (3.26, 4.05), ink)
    arrow((6.74, 4.05), (7.31, 4.05), ink)
    box(0.75, 1.25, 3.2, 1.05, "A's saved context in memory\np_A, u_A, 7 retained", blue, "#eef5fa")
    box(6.05, 1.25, 3.2, 1.05, "B's saved context in memory\np_B, u_B, 42 available", green, "#eef7f2")
    arrow((4.05, 3.27), (2.5, 2.39), blue)
    ax.text(2.6, 2.85, "1. Save A's state", ha="center", color=blue, fontsize=11)
    arrow((7.5, 2.39), (5.95, 3.27), green)
    ax.text(7.45, 2.85, "2. Load B's state", ha="center", color=green, fontsize=11)
    ax.text(5, 0.79, "Selected resume fields; hardware entry and software switching are grouped.",
            ha="center", fontsize=10.5, color=ink)
    ax.text(5, 0.38, "No whole address-space copy. Same-process threads can retain mappings;",
            ha="center", fontsize=11, color=ink)
    ax.text(5, 0.04, "different address spaces may require a memory-management context change.",
            ha="center", fontsize=11, color=ink)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.98, bottom=0.035)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
