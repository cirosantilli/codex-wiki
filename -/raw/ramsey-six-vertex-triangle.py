"""Draw the two cases of the six-vertex monochromatic triangle argument.

Tested with Python 3.14.4 and matplotlib 3.10.7. Write the matching PNG to CWD.
"""

from itertools import combinations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def draw_case(ax, red_neighbor_edge):
    red, blue, ink = "#b82b35", "#1261a0", "#263238"
    points = {"v": (0, 1.28), "a": (-1.05, 0.12), "b": (0, -0.40),
              "c": (1.05, 0.12), "d": (-0.77, -1.18), "e": (0.77, -1.18)}
    pairs = list(combinations(points, 2))
    spoke = {frozenset(("v", u)) for u in "abc"}
    triangle = ("v", "a", "b") if red_neighbor_edge else ("a", "b", "c")
    triangle_edges = {frozenset(p) for p in combinations(triangle, 2)}
    colors = {}
    for i, (u, w) in enumerate(pairs):
        pair = frozenset((u, w))
        if pair in spoke or (red_neighbor_edge and pair == frozenset(("a", "b"))):
            colors[pair] = red
        elif u in "abc" and w in "abc":
            colors[pair] = blue
        else:
            colors[pair] = red if i % 2 else blue
    assert len(colors) == 15
    assert all(colors[p] == red for p in spoke)
    assert len({colors[p] for p in triangle_edges}) == 1
    # Draw all remaining pairs faintly; then the three chosen spokes and witness.
    for layer in (0, 1, 2):
        for u, w in pairs:
            pair = frozenset((u, w))
            importance = 2 if pair in triangle_edges else 1 if pair in spoke else 0
            if importance != layer:
                continue
            x, y = zip(points[u], points[w])
            ax.plot(x, y, color=colors[pair], alpha=(0.28, 0.82, 1)[layer],
                    linewidth=(1.7, 2.7, 4.5)[layer],
                    linestyle="-" if colors[pair] == red else "--", zorder=layer)
    for label, (x, y) in points.items():
        ax.scatter([x], [y], s=460, color="white", edgecolor=ink,
                   linewidth=1.5, zorder=4)
        ax.text(x, y, label, ha="center", va="center", fontsize=13,
                color=ink, zorder=5)
    ax.set(xlim=(-1.30, 1.30), ylim=(-1.42, 1.52), aspect="equal")
    ax.axis("off")
    ax.set_title("Case 1: ab is red" if red_neighbor_edge
                 else "Case 2: ab, ac, bc are blue", fontsize=13, pad=12,
                 color=ink)
    ax.text(0.5, -0.06, "Red triangle: v, a, b" if red_neighbor_edge
            else "Blue triangle: a, b, c", transform=ax.transAxes,
            ha="center", fontsize=12, color=red if red_neighbor_edge else blue)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 6.6), dpi=120,
                             facecolor="white")
    draw_case(axes[0], True)
    draw_case(axes[1], False)
    fig.suptitle(r"$K_6$: a monochromatic triangle is unavoidable", fontsize=18,
                 y=0.97, color="#263238")
    fig.text(0.5, 0.85,
             "Of the five edges at v, at least three share a color.\n"
             "Call that color red and choose neighbors a, b, c.",
             ha="center", fontsize=12, color="#263238", linespacing=1.45)
    fig.legend(handles=[Line2D([0], [0], color="#b82b35", lw=2.8,
                               label="Red edge"),
                        Line2D([0], [0], color="#1261a0", lw=2.8, ls="--",
                               label="Blue edge")],
               loc="lower center", bbox_to_anchor=(0.5, 0.08), ncol=2,
               frameon=False, fontsize=11)
    fig.text(0.5, 0.035,
             "Each panel is a complete graph: all 15 pairs are edges.\n"
             "Faint edges are example choices; bold edges mark the triangle. Vertices have no colors.",
             ha="center", fontsize=10.5, color="#263238", linespacing=1.4)
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.23, top=0.74,
                        wspace=0.18)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("K6 diagrams checked: all 15 edges in each panel; red vab / blue abc witnesses.")


if __name__ == "__main__":
    main()
