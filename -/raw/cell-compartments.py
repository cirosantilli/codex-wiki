"""Original cellular-organization schematic; writes basename.png to the cwd.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Diagrams are illustrative, not microscopy or drawings to scale.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


def label(ax, text, target, position, color="#273445"):
    ax.annotate(text, xy=target, xytext=position, ha="center", va="center",
                fontsize=10, color=color,
                arrowprops={"arrowstyle": "-", "color": color, "lw": 1})


def main():
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 4.4))
    fig.set_facecolor("white")
    theta = np.linspace(0, 2 * np.pi, 300)
    ribosomes = [(-1.1, 0.28), (-0.7, 0.75), (0.9, 0.65),
                 (1.22, 0.1), (0.65, -0.6), (-0.78, -0.65),
                 (-1.2, -0.28), (0.25, -0.86)]
    for ax, nucleated in zip(axes, (False, True)):
        ax.add_patch(Ellipse((0, 0), 3.3, 2.35, facecolor="#eef7fb",
                             edgecolor="#247ba0", lw=3))
        if nucleated:
            ax.add_patch(Ellipse((0, 0.04), 1.45, 1.35,
                                 facecolor="#faf5fd", edgecolor="#80718c", lw=2))
            x = np.linspace(-0.42, 0.42, 200)
            for offset in (0.35, 0.02, -0.31):
                y = offset + 0.08 * np.sin(3 * np.pi * x / 0.84)
                ax.plot(x, y, color="#8b4eaa", lw=2)
            label(ax, "Nucleus boundary", (0.56, 0.46), (1.0, 1.73), "#655772")
        else:
            x = 0.67 * np.cos(theta) + 0.12 * np.cos(5 * theta)
            y = 0.38 * np.sin(theta) + 0.1 * np.sin(4 * theta)
            ax.plot(x, y, color="#8b4eaa", lw=2)
            ax.text(0, 1.73, "No membrane around DNA", ha="center", fontsize=10)
        ax.scatter(*zip(*ribosomes), s=25, color="#c26b18", zorder=4)
        label(ax, "Cell membrane", (-1.52, 0.45), (-1.03, 1.38), "#247ba0")
        label(ax, "Cytoplasm", (1.2, -0.3), (1.02, -1.45))
        label(ax, "Ribosomes", (-0.78, -0.65), (-1.02, -1.45), "#995017")
        label(ax, "DNA", (0.0, -0.32), (0, -1.0), "#8b4eaa")
        ax.set(xlim=(-2, 2), ylim=(-1.8, 2.1), aspect="equal")
        ax.axis("off")
    axes[0].set_title("Typical prokaryotic cell", fontsize=12)
    axes[1].set_title("Typical nucleated eukaryotic cell", fontsize=12)
    fig.suptitle("A shared cellular plan, different compartments", fontsize=14)
    fig.text(0.5, 0.065, "Membrane • cytoplasm • DNA • ribosomes", ha="center", fontsize=12)
    fig.text(0.5, 0.02, "Original schematics; not to scale; additional structures omitted", ha="center", fontsize=9)
    fig.tight_layout(rect=(0, 0.10, 1, 0.94))
    fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
