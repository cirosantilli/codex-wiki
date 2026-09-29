"""Draw exact work ledgers on a common halving tree (Python 3.14, matplotlib 3.10)."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(11.6, 6.2), dpi=120, facecolor="white")
    ax = fig.add_axes((0, 0, 1, 1), facecolor="white")
    ax.set(xlim=(0, 11.6), ylim=(0, 6.2))
    ax.axis("off")
    ink, blue, orange = "#172d41", "#17618f", "#b25a16"
    ax.text(0.35, 5.84, "Halving alone does not determine the work", fontsize=19,
            fontweight="bold", color=ink)
    ax.text(0.35, 5.43, "Two children per call; initial size 16; one unit per terminal call",
            color=ink, fontsize=12)
    ax.text(2.8, 4.95, "Same split tree: labels are instance sizes", ha="center", color=ink)
    ax.text(7.16, 4.95, "Linear local work", ha="center", color=blue, weight="bold")
    ax.text(9.90, 4.95, "Quadratic local work", ha="center", color=orange, weight="bold")
    ax.text(7.16, 4.59, r"$g(s)=s$", ha="center", color=blue, fontsize=14)
    ax.text(9.90, 4.59, r"$g(s)=s^2$", ha="center", color=orange, fontsize=14)

    x0, tree_width, row_height = 0.45, 4.9, 0.38
    level_ys = [4.12 - 0.67 * j for j in range(5)]
    for j, y in enumerate(level_ys):
        calls, size = 2 ** j, 16 // 2 ** j
        cell_width = tree_width / calls
        if j:
            previous_y = level_ys[j - 1]
            for i in range(calls):
                parent_x = x0 + (i // 2 + 0.5) * cell_width * 2
                child_x = x0 + (i + 0.5) * cell_width
                ax.plot([parent_x, child_x], [previous_y - row_height / 2, y + row_height / 2],
                        color="#9aafbd", linewidth=0.8, zorder=1)
        for i in range(calls):
            left = x0 + i * cell_width + 0.025
            ax.add_patch(Rectangle((left, y - row_height / 2), cell_width - 0.05,
                                   row_height, facecolor="#eef5fa" if j < 4 else "#edf6ec",
                                   edgecolor="#7895a8", linewidth=0.8, zorder=2))
            ax.text(left + (cell_width - 0.05) / 2, y, str(size), ha="center", va="center",
                    fontsize=11 if j < 4 else 9, color=ink, zorder=3)
        for x, color, power in [(7.16, blue, 1), (9.90, orange, 2)]:
            if j < 4:
                work = calls * size ** power
                expression = f"{calls} × {size}" + ("²" if power == 2 else "") + f" = {work}"
            else:
                expression = "16 terminal calls = 16"
            ax.text(x, y, expression, ha="center", va="center", color=color, fontsize=12)
        if j == 3:
            ax.plot([5.7, 11.25], [y - 0.36, y - 0.36], color="#c9d4db", lw=1)

    ax.add_patch(FancyArrowPatch((0.22, 4.22), (0.22, 1.45), arrowstyle="->",
                                mutation_scale=14, color=blue, linewidth=1.4))
    ax.text(0.10, 2.83, "split", rotation=90, ha="center", va="center", fontsize=10, color=blue)
    ax.add_patch(FancyArrowPatch((5.53, 1.45), (5.53, 4.22), arrowstyle="->",
                                mutation_scale=14, color=orange, linewidth=1.4))
    ax.text(5.63, 2.83, "combine", rotation=90, ha="center", va="center", fontsize=10, color=orange)
    ax.text(2.90, 0.91, "4 internal levels + terminal level", ha="center", color=ink, fontsize=11)
    ax.text(7.16, 0.91, "Total: 80", ha="center", color=blue, weight="bold", fontsize=17)
    ax.text(9.90, 0.91, "Total: 496", ha="center", color=orange, weight="bold", fontsize=17)
    ax.text(0.35, 0.35, "Exact constructed costs: the tree stays fixed while local reconstruction work changes.",
            color=ink, fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
