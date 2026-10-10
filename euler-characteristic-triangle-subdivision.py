"""Draw a disk subdivision and its boundary; run from _media to save the PNG.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""
from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PolyCollection


def simplicial_counts(faces):
    """Count distinct nonempty faces, including all lower-dimensional faces."""
    cells = [set() for _ in range(max(map(len, faces)))]
    for face in faces:
        for size in range(1, len(face) + 1):
            cells[size - 1].update(combinations(sorted(face), size))
    return tuple(map(len, cells)), cells


def main():
    points = np.array([[0, 0], [2, 0], [1, np.sqrt(3)],
                       [1, 0], [1.5, np.sqrt(3) / 2],
                       [0.5, np.sqrt(3) / 2]])
    examples = [
        ("Filled triangle", [(0, 1, 2)], (3, 3, 1)),
        ("Midpoint subdivision", [(0, 3, 5), (3, 1, 4),
                                  (5, 4, 2), (3, 4, 5)], (6, 9, 4)),
        ("Boundary only", [(0, 1), (1, 2), (0, 2)], (3, 3)),
    ]
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.2))
    for ax, (title, faces, expected) in zip(axes, examples):
        counts, cells = simplicial_counts(faces)
        assert counts == expected
        if len(cells) == 3:
            ax.add_collection(PolyCollection([points[list(f)] for f in sorted(cells[2])],
                              facecolors=["#d8ebf6", "#c2dded", "#e6f2f8", "#accfde"],
                              edgecolors="none"))
        for edge in sorted(cells[1]):
            ax.plot(*points[list(edge)].T, color="#254b63", linewidth=2)
        vertices = [v[0] for v in sorted(cells[0])]
        ax.scatter(*points[vertices].T, s=50, color="#254b63", zorder=4)
        chi = sum((-1) ** i * c for i, c in enumerate(counts))
        v, e = counts[:2]
        f = counts[2] if len(counts) > 2 else 0
        ax.text(1, -0.37, f"V = {v}     E = {e}     F = {f}", ha="center")
        ax.text(1, -0.65, rf"$\chi={v}-{e}+{f}={chi}$", ha="center", fontsize=15)
        ax.set(title=title, xlim=(-0.2, 2.2), ylim=(-0.85, 2.05), aspect="equal")
        ax.axis("off")
    fig.suptitle("A finer mesh preserves the disk's Euler characteristic", fontsize=16)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.81, wspace=0.15)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
