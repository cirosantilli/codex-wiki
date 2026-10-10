"""Original qualitative IP3 pathway; writes matching opaque PNG to the CWD.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Shapes and arrow lengths encode no measured geometry, amount or timing.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10, 6.8), dpi=130, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 7))
    ax.axis("off")
    orange, blue, green = "#ad5f17", "#24689b", "#357d66"
    ax.add_patch(Rectangle((0.2, 5.6), 9.6, 1.1, color="#fff6e8", zorder=0))
    ax.add_patch(Rectangle((0.2, 0.5), 9.6, 4.7, color="#f1f7fb", zorder=0))
    ax.add_patch(Rectangle((0.2, 5.2), 9.6, 0.4, color="#b8c9d5", zorder=0))
    ax.text(9.6, 6.48, "Extracellular fluid", ha="right", fontsize=12, weight="bold")
    ax.text(0.35, 4.85, "Cytosol", fontsize=12, weight="bold")
    ax.text(9.65, 5.4, "Cell membrane", ha="right", fontsize=11)

    def box(x, y, w, h, label, color="white", edge=blue):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                                   facecolor=color, edgecolor=edge, linewidth=1.7))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center")

    def arrow(start, end, color=blue, dashed=False, rad=0):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=16,
                                    linewidth=1.8, color=color,
                                    linestyle="--" if dashed else "-",
                                    connectionstyle=f"arc3,rad={rad}"))

    box(1.3, 6.0, 1.8, 0.45, "Ligand", "#fff4da", orange)
    box(1.35, 5.0, 1.7, 0.65, "Surface\nreceptor", "#fce9ce", orange)
    arrow((2.2, 6.0), (2.2, 5.67), orange, True)
    box(1.4, 3.85, 1.6, 0.65, "G protein", "#fff4da", orange)
    arrow((2.2, 4.97), (2.2, 4.55), orange, True)
    box(3.55, 3.85, 1.3, 0.65, "PLC\ncatalysis", "#fff4da", orange)
    arrow((3.07, 4.18), (3.48, 4.18), orange, True)
    box(3.45, 5.22, 1.5, 0.36, r"PIP$_2$", "white")
    arrow((4.2, 5.2), (4.2, 4.55))
    ax.text(4.3, 4.8, "hydrolysis", fontsize=10)
    box(5.7, 5.22, 1.1, 0.36, "DAG", "white")
    arrow((4.75, 4.55), (6.2, 5.16), rad=-0.12)
    ax.text(6.25, 5.82, "Membrane-associated product", ha="center", fontsize=10)
    box(4.75, 2.95, 1.5, 0.55, r"Soluble IP$_3$", "#fff4da", orange)
    arrow((4.52, 3.8), (5.1, 3.55))

    box(0.65, 0.85, 3.7, 1.7, "ER lumen\nStored calcium", "#edf6e8", green)
    box(3.5, 1.75, 1.15, 0.55, r"IP$_3$R", "white", green)
    arrow((5.2, 2.88), (4.65, 2.27), orange, True)
    ax.text(5.55, 2.53, "Channel gating", ha="center", fontsize=10, color=orange)
    arrow((4.7, 2.03), (6.05, 2.03))
    ax.text(5.25, 1.68, r"Ca$^{2+}$ release", ha="center", fontsize=10)
    box(6.2, 1.72, 2.75, 0.65, "Free cytosolic\ncalcium", "white")
    arrow((7.6, 2.42), (7.6, 3.25), orange, True)
    box(6.55, 3.3, 2.1, 0.65, "Target proteins", "#fff4da", orange)
    arrow((6.15, 1.74), (4.38, 1.23), green, rad=-0.12)
    ax.text(5.65, 0.85, "Pump back into ER", ha="center", fontsize=10, color=green)
    arrow((9.05, 2.05), (9.05, 6.08), green)
    ax.text(9.3, 3.9, "Export pump", rotation=90, va="center", fontsize=10, color=green)
    ax.text(0.4, 0.22, "Dashed: activation relay    Solid: products or calcium movement",
            fontsize=10, color="#374650")
    fig.suptitle("IP3 links membrane reception to an intracellular calcium store", fontsize=15)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.92)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
