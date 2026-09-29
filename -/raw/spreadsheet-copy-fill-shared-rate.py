"""Draw an original spreadsheet fill example; emit PNG in the working directory.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


INPUT = "#e7f0fa"
FORMULA = "#e4f3e9"
RATE = "#fff0cc"
INK = "#233448"


def exact(value):
    return str(value.numerator) if value.denominator == 1 else str(value)


def grid(ax, top, filled):
    widths = [0.44, 1.42, 1.52, 2.05, 3.13, 0.4, 1.34]
    xs = [0.25]
    for width in widths:
        xs.append(xs[-1] + width)
    labels = ["", "A", "B", "C", "D", "E", "F"]
    for j, label in enumerate(labels):
        ax.text((xs[j] + xs[j + 1]) / 2, top + 0.2, label,
                ha="center", va="center", color=INK, weight="bold", fontsize=11)
    rows = [(3, Fraction(5, 2), "2.5"), (4, Fraction(7, 4), "1.75"),
            (2, Fraction(9, 2), "4.5")]
    for i in range(4):
        row = i + 1
        y = top - (i + 1) * 0.61
        for j in range(7):
            if j == 0:
                content, colour = str(row), "#f0f2f5"
            elif i == 0:
                content = ["", "Quantity", "Unit price", "Subtotal", "With tax", "", "0.2 = 1/5"][j]
                colour = RATE if j == 6 else "#f0f2f5"
            elif j in (1, 2):
                content = str(rows[i - 1][0]) if j == 1 else rows[i - 1][2]
                colour = INPUT
            elif j in (3, 4) and (filled or row == 2):
                subtotal = rows[i - 1][0] * rows[i - 1][1]
                formula = f"=A{row}*B{row}" if j == 3 else f"=C{row}*(1+$F$1)"
                value = subtotal if j == 3 else subtotal * Fraction(6, 5)
                content = formula + "\nvalue: " + exact(value)
                colour = FORMULA
            else:
                content, colour = "", "white"
            ax.add_patch(Rectangle((xs[j], y), widths[j], 0.61,
                                   facecolor=colour, edgecolor="#b8c3ce", linewidth=0.8))
            ax.text(xs[j] + widths[j] / 2, y + 0.305, content, ha="center",
                    va="center", fontsize=10 if j == 4 else 10.5, color=INK,
                    fontfamily="DejaVu Sans Mono" if i and j in (3, 4) else "DejaVu Sans")
        if i and row == 2:
            ax.add_patch(Rectangle((xs[3], y), widths[3] + widths[4], 0.61,
                                   fill=False, edgecolor="#288451", linewidth=2))
    ax.add_patch(Rectangle((xs[6], top - 0.61), widths[6], 0.61,
                           fill=False, edgecolor="#b47a0a", linewidth=2))


def main():
    plt.rcParams["text.parse_math"] = False
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 10.7), ylim=(0, 8.2))
    ax.axis("off")
    ax.text(0.25, 7.96, "Write two formulas once; fill three item rows",
            fontsize=17, weight="bold", color=INK)
    ax.text(0.25, 7.59, "Blue: inputs     Green: formulas + exact values     Gold: shared rate in F1",
            fontsize=11, color=INK)
    ax.text(0.25, 7.14, "BEFORE  ·  formulas entered only in C2 and D2", fontsize=12, weight="bold", color=INK)
    grid(ax, 6.72, False)
    ax.annotate("", xy=(5.4, 3.57), xytext=(5.4, 4.13),
                arrowprops={"arrowstyle": "->", "color": "#288451", "lw": 2})
    ax.text(5.64, 3.87, "Fill C2:D2 down to row 4", va="center", fontsize=11, color=INK)
    ax.text(0.25, 3.29, "AFTER  ·  row references advance; $F$1 stays fixed", fontsize=12, weight="bold", color=INK)
    grid(ax, 2.87, True)
    ax.text(0.25, 0.15, "Stored decimal inputs; exact rational outputs shown for checking.  The blank E column separates the shared input.",
            fontsize=10, color=INK)
    fig.subplots_adjust(left=0.015, right=0.985, top=0.99, bottom=0.025)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
