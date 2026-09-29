"""Draw an original triangle-with-leaf subdivision and its edge paths.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg; the matching PNG is saved to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


TARGET_EDGES = (("A", "B"), ("B", "C"), ("C", "A"), ("A", "D"))
EDGE_PATHS = (("A", "x", "B"), ("B", "y", "z", "C"),
              ("C", "A"), ("A", "D"))
COLORS = ("#2166ac", "#c66a10", "#248045", "#8055a5")


def vertex(ax, label, xy, original):
    ax.add_patch(Circle(xy, 0.14 if original else 0.105,
                        facecolor="white", edgecolor="#253444" if original else "#777777",
                        linewidth=2.1 if original else 1.5, zorder=3))
    ax.text(*xy, label, ha="center", va="center", fontsize=13,
            weight="bold" if original else "normal", zorder=4)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.6), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.26, top=0.78, wspace=0.36)
    original = {"A": (-0.7, 0.7), "B": (1.1, 0.7),
                "C": (0.2, -0.8), "D": (-1.6, 1.3)}
    subdivided = dict(original, x=(0.2, 0.7), y=(0.8, 0.2), z=(0.5, -0.3))
    for ax, positions, paths in ((axes[0], original, TARGET_EDGES),
                                  (axes[1], subdivided, EDGE_PATHS)):
        for color, path in zip(COLORS, paths):
            ax.plot([positions[v][0] for v in path], [positions[v][1] for v in path],
                    color=color, linewidth=3, zorder=1)
        for label, xy in positions.items():
            vertex(ax, label, xy, label in original)
        ax.set(xlim=(-1.9, 1.45), ylim=(-1.05, 1.6), aspect="equal")
        ax.axis("off")
    axes[0].set_title("Target H: 4 vertices, 4 edges", fontsize=13, pad=12)
    axes[1].set_title("Subdivision S: 7 vertices, 7 edges", fontsize=13, pad=12)
    fig.suptitle("Subdivision lengthens routes, retaining the junctions", y=0.96,
                 fontsize=16, weight="bold")
    fig.add_artist(FancyArrowPatch((0.455, 0.52), (0.545, 0.52),
                                  transform=fig.transFigure, arrowstyle="-|>",
                                  mutation_scale=20, linewidth=1.7, color="#34495e"))
    for x, text, color in zip((0.16, 0.43, 0.68, 0.88),
                              ("AB → A–x–B", "BC → B–y–z–C", "CA unchanged", "AD unchanged"),
                              COLORS):
        fig.text(x, 0.18, text, color=color, ha="center", fontsize=12)
    fig.text(0.5, 0.095, "A, B, C, D: retained branch vertices     x, y, z: new internal vertices",
             ha="center", fontsize=12)
    fig.text(0.5, 0.04, "Internal vertices are disjoint between routes and avoid all branch vertices.",
             ha="center", fontsize=12)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
