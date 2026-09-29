"""Compare two orientations of one triangle, using original fixed coordinates.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg; save the matching basename PNG to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


POSITIONS = {"A": (-1.0, -0.6), "B": (0.0, 1.0), "C": (1.0, -0.6)}
ACYCLIC_EDGES = (("A", "B"), ("B", "C"), ("A", "C"))
CYCLIC_EDGES = (("A", "B"), ("B", "C"), ("C", "A"))


def draw(ax, edges, color):
    for u, v in edges:
        ax.add_patch(FancyArrowPatch(POSITIONS[u], POSITIONS[v],
                                    arrowstyle="-|>", mutation_scale=22,
                                    shrinkA=15, shrinkB=15, linewidth=2.6,
                                    color=color, zorder=1))
    for name, xy in POSITIONS.items():
        ax.add_patch(Circle(xy, 0.15, facecolor="white", edgecolor="#263746",
                            linewidth=2, zorder=2))
        ax.text(*xy, name, ha="center", va="center", fontsize=15,
                weight="bold", zorder=3)
    ax.set(xlim=(-1.35, 1.35), ylim=(-1.0, 1.35), aspect="equal")
    ax.axis("off")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.2), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.97, top=0.76, bottom=0.22, wspace=0.25)
    for ax, edges, color in zip(axes, (ACYCLIC_EDGES, CYCLIC_EDGES),
                                ("#226c9c", "#ab4529")):
        draw(ax, edges, color)
    axes[0].set_title("Acyclic orientation", fontsize=15, pad=14)
    axes[1].set_title("Cyclic orientation", fontsize=15, pad=14)
    fig.suptitle("One triangle, two different direction choices", y=0.96,
                 fontsize=17, weight="bold")
    fig.text(0.26, 0.15, "A → B → C, with A → C\nC cannot return to A", ha="center",
             fontsize=13, color="#226c9c", linespacing=1.5)
    fig.text(0.74, 0.15, "A → B → C → A\nEvery vertex reaches every other", ha="center",
             fontsize=13, color="#ab4529", linespacing=1.5)
    fig.text(0.5, 0.035, "Both underlying undirected graphs contain the same cycle.",
             ha="center", fontsize=13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
