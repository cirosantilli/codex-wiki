"""Plot the applied-H derivative of a stipulated two-state moment model.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media; save the matching PNG basename to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

NUMBER_DENSITY = 1e26  # m^-3
MOMENT = 9.2740101e-24  # J/T, stipulated
BOLTZMANN = 1.380649e-23  # J/K
VACUUM_PERMEABILITY = 1.25663706e-6  # T m/A, rounded stipulated input


def susceptibility(b0, temperature):
    x = MOMENT * b0 / (BOLTZMANN * temperature)
    return (VACUUM_PERMEABILITY * NUMBER_DENSITY * MOMENT**2 /
            (BOLTZMANN * temperature) / np.cosh(x)**2)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))
    colors = ("#1464a0", "#cf6b17", "#208358")
    h = np.linspace(-1e7, 1e7, 1201)
    b0 = VACUUM_PERMEABILITY * h
    for temperature, color in zip((2.0, 4.0, 8.0), colors):
        axes[0].plot(h / 1e6, 1e4 * susceptibility(b0, temperature),
                     color=color, lw=2, label=f"T = {temperature:g} K")
    temperatures = np.linspace(0.2, 10.0, 1501)
    for bias, color in zip((0.0, 1.0, 4.0), colors):
        axes[1].plot(temperatures, 1e4 * susceptibility(bias, temperatures),
                     color=color, lw=2, label=fr"$B_0={bias:g}$ T")
    axes[0].set_title("Saturation suppresses the field slope")
    axes[0].set_xlabel(r"Applied $H$ (MA/m)")
    axes[1].set_title("Cooling: zero bias versus finite bias")
    axes[1].set_xlabel("Temperature T (K)")
    axes[1].set_ylim(0, 8)
    axes[1].annotate("Zero bias rises off scale", xy=(0.98, 7.99),
                     xytext=(2.2, 6.0), fontsize=9,
                     arrowprops={"arrowstyle": "->", "color": "0.35"})
    for ax in axes:
        ax.set_ylabel(r"$10^4\,\chi_{\mathrm{model}}$ (dimensionless)")
        ax.grid(alpha=0.18)
        ax.legend(loc="upper right", fontsize=10)
    fig.suptitle(r"Differential susceptibility $\chi_{\mathrm{model}}=\partial M/\partial H_{\mathrm{app}}$", fontsize=15)
    fig.subplots_adjust(left=0.085, right=0.985, bottom=0.22, top=0.80, wspace=0.28)
    fig.text(0.5, 0.035, r"Independent moments; stipulated $n=10^{26}$ m$^{-3}$ and $B_0=\mu_0H$. Calculated curves, not measurements.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
