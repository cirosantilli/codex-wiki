"""Draw a historical apparatus sequence and an explicitly separate ideal model.

Run from _media; tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Historical apparatus: Gerlach and Stern (1922), experimental setup and Fig. 1,
in Martin Bauer's translation https://arxiv.org/html/2301.11343v1.
The drawings are original schematics, not reproductions or measured data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon, Rectangle
import numpy as np


MASS = 1.79e-25
MU_B = 9.274e-24
GRADIENT = 300.0
LENGTH = 0.035
DRIFT = 0.100
SPEED = 500.0


def displacement(x):
    """Positive-channel z in metres, from magnet entrance x=0."""
    x = np.asarray(x)
    a = MU_B * GRADIENT / MASS
    return np.where(x <= LENGTH, a * x**2 / (2 * SPEED**2),
                    a * LENGTH * (x - LENGTH / 2) / SPEED**2)


def draw():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(11, 7), facecolor="white")
    fig.suptitle("Stern–Gerlach: apparatus and an ideal flight model", fontsize=17, y=.975)
    top = fig.add_axes((.04, .56, .92, .32))
    top.set(xlim=(0, 11), ylim=(-1.15, 1.4))
    top.axis("off")
    top.text(0, 1.25, "1922 sequence · schematic, not to scale", fontsize=13, weight="bold")
    top.add_patch(Rectangle((.15, -.5), 1.1, 1.0, facecolor="#fff0d8", edgecolor="#9a6020", lw=2))
    top.text(.7, 0, "heated\nAg oven", ha="center", va="center")
    top.text(.7, -.75, "neutral atoms", ha="center", fontsize=10)
    for x, label in [(2.7, "pinhole"), (4.2, "narrow slit")]:
        for z in [-.7, .07]:
            top.add_patch(Rectangle((x, z), .07, .63, color="#555555"))
        top.text(x, .9, label, ha="center")
    top.annotate("two platinum apertures", (3.5, -.85), ha="center", fontsize=10)
    top.plot([1.25, 4.5], [0, 0], color="#555555", lw=2)
    top.add_patch(FancyArrowPatch((1.4, 0), (2.5, 0), arrowstyle="->", mutation_scale=14))
    top.add_patch(Rectangle((4.7, -.48), 3.3, .96, facecolor="#e7eef5", edgecolor="#678197", lw=1.5))
    top.text(6.35, .92, "nonuniform magnet", ha="center")
    top.text(6.35, -.78, "3.5 cm along knife-edge pole", ha="center", fontsize=10)
    top.plot([4.25, 8.1], [0, 0], color=".65", lw=1, ls=":")
    beam_x = np.linspace(4.25, 8.1, 150)
    for sign, color in [(1, "#186a9c"), (-1, "#bc5732")]:
        top.plot(beam_x, sign * .22 * ((beam_x - 4.25) / 3.85)**2, color=color, lw=1.8)
    top.add_patch(Rectangle((8.1, -.55), .11, 1.1, facecolor="#d3e4e6", edgecolor="#465d63"))
    for z, color in [(.22, "#186a9c"), (-.22, "#bc5732")]:
        top.plot([8.1, 8.21], [z, z], color=color, lw=3)
    top.text(8.5, .05, "glass plate\nat magnet exit\n(silver deposit)", va="center")
    top.text(.1, -1.12, "Pumped vacuum throughout; field-off exposure provides the spatial baseline.", fontsize=10)
    # Transverse cross-section inset, not a longitudinal drawing of a wedge.
    inset = fig.add_axes((.82, .84, .12, .095))
    inset.set(xlim=(0, 1), ylim=(0, 1)); inset.axis("off")
    inset.add_patch(Rectangle((.08, .78), .84, .18, color="#8295a7"))
    inset.add_patch(Polygon([[.15, .02], [.85, .02], [.5, .55]], color="#8295a7"))
    inset.plot(.5, .65, "o", color="#bd4c32", markersize=4)
    inset.text(1.04, .5, "pole\nsection", fontsize=9, va="center")
    ax = fig.add_axes((.09, .14, .83, .30))
    end = LENGTH + DRIFT
    x = np.linspace(0, end, 400)
    ax.axvspan(0, LENGTH * 100, color="#e7eef5", zorder=0)
    ax.axhline(0, color=".65", lw=1, ls=":")
    for sign, color in [(1, "#186a9c"), (-1, "#bc5732")]:
        ax.plot(x * 100, sign * displacement(x) * 1000, color=color, lw=2.5)
    ax.axvline(LENGTH * 100, color=".5", lw=1, ls="--")
    ax.axvline(end * 100, color="#465d63", lw=3)
    ax.text(.6, .24, r"constant $G$, length $\ell$", fontsize=10)
    ax.text(7.0, .03, r"drift $D$; $F_z=0$", fontsize=11, ha="center")
    ax.text(end * 100 + .15, .20, r"$+\mu_B$", color="#186a9c", va="center")
    ax.text(end * 100 + .15, -.20, r"$-\mu_B$", color="#bc5732", va="center")
    ax.set(xlim=(-.15, 14.5), ylim=(-.31, .31), xlabel="Forward distance from magnet entrance (cm)",
           ylabel="Displacement z (mm)")
    ax.set_title("Chosen model · parabolic paths in magnet, straight paths during drift", loc="left", fontsize=12, pad=14)
    ax.grid(axis="y", alpha=.2)
    fig.text(.09, .035, "Hypothetical: M = 1.79 × 10⁻²⁵ kg, G = 300 T/m, ℓ = 3.5 cm, D = 10 cm, v = 500 m/s.\n"
             "Predicted separation = 0.511 mm. Extra drift and plotted trajectories are not a reconstruction of the 1922 data.", fontsize=10)
    path = Path(Path(__file__).stem + ".png")
    fig.savefig(path, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    draw()
