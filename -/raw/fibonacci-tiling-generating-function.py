"""Enumerate board coverings and illustrate their recurrence; PNG goes to cwd.

Uses the repository's Matplotlib dependency, Python 3.14.4.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def tilings(length):
    if length == 0:
        return [()]
    return [(first,) + rest for first in (1, 2) if first <= length
            for rest in tilings(length - first)]


def draw_board(ax, pieces, y, x=0):
    for width in pieces:
        ax.add_patch(Rectangle((x + 0.035, y), width - 0.07, 0.52,
                               facecolor="#426c91" if width == 1 else "#bd6f26",
                               edgecolor="white", linewidth=1.2))
        ax.text(x + width / 2, y + 0.26, str(width), ha="center", va="center",
                fontsize=12, color="white")
        x += width


def main():
    counts = [len(tilings(n)) for n in range(7)]
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.0), dpi=120)
    fig.patch.set_facecolor("white")
    ax = axes[0]
    for row, pieces in enumerate(tilings(4)):
        y = 4.2 - row * 0.77
        draw_board(ax, pieces, y)
        ax.text(4.2, y + 0.26, " + ".join(map(str, pieces)), va="center", fontsize=11)
    ax.set(xlim=(-0.12, 6.45), ylim=(0.65, 5.05))
    ax.axis("off")
    ax.set_title("Length four: all five tilings", fontsize=13, pad=10)
    ax.text(0, 0.25, "First tile 1: three continuations\nFirst tile 2: two continuations",
            fontsize=11, linespacing=1.5)

    ax = axes[1]
    for n, count in enumerate(counts):
        ax.text(n, 3.3, str(n), ha="center", va="center", fontsize=12)
        ax.text(n, 2.52, str(count), ha="center", va="center", fontsize=15,
                color="#263746", bbox={"boxstyle": "round,pad=0.3", "fc": "#eef3f7",
                                        "ec": "#bcc9d2"})
    ax.text(-0.75, 3.3, "n", fontsize=12, va="center")
    ax.text(-0.75, 2.52, r"$t_n$", fontsize=12, va="center")
    ax.text(3, 1.55, r"$t_4=t_3+t_2=3+2=5$", fontsize=15, ha="center")
    ax.text(3, 0.85, r"$F(z)=1+(z+z^2)F(z)$", fontsize=15, ha="center")
    ax.text(3, 0.08, r"$F(z)=\frac{1}{1-z-z^2}$", fontsize=16, ha="center")
    ax.set(xlim=(-1.1, 6.55), ylim=(-0.25, 4))
    ax.axis("off")
    ax.set_title("Counts include the empty tiling", fontsize=13, pad=10)
    fig.suptitle("One-unit and two-unit choices produce Fibonacci counts", fontsize=15, y=0.97)
    fig.text(0.5, 0.035, "Blue: length 1     Orange: length 2     Empty board: exactly one tiling",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.035, right=0.98, top=0.83, bottom=0.17, wspace=0.18)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
