"""Compare chosen exchange masses, decay lengths, and scalar suppression.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Inputs are illustrative, not a nuclear-potential fit. Run from _media.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


HBAR_C = 197.3  # Stipulated rounded MeV fm.
REST_ENERGIES = (70.0, 140.0, 280.0)  # Chosen MeV, not measured mass data.


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.3), layout="constrained")
    energies = np.linspace(45, 330, 700)
    axes[0].plot(energies, HBAR_C / energies, color="#666666", linewidth=1.7)
    r = np.linspace(0, 6, 700)
    colors = ("#16805d", "#006e9a", "#b74d14")
    for energy, color in zip(REST_ENERGIES, colors):
        length = HBAR_C / energy
        axes[0].scatter(energy, length, color=color, s=50, zorder=3)
        axes[0].annotate(f"{energy:g} MeV: {length:.3f} fm", (energy, length),
                         xytext=(7, 10), textcoords="offset points", color=color,
                         fontsize=10)
        axes[1].plot(r, np.exp(-r / length), color=color, linewidth=2.2,
                     label=fr"$mc^2={energy:g}$ MeV")
        axes[1].scatter([length], [np.exp(-1)], color=color, s=30, zorder=3)
    axes[0].set(xlabel=r"Chosen rest energy $mc^2$ (MeV)",
                ylabel=r"Decay length $\lambda$ (fm)", xlim=(40, 370),
                ylim=(0, 4.6), title=r"$\lambda = \hbar c/(mc^2)$")
    axes[1].axhline(np.exp(-1), color="#777777", linestyle=":", linewidth=1)
    axes[1].text(5.9, np.exp(-1) + 0.025, r"$e^{-1}$ at $r=\lambda$",
                 ha="right", color="#555555", fontsize=10)
    axes[1].set(xlabel=r"Separation $r$ (fm)", ylabel=r"Relative potential magnitude $e^{-r/\lambda}$",
                xlim=(0, 6), ylim=(0, 1.04), title="After dividing out the common 1/r")
    axes[1].legend(frameon=False)
    for ax in axes:
        ax.grid(alpha=0.2)
    fig.suptitle(r"Illustrative exchange fields: $\hbar c=197.3$ MeV fm", fontsize=14)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
