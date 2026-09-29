"""Compare exact-match lookup in two seven-key binary search trees.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; write the matching opaque white PNG to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


INK = "#243746"
GRAY = "#acb7c0"
ORANGE = "#b65112"
GREEN = "#177458"
TARGET = 5
BALANCED = {4: (2, 6), 2: (1, 3), 6: (5, 7),
            1: (None, None), 3: (None, None),
            5: (None, None), 7: (None, None)}
CHAIN = {key: (None, key + 1 if key < 7 else None)
         for key in range(1, 8)}


def lookup(tree, root, target):
    path = []
    while root is not None:
        path.append(root)
        if target == root:
            return path
        root = tree[root][0 if target < root else 1]
    return path


def draw(ax, tree, positions, root, title, height):
    path = lookup(tree, root, TARGET)
    path_edges = set(zip(path, path[1:]))
    radius = 0.24
    ax.set(xlim=(-0.7, 5.1), ylim=(0, 6.15), aspect="equal")
    ax.axis("off")
    ax.text(2.2, 5.95, title, ha="center", fontsize=15, weight="bold", color=INK)
    ax.text(2.2, 5.57, f"7 keys  |  height = {height} edges", ha="center", color=INK)
    for parent, children in tree.items():
        for side, child in zip(("L", "R"), children):
            if child is None:
                continue
            start = np.asarray(positions[parent], dtype=float)
            end = np.asarray(positions[child], dtype=float)
            direction = (end - start) / np.linalg.norm(end - start)
            selected = (parent, child) in path_edges
            color = ORANGE if selected else GRAY
            ax.add_patch(FancyArrowPatch(start + radius * direction,
                                        end - radius * direction,
                                        arrowstyle="-|>", mutation_scale=12,
                                        linewidth=2.6 if selected else 1.4,
                                        color=color, zorder=1))
            middle = (start + end) / 2
            ax.text(middle[0] + (0.13 if side == "R" else -0.13), middle[1],
                    side, ha="center", va="center", fontsize=10, color=INK,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.4})
    for key, (x, y) in positions.items():
        color = GREEN if key == TARGET else ORANGE if key in path else GRAY
        face = "#e2f3eb" if key == TARGET else "#fff0e2" if key in path else "white"
        ax.add_patch(Circle((x, y), radius, facecolor=face, edgecolor=color,
                            linewidth=2.4 if key in path else 1.4, zorder=2))
        ax.text(x, y, str(key), ha="center", va="center", fontsize=14,
                weight="bold", color=INK, zorder=3)
    ax.text(2.2, 0.62, " → ".join(map(str, path)), ha="center", fontsize=14, color=ORANGE)
    ax.text(2.2, 0.18, f"{len(path)} visited keys / comparisons", ha="center", color=INK)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 5.9), dpi=110)
    fig.patch.set_facecolor("white")
    balanced_positions = {4: (2.2, 5.05), 2: (0.85, 3.65), 6: (3.55, 3.65),
                          1: (0.15, 2.25), 3: (1.55, 2.25),
                          5: (2.85, 2.25), 7: (4.25, 2.25)}
    chain_positions = {key: (0.3 + 0.62 * (key - 1), 5.05 - 0.6 * (key - 1))
                       for key in CHAIN}
    draw(axes[0], BALANCED, balanced_positions, 4, "Balanced shape", 2)
    draw(axes[1], CHAIN, chain_positions, 1, "Only right children", 6)
    fig.suptitle("Binary search tree lookup: target key 5", fontsize=17, color=INK)
    fig.text(0.5, 0.035, "Orange: search path     Green: match     L / R: child position",
             ha="center", color=INK, fontsize=11)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.9, bottom=0.095, wspace=0.09)
    fig.savefig(Path.cwd() / "binary-search-tree-search-path.png", facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
