"""Draw original concrete-to-abstract rational representations.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5 (root pyproject.toml).
Run from _media; writes the matching PNG to the current directory.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(10, 6), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis("off")
    blue, green, red = "#245b93", "#24725b", "#a63535"

    def box(x, y, width, height, label, color, fill):
        ax.add_patch(FancyBboxPatch(
            (x, y), width, height,
            boxstyle="round,pad=0.05,rounding_size=0.12",
            edgecolor=color, facecolor=fill, linewidth=1.5,
        ))
        ax.text(x + width / 2, y + height / 2, label,
                ha="center", va="center", color=color, fontsize=14)

    ax.text(5, 5.75, "One abstract value, several concrete states",
            ha="center", va="center", fontsize=18, weight="bold")
    ax.text(2.2, 5.13, r"Stored integer pairs $(n,d)$",
            ha="center", fontsize=14, color=blue)
    ax.text(7.5, 5.13, "Abstract rational values",
            ha="center", fontsize=14, color=green)
    ax.text(5, 4.66, r"$\alpha(n,d)=n/d$", ha="center", fontsize=15)

    groups = [
        ([(1, 2), (2, 4), (-1, -2)], [4.03, 3.40, 2.77], Fraction(1, 2), 3.40),
        ([(0, 1), (0, -3)], [1.94, 1.31], Fraction(0), 1.63),
    ]
    for pairs, positions, value, target_y in groups:
        label = r"$\frac{1}{2}$" if value else "$0$"
        box(6.85, target_y - 0.28, 1.3, 0.56, label, green, "#edf6f1")
        for (n, d), y in zip(pairs, positions):
            assert Fraction(n, d) == value
            box(1.0, y - 0.24, 2.4, 0.48, f"({n}, {d})", blue, "#eef4fb")
            ax.add_patch(FancyArrowPatch(
                (3.48, y), (6.74, target_y),
                arrowstyle="-|>", mutation_scale=14,
                color=blue, linewidth=1.5, connectionstyle="arc3,rad=0",
            ))

    box(0.7, 0.25, 3.0, 0.48, "(1, 0)     (0, 0)", red, "#fff2f2")
    ax.text(4.05, 0.49, "Invalid: denominator is zero; no abstract value",
            color=red, fontsize=12, va="center")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
    fig.savefig(Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
