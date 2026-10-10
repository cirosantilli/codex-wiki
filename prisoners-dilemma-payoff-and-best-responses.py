"""Draw prisoners-dilemma-payoff-and-best-responses.png in the current directory.

Original diagram; tested with Python 3.14.4 and Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../prisoners-dilemma-payoff-and-best-responses.py
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    blue, orange = "#2166a5", "#b34e14"
    fig, ax = plt.subplots(figsize=(8.6, 5.8), facecolor="white")
    ax.set(xlim=(-0.9, 3.6), ylim=(-0.85, 2.9))
    ax.set_facecolor("white")
    ax.axis("off")
    cells = {(0, 1): (3, 3), (1, 1): (0, 5),
             (0, 0): (5, 0), (1, 0): (1, 1)}
    for (column, row), (u1, u2) in cells.items():
        ax.add_patch(Rectangle((column, row), 1, 1,
                               facecolor="#e8f1f8" if row == column == 0 else
                               "#fff3e7" if row == 0 and column == 1 else "white",
                               edgecolor="#657180", linewidth=1.5))
        # Row best responses lie in the D row; column best responses in D column.
        ax.text(column + .32, row + .5, str(u1), ha="center", va="center",
                color=blue, fontsize=26, fontweight="bold" if row == 0 else "normal")
        ax.text(column + .5, row + .5, ",", ha="center", va="center", fontsize=22)
        ax.text(column + .68, row + .5, str(u2), ha="center", va="center",
                color=orange, fontsize=26, fontweight="bold" if column == 1 else "normal")
    for x in (.13, 1.13):
        ax.annotate("", (x, .30), (x, 1.7),
                    arrowprops={"arrowstyle": "-|>", "color": blue, "lw": 2.2})
    for y in (.84, 1.84):
        ax.annotate("", (1.8, y), (.2, y),
                    arrowprops={"arrowstyle": "-|>", "color": orange, "lw": 2.2})
    for x, label in ((.5, "C"), (1.5, "D")):
        ax.text(x, 2.16, label, ha="center", fontsize=17, fontweight="bold")
    for y, label in ((1.5, "C"), (.5, "D")):
        ax.text(-.22, y, label, ha="center", va="center", fontsize=17, fontweight="bold")
    ax.text(1, 2.5, "Column player's choice", ha="center", color=orange, fontsize=14)
    ax.text(-.67, 1, "Row player's choice", ha="center", va="center",
            rotation=90, color=blue, fontsize=14)
    ax.text(2.2, 1.57, "Mutual cooperation\nBoth get 3", fontsize=13, va="center")
    ax.text(2.2, .45, "Unique Nash equilibrium\nBoth get 1", fontsize=13, va="center")
    ax.text(1, -.24, "C = cooperate     D = defect", ha="center", fontsize=13)
    fig.suptitle("Prisoner's dilemma: individual incentives, shared loss", fontsize=16, y=.965)
    fig.text(.5, .095, "Blue ↓: row best responses     Orange →: column best responses",
             ha="center", fontsize=12)
    fig.text(.5, .045, "Bold numbers mark each player's best response to the other's fixed choice.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.02, right=.98, bottom=.12, top=.89)
    fig.savefig("prisoners-dilemma-payoff-and-best-responses.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
