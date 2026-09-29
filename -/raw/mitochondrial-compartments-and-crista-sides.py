"""Draw an original mitochondrial topology schematic; emit PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Geometry is illustrative, with no physical scale or measured quantities.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11.6, 6.6), dpi=100, facecolor="white")
    ax = fig.add_axes((0.025, 0.08, 0.95, 0.82))
    ax.set(xlim=(0, 12), ylim=(0, 6.6))
    ax.axis("off")
    green, yellow, blue, outer = "#e0f1e7", "#fff0c5", "#21658b", "#74503d"
    fig.suptitle("Mitochondrial compartments: follow the membrane sides", fontsize=17, y=0.97)
    ax.text(3.4, 6.35, "A simplified section", ha="center", weight="bold", fontsize=13)
    ax.text(9.65, 6.35, "One crista, enlarged", ha="center", weight="bold", fontsize=13)
    ax.add_patch(FancyBboxPatch((0.45, 1.45), 6.35, 3.9,
                              boxstyle="round,pad=0,rounding_size=0.45",
                              facecolor=yellow, edgecolor=outer, linewidth=3))
    # The green matrix is one connected polygon. Indentations from its top
    # contain yellow fluid continuously connected to the peripheral space.
    points = [(0.9, 1.9), (6.35, 1.9), (6.35, 4.85), (5.65, 4.85),
              (5.65, 3.0), (5.1, 3.0), (5.1, 4.85), (4.15, 4.85),
              (4.15, 2.65), (3.55, 2.65), (3.55, 4.85), (2.6, 4.85),
              (2.6, 3.2), (2.05, 3.2), (2.05, 4.85), (0.9, 4.85)]
    ax.add_patch(Polygon(points, closed=True, facecolor=green,
                         edgecolor=blue, linewidth=3, joinstyle="round"))
    ax.text(1.05, 5.65, "Cytosol", color="#444444")
    ax.text(1.15, 2.2, "Matrix", color="#256343", fontsize=13, weight="bold")
    ax.annotate("Intermembrane space", xy=(1.15, 5.12), xytext=(0.55, 6.0),
                arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    ax.annotate("Crista lumen", xy=(3.85, 3.35), xytext=(2.8, 0.75),
                arrowprops={"arrowstyle": "->", "color": "#555555"}, ha="center")
    ax.annotate("Outer membrane", xy=(6.8, 3.6), xytext=(5.45, 5.95),
                arrowprops={"arrowstyle": "->", "color": outer}, ha="center", fontsize=10)
    ax.annotate("Inner membrane", xy=(6.35, 2.25), xytext=(5.4, 0.75),
                arrowprops={"arrowstyle": "->", "color": blue}, ha="center")
    ax.text(3.5, 0.1, "Yellow fold interiors open to the peripheral yellow space.",
            ha="center", fontsize=10)

    # A local fold, open at the top; green surrounds the yellow lumen.
    ax.add_patch(Rectangle((7.5, 1.45), 4.15, 4.3, facecolor=green, edgecolor="none"))
    ax.add_patch(Polygon([(8.65, 5.75), (8.65, 2.0), (10.2, 2.0), (10.2, 5.75)],
                         closed=False, facecolor=yellow, edgecolor=blue, linewidth=3,
                         joinstyle="round"))
    ax.annotate("Open to peripheral space", xy=(9.42, 5.5), xytext=(9.5, 6.0),
                ha="center", fontsize=10, arrowprops={"arrowstyle": "->"})
    ax.text(9.43, 4.9, "Crista\nlumen", ha="center", fontsize=12)
    ax.text(11.05, 5.2, "Matrix", ha="center", fontsize=12, color="#256343")
    ax.annotate("", xy=(9.65, 4.0), xytext=(10.9, 4.0),
                arrowprops={"arrowstyle": "-|>", "color": "#c06020", "lw": 3})
    ax.text(10.2, 4.23, "H⁺ pumping", color="#984517", ha="center", fontsize=10)
    ax.add_patch(Rectangle((10.04, 2.7), 0.32, 0.65, facecolor="#367c53", edgecolor="white"))
    ax.annotate("", xy=(10.95, 3.0), xytext=(9.55, 3.0),
                arrowprops={"arrowstyle": "-|>", "color": "#267746", "lw": 3})
    ax.text(9.55, 2.45, "H⁺ return", ha="center", color="#267746", fontsize=10)
    ax.text(10.95, 2.25, "ATP\nsynthase", ha="center", color="#267746", fontsize=10)
    ax.text(9.6, 1.0, "ADP + phosphate → ATP\non the matrix side", ha="center", fontsize=11)
    fig.text(0.5, 0.025, "Original schematic • no scale • arrows show directions, not rates or stoichiometry",
             ha="center", fontsize=10, color="#555555")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
