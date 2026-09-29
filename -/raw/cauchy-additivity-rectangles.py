"""Illustrate Cauchy additivity with original exact rectangle and grid examples."""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, (ax, grid) = plt.subplots(1, 2, figsize=(10, 4.6), dpi=120,
                                   gridspec_kw={"width_ratios": [1.2, 1]})
    fig.suptitle(r"Addition preserved by $f(x)=3x$", fontsize=19, y=0.96)
    x, y = Fraction(2, 3), Fraction(5, 6)
    colors = ["#dcecf7", "#ffead5"]
    for start, width, color in [(0, x, colors[0]), (x, y, colors[1])]:
        ax.add_patch(Rectangle((float(start), 0), float(width), 3,
                               facecolor=color, edgecolor="#243746", linewidth=2))
    for i in range(1, 9):
        ax.plot([i / 6, i / 6], [0, 3], color="#7e8c95", alpha=0.45, lw=0.8)
    for j in [1, 2]:
        ax.plot([0, 1.5], [j, j], color="#7e8c95", alpha=0.45, lw=0.8)
    ax.text(float(x / 2), 1.5, r"$3x=2$", ha="center", fontsize=17,
            bbox={"facecolor": colors[0], "edgecolor": "none", "pad": 3})
    ax.text(float(x + y / 2), 1.5, r"$3y=5/2$", ha="center", fontsize=17,
            bbox={"facecolor": colors[1], "edgecolor": "none", "pad": 3})
    for left, right, label in [(0, float(x), r"$x=2/3$"),
                               (float(x), 1.5, r"$y=5/6$")]:
        ax.annotate("", (left, -0.22), (right, -0.22),
                    arrowprops={"arrowstyle": "|-|", "color": "#243746"})
        ax.text((left + right) / 2, -0.46, label, ha="center")
    ax.text(-0.12, 1.5, "height 3", rotation=90, va="center", ha="center")
    ax.text(0.75, 3.3, r"$3(x+y)=9/2=2+5/2$", ha="center", fontsize=15)
    ax.text(0.75, -0.95, "Each small cell has area 1/6.", ha="center", fontsize=11)
    ax.set(xlim=(-0.3, 1.7), ylim=(-1.1, 3.65))
    ax.set_axis_off()

    xs = [Fraction(-2, 3), Fraction(0), Fraction(2, 3)]
    ys = [Fraction(-1, 6), Fraction(0), Fraction(5, 6)]
    values = [[str(3 * (a + b)) for b in ys] for a in xs]
    grid.set_axis_off()
    grid.set_title(r"Exact grid: every cell is $f(x+y)$", fontsize=13, pad=18)
    table = grid.table(cellText=values, rowLabels=[str(a) for a in xs],
                       colLabels=[str(b) for b in ys], cellLoc="center",
                       rowLoc="center", bbox=[0.12, 0.33, 0.86, 0.52])
    table.auto_set_font_size(False)
    table.set_fontsize(13)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#8294a0")
        if row == 0:
            cell.set_facecolor(colors[1])
        elif col == -1:
            cell.set_facecolor(colors[0])
    table[3, 2].set_facecolor("#d9ecd9")
    grid.text(0.57, 0.96, r"column input $y$", ha="center", transform=grid.transAxes)
    grid.text(0.03, 0.9, r"$x$", ha="center", transform=grid.transAxes)
    grid.text(0.54, 0.18, r"$f(x+y)=3(x+y)=3x+3y$", ha="center",
              transform=grid.transAxes, fontsize=13)
    grid.text(0.54, 0.07, "Negative inputs obey the same rule.", ha="center",
              transform=grid.transAxes, fontsize=11)
    fig.subplots_adjust(left=0.05, right=0.97, top=0.79, bottom=0.07, wspace=0.3)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
