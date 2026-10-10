"""Original qualitative physiology circuit; Python 3.14 / matplotlib 3.10.7.

Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib
python3.14 ../insulin-glucagon-tissue-control-circuit.py
Saves a same-basename opaque PNG to the current working directory.
Arrows describe qualitative effects, not measured gains or response times.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


BLUE = "#176398"
ORANGE = "#ac5319"
GRAY = "#3f4852"


def draw():
    fig, ax = plt.subplots(figsize=(12, 10), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 10))
    ax.axis("off")

    def box(x, y, text, color, height=0.9):
        ax.add_patch(FancyBboxPatch(
            (x, y), 4.2, height, boxstyle="round,pad=0.08,rounding_size=0.13",
            edgecolor=color, facecolor="white", linewidth=1.6,
        ))
        ax.text(x + 2.1, y + height / 2, text, ha="center", va="center",
                fontsize=11, color=GRAY, linespacing=1.4)

    def arrow(start, end, color, style="-|>"):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                    mutation_scale=15, linewidth=1.6, color=color))

    ax.text(6, 9.6, "Insulin and glucagon: tissue-specific glucose control",
            ha="center", fontsize=17, weight="bold", color=GRAY)
    ax.text(6, 9.22, "Qualitative circuit • schematic arrows • no measured gains or timing",
            ha="center", fontsize=11, color=GRAY)

    box(1.1, 8.05, "Rise in blood glucose", BLUE)
    box(6.7, 8.05, "Fall in blood glucose", ORANGE)
    box(1.1, 6.7, "Pancreatic islets: β cells\nMore insulin released", BLUE)
    box(6.7, 6.7, "Pancreatic islets: α cells\nMore glucagon released", ORANGE)
    box(1.1, 4.8, "Insulin receptor (tyrosine kinase)\nIRS → PI3K → Akt\nA major metabolic signaling branch", BLUE, height=1.35)
    box(6.7, 4.8, "Liver: glucagon receptor (GPCR)\nG protein → adenylyl cyclase → cAMP\nProtein kinase A → enzyme regulation", ORANGE, height=1.35)
    box(1.1, 2.95, "Muscle / fat: more GLUT4 at membrane\nLiver / muscle: glycogen storage favored\nLiver glucose output suppressed", BLUE, height=1.35)
    box(6.7, 2.95, "Liver: glycogen breakdown favored\nGlucose synthesis supported\nOutput depends on available substrates", ORANGE, height=1.35)
    box(1.1, 1.5, "Blood glucose tends to fall\nOpposes the initiating rise", BLUE)
    box(6.7, 1.5, "Blood glucose tends to rise\nOpposes the initiating fall", ORANGE)

    for x, color in [(3.2, BLUE), (8.8, ORANGE)]:
        for ya, yb in [(8.03, 7.65), (6.65, 6.2), (4.74, 4.34), (2.89, 2.44)]:
            arrow((x, ya), (x, yb), color)

    # Outer returns close the two restoring loops; inhibition is a terminal bar.
    for x_outer, x_side, color in [(0.48, 1.0, BLUE), (11.52, 11.0, ORANGE)]:
        ax.plot([x_side, x_outer, x_outer], [1.96, 1.96, 8.5], color=color, lw=1.6)
        ax.plot([x_outer, x_side], [8.5, 8.5], color=color, lw=1.6)
        ax.plot([x_side, x_side], [8.36, 8.64], color=color, lw=1.8)

    ax.text(6, 0.89, "Inside the islet: δ cells release somatostatin, inhibiting insulin and glucagon release.",
            ha="center", va="center", fontsize=11, color=GRAY)
    ax.text(6, 0.49, "Local glucagon can support β-cell insulin release: the two hormones also cooperate.",
            ha="center", va="center", fontsize=11, color=GRAY)
    fig.subplots_adjust(left=0.015, right=0.985, top=0.985, bottom=0.02)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    draw()
