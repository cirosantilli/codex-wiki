"""Draw logical address spaces and execution contexts, not physical RAM layouts.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; write the opaque matching PNG to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    ink, blue, green = "#203040", "#155d8a", "#187355"
    fig, ax = plt.subplots(figsize=(11, 6.4), dpi=110, facecolor="white")
    ax.set(xlim=(0, 11), ylim=(0, 6.4), facecolor="white")
    ax.axis("off")

    def box(x, y, width, height, label, color=ink, fill="white", size=11):
        ax.add_patch(FancyBboxPatch((x, y), width, height,
                                   boxstyle="round,pad=0.045", linewidth=1.4,
                                   edgecolor=color, facecolor=fill))
        if label:
            ax.text(x + width / 2, y + height / 2, label, ha="center",
                    va="center", color=color, fontsize=size, linespacing=1.45)

    ax.text(5.5, 6.14, "Processes separate mappings; threads share mappings",
            ha="center", fontsize=17, weight="bold", color=ink)
    ax.text(2.75, 5.58, "Two processes running the same executable",
            ha="center", fontsize=12, weight="bold", color=ink)
    ax.text(8.15, 5.58, "Two threads within one process",
            ha="center", fontsize=12, weight="bold", color=ink)
    for x, name, value, color, fill in [(0.35, "A", 7, blue, "#eef5fa"),
                                        (2.95, "B", 42, green, "#eef7f2")]:
        box(x, 2.65, 2.2, 2.5, "", color, fill)
        ax.text(x + 1.1, 4.89, f"Process {name}: address space",
                ha="center", fontsize=10.5, weight="bold", color=color)
        box(x + 0.15, 3.75, 1.9, 0.65, f"VA 0x1234: x = {value}", color, "white")
        box(x + 0.15, 2.91, 1.9, 0.5, f"Call stack of {name}", color, "white")
        box(x, 1.33, 2.2, 0.85, f"{name}'s execution context\nregisters, PC, SP", color, fill)
        ax.text(x + 1.1, 2.4, "Mappings select contents", ha="center",
                fontsize=9.5, color=color)
    ax.text(2.75, 0.97, "Same numeric VA, different private counters",
            ha="center", fontsize=11, color=ink)

    box(5.8, 2.65, 4.7, 2.5, "", ink, "#f2f4f6")
    ax.text(8.15, 4.89, "One shared address space", ha="center",
            fontsize=12, weight="bold", color=ink)
    box(6.25, 3.75, 3.8, 0.65, "VA 0x1234: one shared x = 0", ink)
    box(6.0, 2.91, 2.05, 0.5, "T1's call stack", blue, "#eef5fa")
    box(8.25, 2.91, 2.05, 0.5, "T2's call stack", green, "#eef7f2")
    ax.text(8.15, 2.4, "Globals, heap and both stacks are addressable by T1 and T2",
            ha="center", fontsize=9.5, color=ink)
    box(5.95, 1.33, 2.1, 0.85, "T1's own context\nregisters, PC1, SP1", blue, "#eef5fa")
    box(8.25, 1.33, 2.1, 0.85, "T2's own context\nregisters, PC2, SP2", green, "#eef7f2")
    ax.text(8.15, 0.97, "Process resources such as file descriptors are shared too",
            ha="center", fontsize=10, color=ink)
    ax.text(5.5, 0.55, "Own stacks are logical assignments, not protection from another thread.",
            ha="center", fontsize=11, color=ink)
    ax.text(5.5, 0.18, "Separate processes may deliberately share memory; code and copy-on-write pages may share physical storage.",
            ha="center", fontsize=10, color=ink)
    fig.subplots_adjust(left=0.015, right=0.985, top=0.985, bottom=0.02)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
