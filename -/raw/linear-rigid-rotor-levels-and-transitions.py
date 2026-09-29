"""Dimensionless linear-rotor energy ladder and dipole-allowed line positions.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
All plotted quantities are exact model values; stick heights carry no intensity.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, (levels, spectrum) = plt.subplots(
        1, 2, figsize=(9.4, 5.5), gridspec_kw={"width_ratios": [1.3, 1]},
        layout="constrained")
    j = np.arange(5)
    energy = j * (j + 1)
    for quantum, value in zip(j, energy):
        levels.hlines(value, 0.05, 1.05, color="#243e63", linewidth=2.3)
        levels.text(1.1, value, f"J = {quantum}: {2 * quantum + 1} states",
                    va="center", fontsize=11)
    colors = ["#167b89", "#3665ad", "#916db1", "#c06c29"]
    for lower, color in zip(range(4), colors):
        x = 0.17 + 0.24 * lower
        y0, y1 = energy[lower:lower + 2]
        levels.annotate("", xy=(x, y1), xytext=(x, y0),
                        arrowprops={"arrowstyle": "->", "color": color,
                                    "lw": 2.4, "shrinkA": 3, "shrinkB": 3})
        levels.text(x + 0.04, (y0 + y1) / 2, f"{2 * (lower + 1)}hB",
                    color=color, va="center", fontsize=10)
    levels.set(xlim=(0, 2.42), ylim=(-1, 22), xticks=[],
               yticks=energy, ylabel=r"Energy $E_J/(hB)$",
               title=r"Levels: $J(J+1)$")
    levels.spines["bottom"].set_visible(False)
    for lower, color in zip(range(4), colors):
        frequency = 2 * (lower + 1)
        spectrum.vlines(frequency, 0, 1, color=color, lw=3)
        spectrum.text(frequency, 1.05, f"{lower} → {lower + 1}",
                      ha="center", color=color, fontsize=11)
    spectrum.annotate("", xy=(4, 0.7), xytext=(2, 0.7),
                      arrowprops={"arrowstyle": "<->", "color": "#333333"})
    spectrum.text(3, 0.76, r"spacing $2B$", ha="center", fontsize=11)
    spectrum.set(xlim=(0, 9.5), ylim=(0, 1.33), yticks=[],
                 xticks=[0, 2, 4, 6, 8], xlabel=r"Frequency $\nu/B$",
                 title=r"Absorption: $\Delta J=+1$")
    spectrum.spines["left"].set_visible(False)
    fig.suptitle("Linear rigid rotor: larger level gaps, regular spectral spacing",
                 fontsize=14)
    fig.supxlabel("Field-free spin-free model • Equal-height sticks show positions only",
                  fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
