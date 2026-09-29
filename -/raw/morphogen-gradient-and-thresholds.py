"""Plot a toy exponential morphogen gradient and idealized fate bands.

Writes morphogen-gradient-and-thresholds.png to the current directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
All concentrations and parameters are illustrative, not measured Bicoid data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    c0, ell = 100.0, 100.0  # arbitrary concentration units; micrometres
    x = np.linspace(0.0, 350.0, 1000)
    boundaries = ell * np.log(c0 / np.array([50.0, 20.0]))
    colors = ["#d8e9f4", "#f8e5b9", "#e0eee4"]
    fig, (ax, bands) = plt.subplots(
        2, 1, figsize=(8.4, 5.8), sharex=True,
        gridspec_kw={"height_ratios": [3.5, 1.0]},
    )
    fig.subplots_adjust(left=0.12, right=0.97, top=0.85, bottom=0.19, hspace=0.18)
    fig.patch.set_facecolor("white")
    edges = [0.0, *boundaries, x[-1]]
    for i, (left, right) in enumerate(zip(edges[:-1], edges[1:])):
        ax.axvspan(left, right, color=colors[i])
        bands.axvspan(left, right, color=colors[i])
        bands.text((left + right) / 2, 0.68, f"Fate {'ABC'[i]}", ha="center", fontsize=11)
        bands.text((left + right) / 2, 0.29,
                   [r"$c\geq50$", r"$20\leq c<50$", r"$c<20$"][i],
                   ha="center", fontsize=11)
    ax.plot(x, c0 * np.exp(-x / ell), lw=2.6, color="#1f587e")
    for threshold, boundary in zip([50, 20], boundaries):
        ax.axhline(threshold, color="#555555", ls="--", lw=1)
        ax.axvline(boundary, color="#555555", ls=":", lw=1)
        ax.plot(boundary, threshold, "o", color="#1f587e", ms=6)
        ax.annotate(f"{boundary:.2f} µm", (boundary, threshold),
                    xytext=(12, 12), textcoords="offset points", fontsize=11,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
        bands.axvline(boundary, color="#777777", lw=1)
    ax.set(xlim=(0, 350), ylim=(0, 108), ylabel="Concentration (arbitrary units)")
    ax.set_yticks([0, 20, 50, 100])
    ax.set_title(r"$c(x)=100e^{-x/\ell},\quad\ell=100\ \mathrm{µm}$", fontsize=13)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=10)
    bands.set(ylim=(0, 1), yticks=[], xlabel="Distance from fixed-concentration source x (µm)")
    bands.spines[["left", "top", "right"]].set_visible(False)
    bands.set_xticks([0, 50, 100, 150, 200, 250, 300, 350])
    fig.suptitle("One smooth gradient, three idealized responses", fontsize=15, y=0.97)
    fig.text(0.5, 0.055, "Toy threshold rule; not measured Bicoid data. Domain continues beyond the plotted range.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
