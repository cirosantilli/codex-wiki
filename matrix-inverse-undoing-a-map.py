"""Illustrate an inverse restoring a grid and a singular map losing information.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
Save an opaque white PNG with this script's basename in the working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def main():
    a = np.array([[2, 1], [1, 1]])
    inverse = np.array([[1, -1], [-1, 2]])
    singular = np.array([[1, 1], [0, 0]])
    v = np.array([1, 2])
    assert np.array_equal(a @ inverse, np.eye(2))
    assert np.array_equal(inverse @ a, np.eye(2))
    assert np.array_equal(a @ v, [4, 3])
    assert np.array_equal(inverse @ a @ v, v)
    assert np.array_equal(singular @ np.array([1, 0]), [1, 0])
    assert np.array_equal(singular @ np.array([0, 1]), [1, 0])

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(10.2, 6.5), facecolor="white")
    fig.subplots_adjust(left=0.055, right=0.98, bottom=0.33, top=0.78, wspace=0.31)
    corners = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
    basis_colors = ["#087c74", "#bd651c"]
    maps = [np.eye(2), a, inverse @ a]
    titles = ["Original grid", "Apply A", "Apply A⁻¹ to the middle panel"]
    vectors = ["v = (1, 2)", "Av = (4, 3)", "A⁻¹Av = (1, 2)"]
    for ax, matrix, heading, label in zip(axes, maps, titles, vectors):
        ax.set_aspect("equal")
        ax.set_xlim(-0.35, 4.8)
        ax.set_ylim(-0.35, 3.65)
        ax.set_xticks(range(5))
        ax.set_yticks(range(4))
        ax.tick_params(labelsize=9, length=0)
        ax.spines[["top", "right"]].set_visible(False)
        ax.axhline(0, color="#aaaaaa", lw=0.8)
        ax.axvline(0, color="#aaaaaa", lw=0.8)
        # Transform a finite input grid, using exactly the same sample lines.
        for value in np.arange(0, 1.51, 0.25):
            for line in [np.array([[value, 0], [value, 1.5]]),
                         np.array([[0, value], [1.5, value]])]:
                mapped = line @ matrix.T
                ax.plot(*mapped.T, color="#a9b5be", lw=0.65, zorder=1)
        square = corners @ matrix.T
        ax.fill(*square.T, color="#d5ece6", zorder=2)
        ax.plot(*square.T, color="#608b7d", lw=1.6, zorder=3)
        for endpoint, color in zip(matrix.T, basis_colors):
            ax.annotate("", endpoint, (0, 0), arrowprops={"arrowstyle": "->",
                        "color": color, "lw": 2.6, "shrinkA": 0, "shrinkB": 0}, zorder=5)
        endpoint = matrix @ v
        ax.annotate("", endpoint, (0, 0), arrowprops={"arrowstyle": "->",
                    "color": "#375fb0", "lw": 2.4, "shrinkA": 0, "shrinkB": 0}, zorder=6)
        ax.plot(*endpoint, "o", color="#375fb0", ms=5, zorder=7)
        ax.text(0.5, -0.16, label, transform=ax.transAxes, ha="center", color="#375fb0")
        ax.set_title(heading, fontsize=12, pad=12)

    for left, right, text in [(0.329, 0.365, "A"), (0.651, 0.687, "A⁻¹")]:
        fig.add_artist(FancyArrowPatch((left, 0.57), (right, 0.57),
                       transform=fig.transFigure, arrowstyle="->", mutation_scale=15,
                       lw=1.6, color="#333333"))
        fig.text((left + right) / 2, 0.595, text, ha="center", fontsize=11)

    fig.suptitle("An inverse undoes the entire map", fontsize=18, y=0.97)
    fig.text(0.5, 0.905, "A = [2  1; 1  1]      A⁻¹ = [1  −1; −1  2]      det A = 1",
             ha="center", fontsize=12)
    fig.text(0.5, 0.855, "Shaded = unit square and its images   •   Colored arrows = basis vectors   •   Same axis scale",
             ha="center", fontsize=10.5)

    # A collision diagram shows why no output-only reconstruction is possible.
    collision = fig.add_axes([0.065, 0.065, 0.89, 0.18])
    collision.set_xlim(0, 1)
    collision.set_ylim(0, 1)
    collision.axis("off")
    collision.text(0, 0.94, "Singular S = [1  1; 0  0]", fontsize=12, weight="bold")
    collision.text(0.32, 0.68, "(1, 0)", ha="center", color=basis_colors[0], fontsize=12)
    collision.text(0.32, 0.18, "(0, 1)", ha="center", color=basis_colors[1], fontsize=12)
    for start_y, color in zip([0.73, 0.23], basis_colors):
        collision.annotate("", (0.58, 0.49), (0.365, start_y),
                           arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
    collision.text(0.61, 0.45, "(1, 0)", ha="center", fontsize=12)
    collision.text(0.77, 0.45, "One output\nTwo possible inputs", ha="left", va="center")
    fig.text(0.5, 0.025, "Information lost by a singular map cannot be recovered from the output alone.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
