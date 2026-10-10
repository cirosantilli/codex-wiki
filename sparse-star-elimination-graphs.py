"""Original four-leaf-star elimination diagrams; emit PNG in the working directory.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle


BLUE = "#23649a"
ORANGE = "#c34e18"
POS = {"c": (0, 0), "1": (-1, 1), "2": (1, 1),
       "3": (-1, -1), "4": (1, -1)}
LEAVES = ["1", "2", "3", "4"]
STAR = [("c", leaf) for leaf in LEAVES]
FILL = [(u, v) for i, u in enumerate(LEAVES) for v in LEAVES[i + 1:]]


def panel(ax, active, edges, fills=(), removed=()):
    for u, v in edges:
        ax.plot([POS[u][0], POS[v][0]], [POS[u][1], POS[v][1]],
                color=BLUE, lw=2.5, zorder=1)
    for u, v in fills:
        ax.plot([POS[u][0], POS[v][0]], [POS[u][1], POS[v][1]],
                color=ORANGE, lw=2.5, ls="--", zorder=1)
    for vertex in active:
        ax.add_patch(Circle(POS[vertex], 0.18, fc="white", ec=BLUE,
                            lw=2, zorder=2))
        ax.text(*POS[vertex], vertex, ha="center", va="center",
                fontsize=13, fontweight="bold", zorder=3)
    for vertex in removed:
        ax.text(*POS[vertex], "×", ha="center", va="center",
                fontsize=22, color="#777777")
    ax.set(xlim=(-1.4, 1.4), ylim=(-1.45, 1.45), aspect="equal")
    ax.axis("off")


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(2, 3, figsize=(10.2, 6.4))
    fig.subplots_adjust(left=0.035, right=0.98, top=0.82, bottom=0.13,
                        wspace=0.13, hspace=0.38)
    fig.suptitle("Elimination creates couplings between remaining neighbors",
                 fontsize=17, y=0.97)
    fig.text(0.5, 0.9, "Original example: A = I + graph Laplacian of the four-leaf star",
             ha="center", fontsize=12)
    panel(axes[0, 0], ["c"] + LEAVES, STAR)
    panel(axes[0, 1], LEAVES, [], FILL, removed=["c"])
    panel(axes[0, 2], LEAVES[1:], [], [("2", "3"), ("2", "4"), ("3", "4")],
          removed=["c", "1"])
    panel(axes[1, 0], ["c"] + LEAVES, STAR)
    panel(axes[1, 1], ["c", "2", "3", "4"], STAR[1:], removed=["1"])
    panel(axes[1, 2], ["c"], [], removed=LEAVES)
    titles = [["Center first: start", "Remove c: six fill edges", "Remove 1: clique remains"],
              ["Leaves first: start", "Remove 1: no fill", "Remove all leaves: no fill"]]
    captions = [["Center diagonal: 5", "Leaf diagonals: 9/5; couplings: −1/5",
                 "Leaf diagonals: 16/9; couplings: −2/9"],
                ["Each leaf diagonal: 2", "Center diagonal: 5 − 1/2 = 9/2",
                 "Center diagonal: 5 − 4/2 = 3"]]
    for row in range(2):
        for col in range(3):
            axes[row, col].set_title(titles[row][col], fontsize=12, pad=5)
            axes[row, col].text(0.5, -0.04, captions[row][col],
                                transform=axes[row, col].transAxes,
                                ha="center", fontsize=9.5)
    fig.legend(handles=[Line2D([0], [0], color=BLUE, lw=2.5, label="Original coupling"),
                        Line2D([0], [0], color=ORANGE, lw=2.5, ls="--", label="Fill coupling"),
                        Line2D([0], [0], marker="x", color="#777777", ls="", label="Eliminated vertex")],
               loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 0.005))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
