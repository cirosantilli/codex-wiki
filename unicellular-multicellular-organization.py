"""Original organization schematic; Python 3.14 / matplotlib 3.10 / numpy 2.3.

Run from _media; writes a matching PNG basename in the current directory.
Shapes, colors and counts are illustrative, not experimental measurements.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

BLUE = "#247ba0"
ORANGE = "#cc7722"
GREEN = "#26826a"
INK = "#243746"


def cell(ax, x, y, color=BLUE, radius=0.105):
    ax.add_patch(Circle((x, y), radius, facecolor=color, alpha=0.18,
                        edgecolor=color, linewidth=2))
    ax.add_patch(Circle((x, y), radius * 0.30, facecolor=color,
                        edgecolor="none"))


def arrow(ax, start, end, color=INK, style="->"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                mutation_scale=13, color=color, linewidth=1.5))


def main():
    plt.rcParams.update({"font.size": 11, "text.color": INK,
                         "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 4, figsize=(11.4, 4.6), dpi=100,
                             facecolor="white")
    fig.subplots_adjust(left=0.015, right=0.99, top=0.76, bottom=0.15, wspace=0.17)
    fig.suptitle("Cell count, ancestry and integration answer different questions",
                 fontsize=16, fontweight="bold", y=0.96)
    fig.text(0.5, 0.875, "Conceptual schematic — panels are not stages in an evolutionary ladder",
             ha="center", fontsize=11)
    titles = ["One cell = one organism", "Association / colony",
              "Clonal development", "Integrated functions"]
    for ax, title in zip(axes, titles):
        ax.set(xlim=(0, 1), ylim=(0, 1.15), aspect="equal")
        ax.axis("off")
        ax.set_title(title, fontsize=12, fontweight="bold", pad=15)

    ax = axes[0]
    cell(ax, 0.50, 0.58, radius=0.24)
    ax.text(0.50, 0.58, "", ha="center")
    arrow(ax, (0.06, 0.58), (0.25, 0.58), GREEN)
    arrow(ax, (0.75, 0.58), (0.94, 0.58), ORANGE)
    ax.text(0.10, 0.75, "uptake", ha="center", fontsize=10)
    ax.text(0.87, 0.75, "release", ha="center", fontsize=10)
    ax.text(0.50, 0.91, "selective boundary", ha="center", fontsize=10)
    ax.text(0.50, 0.24, "metabolism + inherited\ncellular machinery", ha="center", fontsize=11)

    ax = axes[1]
    ax.add_patch(FancyBboxPatch((0.08, 0.24), 0.84, 0.64, boxstyle="round,pad=0.01",
                               fill=False, edgecolor="#a6b4bf", linestyle="--"))
    for x, y, color in [(0.25, 0.42, BLUE), (0.51, 0.43, ORANGE), (0.77, 0.40, BLUE),
                        (0.25, 0.70, ORANGE), (0.50, 0.70, BLUE), (0.76, 0.69, ORANGE)]:
        cell(ax, x, y, color)
    ax.text(0.50, 0.14, "shown: associated lineages", ha="center", fontsize=10)

    ax = axes[2]
    positions = [(0.20, 0.57), (0.42, 0.71), (0.42, 0.43),
                 (0.66, 0.84), (0.66, 0.58), (0.66, 0.31), (0.87, 0.70)]
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (4, 6)]
    for parent, child in edges:
        xs, ys = zip(positions[parent], positions[child])
        ax.plot(xs, ys, color=BLUE, linewidth=3, zorder=0)
    for x, y in positions:
        cell(ax, x, y, BLUE, radius=0.085)
    ax.text(0.15, 0.34, "founder", ha="center", fontsize=10)
    ax.text(0.53, 0.14, "attached descendants", ha="center", fontsize=10)

    ax = axes[3]
    ax.add_patch(FancyBboxPatch((0.06, 0.21), 0.88, 0.70, boxstyle="round,pad=0.01",
                               fill=False, edgecolor=INK, linewidth=1.4))
    for x, y, color in [(0.25, 0.72, GREEN), (0.75, 0.72, ORANGE),
                        (0.25, 0.37, BLUE), (0.75, 0.37, BLUE)]:
        cell(ax, x, y, color, radius=0.09)
    arrow(ax, (0.35, 0.72), (0.64, 0.72), style="<->")
    arrow(ax, (0.25, 0.62), (0.25, 0.48), style="<->")
    arrow(ax, (0.75, 0.62), (0.75, 0.48), style="<->")
    ax.text(0.25, 1.00, "uptake", ha="center", fontsize=10)
    ax.text(0.75, 1.00, "signaling", ha="center", fontsize=10)
    ax.text(0.50, 0.12, "growth + reproduction", ha="center", fontsize=10)

    notes = ["A whole living body\nwithin one cellular boundary",
             "Can also be clonal; association\nalone does not show integration",
             "A mode of descent; specialization\nis not guaranteed",
             "Colors here denote functions,\nnot different ancestry"]
    for ax, note in zip(axes, notes):
        pos = ax.get_position()
        fig.text((pos.x0 + pos.x1) / 2, 0.035, note, ha="center", va="bottom", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
