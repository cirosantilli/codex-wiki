"""Five points in four cells; tested with Python 3.14 and matplotlib 3.10.7.

Write geometric-pigeonhole-square.png in the current working directory.
"""

from collections import Counter
from math import dist, isclose, sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def cell(point):
    """Equality at either half-coordinate goes to the right/upper cell."""
    x, y = point
    return int(x >= 0.5), int(y >= 0.5)


def main():
    points = [(0.1, 0.1), (0.4, 0.4), (0.8, 0.2), (0.2, 0.8), (0.8, 0.8)]
    assert Counter(map(cell, points)) == {(0, 0): 2, (1, 0): 1,
                                        (0, 1): 1, (1, 1): 1}
    assert cell((0.5, 0.5)) == (1, 1)
    assert cell((0.5, 0.0)) == (1, 0)
    assert cell((0.0, 0.5)) == (0, 1)
    assert cell((1.0, 1.0)) == (1, 1)
    pair_distance = dist(points[0], points[1])
    assert isclose(pair_distance, sqrt(0.18), abs_tol=1e-14)
    assert pair_distance <= 1 / sqrt(2)
    fig = plt.figure(figsize=(9, 6.1), dpi=120, facecolor="white")
    ax = fig.add_axes((0.08, 0.19, 0.52, 0.68))
    orange, blue, ink = "#b34e16", "#196a96", "#283644"
    ax.add_patch(Rectangle((0, 0), 0.5, 0.5, facecolor="#fff0e3"))
    ax.add_patch(Rectangle((0, 0), 1, 1, facecolor="none",
                           edgecolor=ink, linewidth=1.8))
    ax.axvline(0.5, color="#758594", linestyle="--", linewidth=1.4)
    ax.axhline(0.5, color="#758594", linestyle="--", linewidth=1.4)
    ax.plot([0.1, 0.4], [0.1, 0.4], color=orange, linewidth=2.5, zorder=3)
    for i, (x, y) in enumerate(points):
        ax.scatter([x], [y], s=90, color=orange if i < 2 else blue,
                   edgecolor="white", linewidth=1, zorder=4)
        offsets = [(6, -21), (-75, 12), (-8, 9), (8, 9), (-8, 9)]
        ax.annotate(f"({x:.1f}, {y:.1f})", (x, y),
                    xytext=offsets[i], textcoords="offset points",
                    ha="right" if i in (2, 4) else "left",
                    fontsize=11, color=ink)
    ax.set_aspect("equal")
    ax.set_xlim(-0.03, 1.03)
    ax.set_ylim(-0.03, 1.03)
    ax.set_xticks([0, 0.5, 1], ["0", "1/2", "1"])
    ax.set_yticks([0, 0.5, 1], ["0", "1/2", "1"])
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("y", fontsize=12, rotation=0, labelpad=12)
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.suptitle("Five points, four cells: a nearby pair must exist",
                 fontsize=16, y=0.96, color=ink)
    fig.text(0.65, 0.79, "Every placement guarantees", fontsize=12, color=ink)
    fig.text(0.65, 0.70, r"$d\leq\sqrt{(1/2)^2+(1/2)^2}$", fontsize=14, color=ink)
    fig.text(0.65, 0.62, r"$=1/\sqrt{2}\approx0.707107$", fontsize=14, color=ink)
    fig.text(0.65, 0.47, "The orange pair here", fontsize=12, color=orange)
    fig.text(0.65, 0.38, r"$d=\sqrt{0.18}\approx0.424264$", fontsize=14, color=orange)
    fig.text(0.5, 0.065,
             "Boundary rule: x = 1/2 goes right; y = 1/2 goes up. Each point has exactly one cell.",
             ha="center", fontsize=11, color=ink)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Cell counts: (2, 1, 1, 1); pair distance {pair_distance:.12f}; "
          f"guaranteed bound {1 / sqrt(2):.12f}.")


if __name__ == "__main__":
    main()
