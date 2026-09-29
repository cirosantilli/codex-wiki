"""Original CO orbital schematic. Python 3.14; matplotlib, numpy.

Run in the output directory: writes paper-2-orbitals.png to cwd.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch

fig, axes = plt.subplots(1, 2, figsize=(11, 3.6), facecolor="white")
blue, orange = "#356ca5", "#dd9c45"
for ax in axes:
    ax.set(xlim=(-2.3, 2.6), ylim=(-1.5, 1.7), aspect="equal")
    ax.axis("off")
    ax.plot([-1.2, 1.3], [0, 0], color="0.75", lw=1)
    for x, name in [(-1.3, "M"), (0.9, "C"), (1.8, "O")]:
        ax.text(x, -0.2, name, ha="center", va="top", fontsize=14)
    ax.plot([1.05, 1.65], [0, 0], color="0.3", lw=2)

ax = axes[0]
ax.set_title(r"Occupied CO $5\sigma$ → empty metal orbital", fontsize=12)
ax.add_patch(Ellipse((-0.9, 0.35), 1.2, 0.55, fc=blue, alpha=0.6))
ax.add_patch(Ellipse((0.45, 0.35), 1.0, 0.55, fc=orange, alpha=0.8))
ax.text(0.45, 0.35, "+", ha="center", va="center", fontsize=15)
ax.annotate("", xy=(-0.8, 0.9), xytext=(0.65, 0.9),
            arrowprops=dict(arrowstyle="->", lw=2, color=orange))
ax.text(-0.1, -0.95, "End-on overlap; C is the donor end", ha="center", fontsize=10)

ax = axes[1]
ax.set_title(r"Occupied metal $d_\pi$ → CO $2\pi^*$", fontsize=12)
for x, y, phase in [(-1.65, .55, "+"), (-.95, .55, "−"),
                    (-1.65, -.55, "−"), (-.95, -.55, "+"),
                    (.9, .55, "−"), (.9, -.55, "+"),
                    (1.8, .55, "+"), (1.8, -.55, "−")]:
    ax.add_patch(Ellipse((x, y), .55, .75,
                        fc=blue if phase == "+" else orange, alpha=.72))
    ax.text(x, y, phase, ha="center", va="center", fontsize=14)
ax.add_patch(FancyArrowPatch((-.65, 1.15), (.65, 1.15),
                             arrowstyle="->", mutation_scale=13, lw=2, color=blue))
ax.text(0, -1.3, "Matching phases at M–C; opposite phases across C–O", ha="center", fontsize=9)
fig.text(.5, .02, "Orbital phases shown schematically; shapes and energies are not to scale.",
         ha="center", fontsize=10)
fig.tight_layout(rect=(0, .07, 1, 1))
fig.savefig("paper-2-orbitals.png", dpi=170, facecolor="white")
