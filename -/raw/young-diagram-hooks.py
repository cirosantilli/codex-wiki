"""Draw English-convention Young diagrams; write basename PNG in CWD.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
"""

from math import prod
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


SHAPE = (3, 2)
DARK = "#243746"
PALE = "#f1f4f7"
ANCHOR, ARM, LEG = "#f8cf91", "#b8d9ee", "#bfe2ca"


def conjugate(shape):
    return tuple(sum(part >= j for part in shape)
                 for j in range(1, max(shape, default=0) + 1))


def hooks(shape):
    columns = conjugate(shape)
    return tuple(tuple(part - j + columns[j - 1] - i + 1
                       for j in range(1, part + 1))
                 for i, part in enumerate(shape, 1))


def draw(ax, shape, labels, colors=None):
    colors = colors or {}
    for i, part in enumerate(shape, 1):
        for j in range(1, part + 1):
            ax.add_patch(Rectangle((j - 1, i - 1), 1, 1,
                                   facecolor=colors.get((i, j), PALE),
                                   edgecolor=DARK, linewidth=1.6))
            ax.text(j - 0.5, i - 0.5, labels[i - 1][j - 1],
                    ha="center", va="center", fontsize=14, color=DARK)
    ax.set(xlim=(-0.12, 3.12), ylim=(3.18, -0.12), aspect="equal")
    ax.axis("off")


def main():
    transposed = conjugate(SHAPE)
    values = hooks(SHAPE)
    assert transposed == (2, 2, 1)
    assert values == ((4, 3, 1), (2, 1))
    assert prod(value for row in values for value in row) == 24
    assert hooks(transposed) == ((4, 2), (3, 1), (1,))

    fig, axes = plt.subplots(1, 4, figsize=(10.8, 4.0), dpi=120,
                             facecolor="white")
    coordinates = tuple(tuple(f"({i}, {j})" for j in range(1, part + 1))
                        for i, part in enumerate(SHAPE, 1))
    draw(axes[0], SHAPE, coordinates)
    draw(axes[1], transposed, tuple(tuple("" for _ in range(part))
                                  for part in transposed))
    draw(axes[2], SHAPE, (("", "own", "right"), ("", "below")),
         {(1, 2): ANCHOR, (1, 3): ARM, (2, 2): LEG})
    draw(axes[3], SHAPE, values)
    titles = (r"Shape $\lambda=(3,2)$", r"Conjugate $\lambda'=(2,2,1)$",
              r"Hook $H_{1,2}$", r"Hook lengths $h_{i,j}$")
    captions = ("3 cells in row 1; 2 in row 2", "Rows and columns exchange",
                "1 own + 1 right + 1 below = 3", "Product: 4 × 3 × 1 × 2 × 1 = 24")
    for ax, title, caption in zip(axes, titles, captions):
        ax.set_title(title, fontsize=12, color=DARK, pad=12)
        ax.text(0.5, -0.06, caption, transform=ax.transAxes,
                ha="center", va="top", fontsize=10, color=DARK)
    fig.suptitle("English convention: rows left-aligned, counted from top to bottom",
                 fontsize=14, color=DARK, y=0.96)
    fig.subplots_adjust(left=0.025, right=0.985, top=0.79, bottom=0.17,
                        wspace=0.17)
    fig.savefig(Path.cwd() / "young-diagram-hooks.png", facecolor="white",
                transparent=False)
    plt.close(fig)
    print("Conjugate (2,2,1); hooks [[4,3,1],[2,1]]; product 24.")


if __name__ == "__main__":
    main()
