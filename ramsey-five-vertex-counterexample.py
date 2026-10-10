"""Draw the sharp five-vertex Ramsey example.

Tested with Python 3.14.4 and matplotlib 3.10.7. Write the matching PNG to CWD.
"""

from itertools import combinations
from math import cos, pi, sin
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def main():
    red, blue, ink = "#b82b35", "#1261a0", "#263238"
    points = {i: (cos(pi / 2 - 2 * pi * (i - 1) / 5),
                  sin(pi / 2 - 2 * pi * (i - 1) / 5)) for i in range(1, 6)}
    pairs = list(combinations(points, 2))
    perimeter = {(1, 2), (2, 3), (3, 4), (4, 5), (1, 5)}
    colors = {pair: red if pair in perimeter else blue for pair in pairs}
    assert len(pairs) == 10
    assert sum(color == red for color in colors.values()) == 5
    for triple in combinations(points, 3):
        assert len({colors[pair] for pair in combinations(triple, 2)}) == 2

    fig, ax = plt.subplots(figsize=(6.6, 6.2), dpi=120, facecolor="white")
    for i, j in pairs:
        x, y = zip(points[i], points[j])
        ax.plot(x, y, color=colors[i, j], linewidth=2.8,
                linestyle="-" if (i, j) in perimeter else "--", zorder=1)
    for i, (x, y) in points.items():
        ax.scatter([x], [y], s=490, color="white", edgecolor=ink,
                   linewidth=1.6, zorder=3)
        ax.text(x, y, str(i), ha="center", va="center", fontsize=13,
                color=ink, zorder=4)
    ax.set(xlim=(-1.2, 1.2), ylim=(-1.05, 1.2), aspect="equal")
    ax.axis("off")
    ax.legend(handles=[Line2D([0], [0], color=red, lw=2.8,
                              label="Red: five perimeter edges"),
                       Line2D([0], [0], color=blue, lw=2.8, ls="--",
                              label="Blue: five diagonal edges")],
              loc="lower center", bbox_to_anchor=(0.5, -0.19),
              frameon=False, fontsize=11)
    fig.suptitle(r"$K_5$: no monochromatic triangle", fontsize=18, y=0.96,
                 color=ink)
    fig.text(0.5, 0.875, "Complete graph: all 10 pairs are edges",
             ha="center", fontsize=12, color=ink)
    fig.text(0.5, 0.035,
             "Colors belong to edges. Crossings are not vertices.\n"
             "Each color forms a five-cycle; every triple has both colors.",
             ha="center", fontsize=11, color=ink, linespacing=1.5)
    fig.subplots_adjust(left=0.06, right=0.94, bottom=0.22, top=0.84)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("K5 diagram checked: 10 edges, 5 per color, 10 nonmonochromatic triples.")


if __name__ == "__main__":
    main()
