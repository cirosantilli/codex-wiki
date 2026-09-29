"""Draw original cylinder normals and bound-current geometry; emit a CWD PNG.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
The projected cylinder is a geometry schematic, not a computed field map.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Polygon
import numpy as np


BLUE, ORANGE, GRAY = "#17649b", "#bf5815", "#5a6269"


def arrow(ax, start, end, color, lw=2.1, size=15):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=size, color=color, lw=lw))


def main():
    plt.rcParams.update({"font.size": 12, "mathtext.fontset": "dejavusans"})
    fig, (side, end) = plt.subplots(1, 2, figsize=(10, 5.9), dpi=120)
    fig.patch.set_facecolor("white")
    fig.suptitle("Uniform magnetization: zero bulk current, circulating side current", fontsize=16, y=0.96)
    for ax in (side, end):
        ax.set_aspect("equal")
        ax.axis("off")
    side.set_xlim(-2.0, 2.5)
    side.set_ylim(-0.75, 4.45)
    side.set_title("Cylinder and outward normals", fontsize=14)
    r, h, squash = 0.9, 2.5, 0.30
    side.add_patch(Polygon([(-r, 0), (r, 0), (r, h), (-r, h)], closed=True, facecolor="#f3f8fc", edgecolor=GRAY, lw=1.4))
    side.add_patch(Ellipse((0, 0), 2 * r, 2 * squash, facecolor="white", edgecolor=GRAY, lw=1.4))
    for z in (0.65, 1.3, 1.95):
        t = np.linspace(0, 2 * np.pi, 240)
        side.plot(r * np.cos(t), z + squash * np.sin(t), color=ORANGE, lw=1.8)
        for t0 in (np.pi / 5, np.pi + np.pi / 5):
            p0 = (r * np.cos(t0), z + squash * np.sin(t0))
            p1 = (r * np.cos(t0 + 0.24), z + squash * np.sin(t0 + 0.24))
            arrow(side, p0, p1, ORANGE, size=13)
    side.add_patch(Ellipse((0, h), 2 * r, 2 * squash, facecolor="#f3f8fc", edgecolor=GRAY, lw=1.4))
    for x in (-0.42, 0.1, 0.58):
        arrow(side, (x, 0.45), (x, 1.92), BLUE, lw=2.5)
    side.text(-0.15, 1.12, r"$\mathbf{M}$", color=BLUE, fontsize=17, ha="right", bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    arrow(side, (0, h), (0, 3.38), GRAY)
    side.text(0.14, 3.33, r"$\mathbf{n}=+\widehat{\mathbf{z}}$", fontsize=13)
    arrow(side, (0, 0), (0, -0.56), GRAY)
    side.text(0.14, -0.5, r"$\mathbf{n}=-\widehat{\mathbf{z}}$", fontsize=13)
    arrow(side, (r, 1.3), (1.77, 1.3), GRAY)
    side.text(1.08, 1.55, r"$\mathbf{n}=\widehat{\mathbf{r}}$", fontsize=13)
    side.text(-1.55, 0.23, r"$\mathbf{J}_{\rm b}=0$", fontsize=14, color=GRAY)
    side.text(0.05, 4.03, r"Both endcaps: $\mathbf{M}\times\mathbf{n}=0$", ha="center", fontsize=13)
    end.set_xlim(-1.85, 1.85)
    end.set_ylim(-2.1, 2.18)
    end.set_title(r"End view from $+z$", fontsize=14)
    end.add_patch(Circle((0, 0), 1, facecolor="#f3f8fc", edgecolor=GRAY, lw=1.5))
    t = np.linspace(0, 2 * np.pi, 300)
    end.plot(np.cos(t), np.sin(t), color=ORANGE, lw=2)
    for t0 in np.arange(0, 2 * np.pi, np.pi / 3):
        arrow(end, (np.cos(t0), np.sin(t0)), (np.cos(t0 + 0.22), np.sin(t0 + 0.22)), ORANGE, size=16)
    end.add_patch(Circle((0, 0), 0.12, fill=False, color=BLUE, lw=2))
    end.plot(0, 0, "o", color=BLUE, ms=4)
    end.text(0, -0.45, r"$\mathbf{M}=M\widehat{\mathbf{z}}$", color=BLUE, ha="center", fontsize=14)
    end.text(0, -0.72, "Toward the viewer", color=BLUE, ha="center", fontsize=11)
    arrow(end, (1, 0), (1.62, 0), GRAY)
    end.text(1.12, -0.30, r"$\widehat{\mathbf{r}}$", color=GRAY, fontsize=14)
    arrow(end, (1, 0), (1, 0.74), ORANGE)
    end.text(1.2, 0.57, r"$\widehat{\boldsymbol{\phi}}$", color=ORANGE, fontsize=14)
    end.text(0, 1.58, r"Side: $\mathbf{K}_{\rm b}=M\widehat{\boldsymbol{\phi}}$", color=ORANGE, ha="center", fontsize=16)
    end.text(0, -1.55, r"$\widehat{\mathbf{z}}\times\widehat{\mathbf{r}}=\widehat{\boldsymbol{\phi}}$", ha="center", fontsize=16)
    fig.text(0.5, 0.047, "Blue: dipole moment per volume     Orange: equivalent surface current     Gray: outward normals", ha="center", fontsize=11)
    fig.subplots_adjust(left=0.025, right=0.985, bottom=0.13, top=0.83, wspace=0.10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
