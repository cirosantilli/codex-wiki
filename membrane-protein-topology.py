"""Draw membrane attachment classes and a constructed crossing example.

Emits basename.png to CWD. Tested with Python 3.14, matplotlib 3.10.7,
and numpy 2.3.5. All geometry is schematic, with an opaque white background.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle


BLUE = "#286b94"
ORANGE = "#ae641e"
DARK = "#26333d"


def bilayer(ax, left, right):
    ax.add_patch(Rectangle((left, 0.39), right - left, 0.22,
                           facecolor="#f4e5bc", edgecolor="none"))
    ax.hlines([0.39, 0.61], left, right, color="#aa9151", lw=2)


def main():
    plt.rcParams.update({"font.size": 11, "text.color": DARK})
    fig = plt.figure(figsize=(10, 6.6), dpi=120, facecolor="white")
    grid = fig.add_gridspec(2, 4, left=0.035, right=0.975, bottom=0.13,
                           top=0.85, hspace=0.65, height_ratios=[1, 1.3])
    labels = ["Spanning chain", "Embedded on one side", "Lipid anchor", "Peripheral attachment"]
    for i, label in enumerate(labels):
        ax = fig.add_subplot(grid[0, i])
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis("off")
        bilayer(ax, 0.04, 0.96)
        if i == 0:
            ax.plot([0.29, 0.46, 0.57, 0.73], [0.82, 0.71, 0.28, 0.19],
                    color=BLUE, lw=8, solid_capstyle="round")
        elif i == 1:
            ax.add_patch(Ellipse((0.5, 0.68), 0.47, 0.30,
                                 facecolor=BLUE, edgecolor="white", lw=1))
        elif i == 2:
            ax.add_patch(Ellipse((0.5, 0.81), 0.45, 0.22,
                                 facecolor=BLUE, edgecolor="white", lw=1))
            ax.plot([0.50, 0.50, 0.62], [0.7, 0.55, 0.52], color=ORANGE, lw=4)
        else:
            ax.add_patch(Ellipse((0.5, 0.63), 0.31, 0.18,
                                 facecolor=BLUE, edgecolor="white", lw=1))
            ax.add_patch(Ellipse((0.5, 0.84), 0.51, 0.22,
                                 facecolor="#5e8965", edgecolor="white", lw=1))
            ax.plot([0.5, 0.5], [0.73, 0.76], ls=":", color=DARK, lw=2)
        ax.set_title(label, fontsize=11, pad=8)
    ax = fig.add_subplot(grid[1, :])
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    bilayer(ax, 0.17, 0.95)
    ax.text(0.01, 0.78, "Outside", va="center")
    ax.text(0.01, 0.24, "Cytosol", va="center")
    x = [0.20, 0.28, 0.33, 0.40, 0.47, 0.54, 0.61, 0.68, 0.75, 0.82, 0.91]
    y = [0.8, 0.8, 0.7, 0.29, 0.2, 0.29, 0.7, 0.8, 0.7, 0.29, 0.2]
    ax.plot(x, y, color=BLUE, lw=6, solid_capstyle="round", solid_joinstyle="round")
    ax.text(0.185, 0.89, "N", color=BLUE, weight="bold", ha="center")
    ax.text(0.93, 0.14, "C", color=BLUE, weight="bold", ha="center")
    for n, xpos in enumerate([0.365, 0.575, 0.785], 1):
        ax.text(xpos, 0.50, str(n), ha="center", va="center", weight="bold",
                bbox={"boxstyle": "circle,pad=0.24", "fc": "white", "ec": BLUE})
    ax.text(0.47, 0.065, "Inside loop", ha="center")
    ax.text(0.68, 0.96, "Outside loop", ha="center")
    fig.suptitle("Membrane proteins: attachment and sidedness", fontsize=16, y=0.97)
    fig.text(0.5, 0.905, "Cross-sections; chain paths are unscaled, not atomic structures",
             ha="center", fontsize=11)
    fig.text(0.5, 0.055, "Constructed example: three complete crossings switch outside → inside → outside → inside.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
