"""Draw a design schematic, without experimental counts or inferred rates.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the matching PNG is written to the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 7.4), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 7.4))
    ax.axis("off")
    ink, blue, amber = "#183245", "#2171a1", "#a56813"

    def box(x, y, w, h, label, edge=ink, fill="white", size=12):
        ax.add_patch(FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.06,rounding_size=0.08",
            linewidth=1.5, edgecolor=edge, facecolor=fill))
        ax.text(x+w/2, y+h/2, label, ha="center", va="center",
                fontsize=size, color=ink, linespacing=1.45)

    def arrow(a, b, color=ink):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>",
                     mutation_scale=14, lw=1.6, color=color))

    ax.text(5, 7.13, "Dietary divergence → mating assay", ha="center",
            fontsize=19, weight="bold", color=ink)
    ax.text(5, 6.82, "Drosophila pseudoobscura · procedure schematic", ha="center",
            fontsize=12, color=ink, style="italic")
    box(3.25, 5.94, 3.5, .6, "One source population")
    arrow((4, 5.92), (2.55, 5.42), blue)
    arrow((6, 5.92), (7.45, 5.42), amber)
    box(.65, 4.58, 3.8, .78, "Starch medium\n4 separate populations", blue, "#eef6fa")
    box(5.55, 4.58, 3.8, .78, "Maltose medium\n4 separate populations", amber, "#fff6e7")
    arrow((2.55, 4.51), (2.55, 4.04), blue)
    arrow((7.45, 4.51), (7.45, 4.04), amber)
    box(.65, 3.3, 3.8, .69, "Common medium\n1 generation", blue)
    box(5.55, 3.3, 3.8, .69, "Common medium\n1 generation", amber)
    arrow((2.55, 3.22), (3.3, 2.84), blue)
    arrow((7.45, 3.22), (6.7, 2.84), amber)
    box(2.35, 2.08, 5.3, .7, "Select two populations → mating chamber\n12 females from each; males from both", size=12)
    ax.text(.5, 2.52, "Cross-diet AND\nsame-diet pairs", fontsize=10.5,
            color=ink, ha="left", va="center", linespacing=1.5)
    ax.text(8.05, 2.52, "Reverse wing\nmarking in repeats", fontsize=10.5,
            color=ink, ha="left", va="center", linespacing=1.5)
    arrow((5, 2), (5, 1.61))
    ax.text(5, 1.39, "Score observed mating categories", ha="center", fontsize=13,
            weight="bold", color=ink)
    for x, label in zip([.7, 3, 5.3, 7.6],
                        ["A female × A male", "A female × B male",
                         "B female × A male", "B female × B male"]):
        box(x, .65, 1.75, .45, label, size=9.5)
    ax.text(5, .18, "A/B label the two populations in a test · no mating counts or isolation rates plotted",
            fontsize=10.5, color=ink, ha="center")
    fig.subplots_adjust(left=.025, right=.975, top=.99, bottom=.02)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
