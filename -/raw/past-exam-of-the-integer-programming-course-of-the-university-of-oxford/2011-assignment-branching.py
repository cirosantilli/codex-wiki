"""Original directed assignment/tour drawings. Python 3.14 / repository plotting packages."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np

ANGLES = np.pi/2 - np.arange(5)*2*np.pi/5
POSITIONS = {i+1: (np.cos(a), np.sin(a)) for i, a in enumerate(ANGLES)}
COST = [[0, 1, 3, 3, 1], [1, 0, 3, 3, 1], [3, 3, 0, 2, 3],
        [3, 3, 2, 0, 3], [1, 1, 3, 3, 0]]


def draw(ax, arcs, title, curved=False):
    for i, j in arcs:
        a, b = np.array(POSITIONS[i]), np.array(POSITIONS[j])
        curve = .20 if curved and {i, j} == {3, 4} else 0
        color = "#a44b43" if curved and {i, j} == {3, 4} else "#2563a5"
        arrow = FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=14, lw=1.7,
                                color=color, shrinkA=14, shrinkB=14,
                                connectionstyle=f"arc3,rad={curve}")
        ax.add_patch(arrow)
        mid = (a+b)/2
        if curve:
            normal = np.array([b[1]-a[1], a[0]-b[0]])
            mid += .16*normal
        else:
            mid *= .84
        ax.text(*mid, str(COST[i-1][j-1]), ha="center", va="center", fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.0})
    for v, xy in POSITIONS.items():
        ax.scatter(*xy, s=420, facecolor="white", edgecolor="#333333", zorder=3)
        ax.text(*xy, str(v), ha="center", va="center", fontsize=11, zorder=4)
    ax.set_title(title, fontsize=11)
    ax.set(xlim=(-1.2, 1.2), ylim=(-1.2, 1.25), aspect="equal", facecolor="white")
    ax.axis("off")


def cycle(order):
    return list(zip(order, order[1:]+order[:1]))


def main():
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.8), facecolor="white")
    draw(axes[0], cycle([1, 2, 5])+cycle([3, 4]), "Root: assignment value 7", True)
    draw(axes[1], cycle([1, 2, 5, 4, 3]), r"Forbid $3\to4$: value 10")
    draw(axes[2], cycle([1, 3, 4, 5, 2]), r"Forbid $4\to3$: value 10")
    fig.tight_layout()
    fig.savefig(Path.cwd() / "2011-assignment-branching.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
