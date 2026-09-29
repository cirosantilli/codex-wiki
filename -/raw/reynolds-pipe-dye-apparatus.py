"""Draw the operating principle of Reynolds' pipe-and-dye experiment.

Original schematic, not a measured record or a scale reconstruction. Historical
principle verified against Reynolds (1883), sections 11, 21-23, pp. 941-956:
https://archive.org/stream/philtrans06508925/06508925_djvu.txt
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../reynolds-pipe-dye-apparatus.py
Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
The matching PNG basename is written to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np


def main():
    fig = plt.figure(figsize=(10.5, 7.2), facecolor="white")
    ax = fig.add_axes([0.04, 0.37, 0.92, 0.48])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5.5)
    ax.axis("off")
    wall, blue, dye = "#344454", "#1765a8", "#a02874"
    fig.suptitle("Reynolds' pipe-and-dye experiment", fontsize=19, weight="bold", y=0.97)
    fig.text(0.5, 0.91, "Historical operating principle • original schematic, not to scale",
             ha="center", fontsize=11)
    ax.add_patch(Rectangle((0.7, 1.2), 8.6, 3.3, facecolor="#edf5fa", edgecolor="none"))
    ax.plot([0.7, 0.7, 9.3, 9.3], [5, 1.2, 1.2, 5], color=wall, lw=2)
    ax.plot([0.7, 9.3], [4.5, 4.5], color=blue, lw=1.8)
    ax.plot([0.7, 9.3], [4.1, 4.1], color=blue, lw=1.2, ls="--")
    ax.text(2.5, 4.73, "settled water tank", fontsize=11)
    ax.add_patch(FancyArrowPatch((8.65, 4.5), (8.65, 4.1), arrowstyle="<->",
                                mutation_scale=12, color=wall))
    ax.text(6.2, 5.03, "time a calibrated level fall", fontsize=11)
    ax.annotate("", (8.64, 4.42), (7.75, 4.9), arrowprops={"arrowstyle": "->", "color": wall})
    # Transparent pipe is immersed in the tank. Bell mouth joins the bore smoothly.
    x = np.linspace(3.1, 3.9, 80)
    half_width = 0.26 + 0.50 * ((3.9 - x) / 0.8) ** 2
    ax.plot(x, 2.45 + half_width, color=wall, lw=2)
    ax.plot(x, 2.45 - half_width, color=wall, lw=2)
    ax.add_patch(Rectangle((3.9, 2.19), 5.9, 0.52, facecolor="white", edgecolor=wall, lw=2))
    ax.plot([1.65, 2.65, 2.95], [3.58, 3.58, 2.45], color=dye, lw=2)
    ax.add_patch(Rectangle((1.25, 3.3), 0.65, 0.60, facecolor="#f5deeb", edgecolor=dye, lw=1.5))
    ax.plot([2.95, 9.55], [2.45, 2.45], color=dye, lw=2)
    ax.text(1.08, 4.13, "dye reservoir", color=dye, fontsize=11)
    ax.annotate("small dye supply", (2.88, 2.67), (3.0, 0.50), fontsize=11, color=dye,
                arrowprops={"arrowstyle": "->", "color": dye})
    ax.annotate("smooth bell mouth", (3.55, 2.92), (3.10, 3.58), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": wall})
    ax.text(5.0, 3.0, "glass observation tube (internal diameter D)", fontsize=11)
    ax.annotate("", (7.45, 2.04), (5.25, 2.04), arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
    ax.text(5.58, 1.58, "flow to outlet", fontsize=11, color=blue)
    ax.plot([9.8, 10.55, 10.55], [2.71, 2.71, 0.15], color=wall, lw=2)
    ax.plot([9.8, 10.05, 10.05], [2.19, 2.19, 0.15], color=wall, lw=2)
    ax.plot([9.97, 10.64], [0.90, 0.90], color=wall, lw=3)
    ax.annotate("outlet\nvalve", (10.32, 0.90), (11.03, 1.65), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": wall})
    ax.plot([1.15, 1.15], [1.8, 2.75], color=blue, lw=3)
    ax.scatter([1.15], [1.72], color=blue, s=38)
    ax.annotate("check temperature\nat several depths", (1.15, 2.26), (0.02, 0.05), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": blue})
    fig.text(0.5, 0.36, r"Discharged volume $V$ in time $\Delta t$ → $Q=V/\Delta t$ → $U=4Q/(\pi D^2)$",
             ha="center", fontsize=12)

    # Conceptual observation windows: no simulation, concentration field or data.
    for bottom, turbulent in [(0.205, False), (0.075, True)]:
        panel = fig.add_axes([0.31, bottom, 0.62, 0.075])
        panel.set_xlim(0, 10)
        panel.set_ylim(-1, 1)
        panel.axis("off")
        panel.add_patch(Rectangle((0, -0.78), 10, 1.56, facecolor="white", edgecolor=wall, lw=1.5))
        if not turbulent:
            panel.plot([0.15, 9.8], [0, 0], color=dye, lw=2.4)
        else:
            panel.plot([0.15, 3.0], [0, 0], color=dye, lw=2.4)
            # Hand-designed curls symbolize spreading; they are not tracer paths.
            for centre, offset, width, amplitude, phase in [
                    (3.7, 0.10, 0.40, 0.34, 0.0), (4.3, -0.15, 0.35, 0.45, 0.8),
                    (5.1, 0.12, 0.57, 0.50, 1.6), (5.9, -0.08, 0.39, 0.39, 0.2),
                    (6.6, 0.13, 0.54, 0.47, 0.9), (7.5, -0.12, 0.63, 0.43, 1.8),
                    (8.4, 0.05, 0.44, 0.54, 0.5), (9.3, -0.10, 0.51, 0.41, 1.2)]:
                t = np.linspace(0, 2.5 * np.pi, 120)
                panel.plot(centre + width * np.cos(t + phase),
                           offset + amplitude * np.sin(t) * (0.6 + 0.4 * t / t[-1]),
                           color=dye, lw=1.4, alpha=0.85)
            panel.plot([3.0, 3.4], [0, 0.4], color=dye, lw=1.5)
        label = "Laminar: coherent band" if not turbulent else "Irregular spreading"
        fig.text(0.065, bottom + 0.034, label, fontsize=11, va="center")
    fig.text(0.5, 0.018, "Dye patterns are conceptual sketches, not measured traces. No universal transition value is implied.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
