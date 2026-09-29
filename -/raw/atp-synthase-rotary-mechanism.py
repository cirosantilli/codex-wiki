"""Original functional schematic; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes an opaque PNG to the current directory.
Geometry is illustrative, not an atomic model or a measured trajectory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Ellipse, FancyArrowPatch, Rectangle
import numpy as np


BLUE = "#176b9a"
ORANGE = "#d56c1f"
GREEN = "#28754e"
INK = "#172c3c"
plt.rcParams.update({"font.size": 11, "text.color": INK, "font.family": "DejaVu Sans"})
fig = plt.figure(figsize=(11, 7.6), facecolor="white")
fig.suptitle("ATP synthase: two motors, one coupled rotor", fontsize=19, y=.97)
fig.text(.5, .915, "Synthesis direction • chosen c-ring size n = 10 • functional geometry, not to scale",
         ha="center", fontsize=11)


def arrow(ax, start, end, color=INK, **kwargs):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=15,
                               lw=2, color=color, **kwargs))


ax = fig.add_axes([.035, .1, .46, .77])
ax.set(xlim=(0, 10), ylim=(0, 11))
ax.axis("off")
ax.text(.1, 10.5, "SIDE VIEW", fontsize=12, weight="bold")
ax.add_patch(Rectangle((0, 6), 10, 2, fc="#eef2e0", ec="none"))
ax.plot([0, 10], [6, 6], color="#9baf85", lw=2)
ax.plot([0, 10], [8, 8], color="#9baf85", lw=2)
ax.text(.1, 7, "Lipid\nbilayer", va="center")
ax.text(.1, 9.6, "P: higher proton\nelectrochemical potential", color=BLUE)
ax.text(.1, 5.25, "N: synthesis side", color=BLUE)
# The cylindrical rotor is symbolized by an ellipse, not ten visible side faces.
ax.add_patch(Ellipse((5.1, 7), 3, 1.65, fc="#f5caa7", ec=ORANGE, lw=2))
ax.text(5.1, 7, "c-ring\nrotor", ha="center", va="center", color=INK)
ax.add_patch(Rectangle((6.7, 6.15), 1.25, 1.7, fc="#b9d8e5", ec=BLUE, lw=2))
ax.text(7.32, 7, "a", ha="center", va="center", fontsize=16)
ax.text(8.4, 7, "$F_0$", fontsize=17, va="center")
arrow(ax, (7.05, 9.5), (7.05, 7.85), BLUE)
arrow(ax, (7.65, 6.15), (7.65, 5.05), BLUE)
ax.text(7.5, 9.3, "H⁺ in", color=BLUE)
ax.text(7.25, 5.25, "H⁺ out", color=BLUE, ha="right")
# Central rotor and peripheral stationary support.
ax.plot([5.1, 5.1], [6.1, 2.5], color=ORANGE, lw=15, solid_capstyle="round")
ax.plot([7.9, 8.9, 8.9, 6.9], [6.6, 6.6, 1.3, 1.3], color=BLUE, lw=7)
ax.annotate("Peripheral stalk\n(stationary)", xy=(8.9, 4.5), xytext=(7.4, 3.5),
            ha="center", va="center", color=BLUE,
            arrowprops={"arrowstyle": "->", "color": BLUE})
ax.annotate("Central shaft γ\n(rotates)", xy=(5.1, 4.6), xytext=(.1, 4.0),
            arrowprops={"arrowstyle": "->", "color": ORANGE}, color=ORANGE)
for i, theta in enumerate(np.linspace(0, 2*np.pi, 6, endpoint=False)):
    x, y = 5.1+1.6*np.cos(theta), 1.9+.75*np.sin(theta)
    ax.add_patch(Ellipse((x, y), 1.3, 1.1, fc="#d3e7ef" if i % 2 == 0 else "#e0edcf",
                         ec=BLUE if i % 2 == 0 else GREEN, lw=1.6))
    ax.text(x, y, "α" if i % 2 == 0 else "β", ha="center", va="center", fontsize=16)
ax.text(1.65, 1.9, "$F_1$", fontsize=17, va="center")
ax.text(5.1, .25, "α₃β₃ head: three catalytic β sites", ha="center", color=GREEN)

top = fig.add_axes([.54, .47, .43, .4])
top.set(xlim=(-2, 3.3), ylim=(-1.6, 2))
top.set_aspect("equal")
top.axis("off")
top.text(-1.9, 1.7, "$F_0$ INSET: offset half-channels", weight="bold", fontsize=12)
top.add_patch(Circle((0, 0), 1, fill=False, ec=ORANGE, lw=8, alpha=.2))
for theta in np.linspace(0, 2*np.pi, 10, endpoint=False):
    top.add_patch(Circle((np.cos(theta), np.sin(theta)), .19, fc="#f5caa7", ec=ORANGE, lw=1.5))
top.text(0, 0, "10 c sites\nchosen example", ha="center", va="center", fontsize=10)
top.add_patch(Rectangle((1.2, -.78), .63, 1.7, fc="#d3e7ef", ec=BLUE))
top.text(1.5, .12, "a", ha="center", fontsize=15)
top.plot([2.9, 1.55, 1.55, .85], [1.2, 1.2, .65, .65], color=BLUE, lw=2)
arrow(top, (1.12, .65), (.82, .58), BLUE)
top.plot([1.02, 1.7, 1.7, 2.9], [-.02, -.02, -1.12, -1.12], color=BLUE, lw=2)
arrow(top, (2.45, -1.12), (2.95, -1.12), BLUE)
top.text(2.95, 1.35, "P → bind H⁺", ha="right", color=BLUE, fontsize=10)
top.text(3.1, -1.4, "release H⁺ → N", ha="right", color=BLUE, fontsize=10)
top.add_patch(Arc((0, 0), 2.75, 2.75, theta1=65, theta2=315, ec=ORANGE, lw=2))
arrow(top, (.87, -1.07), (1.08, -.87), ORANGE)

cat = fig.add_axes([.54, .09, .43, .33])
cat.axis("off")
cat.set(xlim=(0, 10), ylim=(0, 5))
cat.text(0, 4.55, "$F_1$: binding-change cycle at each β site", weight="bold", fontsize=12)
states = [(1.1, "Loose", "ADP + Pᵢ\nbind"), (4.7, "Tight", "Bound ATP\nfavoured"),
          (8.3, "Open", "ATP\nreleased")]
for x, name, desc in states:
    cat.add_patch(Ellipse((x, 3), 2.2, 1.1, fc="#e0edcf", ec=GREEN, lw=2))
    cat.text(x, 3, name, ha="center", va="center", weight="bold")
    cat.text(x, 1.9, desc, ha="center", va="center", fontsize=11)
arrow(cat, (2.3, 3), (3.5, 3), GREEN)
arrow(cat, (5.9, 3), (7.1, 3), GREEN)
cat.text(4.7, .5, "Three sites occupy different states at once.\nOne full turn → 3 ATP; ideal H⁺/ATP = 10/3.",
         ha="center", va="center", fontsize=11)
fig.text(.5, .025, "Blue: stationary support / proton routes    Orange: rotating assembly    Green: catalytic cycle",
         ha="center", fontsize=10)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130, facecolor="white")
plt.close(fig)
