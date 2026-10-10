"""Synthetic isotope and centrifugal-distortion comparisons, never measured CO data.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Stipulated inputs match the article, including integer atomic masses and fixed r.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


H = 6.62607015e-34
MASS_UNIT = 1.66053906660e-27
BOND_LENGTH = 1.13e-10
DISTORTION_RATIO = 0.001


def rotational_constant(m1, m2):
    reduced_mass = m1 * m2 / (m1 + m2) * MASS_UNIT
    inertia = reduced_mass * BOND_LENGTH**2
    return H / (8 * np.pi**2 * inertia)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "axes.spines.left": False,
                         "figure.facecolor": "white", "axes.facecolor": "white",
                         "savefig.facecolor": "white"})
    b_light = rotational_constant(12, 16) / 1e9
    b_heavy = rotational_constant(13, 16) / 1e9
    upper = np.arange(1, 6)
    light = 2 * b_light * upper
    heavy = 2 * b_heavy * upper
    distorted = light - 4 * DISTORTION_RATIO * b_light * upper**3
    fig, axes = plt.subplots(3, 1, figsize=(9.4, 6.2), sharex=True,
                             layout="constrained")
    for ax, values, color, title in zip(
            axes, [light, heavy, distorted],
            ["#20699b", "#167a64", "#be6034"],
            [rf"Rigid $^{{12}}$C$^{{16}}$O model: $B={b_light:.4f}$ GHz",
             rf"Rigid $^{{13}}$C$^{{16}}$O model: $B={b_heavy:.4f}$ GHz",
             r"Lighter form with stipulated distortion: $D/B=0.001$"]):
        ax.vlines(values, 0, 1, lw=2.8, color=color)
        ax.set(ylim=(0, 1.42), yticks=[])
        ax.set_title(title, loc="left", fontsize=11)
        for lower, frequency in enumerate(values):
            ax.text(frequency, 1.08, f"{lower} → {lower + 1}",
                    ha="center", fontsize=10, color=color)
        ax.grid(axis="x", color="#e6e6e6", lw=0.7)
        ax.set_axisbelow(True)
    for frequency, shifted in zip(light, distorted):
        axes[2].vlines(frequency, 0, 0.9, color="#7a7a7a", lw=1.4, ls="--")
        axes[2].annotate("", xy=(shifted, 0.48), xytext=(frequency, 0.48),
                         arrowprops={"arrowstyle": "->", "color": "#555555",
                                     "lw": 1.1, "shrinkA": 0, "shrinkB": 0})
    axes[2].text(12, 0.72, "Gray dashes:\nrigid model",
                 fontsize=10, va="center", color="#555555")
    axes[0].text(12, 0.62, "First line\n115.438 GHz", fontsize=10,
                 color="#20699b")
    axes[1].text(12, 0.62, "First line\n110.363 GHz", fontsize=10,
                 color="#167a64")
    axes[-1].set(xlim=(0, 615), xticks=np.arange(0, 601, 100),
                 xlabel="Calculated transition frequency (GHz)")
    fig.suptitle("Synthetic molecular rotation spectra: isotope and nonrigidity",
                 fontsize=14)
    fig.supxlabel("Stipulated masses 12u, 13u, 16u; r = 1.13 Å • Positions only, not measured spectra",
                  fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
