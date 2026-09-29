"""Draw an original exact row-reduction ledger; Python 3.14, Matplotlib 3.10."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


def matrix(ax, rows, left, bottom, width, height, pivots=(), separators=()):
    """Typeset a matrix without copying a textbook illustration."""
    nrows, ncols = len(rows), len(rows[0])
    dx, dy = width / ncols, height / nrows
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            x, y = left + (j + 0.5) * dx, bottom + height - (i + 0.5) * dy
            if (i, j) in pivots:
                ax.add_patch(FancyBboxPatch((x - 0.022, y - 0.023), 0.044, 0.046,
                                           boxstyle="round,pad=0.003", facecolor="#dcefe7",
                                           edgecolor="#238452", linewidth=1.5))
            ax.text(x, y, str(value), ha="center", va="center", fontsize=19)
    for x, sign in [(left - 0.006, 1), (left + width + 0.006, -1)]:
        ax.plot([x + sign * 0.008, x, x, x + sign * 0.008],
                [bottom, bottom, bottom + height, bottom + height], color="#333333", linewidth=1.3)
    for j in separators:
        ax.plot([left + j * dx] * 2, [bottom, bottom + height], color="#555555", linewidth=1.1)


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(11.2, 7), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.015, right=0.985, bottom=0.025, top=0.98)
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.text(0.5, 0.963, "Two pivots, one invisible input direction", ha="center", fontsize=20)
    for x, text in [(0.15, r"$A$"), (0.49, "Eliminate below first pivot"), (0.85, "Coefficient RREF")]:
        ax.text(x, 0.882, text, ha="center", fontsize=14)
    matrix(ax, [[1, 2, 3], [2, 4, 6], [1, 1, 2]], 0.058, 0.65, 0.184, 0.18)
    matrix(ax, [[1, 2, 3], [0, 0, 0], [0, -1, -1]], 0.398, 0.65, 0.184, 0.18)
    matrix(ax, [[1, 0, 1], [0, 1, 1], [0, 0, 0]], 0.758, 0.65, 0.184, 0.18,
           pivots=((0, 0), (1, 1)))
    for start, end in [(0.263, 0.374), (0.603, 0.734)]:
        ax.annotate("", (end, 0.74), (start, 0.74), arrowprops={"arrowstyle": "->", "lw": 1.6})
    ax.text(0.32, 0.622, r"$R_2\leftarrow R_2-2R_1$" + "\n" + r"$R_3\leftarrow R_3-R_1$",
            ha="center", va="top", fontsize=12)
    ax.text(0.67, 0.622, r"$R_2\leftrightarrow R_3$" + "\n" + r"$R_2\leftarrow -R_2$" + "\n" +
            r"$R_1\leftarrow R_1-2R_2$", ha="center", va="top", fontsize=12)
    ax.plot([0.035, 0.965], [0.49, 0.49], color="#dddddd", linewidth=1)
    ax.text(0.25, 0.456, "Apply the same operations to both right-hand sides", ha="center", fontsize=13)
    ax.text(0.105, 0.410, "After operations", ha="center", fontsize=12)
    ax.text(0.405, 0.415, r"$b$", ha="center", color="#238452", fontsize=15)
    ax.text(0.475, 0.415, r"$b'$", ha="center", color="#c53636", fontsize=15)
    matrix(ax, [[1, 0, 1, -1, -1], [0, 1, 1, 1, 1], [0, 0, 0, 0, 1]],
           0.16, 0.20, 0.35, 0.18, pivots=((0, 0), (1, 1)), separators=(3, 4))
    ax.add_patch(Rectangle((0.37, 0.205), 0.14, 0.05, facecolor="none", edgecolor="#c53636", linewidth=1.5))
    ax.text(0.335, 0.146, r"$b$: $0=0$" + "      " + r"$b'$: $0=1$", ha="center", fontsize=15)
    ax.text(0.335, 0.09, "Attainable                         Inconsistent", ha="center", fontsize=12)
    ax.add_patch(FancyBboxPatch((0.60, 0.08), 0.345, 0.35, boxstyle="round,pad=0.015",
                               facecolor="#f3f7fa", edgecolor="#c4d5df"))
    ax.text(0.773, 0.385, r"$x_1+x_3=0,\quad x_2+x_3=0$", ha="center", fontsize=15)
    ax.text(0.773, 0.32, r"$\ker A=\mathrm{span}\{(-1,-1,1)^T\}$", ha="center", fontsize=14)
    ax.text(0.773, 0.25, r"$Ax=b:\quad x=(-1,1,0)^T$", ha="center", fontsize=14)
    ax.text(0.773, 0.20, r"$+\ t(-1,-1,1)^T$", ha="center", fontsize=14)
    ax.text(0.773, 0.13, "Rank 2 + nullity 1 = 3 input coordinates", ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
