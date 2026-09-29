"""Plot original normalized Gaussian count spectra, never measured material data.

Run from _media; Python 3.14, numpy 2.3.5, matplotlib 3.10.7. No SciPy.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def density(x, center, sigma):
    return np.exp(-.5 * ((x - center) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    x = np.linspace(280, 291, 4401)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), sharey=True, facecolor="white")
    for ax, sigma, heading in zip(axes, [.25, 1.0], ["Narrow response: two maxima", "Broad response: one maximum"]):
        a = .75 * density(x, 284, sigma)
        b = .25 * density(x, 286, sigma)
        ax.plot(x, a + b, color="#223b55", lw=2.3, label="Sum of components")
        ax.plot(x, a, "--", color="#287d8e", lw=1.6, label="A: count weight 0.75")
        ax.plot(x, b, "--", color="#bd6816", lw=1.6, label="B: count weight 0.25")
        ax.fill_between(x, 0, a, color="#287d8e", alpha=.09)
        ax.fill_between(x, 0, b, color="#bd6816", alpha=.09)
        ax.axvline(284.5, color="#8a478b", lw=1.4, linestyle=":", label="Centroid: 284.5 eV")
        ax.set(xlim=(281, 289), ylim=(0, 1.38), xlabel="Binding energy relative to common $E_F$ (eV)")
        ax.set_title(heading + f"\nComponent σ = {sigma:.2f} eV", fontsize=12)
        ax.grid(axis="y", alpha=.18)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(loc="upper right", fontsize=8.8, frameon=False)
    axes[0].set_ylabel("Normalized count density (eV⁻¹)")
    axes[0].annotate("A", (284, .75 / (.25 * np.sqrt(2 * np.pi))), xytext=(283.4, 1.29), color="#287d8e")
    axes[0].annotate("B", (286, .25 / (.25 * np.sqrt(2 * np.pi))), xytext=(286.12, .47), color="#bd6816")
    axes[1].text(.95, .44, "Same centers and count weights\nCentroid unchanged\nVariance: 0.8125 → 1.7500 eV²", transform=axes[1].transAxes,
                 ha="right", va="top", color="#536879", fontsize=10)
    fig.suptitle("Chemical shift and overlap: arbitrary normalized data", fontsize=15, y=.98)
    fig.text(.5, .035, "Not a measured spectrum. Chosen centers: 284 and 286 eV; count weights are not mole fractions.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.075, right=.98, bottom=.17, top=.78, wspace=.12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
