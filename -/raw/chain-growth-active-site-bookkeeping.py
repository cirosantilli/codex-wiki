"""Draw stipulated one-site chain counts; Python 3.14, matplotlib 3.10.7.

Run from _media; the PNG basename matches this generator.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


BLUE = "#176aa3"
GREY = "#6a737d"
ORANGE = "#d67520"


def chain(ax, x, y, n, active=True):
    for i in range(n):
        ax.add_patch(Rectangle((x + i * 0.30, y - 0.15), 0.24, 0.30,
                               facecolor=BLUE if active else GREY, edgecolor="white"))
    if active:
        ax.text(x + n * 0.30, y, "★", color=ORANGE, fontsize=19, va="center")


def arrow(ax, x1, x2, y):
    ax.add_patch(FancyArrowPatch((x1, y), (x2, y), arrowstyle="-|>",
                                mutation_scale=17, color="#343e48", linewidth=1.7))


def main():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=140, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.5))
    ax.axis("off")
    ax.text(0.1, 6.12, "Chain growth: units, molecules, and active sites", fontsize=19,
            weight="bold")
    ax.text(0.1, 5.72, "One active site per growing chain • schematic counts, not kinetic data",
            fontsize=11, color=GREY)
    rows = [(4.7, "Initiation", "+1", "+1", "+1"),
            (3.4, "Propagation", "0", "0", "+1"),
            (2.1, "Termination: join", "−1", "−2", "0"),
            (0.9, "Termination: separate", "0", "−2", "0")]
    for x, title in [(7.45, "ΔC"), (8.30, "ΔA"), (9.15, "ΔS")]:
        ax.text(x, 5.17, title, ha="center", fontsize=15, weight="bold")
    for y, title, dc, da, ds in rows:
        ax.text(0.1, y + 0.40, title, fontsize=12, weight="bold")
        for x, value in [(7.45, dc), (8.30, da), (9.15, ds)]:
            ax.text(x, y, value, ha="center", va="center", fontsize=17)
        arrow(ax, 4.15, 4.95, y)
    ax.text(1.05, 4.7, "$I^*$", fontsize=18, va="center", color=ORANGE)
    ax.text(1.8, 4.7, "+", fontsize=18, va="center")
    chain(ax, 2.35, 4.7, 1, False)
    ax.text(2.47, 4.30, "free M", fontsize=10, ha="center")
    chain(ax, 5.25, 4.7, 1)
    chain(ax, 1.05, 3.4, 3)
    ax.text(2.40, 3.4, "+", fontsize=18, va="center")
    chain(ax, 2.9, 3.4, 1, False)
    chain(ax, 5.25, 3.4, 4)
    for y in [2.1, 0.9]:
        chain(ax, 1.05, y, 2)
        ax.text(2.20, y, "+", fontsize=18, va="center")
        chain(ax, 2.70, y, 3)
    chain(ax, 5.25, 2.1, 5, False)
    chain(ax, 5.05, 0.9, 2, False)
    ax.text(5.90, 0.9, "+", fontsize=18, va="center")
    chain(ax, 6.2, 0.9, 3, False)
    ax.text(0.1, 0.25, "C: polymer molecules     A: polymer-bound active sites     S: incorporated units",
            fontsize=11)
    fig.subplots_adjust(left=0.02, right=0.99, top=0.99, bottom=0.01)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
