"""Draw a conceptual ER cross-section; run from _media to emit the PNG.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(9.6, 5.4), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis("off")
    membrane = "#235579"
    lumen = "#d7eef7"
    ribosome = "#bd6a30"

    # All centerlines form one connected lumen, not separate sacs.
    segments = [
        (np.array([0.9, 4.5]), np.array([y, y])) for y in (2.0, 3.25, 4.5)
    ]
    segments.append((np.array([4.5, 4.5]), np.array([2.0, 4.5])))
    t = np.linspace(0, 1, 160)
    for end_y in (1.6, 3.25, 4.7):
        x = 4.5 + 4.3 * t
        y = 3.25 + (end_y - 3.25) * t + 0.22 * np.sin(2 * np.pi * t)
        segments.append((x, y))
    x = 6.2 + 1.4 * t
    y0 = np.interp(6.2, segments[4][0], segments[4][1])
    y = y0 + (0.7 - y0) * t
    segments.append((x, y))
    for x, y in segments:
        ax.plot(x, y, color=membrane, lw=22, solid_capstyle="round", zorder=1)
    for x, y in segments:
        ax.plot(x, y, color=lumen, lw=16, solid_capstyle="round", zorder=2)

    for y in (2.0, 3.25, 4.5):
        for x in np.linspace(1.2, 3.8, 7):
            for side in (-1, 1):
                ax.plot([x, x], [y + side * 0.20, y + side * 0.27],
                        color=ribosome, lw=1.6, zorder=3)
                ax.add_patch(Circle((x, y + side * 0.32), 0.08,
                                    facecolor=ribosome, edgecolor="#733611", zorder=4))

    ax.text(5, 5.8, "One ER network, two regional appearances", ha="center",
            fontsize=18, weight="bold", color="#173e58")
    ax.text(2.5, 5.25, "Rough region", ha="center", fontsize=14, weight="bold")
    ax.text(7.65, 5.25, "Smooth region", ha="center", fontsize=14, weight="bold")
    ax.text(7.7, 5.0, "No attached ribosomes", ha="center", fontsize=11)
    ax.annotate("Ribosomes on the cytosolic surface", xy=(1.2, 1.68),
                xytext=(0.65, 1.22), ha="left", va="top", fontsize=11,
                arrowprops={"arrowstyle": "-", "color": ribosome})
    ax.annotate("Continuous lumen", xy=(4.5, 3.25), xytext=(5.4, 4.5),
                ha="center", fontsize=12, color=membrane,
                arrowprops={"arrowstyle": "->", "color": membrane,
                            "connectionstyle": "arc3,rad=-0.2"})
    ax.annotate("ER membrane", xy=(8.3, 1.59), xytext=(8.0, 0.8),
                ha="center", fontsize=12, color=membrane,
                arrowprops={"arrowstyle": "->", "color": membrane})
    ax.text(2.5, 0.65, "Cytosol surrounds the network", ha="center", fontsize=12)
    ax.text(5, 0.16, "Conceptual cross-section • not fluorescence or electron microscopy • not to scale",
            ha="center", fontsize=10, color="#505050")
    fig.subplots_adjust(left=0.025, right=0.975, top=0.975, bottom=0.04)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
