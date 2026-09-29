"""Draw the two cycles of multiplication by two modulo seven.

Run from _media; tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


def main():
    p, a = 7, 2
    remaining = set(range(1, p))
    cycles = []
    while remaining:
        start = min(remaining)
        cycle, x = [], start
        while x in remaining:
            cycle.append(x)
            remaining.remove(x)
            x = a * x % p
        assert x == start
        cycles.append(cycle)
    assert cycles == [[1, 2, 4], [3, 6, 5]]

    plt.rcParams.update({"font.size": 14, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(8.6, 5.2), dpi=100, facecolor="white")
    ax.set(xlim=(0, 8.6), ylim=(0, 5.2), aspect="equal")
    ax.axis("off")
    ax.text(4.3, 4.93, "Multiplication by 2 modulo 7: two shorter cycles",
            ha="center", va="center", fontsize=16, weight="bold")
    ax.text(4.3, 4.47, "Every arrow means multiply by 2, then reduce modulo 7.",
            ha="center", fontsize=13)
    for j, cycle in enumerate(cycles):
        center = np.array([2.12 + 4.35 * j, 2.70])
        angles = np.pi / 2 - np.arange(3) * 2 * np.pi / 3
        points = [center + 1.05 * np.array([np.cos(t), np.sin(t)]) for t in angles]
        color = ["#236a9f", "#35814c"][j]
        for k, (value, pos) in enumerate(zip(cycle, points)):
            nxt = points[(k + 1) % 3]
            ax.add_patch(FancyArrowPatch(pos, nxt, arrowstyle="-|>", mutation_scale=19,
                                        shrinkA=21, shrinkB=21, lw=2, color=color,
                                        connectionstyle="arc3,rad=0.12"))
            ax.add_patch(Circle(pos, 0.29, fc="white", ec=color, lw=2))
            ax.text(*pos, str(value), ha="center", va="center", fontsize=19, color=color)
        ax.text(center[0], 1.27, ["Powers of 2: 1, 2, 4", "Other residues: 3, 6, 5"][j],
                ha="center", fontsize=13, color=color)
    ax.text(4.3, 0.76, "$2^3 \\equiv 1 \\;(\\mathrm{mod}\\;7)$: shortest return is 3 steps", ha="center")
    ax.text(4.3, 0.29, "$2^6 \\equiv (2^3)^2 \\equiv 1 \\;(\\mathrm{mod}\\;7)$: Fermat's 6-step return still holds",
            ha="center", fontsize=13)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.98)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
