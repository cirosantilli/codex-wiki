"""Original nuclear-envelope topology schematic; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, PathPatch, Rectangle
from matplotlib.path import Path as MplPath


fig, ax = plt.subplots(figsize=(10, 5.6), dpi=110, facecolor="white")
ax.set(xlim=(0, 10), ylim=(0, 5.6))
ax.axis("off")
blue, purple, orange = "#3975a5", "#70569b", "#cb6a22"
ax.text(5, 5.35, "One pore connects two aqueous compartments", ha="center", fontsize=17, weight="bold")
ax.text(.4, 4.8, "CYTOSOL", fontsize=13, color=blue, weight="bold")
ax.text(.4, .8, "CELL NUCLEUS", fontsize=13, color=purple, weight="bold")

# A single closed membrane band turns around the rim on either side of the pore.
# Its upper and lower arms are the outer and inner nuclear membranes.
for mirror in (False, True):
    vertices = [(.35, 3.45), (3.25, 3.45), (4.05, 3.45), (4.05, 2.15),
                (3.25, 2.15), (.35, 2.15), (.35, 2.33), (3.25, 2.33),
                (3.82, 2.33), (3.82, 3.27), (3.25, 3.27), (.35, 3.27), (.35, 3.45)]
    codes = [MplPath.MOVETO, MplPath.LINETO, MplPath.CURVE4, MplPath.CURVE4,
             MplPath.CURVE4, MplPath.LINETO, MplPath.LINETO, MplPath.LINETO,
             MplPath.CURVE4, MplPath.CURVE4, MplPath.CURVE4, MplPath.LINETO, MplPath.CLOSEPOLY]
    if mirror:
        vertices = [(10-x, y) for x, y in vertices]
    ax.add_patch(PathPatch(MplPath(vertices, codes), facecolor="#e6bd79", edgecolor="#92692a", linewidth=1.6))
ax.text(.55, 3.7, "Outer membrane", fontsize=11)
ax.text(.55, 1.9, "Inner membrane", fontsize=11)
ax.text(.55, 2.7, "Intermembrane space", fontsize=11, color="#795717")

for x in (3.67, 5.84):
    ax.add_patch(Rectangle((x, 1.95), .49, 1.7, facecolor="#c4b4df", edgecolor=purple, linewidth=1.5, zorder=3))
    ax.plot([x+.24, x+.1, x-.1], [3.65, 4.0, 4.15], color=purple, lw=2)
    ax.plot([x+.24, x+.3, x+.4], [3.65, 4.03, 4.15], color=purple, lw=2)
ax.plot([3.91, 4.4, 5.6, 6.08], [1.95, 1.5, 1.5, 1.95], color=purple, lw=2)
ax.text(6.65, 3.9, "Protein scaffold spans\nboth membranes", fontsize=11, color=purple)
ax.add_patch(FancyArrowPatch((6.6, 3.65), (6.1, 3.25), arrowstyle="->", color=purple, mutation_scale=12))
ax.text(6.7, 1.45, "Nuclear side", fontsize=11, color=purple)
ax.text(6.7, 4.5, "Cytosolic side", fontsize=11, color=blue)
for x, color, label in ((4.55, blue, "Diffusion"), (5.45, orange, "Receptor\n+ cargo")):
    ax.add_patch(FancyArrowPatch((x, 4.25), (x, 1.1), arrowstyle="<->", color=color, mutation_scale=17, lw=2))
    ax.text(x, .88, label, ha="center", va="top", fontsize=10, color=color)
ax.text(5, 2.8, "Aqueous\npassage", ha="center", va="center", fontsize=10,
        bbox=dict(facecolor="white", edgecolor="none", alpha=.95))
ax.text(5, .18, "Schematic: dimensions, shapes and transport arrows are illustrative", ha="center", fontsize=10, color="#555555")
fig.subplots_adjust(left=.02, right=.98, bottom=.02, top=.98)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
plt.close(fig)
