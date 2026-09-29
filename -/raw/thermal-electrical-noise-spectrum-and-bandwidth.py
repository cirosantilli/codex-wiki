"""Original ideal resistor-noise spectra; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media; writes this script's basename with a .png extension.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    k_b, temperature, resistance, capacitance = 1.380649e-23, 300, 1e4, 1e-9
    corner = 1 / (2 * np.pi * resistance * capacitance)
    bandwidth = 1 / (4 * resistance * capacitance)
    frequency = np.linspace(0, 100e3, 2500)
    response = 1 / (1 + (frequency / corner) ** 2)
    spectrum = 4 * k_b * temperature * resistance
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.7), layout="constrained")
    fig.patch.set_facecolor("white")
    ax = axes[0]
    ax.plot(frequency / 1e3, np.full_like(frequency, spectrum * 1e18),
            color="#555555", linestyle="--", label="Open-circuit source")
    ax.plot(frequency / 1e3, spectrum * response * 1e18, color="#176a9b",
            linewidth=2.5, label="Voltage across C")
    ax.fill_between(frequency / 1e3, spectrum * response * 1e18,
                    color="#176a9b", alpha=.14)
    ax.set(xlabel="Frequency f (kHz)", ylabel=r"One-sided PSD ($\mathrm{nV^2/Hz}$)",
           title="Flat source, filtered output", xlim=(0, 100), ylim=(0, 190))
    ax.legend(loc="upper right", frameon=True, facecolor="white", framealpha=1)
    ax.text(.48, .47, "R = 10 kΩ\nC = 1 nF\nT = 300 K", transform=ax.transAxes,
            bbox={"facecolor": "white", "edgecolor": ".85", "pad": 7})
    ax = axes[1]
    ax.fill_between([0, bandwidth / 1e3], [1, 1], color="#d67b1f", alpha=.19)
    ax.plot([0, bandwidth / 1e3, bandwidth / 1e3, 100], [1, 1, 0, 0],
            color="#d67b1f", linestyle="--", linewidth=2, label="Equal-area rectangle")
    ax.fill_between(frequency / 1e3, response, color="#176a9b", alpha=.18)
    ax.plot(frequency / 1e3, response, color="#176a9b", linewidth=2.5,
            label=r"RC: $|H(f)|^2$")
    ax.axvline(corner / 1e3, ymax=.5 / 1.25, color="#176a9b", linestyle=":")
    ax.scatter([corner / 1e3], [.5], color="#176a9b", s=25)
    ax.annotate("Nominal corner\n15.915 kHz", xy=(corner / 1e3, .5),
                xytext=(40, .67), arrowprops={"arrowstyle": "->", "color": ".3"})
    ax.text(44, .37, r"$B_n=(\pi/2)f_c$" + "\n= 25.000 kHz", fontsize=12)
    ax.text(42, .14, "RC area includes the\ntail beyond this plot", color="#176a9b")
    ax.set(xlabel="Frequency f (kHz)", ylabel="Squared voltage gain",
           title="Noise bandwidth is an area", xlim=(0, 100), ylim=(0, 1.25))
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    fig.suptitle("Thermal noise: filter the PSD, then integrate", fontsize=15)
    fig.supxlabel("Original ideal-model calculation • no measured data", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")


if __name__ == "__main__":
    main()
