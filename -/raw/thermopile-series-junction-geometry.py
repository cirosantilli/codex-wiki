"""Draw an original thermopile wiring and thermal geometry schematic.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the output is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10, 6.1), dpi=130, facecolor="white")
    ax.set(xlim=(-0.9, 9.7), ylim=(-0.9, 6.1))
    ax.axis("off")
    fig.suptitle("Thermopile: electrical series, shared thermal regions", fontsize=16, y=0.98)
    blue, orange, purple = "#1765a1", "#c24a20", "#70499b"
    ax.add_patch(Rectangle((-0.35, 3.52), 8.7, 0.66, facecolor="#fff0dd", edgecolor=orange, lw=1.5))
    ax.text(4, 3.93, r"Absorber at $T_h$ — thermal contact, electrical insulation", ha="center", fontsize=11)
    ax.add_patch(Rectangle((-0.35, 0.20), 8.7, 0.65, facecolor="#e8f3fb", edgecolor=blue, lw=1.5))
    ax.text(4, 0.40, r"Reference support at $T_c$ — separate electrical junctions", ha="center", fontsize=11)
    for x in (0.3, 3.1, 5.9):
        ax.plot([x, x + 0.8], [0.85, 3.5], color=blue, lw=3.5)
        ax.plot([x + 0.8, x + 1.6], [3.5, 0.85], color=orange, lw=3.5)
        ax.scatter([x + 0.8], [3.5], s=45, color="#282828", zorder=5)
        ax.text(x + 0.1, 2.25, "A", color=blue, fontsize=13, weight="bold")
        ax.text(x + 1.15, 2.25, "B", color=orange, fontsize=13, weight="bold")
    for x in (1.9, 4.7):
        ax.plot([x, x + 1.2], [0.85, 0.85], color="#333333", lw=2)
        ax.scatter([x, x + 1.2], [0.85, 0.85], s=18, color="#333333", zorder=5)
    for x in (2.5, 5.3):
        ax.text(x, 1.04, "B → A", ha="center", fontsize=10)
    ax.plot([0.3, -0.6, -0.6, 3.4], [0.85, 0.85, -0.48, -0.48], color="#333333", lw=1.7)
    ax.plot([7.5, 8.85, 8.85, 5.2], [0.85, 0.85, -0.48, -0.48], color="#333333", lw=1.7)
    ax.add_patch(Rectangle((3.4, -0.78), 1.8, 0.65, facecolor="white", edgecolor="#333333", lw=1.7))
    ax.text(4.3, -0.45, "Voltmeter", ha="center", va="center")
    ax.text(3.25, -0.26, "+", color=blue, weight="bold", fontsize=16)
    ax.text(5.25, -0.26, "−", color=orange, weight="bold", fontsize=16)
    for x in (1.0, 3.3, 5.6):
        ax.add_patch(FancyArrowPatch((x, 5.25), (x, 4.30), arrowstyle="-|>", mutation_scale=18, color=orange, lw=2))
    ax.text(3.3, 5.55, r"Added absorbed radiation: $P_{\rm abs}$", ha="center", color=orange, fontsize=12)
    ax.add_patch(FancyArrowPatch((8.05, 3.45), (8.05, 1.0), arrowstyle="-|>", mutation_scale=17, color=purple, lw=2))
    ax.text(8.28, 2.22, "Heat\nescapes\nto reference", va="center", color=purple, fontsize=10)
    ax.text(4.0, 6.0, r"Three pairs shown; total $N$ pairs. Positive output if $\alpha>0$ and $T_h>T_c$.", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.025, right=0.98, bottom=0.05, top=0.92)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
