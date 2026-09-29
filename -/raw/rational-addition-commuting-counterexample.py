"""Draw correct addition and an invariant-preserving incorrect operation.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5 (root pyproject.toml).
Run from _media; writes the matching PNG to the current directory.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8), dpi=120, facecolor="white")
    blue, green, red = "#245b93", "#24725b", "#a63535"
    expected = Fraction(1, 2) + Fraction(1, 3)
    assert expected == Fraction(5, 6)
    cases = [
        ("Correct addition", "F", (5, 6), green, True),
        ("Incorrect operation", "B", (2, 6), red, False),
    ]
    for ax, (title, operation, result, color, correct) in zip(axes, cases):
        ax.set(xlim=(0, 6), ylim=(0, 6))
        ax.axis("off")

        def node(x, y, label, width=1.8, height=0.72, tint=blue):
            ax.add_patch(FancyBboxPatch(
                (x - width / 2, y - height / 2), width, height,
                boxstyle="round,pad=0.04,rounding_size=0.10",
                edgecolor=tint, facecolor="white", linewidth=1.5,
            ))
            ax.text(x, y, label, ha="center", va="center", fontsize=14, color=tint)

        def arrow(start, end, label, text_xy, tint=blue):
            ax.add_patch(FancyArrowPatch(
                start, end, arrowstyle="-|>", mutation_scale=15,
                color=tint, linewidth=1.7,
            ))
            ax.text(*text_xy, label, ha="center", va="center", fontsize=13, color=tint)

        observed = Fraction(*result)
        assert (observed == expected) == correct
        assert result[1] != 0
        ax.text(3, 5.62, title, ha="center", fontsize=17, weight="bold", color=color)
        formula = (r"$F((a,b),(c,d))=(ad+bc,bd)$" if correct
                   else r"$B((a,b),(c,d))=(a+c,bd)$")
        ax.text(3, 5.10, formula, ha="center", fontsize=13, color=color)
        node(1.08, 4.12, "(1, 2)\n(1, 3)", height=0.94)
        node(4.80, 4.12, f"{result}", tint=color)
        arrow((2.05, 4.12), (3.82, 4.12), operation, (3.00, 4.39), color)
        node(1.08, 1.54, r"$(\frac{1}{2},\frac{1}{3})$", height=0.9, tint=green)
        node(4.80, 1.54, r"$\frac{5}{6}$", width=1.0, tint=green)
        arrow((1.08, 3.57), (1.08, 2.07), r"$\alpha\times\alpha$", (0.64, 2.83))
        arrow((2.05, 1.54), (4.19, 1.54), "abstract addition", (3.10, 1.12), green)
        if correct:
            arrow((4.80, 3.70), (4.80, 2.03), r"$\alpha$", (5.20, 2.85), green)
            ax.text(3, 0.48, "Both paths give 5/6", ha="center", color=green, fontsize=14)
        else:
            node(4.80, 2.85, r"$\frac{1}{3}$", width=1.0, tint=red)
            arrow((4.80, 3.70), (4.80, 3.20), r"$\alpha$", (5.35, 3.46), red)
            ax.text(4.80, 2.15, r"$\ne$", ha="center", va="center", color=red, fontsize=24)
            ax.text(3, 0.48, "Valid output; wrong abstract value", ha="center", color=red, fontsize=13)

    fig.suptitle("A nonzero denominator does not prove correct addition",
                 fontsize=18, weight="bold", y=0.99)
    fig.subplots_adjust(left=0.015, right=0.985, top=0.90, bottom=0.04, wspace=0.06)
    fig.savefig(Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
