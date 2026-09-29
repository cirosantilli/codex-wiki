"""Draw a capacity-five ring at trace step 8; emit PNG in the current directory."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def main():
    fig, ax = plt.subplots(figsize=(9, 5.1), dpi=120, facecolor="white")
    ax.set(xlim=(-0.7, 7.1), ylim=(-0.4, 4.7))
    ax.axis("off")
    fig.subplots_adjust(left=0.035, right=0.985, bottom=0.035, top=0.97)
    ax.text(3.2, 4.37, "One array, two orders", ha="center", fontsize=19, weight="bold")
    ax.text(3.2, 3.94, "Capacity 5  •  front h = 2  •  count n = 4  •  next write w = 1",
            ha="center", fontsize=12)
    colors = {"C": "#c9e8f2", "D": "#d9edba", "E": "#ffe1a6", "F": "#e3d6f2"}
    physical = ["F", "B", "C", "D", "E"]
    ax.text(-0.35, 3.70, "Physical slots (fixed addresses)", fontsize=12, weight="bold")
    for i, item in enumerate(physical):
        ax.add_patch(Rectangle((i * 1.12, 2.1), 1, 0.75,
                               facecolor=colors.get(item, "#f3f3f3"),
                               edgecolor="#35434c", lw=1.4,
                               hatch="///" if i == 1 else None))
        ax.text(i * 1.12 + 0.5, 2.48, item, ha="center", va="center",
                fontsize=20, color="#91979a" if i == 1 else "#172630", weight="bold")
        ax.text(i * 1.12 + 0.5, 2.98, str(i), ha="center", fontsize=11)
    ax.annotate("h: front", (2.74, 2.1), (2.74, 1.6), ha="center", fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#35434c"})
    ax.annotate("w: reuse stale B", (1.62, 2.1), (0.7, 1.45), ha="center", fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#35434c"})
    ax.add_patch(FancyArrowPatch((5.0, 3.12), (0.49, 3.12),
                                connectionstyle="arc3,rad=0.12", arrowstyle="->",
                                mutation_scale=13, color="#925426", lw=1.5))
    ax.text(2.75, 3.53, "after slot 4, wrap to slot 0", ha="center", fontsize=10,
            color="#925426")
    ax.text(-0.35, 0.98, "Logical queue (front → rear)", fontsize=12, weight="bold")
    for j, (item, i) in enumerate(zip("CDEF", [2, 3, 4, 0])):
        x = 0.65 + j * 1.27
        ax.add_patch(Rectangle((x, 0.06), 1, 0.66, facecolor=colors[item], edgecolor="#35434c"))
        ax.text(x + 0.5, 0.39, item, ha="center", va="center", fontsize=19, weight="bold")
        ax.text(x + 0.5, -0.22, f"slot {i}", ha="center", fontsize=10)
        if j < 3:
            ax.annotate("", (x + 1.26, 0.39), (x + 1.02, 0.39),
                        arrowprops={"arrowstyle": "->", "color": "#35434c"})
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
