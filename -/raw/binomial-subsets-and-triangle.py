"""Enumerated two-subsets and matching Pascal coefficients; PNG goes to cwd."""

from itertools import combinations
from math import comb
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    letters = "abcde"
    selections = list(combinations(range(5), 2))
    assert len(selections) == comb(5, 2) == 10
    assert sum(comb(5, k) for k in range(6)) == 32
    assert comb(5, 2) == comb(4, 1) + comb(4, 2)
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.8), dpi=120)
    orange, blue = "#b55d20", "#176997"
    ax = axes[0]
    for j, letter in enumerate(letters):
        ax.text(j, 10.15, letter, ha="center", va="center", fontsize=13)
    ax.text(5.4, 10.15, "selected subset", ha="center", fontsize=11)
    for i, selected in enumerate(selections):
        y = 9.4 - i
        for j in range(5):
            active = j in selected
            ax.scatter(j, y, s=150, facecolor=orange if active else "white",
                       edgecolor=orange if active else "#b9c3ca", lw=1.2)
        pair = "{" + ", ".join(letters[j] for j in selected) + "}"
        ax.text(5.4, y, pair, ha="center", va="center", fontsize=12)
    ax.set_xlim(-0.55, 6.4)
    ax.set_ylim(-0.5, 10.8)
    ax.axis("off")
    ax.set_title("Choose exactly two of five members", fontsize=13, pad=15)
    ax.text(2.9, -1.2, "Orange means included; each row is one subset.",
            ha="center", fontsize=10)
    ax = axes[1]
    for n in range(6):
        for k in range(n + 1):
            x, y = k - n / 2, 5 - n
            color = orange if (n, k) == (5, 2) else "#263746"
            box = {"boxstyle": "circle,pad=0.38", "fc": "#fff2e8",
                   "ec": orange} if (n, k) == (5, 2) else None
            ax.text(x, y, str(comb(n, k)), ha="center", va="center",
                    fontsize=14, color=color, bbox=box, zorder=3)
        ax.text(-3.3, 5 - n, f"n = {n}", va="center", fontsize=10, color="#62707d")
    for k in [1, 2]:
        ax.annotate("", xy=(-0.5, 0), xytext=(k - 2, 1),
                    arrowprops={"arrowstyle": "-|>", "color": blue,
                                "lw": 1.7, "shrinkA": 15, "shrinkB": 20})
    ax.text(0, -1.15, r"$\binom{5}{2}=\binom{4}{1}+\binom{4}{2}=4+6=10$",
            ha="center", fontsize=13, color=blue)
    ax.set_xlim(-3.8, 3.1)
    ax.set_ylim(-0.55, 5.55)
    ax.axis("off")
    ax.set_title("The same counts build Pascal's triangle", fontsize=13, pad=15)
    fig.suptitle("Selections, binary encodings, and binomial coefficients agree",
                 fontsize=15, y=0.97)
    fig.subplots_adjust(left=0.045, right=0.975, top=0.81, bottom=0.21, wspace=0.18)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
