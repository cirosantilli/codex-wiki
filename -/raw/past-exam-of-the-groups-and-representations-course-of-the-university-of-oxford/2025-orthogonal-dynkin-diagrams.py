"""Draw the orthogonal Dynkin families; Python 3.14, numpy/matplotlib.

Run from the desired output directory. Writes only the PNG in that directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def node(ax, x, y, label):
    ax.add_patch(Circle((x, y), 0.105, facecolor="white", edgecolor="#17365a", linewidth=2.2, zorder=3))
    ax.text(x, y - 0.30, label, ha="center", va="top", fontsize=15)


def edge(ax, a, b):
    ax.plot([a[0], b[0]], [a[1], b[1]], color="#17365a", linewidth=2, zorder=1)


def main():
    fig, axes = plt.subplots(2, 1, figsize=(8.0, 4.8), facecolor="white")
    for ax in axes:
        ax.set(xlim=(-1.0, 5.2), ylim=(-1.0, 1.0), aspect="equal")
        ax.axis("off")
    ax = axes[0]
    ax.text(-0.9, 0.45, r"$B_n:\ \mathfrak{so}(2n+1)$", fontsize=18)
    for x, label in [(0, "$1$"), (1, "$2$"), (3, "$n-1$"), (4.35, "$n$")]:
        node(ax, x, 0, label)
    edge(ax, (0, 0), (1, 0))
    edge(ax, (1, 0), (1.4, 0))
    ax.text(2, 0, r"$\cdots$", ha="center", va="center", fontsize=20)
    edge(ax, (2.6, 0), (3, 0))
    for y in [-0.055, 0.055]:
        edge(ax, (3.08, y), (4.27, y))
    ax.add_patch(FancyArrowPatch((3.45, 0), (4.0, 0), arrowstyle="->", mutation_scale=24, linewidth=2, color="#17365a", zorder=4))
    ax.text(4.35, 0.26, "short", ha="center", fontsize=13, color="#9c3e17")
    ax = axes[1]
    ax.text(-0.9, 0.75, r"$D_n:\ \mathfrak{so}(2n)$", fontsize=18)
    for x, label in [(0, "$1$"), (1, "$2$"), (3, "$n-2$")]:
        node(ax, x, 0, label)
    edge(ax, (0, 0), (1, 0))
    edge(ax, (1, 0), (1.4, 0))
    ax.text(2, 0, r"$\cdots$", ha="center", va="center", fontsize=20)
    edge(ax, (2.6, 0), (3, 0))
    for y, label in [(0.60, "$n-1$"), (-0.60, "$n$")]:
        edge(ax, (3, 0), (4.35, y))
        ax.add_patch(Circle((4.35, y), 0.105, facecolor="white", edgecolor="#17365a", linewidth=2.2, zorder=3))
        ax.text(4.65, y, label, ha="left", va="center", fontsize=15)
    fig.subplots_adjust(left=0.04, right=0.96, top=0.96, bottom=0.05, hspace=0.15)
    fig.savefig(Path("2025-orthogonal-dynkin-diagrams.png"), dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
