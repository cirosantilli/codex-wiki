"""Feasible and sustainable average entry-game payoffs; Python 3.14.4.

Uses Matplotlib 3.10.7. Output is an opaque white PNG in the current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def main():
    fig, ax = plt.subplots(figsize=(5.2, 4.0), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.add_patch(Polygon([(1, 1), (2, 6), (3, 3)], closed=True, facecolor="#e8edf2", edgecolor="#526476", linewidth=1.5, label="feasible payoffs"))
    ax.add_patch(Polygon([(2, 3), (2, 6), (3, 3)], closed=True, facecolor="#a9d8c0", edgecolor="#1c7051", linewidth=1.8, label="average-payoff Nash region"))
    ax.axvline(2, color="#1c7051", linestyle=":", linewidth=1.2)
    ax.axhline(3, color="#1c7051", linestyle=":", linewidth=1.2)
    for x, y, text, offset in [(1, 1, "fight (1, 1)", (7, 2)), (2, 6, "stay out (2, 6)", (-8, 11)), (3, 3, "acquiesce (3, 3)", (-5, -18)), (2, 3, "(2, 3)", (-50, -15))]:
        ax.scatter([x], [y], s=35, color="#243c4d", zorder=4)
        ax.annotate(text, (x, y), xytext=offset, textcoords="offset points", fontsize=10,
                    ha="right" if offset[0]<0 else "left")
    ax.set_xlim(0.7, 3.4)
    ax.set_ylim(0.5, 6.9)
    ax.set_xticks([1, 2, 3])
    ax.set_yticks([1, 2, 3, 4, 5, 6])
    ax.set_xlabel("Ann's average payoff (millions)")
    ax.set_ylabel("Bob's average payoff (millions)")
    ax.set_title("Feasibility and the two security bounds", fontsize=12)
    ax.legend(loc="lower right", fontsize=9, framealpha=1)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(pad=0.8)
    fig.savefig(Path.cwd()/(Path(__file__).stem+".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
