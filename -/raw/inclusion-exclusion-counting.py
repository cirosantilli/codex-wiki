"""Exact overlaps of divisibility filters on 1..30; PNG goes to cwd."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def main():
    universe = set(range(1, 31))
    a = {x for x in universe if x % 2 == 0}
    b = {x for x in universe if x % 3 == 0}
    c = {x for x in universe if x % 5 == 0}
    assert (len(a - b), len(a & b), len(b - a), len(universe - (a | b))) == (10, 5, 5, 10)
    assert len(a | b) == len(a) + len(b) - len(a & b) == 20
    sizes = [len(a), len(b), len(c), len(a & b), len(a & c), len(b & c), len(a & b & c)]
    assert sizes == [15, 10, 6, 5, 3, 2, 1]
    assert len(a | b | c) == sum(sizes[:3]) - sum(sizes[3:6]) + sizes[6] == 22
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.3), dpi=120)
    blue, orange = "#176997", "#b55d20"
    ax = axes[0]
    ax.add_patch(Rectangle((-0.5, -0.1), 5, 3.05, fill=False, ec="#aeb8c0", lw=1.2))
    ax.add_patch(Circle((1.3, 1.45), 1.18, facecolor=blue, alpha=0.13, edgecolor=blue, lw=2))
    ax.add_patch(Circle((2.7, 1.45), 1.18, facecolor=orange, alpha=0.13, edgecolor=orange, lw=2))
    for x, count, label in [(0.75, 10, "A only"), (2, 5, "both"), (3.25, 5, "B only")]:
        ax.text(x, 1.45, str(count), ha="center", fontsize=21, color="#273746")
        ax.text(x, 1.12, label, ha="center", fontsize=10, color="#536371")
    ax.text(1.05, 2.75, "A: multiples of 2", ha="center", fontsize=11, color=blue)
    ax.text(3.05, 2.75, "B: multiples of 3", ha="center", fontsize=11, color=orange)
    ax.text(2, 0.05, "neither: 10", ha="center", fontsize=12)
    ax.text(2, -0.57, "15 + 10 − 5 = 20 selected", ha="center", fontsize=14)
    ax.text(2, -0.92, "Region areas are schematic, not proportional.", ha="center", fontsize=10)
    ax.set_xlim(-0.6, 4.6)
    ax.set_ylim(-0.3, 3.1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Two overlapping filters", fontsize=13, pad=15)
    ax = axes[1]
    colors = {0: "#f2f4f6", 1: "#d9eaf4", 2: "#ffd6b7", 3: "#b55d20"}
    for x in range(1, 31):
        column, row = (x - 1) % 6, (x - 1) // 6
        membership = sum(x in s for s in [a, b, c])
        ax.add_patch(Rectangle((column, 4 - row), 0.86, 0.78,
                              facecolor=colors[membership], ec="#b5bfc6", lw=0.8))
        ax.text(column + 0.43, 4 - row + 0.39, str(x), ha="center", va="center",
                fontsize=12, color="white" if membership == 3 else "#263746")
    for i, text in enumerate(["0", "1", "2", "3"]):
        ax.add_patch(Rectangle((i * 1.45, -0.75), 0.28, 0.28,
                              facecolor=colors[i], ec="#b5bfc6", clip_on=False))
        ax.text(i * 1.45 + 0.38, -0.62, text, va="center", fontsize=10)
    ax.text(2.95, -1.15, "Number of filters matched (2, 3, and 5)", ha="center", fontsize=10)
    ax.text(2.95, -1.8, "15 + 10 + 6 − 5 − 3 − 2 + 1 = 22", ha="center", fontsize=13)
    ax.set_xlim(-0.2, 6.0)
    ax.set_ylim(-0.2, 5.05)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Add a third filter: multiples of 5", fontsize=13, pad=15)
    fig.suptitle("Inclusion–exclusion counts each integer in the union once",
                 fontsize=15, y=0.97)
    fig.subplots_adjust(left=0.04, right=0.97, top=0.80, bottom=0.25, wspace=0.23)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
