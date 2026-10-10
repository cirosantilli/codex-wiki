"""Draw an original bridge obstruction and a strongly oriented four-cycle.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg; save the matching basename PNG to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


BRIDGE_POSITIONS = {"A": (-1.2, -0.65), "B": (-1.2, 0.65),
                    "C": (0.0, 0.0), "D": (1.5, 0.0)}
BRIDGE_EDGES = (("A", "B"), ("B", "C"), ("C", "A"), ("C", "D"))
CYCLE_POSITIONS = {"A": (-0.8, 0.65), "B": (0.8, 0.65),
                   "C": (0.8, -0.65), "D": (-0.8, -0.65)}
CYCLE_EDGES = (("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"))


def draw(ax, positions, edges):
    for u, v in edges:
        bridge = (u, v) == ("C", "D") and positions is BRIDGE_POSITIONS
        ax.add_patch(FancyArrowPatch(positions[u], positions[v],
                                    arrowstyle="-|>", mutation_scale=22,
                                    shrinkA=14, shrinkB=14, linewidth=3 if bridge else 2.5,
                                    color="#b14c2a" if bridge else "#226c9c", zorder=1))
    for label, xy in positions.items():
        ax.add_patch(Circle(xy, 0.14, facecolor="white", edgecolor="#263746",
                            linewidth=2, zorder=2))
        ax.text(*xy, label, ha="center", va="center", fontsize=14,
                weight="bold", zorder=3)
    ax.set(xlim=(-1.6, 1.9), ylim=(-1.1, 1.1), aspect="equal")
    ax.axis("off")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.4), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.975, top=0.76, bottom=0.27, wspace=0.12)
    draw(axes[0], BRIDGE_POSITIONS, BRIDGE_EDGES)
    draw(axes[1], CYCLE_POSITIONS, CYCLE_EDGES)
    axes[0].set_title("Triangle with a bridge CD", fontsize=15, pad=15)
    axes[1].set_title("Bridgeless four-cycle", fontsize=15, pad=15)
    axes[0].text(0.75, 0.35, "bridge", color="#b14c2a", ha="center", fontsize=13)
    axes[0].plot([0.75, 0.75], [-0.9, 0.9], linestyle="--", linewidth=1.3,
                 color="#9d9d9d", zorder=0)
    fig.suptitle("A one-way bridge blocks a return journey", y=0.96,
                 fontsize=17, weight="bold")
    fig.text(0.26, 0.19, "C → D: D cannot leave\nReverse CD: D cannot be reached", ha="center",
             fontsize=13, color="#b14c2a", linespacing=1.5)
    fig.text(0.75, 0.19, "A → B → C → D → A\nAll ordered pairs are reachable", ha="center",
             fontsize=13, color="#226c9c", linespacing=1.5)
    fig.text(0.5, 0.045, "Both graphs are connected; only the right graph admits a strong orientation.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
