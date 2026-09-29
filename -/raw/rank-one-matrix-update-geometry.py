"""Map a unit square under I + t u v^T; write matching PNG to CWD."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch
import numpy as np


def example_matrix(t):
    u = np.array([1.0, 2.0])
    v = np.array([3.0, -1.0])
    return np.eye(2) + t * np.outer(u, v)


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    square = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])
    fig, axes = plt.subplots(1, 3, figsize=(12, 5.5), dpi=100)
    for ax, t, area in zip(axes, [0, 1, -1], [1, 2, 0], strict=True):
        matrix = example_matrix(t)
        mapped = square @ matrix.T
        assert np.isclose(np.linalg.det(matrix), 1 + t)
        ax.add_patch(Polygon(square, closed=True, fill=False, edgecolor="#69747d",
                             linestyle="--", linewidth=1.3))
        if area:
            ax.add_patch(Polygon(mapped, closed=True, facecolor="#cee7dc",
                                 edgecolor="#23855b", alpha=0.85, linewidth=2))
        else:
            ax.plot([-2, 1], [-6, 3], color="#965aa8", linewidth=5, alpha=0.35)
        for index, color in [(0, "#246bce"), (1, "#bf5520")]:
            column = matrix[:, index]
            ax.add_patch(FancyArrowPatch([0, 0], column, arrowstyle="-|>",
                                        mutation_scale=18, linewidth=2.5,
                                        color=color, shrinkA=0, shrinkB=1))
            offset = np.array([0.05, 0.11]) if t == 0 else np.array([0.15, 0.2])
            label_point = column + offset
            ax.text(*label_point, rf"$B e_{index + 1}$", color=color, fontsize=13)
        all_points = np.vstack((square, mapped))
        minimum, maximum = all_points.min(axis=0), all_points.max(axis=0)
        span = np.maximum(maximum - minimum, 1)
        margin = 0.22 * span
        ax.set(xlim=(minimum[0] - margin[0], maximum[0] + margin[0]),
               ylim=(minimum[1] - margin[1], maximum[1] + margin[1]),
               aspect="equal", xlabel="First coordinate", ylabel="Second coordinate")
        ax.axhline(0, color="#69747d", linewidth=0.8)
        ax.axvline(0, color="#69747d", linewidth=0.8)
        ax.grid(alpha=0.16)
        ax.set_title(f"t = {t}: determinant = {1 + t}", weight="bold", fontsize=13)
        ax.text(0.5, -0.21,
                ["Unit square: area 1",
                 "Skew parallelogram: area 2",
                 "Collapsed line: area 0"][axes.tolist().index(ax)],
                transform=ax.transAxes, ha="center", va="top", fontsize=11)
    fig.suptitle("A rank-one correction changes area through one scalar: det B(t) = 1 + t",
                 fontsize=15, weight="bold", y=0.97)
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.22, top=0.81, wspace=0.40)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
