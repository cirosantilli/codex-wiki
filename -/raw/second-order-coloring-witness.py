"""Draw second-order-coloring-witness.png in the current working directory.

Tested with Python 3.14.4 and Matplotlib 3.10.7. Uses the repository's
Matplotlib dependency. Run from _media to regenerate the published figure.
"""

from itertools import combinations, permutations, product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Patch


PALETTE = ("#efac91", "#95c8ef", "#b9dc9b")
INK = "#243746"


def formula_holds(n, edges, masks):
    """Evaluate One and Different directly on three unary predicate bitsets."""
    one = all(sum(bool(mask & (1 << x)) for mask in masks) == 1
              for x in range(n))
    different = all(not any(mask & (1 << x) and mask & (1 << y)
                            for mask in masks) for x, y in edges)
    return one and different


def verify():
    # Independently compare predicate semantics with the usual color function
    # definition on every labeled simple graph with one to four vertices.
    complete_counts = {}
    graph_count = 0
    for n in range(1, 5):
        pairs = list(combinations(range(n), 2))
        for edge_bits in range(1 << len(pairs)):
            edges = [pair for i, pair in enumerate(pairs) if edge_bits & (1 << i)]
            predicates = {masks for masks in product(range(1 << n), repeat=3)
                          if formula_holds(n, edges, masks)}
            color_functions = set()
            for colors in product(range(3), repeat=n):
                if all(colors[x] != colors[y] for x, y in edges):
                    color_functions.add(tuple(sum(1 << x for x in range(n)
                                                  if colors[x] == c)
                                              for c in range(3)))
            assert predicates == color_functions
            graph_count += 1
            if len(edges) == len(pairs):
                complete_counts[n] = len(predicates)
    assert complete_counts == {1: 3, 2: 6, 3: 6, 4: 0}
    # Restricted-range example: neither singleton is available on two objects.
    assert not any(all(bool(mask & (1 << x)) == (x == 0) for x in range(2))
                   for mask in (0, 3))
    assert not any(formula_holds(3, list(combinations(range(3), 2)), masks)
                   for masks in product((0, 7), repeat=3))
    print(f"Verified predicate/color-function equivalence on {graph_count} graphs.")
    print(f"Fixed named-color witness counts for K1–K4: {complete_counts}.")
    print("Verified restricted unary ranges fail singleton and K3 witnesses.")


def draw_graph(ax, points, colors, rejected=False):
    for x, y in combinations(range(len(points)), 2):
        conflict = rejected and colors[x] == colors[y]
        ax.plot([points[x][0], points[y][0]], [points[x][1], points[y][1]],
                color="#b52b36" if conflict else "#7b8792",
                linewidth=3.5 if conflict else 1.7, zorder=1)
    for i, ((x, y), color) in enumerate(zip(points, colors)):
        ax.add_patch(Circle((x, y), 0.14, facecolor=PALETTE[color],
                            edgecolor=INK, linewidth=1.2, zorder=2))
        ax.text(x, y, chr(ord("a") + i), ha="center", va="center",
                fontsize=12, color=INK, zorder=3)
    ax.set(aspect="equal", xlim=(-0.22, 1.22), ylim=(-0.20, 1.16))
    ax.axis("off")


def main():
    verify()
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "text.color": INK})
    fig = plt.figure(figsize=(9.6, 5.2), facecolor="white")
    fig.suptitle("A coloring is a triple of unary relation witnesses", fontsize=17,
                 y=0.965)
    fig.legend(handles=[Patch(facecolor=color, edgecolor=INK,
                              label=f"C{i + 1}")
                        for i, color in enumerate(PALETTE)],
               loc="upper center", bbox_to_anchor=(0.5, 0.915), ncol=3,
               frameon=False, handlelength=1.2)
    fig.text(0.35, 0.81, r"$K_3$: all six witnesses", ha="center", fontsize=15)
    for index, colors in enumerate(permutations(range(3))):
        row, col = divmod(index, 3)
        left = 0.035 + col * 0.215
        bottom = 0.485 - row * 0.345
        ax = fig.add_axes((left, bottom, 0.195, 0.255))
        draw_graph(ax, [(0.5, 0.92), (0.04, 0.08), (0.96, 0.08)], colors)
        names = [chr(ord("a") + colors.index(c)) for c in range(3)]
        fig.text(left + 0.0975, bottom - 0.022,
                 "   ".join(f"C{c + 1}={{{name}}}" for c, name in enumerate(names)),
                 ha="center", va="top", fontsize=9)
    fig.add_artist(plt.Line2D((0.704, 0.704), (0.115, 0.825),
                             transform=fig.transFigure, color="#d2d8de"))
    fig.text(0.855, 0.81, r"$K_4$: no witness", ha="center", fontsize=15)
    ax = fig.add_axes((0.735, 0.41, 0.235, 0.34))
    draw_graph(ax, [(0.06, 0.94), (0.94, 0.94), (0.06, 0.06), (0.94, 0.06)],
               (0, 1, 2, 0), rejected=True)
    fig.text(0.855, 0.365, "One rejected proposal:\na and d both belong to C1",
             ha="center", va="top", fontsize=11)
    fig.text(0.855, 0.23, "Every proposal fails:\n4 vertices, 3 colors\nforce a shared color\non an adjacent pair.",
             ha="center", va="top", fontsize=11)
    fig.text(0.5, 0.045, "Vertex labels and color names are fixed; every vertex belongs to exactly one Ci.",
             ha="center", fontsize=10)
    fig.savefig(Path("second-order-coloring-witness.png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
