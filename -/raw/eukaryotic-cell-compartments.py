"""Original compartment schematic; writes same-basename PNG in the CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
All sizes, positions and component counts are illustrative, not measurements.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse
import numpy as np


def label(ax, text, target, position, color="#243447", align="center"):
    ax.annotate(text, xy=target, xytext=position, ha=align, va="center",
                color=color, fontsize=11,
                arrowprops={"arrowstyle": "-", "color": color, "lw": 1.2})


def main():
    fig, ax = plt.subplots(figsize=(8.2, 5.6))
    fig.patch.set_facecolor("white")
    ax.add_patch(Ellipse((0, 0), 6.5, 4.2, facecolor="#eaf5fb",
                         edgecolor="#267e9e", lw=2.8))
    center = (-0.75, 0.15)
    ax.add_patch(Circle(center, 1.20, facecolor="#faf1ff",
                        edgecolor="#79519b", lw=2))
    ax.add_patch(Circle(center, 1.10, facecolor="#faf1ff",
                        edgecolor="#79519b", lw=1.7))
    x = np.linspace(-1.38, -0.18, 140)
    for offset in (0.73, 0.36, -0.37):
        ax.plot(x, offset + 0.085 * np.sin(12 * x), color="#9a64b2", lw=2)
    ax.add_patch(Circle((-0.83, -0.04), 0.22, facecolor="#c994db",
                        edgecolor="#79519b", lw=1))
    # An illustrative pore crosses both membranes at the right edge.
    ax.plot([0.32, 0.46], [0.22, 0.22], color="white", lw=9)
    ax.plot([0.30, 0.49], [0.30, 0.30], color="#4c5260", lw=3)
    ax.plot([0.30, 0.49], [0.13, 0.13], color="#4c5260", lw=3)
    ax.add_patch(Ellipse((1.75, -0.50), 1.25, 0.70, angle=18,
                         facecolor="#fff0cf", edgecolor="#b17816", lw=2))
    t = np.linspace(-0.44, 0.44, 120)
    ax.plot(1.75 + t, -0.50 + 0.18 * t + 0.13 * np.sin(22 * t),
            color="#b17816", lw=1.8)
    points = [(-2.45, 0.2), (-2.1, -0.95), (-0.25, -1.5), (0.9, 0.8),
              (1.75, 0.60), (2.45, 0.05), (0.70, -0.75)]
    ax.scatter(*zip(*points), s=45, color="#d16c31", zorder=5)
    label(ax, "Cell membrane", (1.8, 1.75), (2.35, 2.48), "#267e9e")
    label(ax, "Cell nucleus\n(excluded from cytoplasm)", (-1.10, 0.60),
          (-2.40, 2.50), "#79519b")
    label(ax, "DNA", (-0.70, 0.73), (-0.10, 1.84), "#79519b")
    label(ax, "Nuclear envelope\n(two membranes)", (-1.86, -0.20),
          (-3.90, -0.50), "#79519b")
    label(ax, "Nucleolus", (-0.83, -0.04), (-2.6, -2.38), "#79519b")
    label(ax, "Nuclear pore complex", (0.43, 0.22), (2.02, 1.34))
    label(ax, "Cytosol\n(pale blue)", (0.65, -1.25), (0.05, -2.40), "#267e9e")
    label(ax, "Mitochondrion", (1.9, -0.55), (2.83, -1.85), "#9d6b16")
    label(ax, "Free ribosomes\n(no enclosing membranes)", (1.75, 0.60),
          (3.62, 0.83), "#b65620")
    ax.set(xlim=(-4.8, 5.05), ylim=(-2.75, 2.9), aspect="equal")
    ax.axis("off")
    fig.suptitle("Cytoplasm includes cytosol and organelles", fontsize=15, y=0.97)
    fig.text(0.5, 0.08, "The nucleus is separate; organelle interiors are not cytosol.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.025, "Original schematic of a nucleated eukaryotic cell • not to scale • many structures omitted",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.14, top=0.90)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
