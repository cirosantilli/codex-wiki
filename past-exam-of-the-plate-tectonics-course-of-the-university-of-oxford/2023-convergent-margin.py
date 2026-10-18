"""Original subduction schematic; Python 3.14.4, Matplotlib 3.10.7.

Run from any directory: the opaque PNG is written to the current directory.
Geometry is illustrative, not a measured section or a reproduction of a source.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    fig, ax = plt.subplots(figsize=(9.6, 5.4), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 100), ylim=(-69, 19))
    ax.set_facecolor("white")
    ax.axis("off")
    ax.add_patch(Polygon([(0, -69), (100, -69), (100, -18), (0, -18)], facecolor="#f7d8b1"))
    # Incoming plate bends into a coherent descending slab.
    slab_top = [(0, -2), (25, -2), (32, -6), (44, -20), (65, -47), (79, -65)]
    slab_bottom = [(69, -69), (55, -52), (33, -24), (23, -18), (0, -18)]
    ax.add_patch(Polygon(slab_top + slab_bottom, closed=True, facecolor="#a0b6c9", edgecolor="#425c71", lw=1.4))
    ax.plot([0, 25, 32, 44, 65, 79], [-4, -4, -8, -22, -49, -67], color="#314c64", lw=3)
    # Upper plate, crust and a deliberately exaggerated volcano.
    surface = [(33, -3), (43, -1), (51, 1), (62, 2), (69, 13), (76, 3), (100, 3)]
    ax.add_patch(Polygon(surface + [(100, -24), (50, -24)], facecolor="#d8c2a2", edgecolor="#61554a", lw=1.2))
    ax.plot([47, 100], [-12, -12], color="#61554a", lw=1.2)
    ax.add_patch(Polygon([(31, -6), (35, 0), (44, -1), (44, -20)], facecolor="#e6d393", edgecolor="#8f7845", lw=1.0))
    for i in range(3):
        ax.plot([33 + 3*i, 37 + 3*i], [-4 - 3*i, -1], color="#8f7845", lw=1)
    ax.plot([0, 26, 30, 33], [1, 1, -5, -3], color="#167b9a", lw=2)
    ax.fill_between([0, 25], [-2, -2], [1, 1], color="#bce3ef")
    # Magma ascent, slab fluids and earthquake band.
    for x, y in [(49, -28), (55, -36), (61, -43)]:
        ax.annotate("", (x + 5, y + 13), (x, y), arrowprops={"arrowstyle": "->", "color": "#147d9a", "lw": 1.6})
    ax.annotate("", (69, 10), (63, -19), arrowprops={"arrowstyle": "->", "color": "#c34630", "lw": 3})
    ax.add_patch(Polygon([(58, -22), (64, -14), (70, -22)], facecolor="#e99b72", edgecolor="#c34630"))
    ax.scatter([40, 48, 56, 64, 72], [-16, -26, -36, -47, -57], marker="*", s=45, c="#b32432", zorder=8)
    ax.add_patch(FancyArrowPatch((88, -37), (64, -39), connectionstyle="arc3,rad=-0.45", arrowstyle="->", mutation_scale=14, color="#a56d34", lw=1.8))
    ax.annotate("", (23, -11), (7, -11), arrowprops={"arrowstyle": "->", "color": "#283d51", "lw": 2})
    ax.annotate("", (82, -6), (94, -6), arrowprops={"arrowstyle": "->", "color": "#61554a", "lw": 2})
    labels = [
        ("Oceanic crust + mantle\nmove toward trench", (13, -6), (1, 12)),
        ("Trench", (30, -5), (29, 10)),
        ("Accretionary prism", (37, -6), (38, 17)),
        ("Forearc basin", (49, 0), (47, 9)),
        ("Volcanic arc", (69, 12), (78, 16)),
        ("Continental crust", (89, -1), (77, 7)),
        ("Moho", (93, -12), (91, -20)),
        ("Overriding lithospheric mantle", (85, -18), (72, -29)),
        ("Hot mantle wedge\n+ partial melting", (64, -19), (77, -47)),
        ("Slab dehydration: H₂O rises", (56, -31), (18, -41)),
        ("Earthquakes within\nand along the cold slab", (56, -36), (8, -54)),
        ("Dense slab sinks; oceanic\nlithosphere is recycled", (70, -57), (49, -65)),
    ]
    for text, xy, pos in labels:
        ax.annotate(text, xy, xytext=pos, fontsize=9.2, ha="left", va="center", arrowprops={"arrowstyle": "-", "lw": 0.8, "color": "#555555"}, bbox={"facecolor": "white", "alpha": 0.88, "edgecolor": "none", "pad": 1.4})
    fig.suptitle("Ocean–continent convergence: recycling and new arc crust", fontsize=13, y=0.98)
    fig.text(0.02, 0.025, "Original schematic • not to scale • blue arrows: fluids; red arrow: magma", fontsize=9)
    fig.subplots_adjust(left=0.015, right=0.985, top=0.91, bottom=0.08)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
