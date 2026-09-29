"""Show exact cancellation of five reciprocal-product terms; PNG to CWD."""

from pathlib import Path
from fractions import Fraction

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def main():
    assert sum((Fraction(1, n * (n + 1)) for n in range(1, 6)), Fraction()) == Fraction(5, 6)
    plt.rcParams.update({"font.size": 14, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(12, 3.8), dpi=100)
    palette = ["#246bce", "#bf5520", "#23855b", "#965aa8"]
    ax.set(xlim=(-0.25, 4.95), ylim=(0, 1))
    ax.axis("off")
    for index in range(5):
        positive = (index + 0.08, 0.67)
        negative = (index + 0.61, 0.67)
        positive_color = "#172434" if index == 0 else palette[index - 1]
        negative_color = "#172434" if index == 4 else palette[index]
        ax.text(*positive, rf"$\frac{{1}}{{{index + 1}}}$",
                ha="center", va="center", fontsize=28, color=positive_color)
        ax.text(index + 0.34, 0.67, "−", ha="center", va="center", fontsize=24)
        ax.text(*negative, rf"$\frac{{1}}{{{index + 2}}}$",
                ha="center", va="center", fontsize=28, color=negative_color)
        ax.text(index + 0.34, 0.41, rf"Term {index + 1}: $\frac{{1}}{{{(index + 1) * (index + 2)}}}$",
                ha="center", va="center", fontsize=13, color="#45566b")
        if index < 4:
            ax.text(index + 0.86, 0.67, "+", ha="center", va="center", fontsize=22)
            ax.add_patch(FancyArrowPatch(
                (index + 0.61, 0.80), (index + 1.08, 0.80),
                arrowstyle="-", connectionstyle="arc3,rad=-0.55",
                color=palette[index], linewidth=2.5,
            ))
            ax.text(index + 0.845, 0.925, "cancel",
                    color=palette[index], ha="center", va="center", fontsize=11)
    ax.text(2.34, 0.15, r"$S_5 = 1-\frac{1}{6}=\frac{5}{6}$",
            ha="center", va="center", fontsize=26, color="#172434")
    fig.suptitle("Internal contributions cancel; the two boundary terms survive",
                 fontsize=16, weight="bold", y=0.97)
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.03, top=0.78)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
