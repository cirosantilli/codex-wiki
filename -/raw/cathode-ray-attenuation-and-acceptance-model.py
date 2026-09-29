"""Plot a stipulated two-channel attenuation model, not electron transport data.

Python 3.14; matplotlib 3.10.7; numpy 2.3.5. Run from _media.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def fractions(x, removal=0.15, diversion=0.35):
    narrow = np.exp(-(removal + diversion) * x)
    wide = np.exp(-removal * x)
    return narrow, wide - narrow, 1 - wide


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    x = np.linspace(0, 6, 301)
    narrow, diverted, removed = fractions(x)
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.7, 5.2), facecolor="white")
    left.stackplot(x, narrow, diverted, removed,
                   colors=["#a6cee3", "#b2df8a", "#dddddd"],
                   labels=["Narrow U", "Diverted D", "Removed 1 − W"])
    left.plot(x, narrow, color="#1f78b4", lw=2)
    left.plot(x, narrow + diverted, color="#238443", lw=2)
    left.axvline(2, color="#555555", lw=1, ls="--")
    left.set(xlim=(0, 6), ylim=(0, 1), xlabel="Forward depth x (cm)", ylabel="Fraction of entering population",
             title="Population balance")
    left.legend(loc="upper right", fontsize=9, framealpha=1)
    for y, label in ((0.18, "U = 0.3679"), (0.55, "D = 0.3729"), (0.86, "1 − W = 0.2592")):
        left.text(2.10, y, label, fontsize=10,
                  bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9, "pad": 2})
    right.plot(x, -np.log(narrow), color="#1f78b4", lw=2.5,
               label=r"Narrow: $-\ln U=(a+b)x$")
    right.plot(x, -np.log(narrow+diverted), color="#238443", lw=2.5,
               label=r"Wide: $-\ln W=ax$")
    right.axvline(2, color="#555555", lw=1, ls="--")
    right.scatter([2, 2], [1, 0.3], c=["#1f78b4", "#238443"], s=45, zorder=4)
    right.annotate("1.00", (2, 1), xytext=(2.25, 1.02), color="#1f78b4")
    right.annotate("0.30", (2, 0.3), xytext=(2.25, 0.19), color="#238443")
    right.text(3.3, 1.95, r"Slope $a+b=0.50\ \mathrm{cm}^{-1}$", rotation=31,
               color="#1f78b4", fontsize=10)
    right.text(3.1, 0.68, r"Slope $a=0.15\ \mathrm{cm}^{-1}$", rotation=10,
               color="#238443", fontsize=10)
    right.set(xlim=(0, 6), ylim=(0, 3.2), xlabel="Forward depth x (cm)",
              ylabel="Negative natural logarithm of transmission", title="Two collection geometries give two slopes")
    right.legend(loc="upper left", fontsize=9)
    right.grid(alpha=0.18)
    fig.suptitle("Redistribution can look like removal to a narrow collector", fontsize=15, weight="bold")
    fig.text(0.5, 0.025, "Chosen toy rates: a = 0.15 cm⁻¹, b = 0.35 cm⁻¹ • no continuous slowing or channel return",
             fontsize=10, ha="center", color="#555555")
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.84, wspace=0.30)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
