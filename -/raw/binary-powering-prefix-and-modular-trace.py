"""Draw binary-prefix traces; run from _media with Python 3.14 / Matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(10, 5.3), dpi=120, facecolor="white")
    ax.set(xlim=(-0.6, 7.6), ylim=(-0.85, 4.2))
    ax.axis("off")
    fig.suptitle("Binary powering: append a digit, square, then multiply if it is 1",
                 fontsize=15, y=0.96)
    xs = [0.45, 2.45, 4.45, 6.45]
    prefixes = ["1", "11", "110", "1101"]
    exponents = [int(p, 2) for p in prefixes]
    ordinary = [3**p for p in exponents]
    residues = [pow(2, p, 17) for p in exponents]
    assert ordinary == [3, 27, 729, 1594323]
    assert residues == [2, 8, 13, 15]
    for x, prefix, exponent in zip(xs, prefixes, exponents):
        ax.text(x, 3.65, f"prefix {prefix}₂\np = {exponent}", ha="center", va="center",
                color="#333333", fontsize=13)
    for y, values, color, label in [(2.45, ordinary, "#18639a", "Ordinary: 3ᵖ"),
                                    (0.95, residues, "#13775f", "Reduced: 2ᵖ mod 17")]:
        ax.text(-0.4, y + 0.64, label, color=color, weight="bold")
        for x, value in zip(xs, values):
            ax.add_patch(FancyBboxPatch((x - 0.69, y - 0.29), 1.38, 0.58,
                                       boxstyle="round,pad=0.04", facecolor="white",
                                       edgecolor=color, linewidth=1.6))
            ax.text(x, y, f"{value:,}", ha="center", va="center", color=color,
                    weight="bold", fontsize=13)
        for i, bit in enumerate("101"):
            ax.add_patch(FancyArrowPatch((xs[i] + 0.76, y), (xs[i + 1] - 0.76, y),
                                        arrowstyle="->", mutation_scale=13, color=color))
            operation = "square; × base" if bit == "1" else "square"
            ax.text((xs[i] + xs[i + 1]) / 2, y - 0.53, operation,
                    ha="center", color=color, fontsize=10)
    ax.text(3.45, -0.28,
            "Initialize at the leading 1: no multiplication.\n"
            "Read 1, 0, 1: three squarings + two further multiplications = five.\n"
            "In the lower row, reduce after every product: 4 → 8; 64 → 13; 169 → 16 → 15.",
            ha="center", va="center", fontsize=11)
    fig.subplots_adjust(left=0.035, right=0.985, top=0.85, bottom=0.075)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
