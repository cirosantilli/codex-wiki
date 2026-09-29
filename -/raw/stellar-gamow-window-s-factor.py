"""Original reaction-window example; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes stellar-gamow-window-s-factor.png to the current directory.
All shapes are analytic toy curves, not measured energy distributions.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def model():
    kt = 8.617333262e-8 * 15e6  # keV
    eg = 493.0  # chosen rounded proton-proton Gamow energy, keV
    e0 = (eg * kt**2 / 4) ** (1 / 3)
    sigma = np.sqrt(2 * e0 * kt / 3)
    energy = np.linspace(0.002, 18, 16000)
    phi = energy / kt + np.sqrt(eg / energy)
    kernel = np.exp(-phi + 3 * e0 / kt)
    maxwell = np.sqrt(energy) * np.exp(-energy / kt)
    maxwell /= np.sqrt(kt / 2) * np.exp(-0.5)
    s_ratio = 1 + 5 * np.exp(-0.5 * ((energy - 10) / 0.7) ** 2)
    return kt, e0, sigma, energy, kernel, maxwell, s_ratio


def main():
    kt, e0, sigma, energy, kernel, maxwell, s_ratio = model()
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), layout="constrained")
    blue, orange, green = "#1768a2", "#c55a11", "#16806a"
    ax = axes[0]
    ax.plot(energy, maxwell, color=blue, label=r"Maxwell energy density: $\sqrt{E}e^{-E/kT}$")
    ax.plot(energy, kernel, color=orange, label=r"Constant-$S$ reaction kernel")
    ax.axvspan(e0 - np.sqrt(2) * sigma, e0 + np.sqrt(2) * sigma,
               color=orange, alpha=0.12, label=r"Gaussian full $e^{-1}$ window")
    ax.axvline(e0, color=orange, ls=":", lw=1.4)
    ax.text(e0 - 2.7, 1.07, rf"$E_0={e0:.2f}$ keV", color=orange)
    ax.set(title="Most particles are below the reaction window",
           xlabel="Relative kinetic energy E (keV)", ylabel="Each curve divided by its own peak",
           xlim=(0, 16), ylim=(0, 1.18))
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    ax = axes[1]
    ax.plot(energy, kernel, color=orange, label=r"Constant $S=S_0$")
    ax.plot(energy, s_ratio * kernel, color=green, label=r"Toy localized $S(E)$ enhancement")
    ax.axvline(10, color=green, ls=":", lw=1.3)
    ax.text(10.35, 2.32, "Chosen feature\nat 10 keV", color=green, fontsize=10)
    ax.set(title="Nuclear structure can change which energies matter",
           xlabel="Relative kinetic energy E (keV)",
           ylabel="Integrand / constant-S peak", xlim=(0, 16), ylim=(0, 2.7))
    ax.legend(loc="upper left", fontsize=9, frameon=False)
    for ax in axes:
        ax.grid(alpha=0.18)
    fig.suptitle(r"A Gamow window is a weighting kernel, not a particle histogram", fontsize=15)
    fig.supxlabel(r"Chosen p+p barrier, T = 15 MK; $S/S_0=1+5\exp[-(E-10)^2/(2\times0.7^2)]$ (E in keV)", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
