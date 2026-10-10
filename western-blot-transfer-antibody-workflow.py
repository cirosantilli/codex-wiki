"""Draw a schematic Western blot workflow; no experimental measurements.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the matching PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle


BLUE = "#1764a0"
INK = "#203040"
ORANGE = "#c65a16"


def box(ax, x, y, w, h, color="white", edge=INK, lw=1.4):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor=edge, lw=lw))


def arrow(ax, a, b, color=INK, lw=1.8):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=15,
                               color=color, lw=lw))


def antibody(ax, x, y, color, scale=1):
    ax.plot([x, x, x - .14 * scale], [y + .39 * scale, y + .17 * scale, y],
            color=color, lw=3)
    ax.plot([x, x + .14 * scale], [y + .17 * scale, y],
            color=color, lw=3)


def main():
    fig, ax = plt.subplots(figsize=(12, 7.4), dpi=110, facecolor="white")
    ax.set(xlim=(0, 12), ylim=(0, 7.4))
    ax.axis("off")
    ax.text(6, 7.08, "Western blot: separation → transfer → detection",
            ha="center", fontsize=19, weight="bold", color=INK)
    ax.text(6, 6.68, "SDS-PAGE workflow • schematic symbols, no measured bands",
            ha="center", fontsize=12, color=INK)

    for x, title in [(0.2, "1  Separate"), (4.35, "2  Transfer"), (8.45, "3  Detect")]:
        box(ax, x, 2.35, 3.35, 3.92, edge="#b8c5ce")
        ax.text(x + 1.675, 5.9, title, ha="center", fontsize=16,
                weight="bold", color=INK)

    box(ax, .72, 3.18, 2.18, 2.18, "#edf5fa")
    for x in [1.08, 1.67, 2.25]:
        box(ax, x, 5.16, .25, .14, "white", BLUE)
    for x, ys in [(1.08, [4.7, 4.1, 3.58]), (1.67, [4.7, 3.77]),
                  (2.25, [4.4, 4.1, 3.58])]:
        for y in ys:
            ax.plot([x - .02, x + .3], [y, y], color=BLUE, lw=4)
    arrow(ax, (3.12, 5.1), (3.12, 3.5), BLUE)
    ax.text(1.8, 2.8, "Anionic protein complexes\nmigrate through a gel", ha="center",
            fontsize=11, color=INK)

    # Section through the stack: negatively charged SDS-protein complexes
    # travel from the gel towards the membrane on the anode side.
    box(ax, 4.62, 3.43, .13, 1.72, "#dbe4ea")
    box(ax, 5.08, 3.43, .47, 1.72, "#edf5fa", BLUE)
    box(ax, 6.3, 3.43, .12, 1.72, "#f2dbc9", ORANGE)
    box(ax, 7.3, 3.43, .13, 1.72, "#dbe4ea")
    for y in [3.78, 4.27, 4.76]:
        ax.add_patch(Circle((5.31, y), .07, color=BLUE))
        arrow(ax, (5.61, y), (6.19, y), BLUE, 1.4)
        ax.add_patch(Circle((6.36, y), .06, color=BLUE))
    ax.text(4.68, 5.42, "−", ha="center", fontsize=20, color=INK)
    ax.text(7.36, 5.42, "+", ha="center", fontsize=20, color=INK)
    ax.text(4.68, 3.1, "cathode", ha="center", fontsize=10, color=INK)
    ax.text(5.3, 5.24, "gel", ha="center", fontsize=11, color=BLUE)
    ax.text(6.36, 5.25, "membrane", ha="center", fontsize=10, color=ORANGE)
    ax.text(7.36, 3.1, "anode", ha="center", fontsize=10, color=INK)
    ax.text(6.025, 2.65, "Transfer across gel thickness\nClose contact preserves positions",
            ha="center", fontsize=10.5, color=INK)

    box(ax, 8.92, 3.65, 2.44, .15, "#f2dbc9", ORANGE)
    ax.add_patch(Circle((9.52, 3.85), .13, facecolor=BLUE, edgecolor=BLUE))
    antibody(ax, 9.7, 3.96, BLUE, 1.3)
    antibody(ax, 9.7, 4.4, ORANGE, 1.15)
    ax.add_patch(Circle((9.85, 4.88), .12, facecolor="#f0b429", edgecolor=ORANGE))
    ax.text(10.13, 5.12, "label", fontsize=11, color=ORANGE)
    ax.text(10.16, 4.67, "secondary", fontsize=11, color=ORANGE)
    ax.text(10.16, 4.15, "primary", fontsize=11, color=BLUE)
    ax.text(9.5, 3.27, "retained target", fontsize=11, color=BLUE)
    ax.text(10.12, 2.67, "Block → probe → wash\nLabel produces the readout",
            ha="center", fontsize=11, color=INK)

    arrow(ax, (3.62, 4.25), (4.27, 4.25))
    arrow(ax, (7.79, 4.25), (8.38, 4.25))
    for x, title, detail in [(.2, "Position", "Reference lanes estimate apparent mass"),
                           (4.35, "Retention", "Check the receiving sheet and residual gel"),
                           (8.45, "Recognition", "Positive, negative and no-primary controls")]:
        ax.text(x + 1.675, 1.85, title, ha="center", fontsize=13,
                weight="bold", color=INK)
        ax.text(x + 1.675, 1.35, detail.replace(" estimate ", "\nestimate ")
                .replace(" and residual", "\nand residual")
                .replace(" and no-primary", "\nand no-primary"),
                ha="center", fontsize=10.5, color=INK)
    ax.text(6, .53, "Band identity and amount require controls; darkness alone is insufficient.",
            ha="center", fontsize=12, color=INK)
    fig.subplots_adjust(left=.015, right=.985, bottom=.025, top=.985)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
