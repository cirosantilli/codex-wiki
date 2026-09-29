"""Draw a degree-three tree and its degree-four star contraction minor.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg; the matching PNG is saved to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch


TREE_EDGES = (("u", "v"), ("u", "a"), ("u", "b"), ("v", "c"), ("v", "d"))
CONTRACTION_MAP = {"u": "w", "v": "w", "a": "a", "b": "b", "c": "c", "d": "d"}


def vertex(ax, label, xy, centre=False):
    ax.add_patch(Circle(xy, 0.15, facecolor="white",
                        edgecolor="#2166ac" if centre else "#34495e",
                        linewidth=2.2, zorder=3))
    ax.text(*xy, label, ha="center", va="center", fontsize=14,
            weight="bold", color="#2166ac" if centre else "#34495e", zorder=4)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.6), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.26, top=0.78, wspace=0.36)
    tree_pos = {"u": (-0.62, 0), "v": (0.62, 0), "a": (-1.55, 1),
                "b": (-1.55, -1), "c": (1.55, 1), "d": (1.55, -1)}
    star_pos = {"w": (0, 0), "a": (-1.25, 1), "b": (-1.25, -1),
                "c": (1.25, 1), "d": (1.25, -1)}
    star_edges = tuple(("w", leaf) for leaf in "abcd")
    axes[0].add_patch(Ellipse((0, 0), 1.8, 0.65, facecolor="#e8f1fa",
                             edgecolor="#2166ac", linestyle="--", linewidth=1.4))
    for ax, pos, edges in ((axes[0], tree_pos, TREE_EDGES), (axes[1], star_pos, star_edges)):
        for u, v in edges:
            ax.plot(*zip(pos[u], pos[v]), color="#2166ac" if (u, v) == ("u", "v") else "#34495e",
                    linewidth=3.3 if (u, v) == ("u", "v") else 2.2, zorder=1)
        for label, xy in pos.items():
            vertex(ax, label, xy, label in {"u", "v", "w"})
        ax.set(xlim=(-1.9, 1.9), ylim=(-1.3, 1.5), aspect="equal")
        ax.axis("off")
    axes[0].text(0, 0.72, "branch set {u, v}", ha="center", color="#2166ac", fontsize=12)
    axes[0].text(-0.62, -0.52, "degree 3", ha="center", fontsize=11)
    axes[0].text(0.62, -0.52, "degree 3", ha="center", fontsize=11)
    axes[1].text(0, -0.52, "degree 4", ha="center", fontsize=12, color="#2166ac")
    axes[0].set_title("Tree T: 6 vertices, 5 edges", fontsize=13, pad=12)
    axes[1].set_title(r"Contraction T/uv: star $K_{1,4}$", fontsize=13, pad=12)
    fig.suptitle("Contraction can combine the capacities of junctions", y=0.96,
                 fontsize=16, weight="bold")
    fig.add_artist(FancyArrowPatch((0.455, 0.52), (0.545, 0.52),
                                  transform=fig.transFigure, arrowstyle="-|>",
                                  mutation_scale=20, linewidth=1.7, color="#34495e"))
    fig.text(0.5, 0.34, "contract uv", ha="center", fontsize=12, color="#2166ac")
    fig.text(0.5, 0.17, r"$K_{1,4}$ is a minor of T, but not a topological minor.",
             ha="center", fontsize=14, weight="bold")
    fig.text(0.5, 0.085, "Four internally disjoint routes require four distinct edges leaving one centre.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.035, "Every vertex of T has degree at most three.", ha="center", fontsize=12)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
