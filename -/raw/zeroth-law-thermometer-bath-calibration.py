"""Draw a bath comparison and constructed calibration, with opaque white output.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11.4, 5.0), dpi=110, facecolor="white")
    bath = fig.add_axes((.025, .16, .47, .68))
    plot = fig.add_axes((.60, .24, .36, .57))
    blue, orange, ink = "#2274a5", "#b55236", "#223344"
    bath.set(xlim=(0, 5), ylim=(0, 4))
    bath.axis("off")
    fig.text(.265, .93, "Compare probes in a common bath", ha="center",
             fontsize=15, weight="bold", color=ink)
    fig.text(.78, .93, "Assign a response scale", ha="center",
             fontsize=15, weight="bold", color=ink)

    bath.add_patch(Rectangle((.62, .66), 3.76, 1.96, facecolor="#e9f4fa",
                             edgecolor="none"))
    bath.plot([.6, .6, 4.4, 4.4], [3, .62, .62, 3], color=ink, linewidth=2)
    bath.plot([.62, 4.38], [2.62, 2.62], color=blue, linewidth=1.5)
    bath.add_patch(FancyBboxPatch((.58, .04), 3.84, .37,
                                  boxstyle="round,pad=.04", facecolor="#edf0f3",
                                  edgecolor=ink))
    bath.text(2.5, .225, "Stirrer on • heater off", ha="center", va="center", fontsize=11)
    for x, color, label in [(1.62, blue, "Reference"), (3.35, orange, "Test")]:
        bath.add_patch(FancyBboxPatch((x-.57, 3.30), 1.14, .42,
                                      boxstyle="round,pad=.05", facecolor="white",
                                      edgecolor=color, linewidth=1.5))
        bath.text(x, 3.51, label, ha="center", va="center", color=color, weight="bold")
        bath.plot([x, x], [3.25, 1.32], color=color, linewidth=4, solid_capstyle="round")
        bath.scatter([x], [1.32], s=70, color=color, zorder=4)
    bath.annotate("Tips clear\nof walls", xy=(3.34, 1.32),
                  xytext=(4.26, 1.93), ha="right", fontsize=10,
                  arrowprops={"arrowstyle": "->", "color": ink}, color=ink)
    bath.text(1.12, 2.22, "Water", ha="center", color=blue)
    bath.plot([2.05, 2.8], [.9, .9], color=ink, linewidth=6, solid_capstyle="round")
    bath.add_patch(FancyArrowPatch((1.94, .89), (2.81, 1.08),
                                   connectionstyle="arc3,rad=-.7", arrowstyle="->",
                                   color=blue, mutation_scale=14))
    bath.text(2.45, 1.59, "Gentle\nstirring", ha="center", color=blue, fontsize=11)
    fig.text(.265, .085, "Wait • apply reference correction • reverse reading order",
             ha="center", fontsize=10, color=ink)

    heights = np.linspace(12, 52, 200)
    temperatures = 40 * (heights - 12) / (52 - 12)
    plot.plot(heights, temperatures, color=blue, linewidth=2.5)
    plot.scatter([12, 52], [0, 40], s=70, color=blue, zorder=4, label="Reference inputs")
    plot.scatter([37], [25], s=80, color=orange, zorder=5)
    plot.plot([37, 37, 7], [-5, 25, 25], color=orange, linestyle="--", linewidth=1.2)
    plot.annotate("37 mm → 25 °C", xy=(37, 25), xytext=(24, 32),
                  color=orange, weight="bold", fontsize=11,
                  arrowprops={"arrowstyle": "->", "color": orange})
    plot.set(xlim=(7, 57), ylim=(-5, 45), xticks=[12, 22, 32, 37, 42, 52],
             yticks=[0, 10, 20, 25, 30, 40], xlabel="Column height X (mm)",
             ylabel="Assigned temperature (°C)")
    plot.tick_params(labelsize=10)
    plot.spines[["top", "right"]].set_visible(False)
    plot.grid(alpha=.2)
    fig.text(.78, .085, "Constructed values • linear response assumed", ha="center",
             fontsize=10, color=ink)
    fig.text(.5, .025, "Bath apparatus is schematic; calibration values are a separate worked example, not measured data.",
             ha="center", fontsize=10, color="#566575")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
