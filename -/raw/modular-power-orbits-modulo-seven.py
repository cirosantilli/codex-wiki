"""Draw exact modular multiplication cycles; Python 3.14, matplotlib 3.10.7.

Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path
import math

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def main():
    fig, ax = plt.subplots(figsize=(9.2, 5.5), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(-0.6, 9.0), ylim=(-1.6, 4.3), aspect="equal")
    ax.axis("off")
    ax.text(4.2, 4.0, "Multiplication by 2 modulo 7", ha="center", fontsize=19)
    for cx, initial, color in [(1.9, 1, "#176b91"), (6.5, 3, "#95502b")]:
        orbit = [initial]
        value = (2 * initial) % 7
        while value != initial:
            orbit.append(value)
            value = (2 * value) % 7
        angles = [math.pi / 2 - 2 * math.pi * j / len(orbit) for j in range(len(orbit))]
        points = [(cx + 1.13 * math.cos(t), 2.0 + 1.13 * math.sin(t)) for t in angles]
        for j, (x, y) in enumerate(points):
            nx, ny = points[(j + 1) % len(points)]
            ax.add_patch(FancyArrowPatch((x, y), (nx, ny), shrinkA=22, shrinkB=22,
                                        arrowstyle="-|>", mutation_scale=18, lw=2, color=color))
            ax.add_patch(Circle((x, y), 0.27, fc="white", ec=color, lw=2))
            ax.text(x, y, str(orbit[j]), ha="center", va="center", fontsize=18, color=color)
        label = "Powers of 2: start at 1" if initial == 1 else "Start at 3: a different cycle"
        ax.text(cx, 0.58, label, ha="center", fontsize=12, color=color)
    ax.text(4.2, 0.12, r"$\operatorname{ord}_7(2)=3\quad\mid\quad\varphi(7)=6$",
            ha="center", fontsize=18)
    residues = [pow(2, k, 7) for k in range(9)]
    ax.text(-0.15, -0.49, r"$k$", ha="center", fontsize=13)
    ax.text(-0.15, -0.98, r"$2^k\;\mathrm{mod}\;7$", ha="center", fontsize=13)
    for k, residue in enumerate(residues):
        x = 0.95 + 0.83 * k
        ax.text(x, -0.49, str(k), ha="center", fontsize=13)
        ax.text(x, -0.98, str(residue), ha="center", fontsize=15, color="#176b91")
    for j in range(3):
        left = 0.60 + 2.49 * j
        ax.plot([left, left + 2.36], [-1.2, -1.2], lw=3, color="#176b91")
    ax.text(4.2, -1.52, "Each three-term block is 1, 2, 4; no repeats within a block.",
            ha="center", fontsize=12)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.98)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
