"""Original graph/forest drawings. Python 3.14 with repository NumPy/Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

POSITIONS = {1: (-1.8, 1), 2: (-.6, 1), 3: (.6, 1), 4: (1.8, 1), 5: (0, -.7)}
EDGES = {(1, 2): 9, (1, 5): 8, (2, 3): 4, (2, 5): 7,
         (3, 4): -1, (3, 5): 3, (4, 5): -2}
SELECTED = {(1, 2), (1, 5), (2, 3)}


def draw(ax, selected, title, weights):
    ax.set_facecolor("white")
    for edge in selected:
        a, b = (POSITIONS[v] for v in edge)
        ax.plot([a[0], b[0]], [a[1], b[1]], color="#2563a5", lw=2.4, zorder=1)
        if weights:
            x, y = ((a[i] + b[i]) / 2 for i in range(2))
            ax.text(x, y + .11, str(EDGES[edge]), ha="center", va="center", fontsize=11,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5}, zorder=3)
    for v, (x, y) in POSITIONS.items():
        ax.scatter([x], [y], s=490, facecolor="white", edgecolor="#333333", linewidth=1.5, zorder=4)
        ax.text(x, y, str(v), ha="center", va="center", fontsize=12, zorder=5)
    ax.set_title(title, fontsize=12)
    ax.set(xlim=(-2.15, 2.15), ylim=(-1.05, 1.55), aspect="equal")
    ax.axis("off")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.8), facecolor="white")
    draw(axes[0], EDGES, "All seven edges", False)
    draw(axes[1], SELECTED, "Maximum-weight forest: total 21", True)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "2011-graph-and-maximum-forest.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
