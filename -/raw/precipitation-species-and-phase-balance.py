"""Illustrative ion inventories; Python 3.14, matplotlib 3.10.7.

Run from _media; writes an opaque PNG to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle


COLORS = {"A": "#2675ac", "B": "#d98527", "X": "#76569c", "Y": "#34876a"}
LABELS = {"A": "A+", "B": "B−", "X": "X−", "Y": "Y+"}


def ion(ax, x, y, species):
    ax.add_patch(Circle((x, y), 0.16, color=COLORS[species]))
    ax.text(x, y, LABELS[species], ha="center", va="center", color="white", fontsize=11)


def main():
    fig, ax = plt.subplots(figsize=(11, 6), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 11), ylim=(0, 6))
    ax.axis("off")
    ax.text(5.5, 5.72, "Same inventory, different phases", ha="center", fontsize=20, weight="bold")
    ax.text(5.5, 5.33, "Invented one-to-one AB model: three pairs enter the solid", ha="center", fontsize=12)
    ax.add_patch(Rectangle((0.45, 1.35), 3.6, 3.55, facecolor="#f2f8fc", edgecolor="#6b8291", lw=1.5))
    ax.add_patch(Rectangle((6.45, 2.15), 4.1, 2.75, facecolor="#f2f8fc", edgecolor="#6b8291", lw=1.5))
    ax.add_patch(Rectangle((6.45, 1.15), 4.1, 0.85, facecolor="#fff6e7", edgecolor="#ac8549", lw=1.5))
    ax.text(2.25, 4.63, "Before: all dissolved", ha="center", fontsize=14, weight="bold")
    ax.text(8.5, 4.63, "After: aqueous ions", ha="center", fontsize=14, weight="bold")
    for row, species in enumerate(["A", "B", "X", "Y"]):
        y = 4.05 - 0.65 * row
        for column in range(4):
            ion(ax, 1.15 + 0.72 * column, y, species)
    ion(ax, 7.20, 4.02, "A")
    ion(ax, 8.02, 4.02, "B")
    ax.text(9.52, 4.02, "one of each", ha="center", va="center", fontsize=11)
    for row, species in enumerate(["X", "Y"]):
        for column in range(4):
            ion(ax, 7.20 + 0.75 * column, 3.29 - 0.68 * row, species)
    ax.text(8.48, 1.88, "AB solid: three of each", ha="center", va="center", fontsize=11)
    for pair in range(3):
        ion(ax, 7.16 + pair * 1.13, 1.47, "A")
        ion(ax, 7.59 + pair * 1.13, 1.47, "B")
    ax.add_patch(FancyArrowPatch((4.25, 3.3), (6.20, 3.3), arrowstyle="-|>", mutation_scale=24, lw=2, color="#334652"))
    ax.text(5.2, 3.75, "precipitation", ha="center", fontsize=12)
    ax.text(5.2, 2.72, "A+ + B−\n→ AB(s)", ha="center", va="center", fontsize=13)
    ax.text(5.5, 0.66, "A: 4 = 1 dissolved + 3 in solid     B: 4 = 1 dissolved + 3 in solid", ha="center", fontsize=13)
    ax.text(5.5, 0.23, "Spectators unchanged: X = 4, Y = 4     •     Total charge = 0 before and after", ha="center", fontsize=12)
    fig.subplots_adjust(left=0.015, right=0.985, bottom=0.02, top=0.98)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
