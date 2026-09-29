"""Draw conceptual secretory routing and conserved membrane orientation.

Run from _media. Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle


def main():
    fig, ax = plt.subplots(figsize=(11, 6), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 11), ylim=(0, 6))
    ax.axis("off")
    blue = "#d7eef7"
    membrane = "#235579"
    cargo = "#bd6a30"
    centers = [1.4, 4.1, 6.8, 9.5]
    labels = ["ER lumen", "Golgi interior", "Vesicle interior", "Cell exterior"]

    ax.text(5.5, 5.75, "Secretory routing preserves membrane sides", ha="center",
            fontsize=18, weight="bold", color="#173e58")
    ax.text(0.25, 5.17, "Soluble cargo", fontsize=13, weight="bold")
    for x, label in zip(centers, labels):
        color = blue if x != centers[-1] else "#e7f2df"
        box = FancyBboxPatch((x - 1.03, 3.63), 2.06, 1.18,
                             boxstyle="round,pad=0.03,rounding_size=0.12",
                             facecolor=color, edgecolor=membrane, lw=1.8)
        ax.add_patch(box)
        ax.text(x, 4.58, label, fontsize=12, ha="center")
        for dx, dy in [(-0.18, -0.12), (0.16, -0.12), (0, 0.12)]:
            ax.add_patch(Circle((x + dx, 4.05 + dy), 0.075, facecolor=cargo,
                                edgecolor="#733611"))
    for a, b, label in zip(centers[:-1], centers[1:],
                           ["ER export", "Onward sorting", "Exocytosis"]):
        ax.add_patch(FancyArrowPatch((a + 1.1, 4.13), (b - 1.1, 4.13),
                                    arrowstyle="-|>", mutation_scale=15,
                                    color=membrane, lw=1.7))
        ax.text((a + b) / 2, 3.30, label, fontsize=10.5, ha="center")

    ax.text(0.25, 2.82, "Membrane cargo: track the same two sides", fontsize=13, weight="bold")
    for x, label in zip(centers, labels):
        color = blue if x != centers[-1] else "#e7f2df"
        ax.add_patch(Rectangle((x - 0.91, 1.62), 1.82, 0.89,
                               facecolor=color, edgecolor="none"))
        ax.plot([x - 0.91, x + 0.91], [1.58, 1.58], lw=10,
                color=membrane, solid_capstyle="butt")
        ax.text(x, 2.33, label, ha="center", fontsize=11)
        ax.plot([x, x], [1.13, 1.99], color=cargo, lw=5, zorder=3)
        for y, tag in [(2.0, "A"), (1.12, "B")]:
            ax.add_patch(Circle((x, y), 0.13, facecolor=cargo, edgecolor="#733611", zorder=4))
            ax.text(x, y, tag, color="white", ha="center", va="center",
                    fontsize=11, weight="bold", zorder=5)
        ax.text(x, 0.74, "Cytosol", ha="center", fontsize=11)
    for a, b in zip(centers[:-1], centers[1:]):
        ax.add_patch(FancyArrowPatch((a + 1.02, 1.58), (b - 1.02, 1.58),
                                    arrowstyle="-|>", mutation_scale=15,
                                    color="#666666", lw=1.5))
    ax.text(5.5, 0.29, "A: lumen-facing → exterior-facing     B: cytosol-facing throughout",
            ha="center", fontsize=12, color=membrane)
    ax.text(5.5, 0.02, "Conceptual stages and local membrane views • no measured times or imaging data • return routes omitted",
            ha="center", fontsize=10, color="#505050")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.05)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
