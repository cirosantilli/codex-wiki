"""Illustrative feeding routes, not measurements of a named ecosystem.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Write an opaque white same-basename PNG to the working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


INK = "#243642"
BLUE = "#246a92"
BROWN = "#8b5939"


def arrow(ax, start, end, *, dashed=False, bend=0):
    ax.add_patch(FancyArrowPatch(
        start, end, arrowstyle="-|>", mutation_scale=18,
        connectionstyle=f"arc3,rad={bend}", linewidth=2,
        linestyle="--" if dashed else "-", color=BROWN if dashed else BLUE,
        zorder=1,
    ))


def box(ax, x, y, name, role, color):
    ax.add_patch(FancyBboxPatch(
        (x - 0.93, y - 0.43), 1.86, 0.86,
        boxstyle="round,pad=0.05", facecolor=color,
        edgecolor=INK, linewidth=1.3, zorder=2,
    ))
    ax.text(x, y + 0.11, name, ha="center", va="center",
            fontsize=12, weight="bold", color=INK)
    ax.text(x, y - 0.18, role, ha="center", va="center",
            fontsize=9.5, color=INK)


def main():
    fig, ax = plt.subplots(figsize=(9.0, 4.8))
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 10.6), ylim=(0, 5.5))
    ax.axis("off")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.96, bottom=0.04)
    ax.text(5.3, 5.14, "An illustrative aquatic food web",
            ha="center", fontsize=16, weight="bold", color=INK)
    ax.text(5.3, 4.72, "Generic groups and assumed routes • not ecosystem measurements",
            ha="center", fontsize=11, color=INK)

    xs = [1.25, 3.95, 6.65, 9.35]
    names = ["Algae", "Zooplankton", "Small fish", "Large fish"]
    roles = ["primary producers", "primary consumers",
             "predator AND prey", "predators of small fish"]
    colors = ["#e7f2de", "#e5f1fb", "#e5f1fb", "#e5f1fb"]
    for x, name, role, color in zip(xs, names, roles, colors):
        box(ax, x, 3.65, name, role, color)
    for x1, x2 in zip(xs[:-1], xs[1:]):
        arrow(ax, (x1 + 1.0, 3.65), (x2 - 1.0, 3.65))

    box(ax, 3.7, 1.75, "Detritus", "dead organic material", "#f6ecdf")
    box(ax, 7.4, 1.75, "Decomposers", "e.g. bacteria and fungi", "#f6ecdf")
    arrow(ax, (1.25, 3.17), (2.69, 1.9), dashed=True, bend=0.10)
    arrow(ax, (6.65, 3.17), (4.71, 1.9), dashed=True, bend=-0.10)
    arrow(ax, (4.72, 1.75), (6.39, 1.75))
    ax.text(3.7, 2.72, "Selected dead-material transfers",
            ha="center", fontsize=10.5, color=BROWN)

    arrow(ax, (0.45, 0.8), (1.35, 0.8))
    ax.text(1.55, 0.8, "RESOURCE → CONSUMER", va="center",
            fontsize=11, color=BLUE, weight="bold")
    arrow(ax, (6.0, 0.8), (6.9, 0.8), dashed=True)
    ax.text(7.1, 0.8, "dead-material transfer", va="center",
            fontsize=11, color=BROWN)
    ax.text(5.3, 0.24, "Other routes omitted; box sizes and arrow widths carry no quantitative scale",
            ha="center", fontsize=10, color=INK)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Illustration: 4 feeding positions, 3 chain arrows, 2 dead-material arrows.")


if __name__ == "__main__":
    main()
