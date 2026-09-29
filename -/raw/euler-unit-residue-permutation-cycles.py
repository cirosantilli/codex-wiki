"""Generate original unit permutations; run from _media with Python 3.14.

Uses the repository's matplotlib 3.10.7 dependency. Writes its own basename
as an opaque PNG in the current working directory.
"""

from math import cos, gcd, pi, sin
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def unit_cycles(multiplier, modulus):
    remaining = {u for u in range(modulus) if gcd(u, modulus) == 1}
    cycles = []
    while remaining:
        start = min(remaining)
        cycle = []
        u = start
        while u in remaining:
            cycle.append(u)
            remaining.remove(u)
            u = multiplier * u % modulus
        assert u == start
        cycles.append(cycle)
    return cycles


def main():
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.8), dpi=80)
    fig.patch.set_facecolor("white")
    fig.suptitle("Multiplication by a unit rearranges every unit", fontsize=18, y=0.95)
    for ax, (a, n, color) in zip(axes, [(5, 12, "#176b8c"), (7, 15, "#8350a2")]):
        cycles = unit_cycles(a, n)
        assert len(cycles) == 2
        for cx, cycle in zip([-1.45, 1.45], cycles):
            points = [(cx + 0.80 * cos(pi / 2 - 2 * pi * j / len(cycle)),
                       0.80 * sin(pi / 2 - 2 * pi * j / len(cycle)))
                      for j in range(len(cycle))]
            for j, (u, pos) in enumerate(zip(cycle, points)):
                nxt = points[(j + 1) % len(cycle)]
                ax.annotate("", xy=nxt, xytext=pos,
                            arrowprops={"arrowstyle": "-|>", "color": color,
                                        "lw": 2, "shrinkA": 18, "shrinkB": 18,
                                        "connectionstyle": "arc3,rad=0.40" if len(cycle) == 2 else "arc3,rad=0"})
                ax.add_patch(Circle(pos, 0.24, facecolor="white", edgecolor=color, lw=2.2, zorder=3))
                ax.text(*pos, str(u), ha="center", va="center", fontsize=17, zorder=4)
            ax.text(cx, -1.32, "cycle through 1" if 1 in cycle else "other units",
                    ha="center", fontsize=12, color=color)
        ax.set_title(f"Multiply by {a}, modulo {n}", fontsize=16, pad=16)
        phi = sum(gcd(u, n) == 1 for u in range(n))
        order = len(next(c for c in cycles if 1 in c))
        ax.text(0, -1.80, f"{phi} units     |     first return of {a}: {order} steps",
                ha="center", fontsize=13)
        ax.set(xlim=(-2.7, 2.7), ylim=(-2.1, 1.7), aspect="equal")
        ax.axis("off")
    fig.text(0.5, 0.065, "Follow the arrows: no unit is lost, merged or duplicated.",
             ha="center", fontsize=13)
    fig.subplots_adjust(left=0.035, right=0.965, bottom=0.15, top=0.80, wspace=0.13)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
