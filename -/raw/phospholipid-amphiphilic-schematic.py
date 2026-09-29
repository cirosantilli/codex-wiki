"""Draw lipid regions, not an atomistic structure; write basename.png in cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Shapes and connectors are illustrative and do not encode chemical bonds.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np


def main():
    blue, orange, purple = "#236d99", "#bc6419", "#744299"
    fig, ax = plt.subplots(figsize=(9.6, 5.5))
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.12, top=0.88)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 10), ylim=(0, 5.6), aspect="equal")
    ax.axis("off")

    # Filled regions are intentionally unlike skeletal bond diagrams.
    ax.add_patch(FancyBboxPatch((3.7, 3.9), 2.6, 0.85,
                               boxstyle="round,pad=0.08,rounding_size=0.3",
                               facecolor="#d9edf6", edgecolor=blue, lw=2))
    ax.text(5, 4.32, "Phosphate-containing\nhead region", ha="center",
            va="center", fontsize=12, color=blue)
    ax.add_patch(FancyBboxPatch((4.05, 3.0), 1.9, 0.55,
                               boxstyle="round,pad=0.08,rounding_size=0.18",
                               facecolor="#ece1f4", edgecolor=purple, lw=2))
    ax.text(5, 3.28, "Glycerol scaffold", ha="center", va="center",
            fontsize=11, color=purple)
    ax.annotate("", (5, 3.66), (5, 3.84),
                arrowprops={"arrowstyle": "-", "color": "#888888",
                            "linestyle": ":", "lw": 1.5})
    for x in (4.25, 5.2):
        ax.add_patch(FancyBboxPatch((x, 0.6), 0.55, 2.25,
                                   boxstyle="round,pad=0.03,rounding_size=0.22",
                                   facecolor="#fbe3c3", edgecolor=orange, lw=2))
        ax.annotate("", (x + 0.275, 2.9), (x + 0.275, 2.97),
                    arrowprops={"arrowstyle": "-", "color": "#888888",
                                "linestyle": ":", "lw": 1.5})
    ax.annotate("Hydrophilic head\nPolar; interacts with water",
                (3.6, 4.32), (0.25, 4.15), fontsize=12, color=blue,
                va="center", arrowprops={"arrowstyle": "->", "color": blue})
    ax.annotate("Two fatty-acid-derived chains\nHydrophobic hydrocarbon regions",
                (5.95, 1.75), (6.4, 2.15), fontsize=11, color=orange,
                va="center", arrowprops={"arrowstyle": "->", "color": orange})
    ax.text(0.25, 1.85, "Typical two-acyl-chain\nglycerophospholipid\n\nOne illustrative subclass",
            fontsize=11, va="center", color="#333333")
    ax.text(7.9, 4.9, "Shorthand", ha="center", fontsize=11, color="#333333")
    for x in (7.68, 8.12):
        y = np.linspace(3.15, 4.14, 45)
        ax.plot(x + 0.055 * np.sin(8 * y), y, color=orange, lw=7,
                solid_capstyle="round")
    ax.add_patch(Circle((7.9, 4.36), 0.32, facecolor="#7db7d2",
                        edgecolor=blue, lw=1.5))
    fig.suptitle("A phospholipid can have two different affinities for water",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.055, "Regions and connectivity only: no atoms or exact bonds are shown.",
             ha="center", fontsize=11, color="#444444")
    fig.text(0.5, 0.015, "The phosphate-containing head is not always net negative.",
             ha="center", fontsize=10, color="#444444")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}: 1152 x 660 pixels")


if __name__ == "__main__":
    main()
