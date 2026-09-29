"""Draw graph-coloring-cycle-examples.png in cwd; tested with Python 3.14.4.

Uses the repository's Matplotlib dependency; verifies small colorings by enumeration.
"""

from itertools import combinations, product
from math import cos, pi, sin
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


PALETTE = {1: "#9ed8f0", 2: "#ffd38a", 3: "#cebbeb"}
EXAMPLES = [(3, (1, 2, 3)), (4, (1, 2, 1, 2)), (5, (1, 2, 1, 2, 3))]


def cycle_edges(n):
    return [(i, (i + 1) % n) for i in range(n)]


def proper(colors, edges):
    return all(colors[u] != colors[v] for u, v in edges)


def coloring_count(n, edges, k):
    return sum(proper(colors, edges) for colors in product(range(1, k + 1), repeat=n))


def check_examples():
    counts = {}
    for n, colors in EXAMPLES:
        assert proper(colors, cycle_edges(n))
        counts[n] = [coloring_count(n, cycle_edges(n), k) for k in range(1, 4)]
    assert counts == {3: [0, 0, 6], 4: [0, 2, 18], 5: [0, 0, 30]}
    for n in range(3, 9):
        k = 2 if n % 2 == 0 else 3
        assert coloring_count(n, cycle_edges(n), k) > 0
        assert coloring_count(n, cycle_edges(n), k - 1) == 0
    for n in range(1, 6):
        edges = list(combinations(range(n), 2))
        assert coloring_count(n, edges, n) > 0
        assert coloring_count(n, edges, n - 1) == 0
    edges = {frozenset(edge) for edge in cycle_edges(5)}
    assert not any(all(frozenset(pair) in edges for pair in combinations(triple, 2))
                   for triple in combinations(range(5), 3))
    print(f"Verified C3/C4/C5 labeled-coloring counts for k=1,2,3: {counts}.")
    print("Verified chromatic numbers for C3–C8, K1–K5, and triangle-freeness of C5.")


def main():
    check_examples()
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 4.0), facecolor="white")
    fig.suptitle("An odd cycle needs a third colour", fontsize=19, y=0.97)
    for ax, (n, colors) in zip(axes, EXAMPLES):
        points = [(cos(pi / 2 - 2 * pi * i / n), sin(pi / 2 - 2 * pi * i / n))
                  for i in range(n)]
        for u, v in cycle_edges(n):
            ax.plot([points[u][0], points[v][0]], [points[u][1], points[v][1]],
                    color="#46515c", linewidth=2.5, zorder=1)
        for i, ((x, y), color) in enumerate(zip(points, colors)):
            ax.add_patch(Circle((x, y), 0.18, facecolor=PALETTE[color],
                                edgecolor="#24313d", linewidth=1.5, zorder=2))
            ax.text(x, y, str(color), ha="center", va="center", fontsize=14, zorder=3)
            ax.text(1.34 * x, 1.34 * y, f"v{i + 1}", ha="center", va="center", fontsize=11)
        ax.set_title(rf"$C_{n}$: $\chi = {max(colors)}$", fontsize=16, pad=9)
        ax.text(0, -1.62, {3: "Every pair is adjacent", 4: "Two colours alternate",
                           5: "No triangle; still three colours"}[n],
                ha="center", va="center", fontsize=11)
        ax.set(xlim=(-1.6, 1.6), ylim=(-1.78, 1.6), aspect="equal", facecolor="white")
        ax.axis("off")
    fig.text(0.5, 0.035, "Inside each dot: colour number     Outside: vertex label",
             ha="center", fontsize=11, color="#46515c")
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.11, top=0.78, wspace=0.13)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
