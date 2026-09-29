"""Draw selected matter paths and energy coupling; write basename.png to CWD.

Tested with Python 3.14 and the repository's Matplotlib/NumPy environment.
This is a schematic, not measured yields or a complete reaction mechanism.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    blue, orange, ink = "#176b92", "#a65412", "#253442"
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(11.2, 6.6))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 14), ylim=(0, 8.8))
    ax.axis("off")

    def box(x, y, w, label, color=blue):
        ax.add_patch(FancyBboxPatch(
            (x - w / 2, y - 0.52), w, 1.04,
            boxstyle="round,pad=0.06,rounding_size=0.12",
            facecolor="#f4f8fa" if color == blue else "#fff7ef",
            edgecolor=color, linewidth=1.6,
        ))
        ax.text(x, y, label, ha="center", va="center", color=ink)

    def arrow(start, end, label="", color=blue, dashed=False):
        ax.add_patch(FancyArrowPatch(
            start, end, arrowstyle="-|>", mutation_scale=17,
            linewidth=2, color=color, linestyle="--" if dashed else "-",
        ))
        if label:
            ax.text((start[0] + end[0]) / 2, start[1] + 0.28,
                    label, ha="center", va="bottom", color=color, fontsize=11)

    ax.text(7, 8.5, "Photosynthesis: follow matter and energy separately",
            ha="center", va="center", fontsize=17, weight="bold", color=ink)
    ax.text(0.4, 7.7, "OXYGEN SOURCE  ·  selected matter path", color=blue,
            fontsize=11, weight="bold")
    box(1.5, 6.7, 2.1, "Water\nH₂O")
    box(6.8, 6.7, 2.9, "Water splitting\nin light reactions")
    box(12.2, 6.7, 2.5, "Released oxygen\nO₂")
    arrow((2.62, 6.7), (5.28, 6.7), "water supplies electrons")
    arrow((8.32, 6.7), (10.89, 6.7), "O atoms from water")

    ax.text(0.4, 5.1, "CARBON SOURCE  ·  selected matter path", color=blue,
            fontsize=11, weight="bold")
    box(1.5, 4.1, 2.1, "Carbon dioxide\nCO₂")
    box(5.6, 4.1, 2.6, "Carbon fixation\nCalvin cycle")
    box(9.7, 4.1, 2.3, "Triose phosphate\n3 carbons")
    box(12.8, 4.1, 1.6, "Sugars")
    arrow((2.62, 4.1), (4.23, 4.1), "carbon")
    arrow((6.96, 4.1), (8.49, 4.1), "net product")
    arrow((10.92, 4.1), (11.93, 4.1))
    ax.text(12.2, 3.31, "further reactions", ha="center", fontsize=10, color=blue)

    ax.text(0.4, 2.6, "ENERGY COUPLING  ·  dashed arrows", color=orange,
            fontsize=11, weight="bold")
    box(1.5, 1.65, 2.1, "Light", orange)
    box(6.8, 1.65, 2.9, "ATP + NADPH\nchemical carriers", orange)
    box(12.2, 1.65, 2.5, "Supports\ncarbon fixation", orange)
    arrow((2.62, 1.65), (5.28, 1.65), "via light reactions", orange, True)
    arrow((8.32, 1.65), (10.89, 1.65), "energy + electrons", orange, True)
    ax.text(7, 0.35,
            "Schematic of oxygenic photosynthesis. Carriers are molecules too; arrows omit intermediate steps.\n"
            "Energy is transformed, not created; some absorbed energy is dissipated as heat.",
            ha="center", va="center", color=ink, fontsize=10)
    fig.subplots_adjust(left=0.025, right=0.985, top=0.975, bottom=0.025)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
