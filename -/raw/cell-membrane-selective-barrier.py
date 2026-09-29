"""Draw a conceptual membrane cross-section; output basename.png in cwd.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Shapes, sizes and positions are illustrative, not atomistic structural data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle
import numpy as np


def main():
    blue, orange, purple = "#236d99", "#bc6419", "#744299"
    fig, ax = plt.subplots(figsize=(10, 5.8))
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.09, top=0.90)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis("off")
    ax.add_patch(Rectangle((0.2, 2.2), 9.6, 1.6, color="#fff2df", zorder=0))
    for x in np.arange(0.4, 9.8, 0.35):
        if 4.15 < x < 5.35 or 6.65 < x < 7.95:
            continue
        for head, end in ((3.8, 3.05), (2.2, 2.95)):
            direction = np.sign(end - head)
            for offset in (-0.055, 0.055):
                ax.plot([x + offset, x + offset, x + offset + 0.055],
                        [head + direction * 0.12, end + direction * -0.13, end],
                        color=orange, lw=1.8, zorder=1)
            ax.add_patch(Circle((x, head), 0.115, facecolor="#7db7d2",
                                edgecolor=blue, lw=1, zorder=2))
    ax.add_patch(FancyBboxPatch((4.2, 1.98), 1.15, 2.04,
                               boxstyle="round,pad=0.04,rounding_size=0.24",
                               facecolor="#accdc0", edgecolor="#356957", lw=1.8))
    ax.add_patch(Rectangle((4.63, 1.93), 0.29, 2.14,
                           facecolor="white", edgecolor="none"))
    ax.add_patch(FancyBboxPatch((6.7, 1.98), 1.2, 2.04,
                               boxstyle="round,pad=0.04,rounding_size=0.42",
                               facecolor="#d3c5e5", edgecolor=purple, lw=1.8))
    ax.add_patch(Circle((7.3, 3.25), 0.21, facecolor="white", edgecolor=purple))
    ax.text(7.3, 2.65, "binds;\nchanges\nshape", ha="center", va="center",
            fontsize=10, color="#42315b")
    ax.annotate("", (4.775, 1.60), (4.775, 4.35),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": purple})
    ax.add_patch(Circle((4.775, 4.4), 0.105, color=purple))
    ax.annotate("", (9.1, 1.60), (9.1, 4.35),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": orange})
    ax.add_patch(Circle((9.1, 4.4), 0.105, color=orange))
    ax.add_patch(Circle((3.0, 4.65), 0.14, color=purple))
    ax.text(3.0, 4.65, "+", ha="center", va="center", color="white", fontsize=12)
    ax.annotate("", (3.0, 4.08), (3.0, 4.45),
                arrowprops={"arrowstyle": "->", "lw": 1.8, "color": purple})
    ax.plot([2.84, 3.16], [4.03, 4.03], color="#ac3434", lw=3)
    ax.text(3.0, 5.18, "Ion: strongly\nrestricted here", ha="center", fontsize=10)
    ax.text(4.775, 5.18, "Selective\nion channel", ha="center", fontsize=11)
    ax.text(7.3, 5.18, "Carrier\nprotein", ha="center", fontsize=11)
    ax.text(9.1, 5.18, "Small nonpolar\nmolecule", ha="center", fontsize=10)
    ax.annotate("Hydrophilic heads", (1.1, 3.85), (1.05, 4.6), ha="center",
                fontsize=11, color=blue,
                arrowprops={"arrowstyle": "->", "color": blue, "lw": 1.2})
    ax.annotate("Hydrophobic tails", (1.7, 2.95), (1.65, 1.20), ha="center",
                fontsize=11, color=orange,
                arrowprops={"arrowstyle": "->", "color": orange, "lw": 1.2})
    ax.text(0.35, 5.8, "Outside: water", fontsize=12, weight="bold")
    ax.text(0.35, 0.35, "Inside: cytoplasm containing water", fontsize=12, weight="bold")
    ax.text(5.9, 1.12, "Two leaflets; tails face inward", ha="center", fontsize=11)
    fig.suptitle("Cell membrane: a selective barrier with specific routes", fontsize=15, y=0.97)
    fig.text(0.5, 0.025, "Schematic only: shapes, spacing and arrows do not specify structures or measured rates.",
             ha="center", fontsize=10, color="#444444")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}: 1200 x 696 pixels")


if __name__ == "__main__":
    main()
