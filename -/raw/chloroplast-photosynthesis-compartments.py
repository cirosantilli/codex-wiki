"""Draw chloroplast stage locations; write basename.png to CWD.

Tested with Python 3.14 and the repository's Matplotlib/NumPy environment.
Original schematic, not an experimental photograph or a scale drawing.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    green, blue, orange, ink = "#438251", "#176b92", "#a65412", "#253442"
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(11.2, 6.8))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 15), ylim=(0, 9.6))
    ax.axis("off")

    def rounded(x, y, w, h, fill, edge, lw=1.6):
        ax.add_patch(FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.35",
            facecolor=fill, edgecolor=edge, linewidth=lw,
        ))

    def arrow(start, end, color=blue, dashed=False):
        ax.add_patch(FancyArrowPatch(
            start, end, arrowstyle="-|>", mutation_scale=17,
            color=color, linewidth=2, linestyle="--" if dashed else "-",
        ))

    ax.text(7.5, 9.2, "Chloroplast: two stages in different compartments",
            ha="center", fontsize=17, weight="bold", color=ink)
    rounded(1.7, 1.5, 11.6, 6.4, "#f6faf0", green)
    rounded(1.87, 1.67, 11.26, 6.06, "#f6faf0", green, 1)
    ax.text(11.6, 7.25, "Stroma", color=green, fontsize=14, weight="bold")
    ax.text(7.4, 1.05, "Chloroplast envelope", color=green, ha="center", fontsize=11)

    rounded(2.55, 3.05, 3.7, 2.85, "#d9ecdd", green, 5)
    ax.text(4.4, 4.1, "Thylakoid interior\n(lumen)", ha="center", color=green)
    rounded(2.75, 5.1, 3.3, 1.28, "#ffffff", green)
    ax.text(4.4, 5.75, "1  Light reactions\nat the membrane", ha="center",
            va="center", weight="bold", fontsize=11, color=ink)
    ax.text(4.4, 2.6, "Thylakoid membrane", color=green, ha="center", fontsize=11)

    rounded(9.2, 3.5, 3.15, 2.45, "#ffffff", blue)
    ax.text(10.78, 4.72, "2  Calvin cycle\nCarbon fixation\nin the stroma",
            ha="center", va="center", color=ink, weight="bold", fontsize=12)

    ax.text(4.4, 8.4, "Light", ha="center", color=orange, weight="bold")
    arrow((4.4, 8.1), (4.4, 6.45), orange, True)
    ax.text(0.75, 5.8, "H₂O\nWater", ha="center", va="center", color=blue)
    arrow((1.22, 5.75), (2.7, 5.75))
    arrow((2.52, 3.8), (1.1, 3.8))
    ax.text(0.75, 3.15, "O₂\nReleased oxygen", ha="center", va="center",
            color=blue, fontsize=10)
    ax.text(10.78, 8.4, "CO₂", ha="center", color=blue, weight="bold")
    arrow((10.78, 8.1), (10.78, 6.02))
    arrow((6.12, 5.6), (9.14, 5.6), orange, True)
    ax.text(7.63, 6.08, "ATP + NADPH", ha="center", color=orange, fontsize=11)
    ax.text(7.63, 5.18, "energy + electrons", ha="center", color=orange, fontsize=10)
    arrow((9.14, 3.85), (6.33, 3.85), orange, True)
    ax.text(7.65, 3.4, "ADP + Pᵢ; NADP⁺\ncarriers return for reuse",
            ha="center", va="top", color=orange, fontsize=10)
    arrow((12.42, 4.65), (14.25, 4.65))
    ax.text(14.15, 3.55, "Triose\nphosphate\nfor sugars",
            ha="center", color=blue, fontsize=10)
    ax.text(7.5, 0.3,
            "Original schematic, not an experimental photo. Sizes and molecular counts are not to scale.\n"
            "Solid blue: selected matter transfers. Dashed orange: light and carrier coupling.",
            ha="center", va="center", color=ink, fontsize=10)
    fig.subplots_adjust(left=0.025, right=0.985, top=0.97, bottom=0.03)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
