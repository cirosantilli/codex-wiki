"""Draw a fictitious symmetric TSP instance and all three undirected tours.

Tested with Python 3.14, matplotlib 3.10.7; run from _media.
Costs are arbitrary units, independent of the drawing's geometry.
"""

from itertools import permutations
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def main():
    weights = {"AB": 2, "BC": 3, "CD": 4, "AD": 5, "AC": 6, "BD": 7}
    positions = dict(A=(0, 1), B=(1, 1), C=(1, 0), D=(0, 0))
    tours = []
    for p in permutations("BCD"):
        if p > p[::-1]:
            continue
        route = ("A",) + p + ("A",)
        costs = [weights["".join(sorted((u, v)))] for u, v in zip(route, route[1:])]
        tours.append((route, costs, sum(costs)))
    tours.sort(key=lambda t: t[2])
    assert [t[2] for t in tours] == [14, 19, 21]
    optimum = {"".join(sorted((u, v))) for u, v in zip(tours[0][0], tours[0][0][1:])}
    fig, (graph, table) = plt.subplots(1, 2, figsize=(9.6, 4.5), facecolor="white",
                                      gridspec_kw={"width_ratios": [1, 1.3]})
    fig.subplots_adjust(left=0.045, right=0.975, top=0.78, bottom=0.18, wspace=0.15)
    fig.suptitle("A toy weighted Hamilton tour", fontsize=18, y=0.96)
    for key, cost in weights.items():
        u, v = key
        p, q = positions[u], positions[v]
        color = "#1764a0" if key in optimum else "#a2a9b0"
        graph.plot([p[0], q[0]], [p[1], q[1]], color=color,
                   lw=3 if key in optimum else 1.8, zorder=1)
        x, y = ((a + b) / 2 for a, b in zip(p, q))
        if key == "AC":
            x, y = 0.34, 0.66
        elif key == "BD":
            x, y = 0.66, 0.66
        graph.text(x, y, str(cost), ha="center", va="center", fontsize=13,
                   color="#263746", bbox=dict(facecolor="white", edgecolor="none", pad=3),
                   zorder=3)
    for name, (x, y) in positions.items():
        graph.add_patch(Circle((x, y), 0.055, facecolor="white", edgecolor="#263746",
                               lw=1.5, zorder=4))
        graph.text(x, y, name, ha="center", va="center", fontsize=12, zorder=5)
    graph.set(xlim=(-0.2, 1.2), ylim=(-0.25, 1.25), aspect="equal")
    graph.axis("off")
    graph.set_title("All six symmetric edge costs", fontsize=13, pad=12)
    graph.text(0.5, -0.20, "Blue: the cheapest tour (cost 14)", ha="center", fontsize=11,
               color="#1764a0")
    table.axis("off")
    table.set_title("Fix A; identify each tour with its reverse", fontsize=12, pad=12)
    for i, (route, costs, total) in enumerate(tours):
        y = 0.86 - 0.30 * i
        color = "#1764a0" if i == 0 else "#263746"
        table.text(0.02, y, " → ".join(route), fontsize=14, color=color)
        table.text(0.02, y - 0.115, " + ".join(map(str, costs)) + f" = {total}",
                   fontsize=13, color=color)
    fig.text(0.5, 0.065, "Fictitious costs in arbitrary units; drawn lengths are not costs.",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
