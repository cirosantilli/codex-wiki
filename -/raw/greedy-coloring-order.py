"""Draw greedy-coloring-order.png in cwd; tested with Python 3.14.4.

Uses Matplotlib and verifies every vertex order of P4 with standard-library enumeration.
"""

from collections import Counter
from itertools import permutations, product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


EDGES = ((1, 2), (2, 3), (3, 4))
PALETTE = {1: "#9ed8f0", 2: "#ffd38a", 3: "#cebbeb"}
ORDERS = ((1, 2, 3, 4), (1, 4, 2, 3))


def greedy(order):
    colors = {}
    for vertex in order:
        neighbors = {v if u == vertex else u for u, v in EDGES if vertex in (u, v)}
        forbidden = {colors[v] for v in neighbors if v in colors}
        color = 1
        while color in forbidden:
            color += 1
        colors[vertex] = color
    return colors


def check_examples():
    assert greedy(ORDERS[0]) == {1: 1, 2: 2, 3: 1, 4: 2}
    assert greedy(ORDERS[1]) == {1: 1, 4: 1, 2: 2, 3: 3}
    counts = Counter()
    for order in permutations(range(1, 5)):
        colors = greedy(order)
        assert all(colors[u] != colors[v] for u, v in EDGES)
        assert max(colors.values()) <= 3
        counts[max(colors.values())] += 1
    assert sum(counts.values()) == 24
    degrees = [sum(v in edge for edge in EDGES) for v in range(1, 5)]
    assert degrees == [1, 2, 2, 1]
    colorings = [sum(all(colors[u - 1] != colors[v - 1] for u, v in EDGES)
                     for colors in product(range(k), repeat=4)) for k in (1, 2)]
    assert colorings == [0, 2]
    print(f"Verified both assignments and all 24 P4 orders: {dict(sorted(counts.items()))}.")
    print("Verified P4 has chromatic number 2, maximum degree 2, and greedy bound 3.")


def main():
    check_examples()
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(2, 1, figsize=(8.4, 5.0), facecolor="white")
    fig.suptitle("Same path, different greedy orders", fontsize=19, y=0.97)
    for ax, order in zip(axes, ORDERS):
        colors = greedy(order)
        steps = {v: i + 1 for i, v in enumerate(order)}
        ax.plot([1, 4], [0, 0], color="#46515c", linewidth=3, zorder=1)
        for vertex in range(1, 5):
            ax.add_patch(Circle((vertex, 0), 0.17, facecolor=PALETTE[colors[vertex]],
                                edgecolor="#24313d", linewidth=1.5, zorder=2))
            ax.text(vertex, 0, str(colors[vertex]), ha="center", va="center", fontsize=14)
            ax.text(vertex, 0.33, f"vertex {vertex}", ha="center", va="center", fontsize=11)
            ax.text(vertex, -0.34, f"step {steps[vertex]}", ha="center", va="center", fontsize=11)
        ax.set_title("Order " + " → ".join(map(str, order))
                     + f"     |     {max(colors.values())} colours", fontsize=14, pad=7)
        ax.text(2.5, -0.72, "Assignments in processing order: "
                + ", ".join(f"c({v})={colors[v]}" for v in order),
                ha="center", va="center", fontsize=11)
        ax.set(xlim=(0.5, 4.5), ylim=(-0.9, 0.58), aspect="equal", facecolor="white")
        ax.axis("off")
    fig.text(0.5, 0.035, "Number inside each dot: assigned colour    •    Edges: 1–2, 2–3, 3–4",
             ha="center", fontsize=11, color="#46515c")
    fig.subplots_adjust(left=0.035, right=0.965, bottom=0.1, top=0.81, hspace=0.68)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
