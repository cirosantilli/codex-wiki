"""Draw an original explanatory cartoon; run from _media. Python 3.14, matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle


def arrow(ax, start, end, color, **kwargs):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=17,
                                linewidth=2, color=color, **kwargs))


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, (tank, mesh) = plt.subplots(1, 2, figsize=(10.4, 6.4), dpi=100,
                                    gridspec_kw={"width_ratios": [1.15, 1]})
    fig.patch.set_facecolor("white")
    fig.suptitle("DNA: electric charge sets direction; the gel enables separation", fontsize=16, y=.97)
    blue, red, teal = "#2563a6", "#b33438", "#047c83"
    for ax in (tank, mesh):
        ax.set_xlim(0, 7)
        ax.set_ylim(0, 7.3)
        ax.axis("off")

    tank.set_title("A. Horizontal gel apparatus (top view)", fontsize=13, pad=10)
    tank.add_patch(Rectangle((1.5, .65), 5.2, 5.8, facecolor="#edf5fa", edgecolor="#607d8b", lw=1.5))
    tank.text(4.1, 6.75, "Negative cathode  (−)", ha="center", color=blue, weight="bold")
    tank.plot([1.7, 6.5], [6.1, 6.1], color=blue, lw=5)
    tank.plot([1.7, 6.5], [1, 1], color=red, lw=5)
    tank.text(4.1, .18, "Positive anode  (+)", ha="center", color=red, weight="bold")
    tank.add_patch(Rectangle((2.15, 1.55), 3.9, 4, facecolor="#d5e8df", edgecolor="#7b9c89", lw=1.5))
    for x in (2.75, 4.1, 5.45):
        tank.add_patch(Rectangle((x-.32, 5.16), .64, .22, facecolor="white", edgecolor="#52705d"))
    tank.text(4.1, 5.78, "Wells: load samples here", ha="center", fontsize=11)
    tank.text(6.3, 3.6, "Buffer\ncovers\nthe gel", ha="center", va="center", fontsize=10)
    tank.text(4.1, 1.78, "Agarose gel", ha="center", fontsize=11)
    for y, c in [(4.35, "#6e4297"), (3.45, teal), (2.65, "#d08424")]:
        tank.plot([3.78, 4.42], [y, y], lw=5, color=c, solid_capstyle="butt")
    tank.text(2.35, 3.4, "Separated\nDNA bands", ha="left", va="center", fontsize=10)
    arrow(tank, (.35, 1.45), (.35, 5.5), red)
    tank.text(.10, 3.5, "Electric field E", rotation=90, ha="center", va="center", fontsize=11, color=red)
    arrow(tank, (1.05, 5.5), (1.05, 1.45), blue)
    tank.text(.81, 3.5, "DNA migration", rotation=90, ha="center", va="center", fontsize=11, color=blue)

    mesh.set_title("B. Same start, same elapsed time", fontsize=13, pad=10)
    mesh.text(3.5, 6.75, "Simplified porous mesh", ha="center", fontsize=11)
    for y in np.arange(1.2, 6, .65):
        x = np.linspace(.55, 6.2, 160)
        mesh.plot(x, y + .10*np.sin(4*x+y), color="#ccd8ce", lw=1.3)
    for x in np.arange(.7, 6.3, .65):
        y = np.linspace(1.1, 6, 160)
        mesh.plot(x + .09*np.sin(4*y+x), y, color="#ccd8ce", lw=1.3)
    mesh.plot([.5, 6.3], [5.95, 5.95], "--", color="#607d8b", lw=1)
    mesh.text(3.4, 6.15, "Common starting line", ha="center", fontsize=10)
    for x, end_y, color in [(2, 4.1, "#6e4297"), (4.8, 2.15, teal)]:
        arrow(mesh, (x, 5.78), (x, end_y+.35), color)
    t = np.linspace(0, 1, 100)
    mesh.plot(1.55 + .9*t, 4.0 + .15*np.sin(5*np.pi*t), color="#6e4297", lw=3)
    mesh.plot(4.57 + .46*t, 2.05 + .09*np.sin(2*np.pi*t), color=teal, lw=3)
    mesh.text(2, 3.5, "Longer linear DNA", ha="center", fontsize=10, color="#6e4297")
    mesh.text(4.8, 1.55, "Shorter linear DNA", ha="center", fontsize=10, color=teal)
    mesh.text(3.5, .45, r"Negative DNA: $\mathbf{F}=q\mathbf{E}$, $q<0$"+"\nForce opposes the electric field", ha="center", fontsize=12)
    fig.text(.5, .025, "Conceptual cartoon: mesh and chains are not to scale; positions are not measurements.",
             ha="center", fontsize=10, color="#455a64")
    fig.subplots_adjust(left=.055, right=.985, top=.86, bottom=.10, wspace=.20)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
