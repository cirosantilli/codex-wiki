"""Draw a local fluid bilayer schematic; write basename.png in cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Illustrative shapes and arrows do not specify atoms, bonds or measured motion.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    blue, orange = "#236d99", "#bc6419"
    fig, ax = plt.subplots(figsize=(9.6, 5.5))
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.13, top=0.89)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 10), ylim=(0, 5.8))
    ax.axis("off")
    ax.text(5, 5.45, "Water on this side", color=blue, ha="center", fontsize=13)
    ax.text(5, 0.3, "Water on this side too", color=blue, ha="center", fontsize=13)
    for i, x in enumerate(np.linspace(0.7, 9.3, 23)):
        for head, direction in ((3.85, -1), (1.85, 1)):
            for offset in (-0.055, 0.055):
                distance = np.linspace(0.12, 0.83, 35)
                wiggle = 0.022 * np.sin(10 * distance + 0.7 * i)
                ax.plot(x + offset + wiggle, head + direction * distance,
                        color=orange, lw=2.5, solid_capstyle="round", zorder=1)
            ax.add_patch(Circle((x, head), 0.125, facecolor="#7db7d2",
                                edgecolor=blue, lw=1, zorder=2))
    # Leave the individual regions visible; no solid-wall interior fill.
    ax.text(5, 2.84, "Hydrophobic interior: chains face one another",
            ha="center", va="center", fontsize=11, color=orange,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    ax.annotate("Hydrophilic heads", (1.8, 4.02), (0.65, 4.8),
                fontsize=12, color=blue,
                arrowprops={"arrowstyle": "->", "color": blue})
    ax.annotate("Hydrophilic heads", (1.8, 1.69), (0.65, 0.93),
                fontsize=12, color=blue,
                arrowprops={"arrowstyle": "->", "color": blue})
    for y, text_y in ((4.35, 4.65), (1.3, 0.9)):
        ax.annotate("", (7.8, y), (5.0, y),
                    arrowprops={"arrowstyle": "<->", "color": "#744299", "lw": 1.8})
        ax.text(6.4, text_y, "Motion within a fluid leaflet", ha="center",
                fontsize=11, color="#744299")
    fig.suptitle("A lipid bilayer: water-facing heads, sheltered chains",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.065, "Two opposing leaflets form a flexible, selective barrier.",
             ha="center", fontsize=11, color="#333333")
    fig.text(0.5, 0.025, "Local cross-section; unscaled symbols and arrows, not exact structures or rates.",
             ha="center", fontsize=10, color="#444444")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}: 1152 x 660 pixels")


if __name__ == "__main__":
    main()
