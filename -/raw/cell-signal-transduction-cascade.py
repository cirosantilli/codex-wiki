"""Draw reception, intracellular relay and response; write basename.png in cwd.

Tested with Python 3.14.4 and Matplotlib 3.10.7.
Original schematic, not a particular measured pathway or molecular structure.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle


def main():
    fig, ax = plt.subplots(figsize=(9.6, 6.2))
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.13, top=0.90)
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis("off")
    blue, orange, purple = "#236d99", "#b6531f", "#744299"

    def arrow(start, end):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=17,
                                    lw=2, color="#444444", zorder=5))

    def box(x, y, width, height, text, color):
        ax.add_patch(FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.07",
                                    facecolor="white", edgecolor=color, lw=2, zorder=3))
        ax.text(x + width / 2, y + height / 2, text, ha="center", va="center",
                fontsize=12, color=color, zorder=4)

    ax.text(0.4, 5.7, "OUTSIDE THE CELL", fontsize=12, color="#444444")
    ax.text(0.4, 3.15, "INSIDE\nTHE CELL", fontsize=11, color="#444444", va="center")
    ax.add_patch(Rectangle((0.15, 3.85), 9.7, 0.48, facecolor="#e4eef3", edgecolor=blue, lw=1.5))
    ax.text(7.9, 4.09, "Cell membrane", ha="center", va="center", color=blue, fontsize=12)
    box(1.2, 3.6, 1.8, 1.1, "Surface\nreceptor", blue)
    ax.add_patch(Circle((2.1, 5.35), 0.18, facecolor="#ebba8e", edgecolor=orange, lw=2))
    ax.text(2.5, 5.35, "Extracellular ligand", va="center", fontsize=12, color=orange)
    arrow((2.1, 5.13), (2.1, 4.78))
    ax.text(0.5, 5.03, "1  Reception", fontsize=12, color=orange, ha="left")
    box(1.25, 2.05, 1.7, 0.65, "Relay A", purple)
    box(4.15, 2.05, 1.7, 0.65, "Relay B", purple)
    arrow((2.1, 3.53), (2.1, 2.78))
    arrow((3.03, 2.375), (4.07, 2.375))
    ax.text(3.7, 3.08, "2  Intracellular transduction", fontsize=13, color=purple)
    box(6.8, 2.50, 2.65, 0.8, "Change gene\nexpression", blue)
    box(6.8, 0.9, 2.65, 0.9, "Other response:\nenzyme or channel", blue)
    arrow((5.93, 2.50), (6.72, 2.9))
    arrow((5.93, 2.2), (6.72, 1.35))
    ax.text(7.8, 3.48, "3  Response", fontsize=13, ha="center", color=blue)
    ax.text(3.45, 0.53, "Relays can branch; no universal number of steps.", fontsize=11, ha="center", color="#444444")
    fig.suptitle("A surface receptor carries the message across the boundary", fontsize=15, y=0.97)
    fig.text(0.5, 0.07, "The ligand stays outside in this example; arrows represent causal steps.", ha="center", fontsize=11)
    fig.text(0.5, 0.025, "Unscaled cartoon; amplification, feedback and adaptation are possible, not obligatory.", ha="center", fontsize=10, color="#444444")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}: 1152 x 744 pixels")


if __name__ == "__main__":
    main()
