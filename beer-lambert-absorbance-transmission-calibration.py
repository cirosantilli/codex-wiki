"""Draw an original Beer-Lambert calibration model, not measured material data.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
Run from the output directory; no input files are needed.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    epsilon, length = 8000.0, 1.0
    standards = np.array([0, 25, 50, 75, 100], dtype=float)
    concentration = np.linspace(0, 105, 500)
    absorbance = epsilon * length * concentration * 1e-6
    standard_absorbance = epsilon * length * standards * 1e-6
    transmission = 10.0 ** -absorbance
    reading = 0.4
    inferred_absorbance = -np.log10(reading)
    inferred_concentration = inferred_absorbance / (epsilon * length) * 1e6

    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.6), dpi=140, facecolor="white")
    fig.subplots_adjust(left=0.07, right=0.975, bottom=0.18, top=0.74, wspace=0.25)
    fig.suptitle("One calibration, two scales", fontsize=18, weight="bold", y=0.97)
    fig.text(0.5, 0.87, r"Stipulated model: $\varepsilon=8000\ \mathrm{L\,mol^{-1}\,cm^{-1}},\quad l=1\ \mathrm{cm}$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.04, "Circles: chosen standards   |   Diamond: stipulated T = 0.40 reading, c = 49.7425 μM",
             ha="center", fontsize=11)
    blue, orange, highlight = "#147a9a", "#b45019", "#6b3e91"
    data = [(absorbance, standard_absorbance, inferred_absorbance, blue,
             r"Absorbance $A$", r"$A=\varepsilon lc$"),
            (transmission, 10.0 ** -standard_absorbance, reading, orange,
             r"Transmittance $T=P/P_0$", r"$T=10^{-\varepsilon lc}$")]
    for ax, (curve, dots, value, color, ylabel, formula) in zip(axes, data):
        ax.plot(concentration, curve, color=color, linewidth=2.6)
        ax.scatter(standards, dots, s=48, color=color, edgecolor="white", zorder=3)
        ax.plot([inferred_concentration, inferred_concentration], [0, value],
                linestyle="--", color=highlight, linewidth=1.4)
        ax.plot([0, inferred_concentration], [value, value],
                linestyle="--", color=highlight, linewidth=1.4)
        ax.scatter([inferred_concentration], [value], marker="D", s=60,
                   color=highlight, edgecolor="white", zorder=4)
        ax.set(xlim=(-3, 105), ylim=(0, 1.04), xlabel="Concentration c (μM)", ylabel=ylabel,
               xticks=standards, yticks=np.arange(0, 1.01, 0.2))
        ax.grid(alpha=0.22)
        ax.spines[["top", "right"]].set_visible(False)
        ax.text(0.97, 0.93, formula, transform=ax.transAxes, ha="right", color=color, fontsize=14)
    axes[0].annotate("A = 0.397940", xy=(inferred_concentration, inferred_absorbance),
                     xytext=(59, 0.20), color=highlight, fontsize=11,
                     arrowprops={"arrowstyle": "-", "color": highlight})
    axes[1].annotate("T = 0.40", xy=(inferred_concentration, reading),
                     xytext=(60, 0.61), color=highlight, fontsize=11,
                     arrowprops={"arrowstyle": "-", "color": highlight})
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
