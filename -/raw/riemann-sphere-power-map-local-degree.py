"""Draw the power-map schematic; run in _media with Python 3.14.

Uses matplotlib 3.10.7 and numpy 2.3.5. Output goes to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch


def main():
    plt.rcParams.update({"font.size": 12, "mathtext.fontset": "dejavusans"})
    fig = plt.figure(figsize=(10, 6), facecolor="white")
    ax = fig.add_axes((0.02, 0.04, 0.96, 0.86))
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis("off")
    blue, red = "#226b9a", "#b74339"
    fig.suptitle("Power map: two exceptional points, local degree d", fontsize=17, y=0.97)
    for x, label in [(2.3, "Source sphere X"), (7.7, "Target sphere Y")]:
        ax.add_patch(Circle((x, 4.55), 0.92, fill=False, lw=2, ec=blue))
        ax.add_patch(Ellipse((x, 4.55), 1.84, 0.42, fill=False, lw=1, ec=blue, ls="--"))
        ax.scatter([x, x], [3.63, 5.47], color=red, s=45, zorder=4)
        ax.text(x + 0.18, 5.53, r"$\infty$", color=red)
        ax.text(x + 0.18, 3.45, "0", color=red)
        ax.text(x, 5.82, label, ha="center", fontsize=13)
    ax.add_patch(FancyArrowPatch((3.5, 4.7), (6.5, 4.7), arrowstyle="->", mutation_scale=18, lw=2))
    ax.text(5, 5.05, r"$f(z)=z^d,\quad d\geq 2$", ha="center", fontsize=15)
    ax.text(5, 4.18, r"$e_0=e_\infty=d$", ha="center", color=red, fontsize=14)
    ax.text(5, 3.73, r"$R_f=(d-1)+(d-1)=2d-2$", ha="center", fontsize=14)
    ax.text(5, 3.13, "Local coordinate disks: illustrated for d = 3", ha="center", fontsize=13)
    theta = np.linspace(0, 2 * np.pi, 500)
    radius, angle = 0.8, 0.45
    roots = radius * np.exp(1j * (angle + 2 * np.pi * np.arange(3)) / 3)
    value = radius**3 * np.exp(1j * angle)
    for x in [2.3, 7.7]:
        ax.add_patch(Circle((x, 1.65), 1.08, fill=False, lw=1.2, ec=blue))
        ax.scatter([x], [1.65], color=red, s=35, zorder=4)
        ax.text(x + 0.13, 1.47, "0", color=red)
    ax.plot(2.3 + radius * np.cos(theta), 1.65 + radius * np.sin(theta), color=blue, lw=1, ls="--")
    ax.plot(7.7 + radius**3 * np.cos(theta), 1.65 + radius**3 * np.sin(theta), color=blue, lw=1, ls="--")
    ax.scatter(2.3 + roots.real, 1.65 + roots.imag, color=blue, s=45, zorder=5)
    ax.scatter([7.7 + value.real], [1.65 + value.imag], color=blue, s=45, zorder=5)
    ax.add_patch(FancyArrowPatch((3.65, 1.8), (6.35, 1.8), arrowstyle="->", mutation_scale=18, lw=2))
    ax.text(5, 2.2, r"$t\mapsto t^3$", ha="center", fontsize=16)
    ax.text(5, 1.18, "Three preimages of one\nnonzero nearby value", ha="center")
    ax.text(2.3, 0.27, "Near 0: t = z", ha="center")
    ax.text(7.7, 0.27, r"Near $\infty$: $t=1/z$, $v=1/f(z)$", ha="center")
    fig.text(0.5, 0.017, "Schematic sphere symbols and coordinate disks; no geometric embedding of the map is implied.", ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
