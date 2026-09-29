"""Draw an original uniaxial slab diagram; run from _media.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
The indices are stipulated model values, not measured calcite data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np


def arrow(ax, start, end, color, style="->", **kwargs):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                mutation_scale=13, color=color, lw=2, **kwargs))


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    blue, orange = "#1765a5", "#b74d0b"
    fig = plt.figure(figsize=(10, 6), layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=(1.35, 1))
    ax = fig.add_subplot(grid[0, :])
    ax.set(xlim=(-1.6, 7.3), ylim=(-1.1, 1.25))
    ax.axis("off")
    ax.add_patch(Rectangle((0, -.86), 4, 1.8, facecolor="#f0f4f7",
                           edgecolor="#858f98", lw=1.5))
    ax.text(2, 1.02, "Parallel slab; normal incidence", ha="center", weight="bold")
    # OA = (cos beta, sin beta) in this drawing. Rotate the exact
    # extraordinary dispersion gradient back to laboratory coordinates.
    no, ne, beta = 1.65, 1.49, np.pi / 4
    axis = np.array([np.cos(beta), np.sin(beta)])
    transverse = np.array([-np.sin(beta), np.cos(beta)])
    direction = axis * np.cos(beta) / no**2 - transverse * np.sin(beta) / ne**2
    slope = direction[1] / direction[0]
    shift = 4 * slope
    arrow(ax, (-1.4, .22), (0, .22), "#444444")
    ax.text(-1.5, .46, "Both components", fontsize=10)
    arrow(ax, (0, .22), (4, .22), blue)
    arrow(ax, (0, .22), (4, .22 + shift), orange)
    arrow(ax, (4, .22), (7, .22), blue)
    arrow(ax, (4, .22 + shift), (7, .22 + shift), orange)
    ax.text(4.5, .45, "Ordinary energy path", color=blue)
    ax.text(4.5, .22 + shift - .25, "Extraordinary energy path", color=orange)
    arrow(ax, (6.95, .22), (6.95, .22 + shift), "#444444", "<->")
    ax.text(7.1, .22 + shift / 2, "Shift", va="center", rotation=90, fontsize=10)
    arrow(ax, (.35, -.61), (1.32, .36), "#657849", "<->")
    ax.text(.3, -.8, "Tilted optic axis", color="#52663a", fontsize=10)
    arrow(ax, (2.4, .62), (3.15, .62), "#333333")
    ax.text(2.3, .78, r"$\mathbf{k}_o$, $\mathbf{k}_e$: face normal", fontsize=10)
    ax.text(2.2, -.53, r"$\mathbf{S}_e$: energy direction", color=orange, fontsize=10)
    ax.text(2.8, -1.03, "Exit rays parallel; paths displaced", ha="center", fontsize=10)

    left = fig.add_subplot(grid[1, 0])
    left.set(xlim=(-1.3, 1.3), ylim=(-1, 1), aspect="equal")
    left.axis("off")
    left.set_title("Two image channels (symbolic)", fontsize=12)
    left.text(-.58, .2, "F", color=blue, fontsize=46, ha="center")
    left.text(.58, .2, "F", color=orange, fontsize=46, ha="center")
    arrow(left, (-.85, -.24), (-.31, -.24), blue, "<->")
    arrow(left, (.58, -.52), (.58, .02), orange, "<->")
    left.text(-.58, -.8, "o: horizontal", ha="center", color=blue, fontsize=10)
    left.text(.58, -.8, "e: vertical", ha="center", color=orange, fontsize=10)

    right = fig.add_subplot(grid[1, 1])
    right.set(xlim=(-1.6, 1.6), ylim=(-1.25, 1.25), aspect="equal")
    right.axis("off")
    right.set_title("Exit polarizations; rotate analyzer", fontsize=12)
    right.add_patch(Circle((0, 0), .76, fill=False, edgecolor="#8b949d"))
    alpha = np.pi / 6
    p = .72 * np.array([np.cos(alpha), np.sin(alpha)])
    arrow(right, -p, p, "#333333", "<->")
    right.text(.92, .32, "Pass axis", fontsize=10)
    right.text(0, -1.05, r"$I_o \propto \cos^2\alpha$   $I_e \propto \sin^2\alpha$", ha="center")
    right.text(0, .98, "Axes drawn in the exit transverse plane", ha="center", fontsize=9)
    fig.suptitle("Birefringence: different polarizations, different energy paths", fontsize=15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
