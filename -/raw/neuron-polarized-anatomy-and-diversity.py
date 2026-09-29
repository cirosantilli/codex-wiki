"""Original anatomy schematic; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media: python3 ../neuron-polarized-anatomy-and-diversity.py
Produces its own basename PNG in the current directory. No empirical image data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse
import numpy as np

BLUE = "#28628a"
ORANGE = "#b3541b"
GREEN = "#287a61"


def branch(ax, points, color=BLUE, width=3):
    xy = np.asarray(points)
    ax.plot(xy[:, 0], xy[:, 1], color=color, lw=width, solid_capstyle="round")


def arrow(ax, start, end, color=ORANGE, dashed=False):
    ax.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "->",
                "color": color, "lw": 2, "linestyle": "--" if dashed else "-"})


def main():
    fig = plt.figure(figsize=(10, 7.2), facecolor="white")
    ax = fig.add_axes((.04, .09, .92, .8))
    ax.set(xlim=(0, 12), ylim=(0, 8.4))
    ax.axis("off")
    fig.suptitle("Neuronal anatomy and signaling routes", fontsize=17, y=.98)
    fig.text(.5, .922, "Original schematic • illustrative shapes • not to scale",
             ha="center", fontsize=11, color="#555555")
    # The large neuron has one soma and a branching output axon.
    soma = np.array((3.2, 5.8))
    roots = [(2.8, 6.25), (2.6, 5.8), (2.8, 5.35), (3.3, 6.42)]
    splits = [(1.9, 6.9), (1.55, 5.8), (1.8, 4.6), (3.35, 7.3)]
    for i, (root, split) in enumerate(zip(roots, splits)):
        branch(ax, [soma, root, split])
        off = -.55 if i == 3 else -.85
        for dy in (-.38, .4):
            tip = (split[0] + off, split[1] + dy)
            branch(ax, [split, tip], width=2)
    ax.add_patch(Ellipse(soma, 1.45, 1.4, facecolor="#e4f1fa", edgecolor=BLUE, lw=2, zorder=3))
    ax.add_patch(Circle((3.18, 5.8), .28, facecolor="#d8c6eb", edgecolor="#705091", lw=1.5, zorder=4))
    branch(ax, [(3.9, 5.8), (4.8, 5.8)], ORANGE, 6)
    branch(ax, [(4.8, 5.8), (8.6, 5.8)], ORANGE, 3)
    terminals = [(10.65, 7), (10.8, 5.8), (10.65, 4.6)]
    for point in terminals:
        branch(ax, [(8.6, 5.8), (9.5, point[1]), point], ORANGE, 2)
        ax.add_patch(Circle(point, .12, facecolor=ORANGE, edgecolor=ORANGE))
        ax.add_patch(Ellipse((11.2, point[1]), .45, .55, facecolor="#e6f3ec", edgecolor=GREEN, lw=1.5))
    ax.text(.15, 8.05, "Dendrites", fontsize=12, color=BLUE)
    ax.text(3.2, 4.85, "Soma", ha="center", fontsize=12, color=BLUE)
    ax.annotate("Nucleus", xy=(3.18, 5.8), xytext=(4.1, 7.15), fontsize=11,
                arrowprops={"arrowstyle": "-", "color": "#705091"})
    ax.text(4.45, 4.8, "Axon initial\nsegment", ha="center", fontsize=11, color=ORANGE)
    ax.text(7.1, 6.05, "Axon", ha="center", fontsize=12, color=ORANGE)
    ax.text(10.2, 7.65, "Axon terminals", ha="center", fontsize=12, color=ORANGE)
    ax.text(11.2, 3.8, "Target cells", ha="center", fontsize=10, color=GREEN)
    arrow(ax, (1.35, 6.5), (2.45, 6.05))
    arrow(ax, (5.8, 5.4), (8, 5.4))
    ax.text(6.9, 4.9, "Usual output direction", fontsize=10, ha="center", color=ORANGE)
    arrow(ax, (5, 6.55), (2.6, 6.55), color=GREEN, dashed=True)
    ax.text(6.4, 6.75, "Possible active return into dendrites", ha="center", fontsize=10, color=GREEN)
    ax.plot((.2, 11.8), (3.65, 3.65), color="#dddddd", lw=1)
    # Small examples deliberately have different process arrangements.
    ax.text(2.85, 3.13, "Bipolar neuron", ha="center", fontsize=12)
    branch(ax, [(.8, 1.8), (2.55, 1.8)], BLUE, 3)
    branch(ax, [(.8, 1.8), (.3, 2.15)], BLUE, 2)
    branch(ax, [(.8, 1.8), (.3, 1.45)], BLUE, 2)
    ax.add_patch(Circle((2.85, 1.8), .32, facecolor="#e4f1fa", edgecolor=BLUE, lw=2))
    branch(ax, [(3.17, 1.8), (5.3, 1.8)], ORANGE, 3)
    arrow(ax, (1.3, 1.1), (4.5, 1.1))
    ax.text(1.5, 2.45, "Dendrite", ha="center", fontsize=10, color=BLUE)
    ax.text(4.3, 2.45, "Axon", ha="center", fontsize=10, color=ORANGE)
    ax.text(2.85, .45, "Soma lies between main processes", ha="center", fontsize=10)
    ax.text(9.05, 3.13, "Pseudounipolar neuron", ha="center", fontsize=12)
    branch(ax, [(6.5, 1.35), (11.55, 1.35)], ORANGE, 3)
    branch(ax, [(9, 1.35), (9, 2.3)], ORANGE, 2)
    ax.add_patch(Circle((9, 2.6), .3, facecolor="#e4f1fa", edgecolor=BLUE, lw=2))
    arrow(ax, (7, .9), (11, .9))
    ax.text(7.2, 1.85, "Peripheral\nbranch", ha="center", fontsize=10)
    ax.text(10.85, 1.85, "Central\nbranch", ha="center", fontsize=10)
    ax.text(9.05, .45, "Soma lies off the main transmission route", ha="center", fontsize=10)
    fig.text(.5, .025, "Compartment roles and signaling routes vary across neurons.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
