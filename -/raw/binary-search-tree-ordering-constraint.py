"""Show why binary search tree bounds apply to all descendants.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; write the matching opaque white PNG to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
import numpy as np


INK = "#243746"
GREEN = "#177458"
RED = "#b43132"
BLUE = "#236b95"


def draw(ax, lower_key, valid):
    color = GREEN if valid else RED
    ax.set(xlim=(-2.3, 2.15), ylim=(-0.25, 4.95), aspect="equal")
    ax.axis("off")
    ax.text(0, 4.65, "Valid search tree" if valid else "Invalid search tree",
            fontsize=15, weight="bold", ha="center", color=color)
    ax.add_patch(FancyBboxPatch((-1.85, 0.9), 1.8, 2.3,
                                boxstyle="round,pad=0.1", facecolor="#edf5fa",
                                edgecolor=BLUE, linewidth=1.4, linestyle="--"))
    positions = {"root": (0, 3.85), "left": (-1.3, 2.75),
                 "right": (1.3, 2.75), "lower": (-0.4, 1.45)}
    labels = {"root": 4, "left": 2, "right": 6, "lower": lower_key}
    edges = [("root", "left", "L"), ("root", "right", "R"),
             ("left", "lower", "R")]
    radius = 0.25
    for parent, child, side in edges:
        start = np.asarray(positions[parent], dtype=float)
        end = np.asarray(positions[child], dtype=float)
        direction = (end - start) / np.linalg.norm(end - start)
        ax.add_patch(FancyArrowPatch(start + radius * direction,
                                    end - radius * direction,
                                    arrowstyle="-|>", mutation_scale=13,
                                    color=INK, linewidth=1.6))
        middle = (start + end) / 2
        ax.text(middle[0] + (0.15 if side == "R" else -0.15), middle[1],
                side, color=INK, ha="center", va="center", fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.4})
    for name, (x, y) in positions.items():
        focus = name == "lower"
        ax.add_patch(Circle((x, y), radius,
                            facecolor=("#e2f3eb" if valid else "#ffe7e7") if focus else "white",
                            edgecolor=color if focus else INK, linewidth=2 if focus else 1.5))
        ax.text(x, y, str(labels[name]), fontsize=14, weight="bold",
                color=INK, ha="center", va="center")
    ax.text(-1.02, 0.63, "Entire left subtree: keys < 4", color=BLUE, fontsize=10, ha="center")
    ax.text(0, 0.1, "2 < 3 < 4: both bounds hold" if valid else "2 < 5 holds, but 5 < 4 fails",
            color=color, fontsize=12, ha="center", weight="bold")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 5.8), dpi=110)
    fig.patch.set_facecolor("white")
    draw(axes[0], 3, True)
    draw(axes[1], 5, False)
    fig.suptitle("A child's key must respect every ancestor bound", fontsize=17, color=INK)
    fig.text(0.5, 0.035, "Both diagrams pass immediate parent-child comparisons. Only the left satisfies the full rule.",
             ha="center", color=INK, fontsize=10.5)
    fig.subplots_adjust(left=0.035, right=0.975, top=0.9, bottom=0.09, wspace=0.17)
    fig.savefig(Path.cwd() / "binary-search-tree-ordering-constraint.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
