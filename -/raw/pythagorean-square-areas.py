"""Draw the exact square areas on a 3-4-5 right triangle; output in cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def polygon_area(vertices):
    x, y = vertices.T
    return abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1))) / 2


def main():
    triangle = np.array([[0, 0], [4, 0], [0, 3]])
    squares = [
        (np.array([[0, 0], [0, 3], [-3, 3], [-3, 0]]), 9,
         "#e5eefb", "#245b9b", (-1.5, 1.5), "3² = 9"),
        (np.array([[0, 0], [4, 0], [4, -4], [0, -4]]), 16,
         "#fff0d5", "#9b650c", (2, -2.2), "4² = 16"),
        (np.array([[4, 0], [0, 3], [3, 7], [7, 4]]), 25,
         "#e1f2e9", "#287551", (3.5, 3.5), "5² = 25"),
    ]
    assert np.dot(triangle[1] - triangle[0], triangle[2] - triangle[0]) == 0
    assert polygon_area(triangle) == 6
    assert sorted(np.linalg.norm(np.roll(triangle, -1, axis=0) - triangle,
                                 axis=1)) == [3, 4, 5]
    for vertices, area, *_ in squares:
        edges = np.roll(vertices, -1, axis=0) - vertices
        assert polygon_area(vertices) == area
        assert np.all(np.sum(edges * edges, axis=1) == area)
        assert np.all(np.sum(edges * np.roll(edges, -1, axis=0), axis=1) == 0)

    plt.rcParams.update({"font.size": 13, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(6.8, 7.0), facecolor="white")
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.08, top=0.88)
    ax.set_facecolor("white")
    ax.set_aspect("equal")
    for vertices, _, face, edge, center, label in squares:
        ax.add_patch(Polygon(vertices, facecolor=face, edgecolor=edge, linewidth=2))
        ax.text(*center, label, color=edge, ha="center", va="center",
                fontsize=18, fontweight="bold")
    ax.add_patch(Polygon(triangle, facecolor="#f5f5f5", edgecolor="#333333",
                         linewidth=2.2))
    ax.plot([0.35, 0.35, 0], [0, 0.35, 0.35], color="#333333", linewidth=1.5)
    ax.text(0.47, 0.29, "90°", fontsize=10)
    ax.text(1.25, 0.93, "Triangle\narea = 6", ha="center", va="center", fontsize=11)
    ax.text(-0.22, 1.7, "3", ha="right", color="#245b9b", fontsize=16,
            bbox={"facecolor": "#e5eefb", "edgecolor": "none", "pad": 1})
    ax.text(2.5, -0.18, "4", ha="center", va="top", color="#9b650c", fontsize=16)
    ax.text(2.25, 1.85, "5", ha="center", color="#287551", fontsize=16,
            bbox={"facecolor": "#e1f2e9", "edgecolor": "none", "pad": 1})
    ax.set_xlim(-3.55, 7.55)
    ax.set_ylim(-4.45, 7.45)
    ax.axis("off")
    fig.suptitle("Pythagorean theorem: square areas", fontsize=19, y=0.97)
    fig.text(0.5, 0.92, "The marked right angle is an assumption, not a guess.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.035, "Lengths: 3, 4, 5     •     Square areas: 9 + 16 = 25",
             ha="center", fontsize=13)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=140, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Saved {output.name}; right angle, side lengths and areas checked.")


if __name__ == "__main__":
    main()
