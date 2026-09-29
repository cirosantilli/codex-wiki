"""Draw the coordinate-conversion square and similarity invariants.

Emit the matching PNG into CWD. Tested with Python 3.14 and matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


INK = "#243444"
BLUE = "#1769a4"
ORANGE = "#bc5318"
GREEN = "#287451"


def main():
    plt.rcParams.update({"font.size": 13, "text.color": INK,
                         "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(11.2, 6.5), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set_xlim(0, 11.2)
    ax.set_ylim(0, 6.5)
    ax.axis("off")
    ax.text(5.6, 6.16, "Two routes, one output:  AS = SB", ha="center",
            fontsize=19, weight="bold")

    def card(cx, cy, title, formula, color):
        ax.add_patch(FancyBboxPatch((cx - 1.7, cy - 0.58), 3.4, 1.16,
                                   boxstyle="round,pad=0.08,rounding_size=0.1",
                                   facecolor="#f7f9fb", edgecolor=color, lw=1.5))
        ax.text(cx, cy + 0.20, title, ha="center", fontsize=12, color=color)
        ax.text(cx, cy - 0.22, formula, ha="center", fontsize=16)

    card(2.3, 4.86, "Old input coordinates", "$x=Sy=(2,1)^T$", BLUE)
    card(8.9, 4.86, "Old output coordinates", "$x'=Ax=(4,5)^T$", ORANGE)
    card(2.3, 2.79, "New input coordinates", "$y=(1,1)^T$", BLUE)
    card(8.9, 2.79, "New output coordinates", "$y'=By=(-1,5)^T$", ORANGE)
    for yy, label in [(4.86, r"$A=\operatorname{diag}(2,5)$"),
                      (2.79, "$B=S^{-1}AS$")]:
        ax.annotate("", xy=(7.07, yy), xytext=(4.13, yy),
                    arrowprops=dict(arrowstyle="->", lw=2, color=INK, mutation_scale=17))
        ax.text(5.6, yy + 0.20, label, ha="center", fontsize=14)
    for xx in [2.3, 8.9]:
        ax.annotate("", xy=(xx, 4.19), xytext=(xx, 3.47),
                    arrowprops=dict(arrowstyle="->", lw=2.5, color=GREEN,
                                    mutation_scale=17))
        ax.text(xx + 0.16, 3.83, "$S$", color=GREEN, fontsize=17, va="center")
    ax.text(5.6, 3.86, "$S$ reconstructs old coordinates\nfrom the new basis",
            ha="center", va="center", fontsize=12, color=GREEN)
    ax.text(5.6, 1.88, "Unchanged: trace 7  •  determinant 10  •  eigenvalues 2 and 5",
            ha="center", fontsize=14, weight="bold")
    ax.text(5.6, 1.40, r"$\chi_A(t)=\chi_B(t)=t^2-7t+10$", ha="center", fontsize=16)
    ax.plot([0.6, 10.6], [1.06, 1.06], color="#d3dbe2", lw=1)
    ax.text(5.6, 0.70, "Eigenvector for 5: old tuple (0, 1), new tuple (−1, 1)",
            ha="center", fontsize=13)
    ax.text(5.6, 0.24, "$S(-1,1)^T=(0,1)^T$  —  the same physical vertical vector",
            ha="center", fontsize=13)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
