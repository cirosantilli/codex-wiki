"""Area models of distributivity and a fraction product; PNG goes to cwd."""

from fractions import Fraction
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    assert 3 * (2 + 4) == 3 * 2 + 3 * 4 == 18
    assert Fraction(3, 4) * Fraction(2, 3) == Fraction(1, 2)
    assert Fraction(3, 2) * Fraction(2, 3) == 1
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0), dpi=120,
                             gridspec_kw={"width_ratios": [1.15, 1]})
    blue, orange = "#176997", "#b55d20"
    ax = axes[0]
    ax.add_patch(Rectangle((0, 0), 2, 3, fc="#d9eaf4", ec=blue, lw=2))
    ax.add_patch(Rectangle((2, 0), 4, 3, fc="#ffe1c9", ec=orange, lw=2))
    for x in range(1, 6):
        ax.plot([x, x], [0, 3], color="#a9b5bd", lw=0.7)
    for y in [1, 2]:
        ax.plot([0, 6], [y, y], color="#a9b5bd", lw=0.7)
    ax.text(1, 1.5, "6", ha="center", va="center", fontsize=23, color=blue)
    ax.text(4, 1.5, "12", ha="center", va="center", fontsize=23, color=orange)
    ax.text(-0.35, 1.5, "3", ha="center", va="center", fontsize=14)
    ax.text(1, 3.3, "2", ha="center", fontsize=14, color=blue)
    ax.text(4, 3.3, "4", ha="center", fontsize=14, color=orange)
    ax.text(3, -0.6, "3(2 + 4) = 6 + 12 = 18", ha="center", fontsize=13)
    ax.set_xlim(-0.7, 6.3)
    ax.set_ylim(-0.8, 3.8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Whole-number grouping gives distributivity", fontsize=13, pad=18)
    ax = axes[1]
    count = 0
    for i in range(4):
        for j in range(3):
            overlap = i < 3 and j < 2
            color = "#e7c5ae" if overlap else ("#d9eaf4" if i < 3 else ("#ffe1c9" if j < 2 else "white"))
            ax.add_patch(Rectangle((i / 4, j / 3), 1 / 4, 1 / 3,
                                  fc=color, ec="#6e808e", lw=0.9))
            if overlap:
                ax.text((i + 0.5) / 4, (j + 0.5) / 3, "●", ha="center", va="center",
                        color="#874518", fontsize=14)
                count += 1
    assert count == 6
    ax.plot([0, 0.75], [1.1, 1.1], color=blue, lw=3)
    ax.text(0.375, 1.16, "width 3/4", ha="center", fontsize=12, color=blue)
    ax.plot([1.1, 1.1], [0, 2 / 3], color=orange, lw=3)
    ax.text(1.16, 1 / 3, "height 2/3", va="center", fontsize=12, color=orange,
            rotation=90)
    ax.text(0.5, -0.20, "6 of 12 equal cells: area 1/2", ha="center", fontsize=12)
    ax.text(0.5, -0.40, r"$\frac{3}{4}\times\frac{2}{3}=\frac{6}{12}=\frac{1}{2}$",
            ha="center", fontsize=15)
    ax.set_xlim(-0.08, 1.3)
    ax.set_ylim(-0.1, 1.36)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Fractional lengths multiply as area", fontsize=13, pad=18)
    fig.suptitle("The product counts area, even when the sides are fractions",
                 fontsize=15, y=0.97)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.8, bottom=0.19, wspace=0.22)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
