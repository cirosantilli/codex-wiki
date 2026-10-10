"""Draw blank and sample measurements; run from the output directory.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=140, facecolor="white")
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.03, top=0.95)
    ax.set(xlim=(0, 12), ylim=(0, 7))
    ax.axis("off")
    ink, blue, orange = "#23364d", "#147a9a", "#b45019"
    ax.text(6, 6.7, "One instrument, two successive measurements", ha="center",
            fontsize=17, weight="bold", color=ink)
    ax.text(6, 6.25, "Same wavelength band, collection geometry, and detector", ha="center", color=ink)

    def box(x, y, w, text):
        ax.add_patch(FancyBboxPatch((x, y - 0.5), w, 1,
                     boxstyle="round,pad=0.06", facecolor="#f4f7fa", edgecolor=ink, linewidth=1.5))
        ax.text(x + w / 2, y, text, ha="center", va="center", color=ink)

    def arrow(x0, x1, y, color):
        ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle="-|>",
                     mutation_scale=17, color=color, linewidth=2.5))

    for y, step, fill, label, power, color in [
        (4.75, "1. Reference blank", "#e4f3f8", "Solvent + background", r"$P_0$", blue),
        (2.5, "2. Sample", "#ffdfbc", "Blank ingredients + target", r"$P$", orange),
    ]:
        ax.text(0.15, y + 0.83, step, color=color, weight="bold", fontsize=13)
        box(0.2, y, 1.4, "Light\nsource")
        box(2.25, y, 2.05, "Monochromator\n(select band)")
        ax.add_patch(Rectangle((5.2, y - 0.6), 1.05, 1.2, facecolor=fill, edgecolor=ink, linewidth=2))
        ax.plot([5.33, 6.12], [y + 0.38, y + 0.38], color=ink, linewidth=1)
        ax.text(5.72, y + 0.77, "Cuvette", ha="center", color=ink)
        box(8.6, y, 1.8, "Photo-\ndetector")
        for x0, x1 in [(1.65, 2.16), (4.4, 5.1), (6.34, 8.45)]:
            arrow(x0, x1, y, color)
        ax.text(7.38, y + 0.28, power, ha="center", color=color, fontsize=16)
        ax.text(5.72, y - 0.97, label, ha="center", color=ink, fontsize=11)
        ax.text(10.7, y, "Dark response\nsubtracted", va="center", color=ink, fontsize=10)

    ax.annotate("", (6.25, 1.17), (5.2, 1.17),
                arrowprops={"arrowstyle": "<->", "color": ink, "linewidth": 1.4})
    ax.text(5.72, 0.82, r"Geometric length $l$", ha="center", color=ink, fontsize=11)
    ax.text(0.25, 0.14, "Match orientation and keep\noptical faces clean", color=ink, fontsize=11)
    ax.text(8.45, 0.77, r"$T=P/P_0$", color=ink, fontsize=18, ha="center")
    ax.text(8.45, 0.17, r"$A=-\log_{10} T$", color=ink, fontsize=18, ha="center")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
