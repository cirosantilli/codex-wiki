"""Draw the symbolic band changes in unpivoted tridiagonal elimination.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; the output basename matches this generator.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def panel(ax, stage):
    n = 5
    colors = {"diagonal": "#dbe9f4", "upper": "#e6f1e8", "lower": "#eee7f7"}
    for i in range(n):
        for j in range(n):
            eliminated = i == j + 1 and i <= stage
            text, color = "", "white"
            if i == j:
                text = rf"$p_{i+1}$" if i <= stage else rf"$b_{i+1}$"
                color = colors["diagonal"]
                if i == stage and stage:
                    color = "#ffdba1"
            elif j == i + 1:
                text, color = rf"$c_{i+1}$", colors["upper"]
            elif i == j + 1:
                text = "0" if eliminated else rf"$a_{i+1}$"
                color = "#f7f7f7" if eliminated else colors["lower"]
            ax.add_patch(Rectangle((j, n - i - 1), 1, 1, facecolor=color,
                                   edgecolor="#b9c0c6", linewidth=0.7))
            if text:
                ax.text(j + .5, n - i - .5, text, ha="center", va="center", fontsize=13)
    ax.set(xlim=(-.05, 5.05), ylim=(-.05, 5.05), aspect="equal")
    ax.axis("off")


def main():
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.2), facecolor="white")
    titles = ["Start: three diagonals", "After eliminating row 2", "After eliminating row 3"]
    for stage, ax in enumerate(axes):
        panel(ax, stage)
        ax.set_title(titles[stage], fontsize=12, pad=12)
    fig.suptitle("Eliminate one neighbour; update one diagonal", fontsize=16, y=.98)
    fig.text(.5, .11, r"$m_i=a_i/p_{i-1}$     $p_i=b_i-m_i c_{i-1}$     $g_i=d_i-m_i g_{i-1}$",
             ha="center", fontsize=14)
    fig.text(.5, .025, "Orange: newly updated pivot. Blank cells stay zero. The upper diagonal stays unchanged.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.035, right=.975, top=.79, bottom=.21, wspace=.22)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
