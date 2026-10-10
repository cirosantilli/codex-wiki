"""Plot pressure slices of PV = n_mol R T for one mole of ideal gas.

Writes ideal-gas-state-slices.png to the current working directory.
Tested with Python 3.14.4, Matplotlib 3.10.7, and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


GAS_CONSTANT = 8.31446261815324  # Exact SI value, J / (mol K).
AMOUNT_MOL = 1.0
REFERENCE_VOLUME = 0.025  # m^3.


def pressure_kpa(volume, temperature):
    return AMOUNT_MOL * GAS_CONSTANT * temperature / volume / 1000


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 5.2), dpi=120)
    fig.subplots_adjust(left=0.085, right=0.975, bottom=0.22,
                        top=0.79, wspace=0.31)
    fig.suptitle("One mole of ideal gas: two slices of the same state relation",
                 fontsize=15, y=0.965)
    fig.text(0.5, 0.89, r"$PV=n_{\rm mol}RT$     |     "
             r"$n_{\rm mol}=1\,\mathrm{mol}$     |     "
             r"$R=8.31446261815324\,\mathrm{J/(mol\,K)}$", ha="center")
    blue, orange, green = "#226a9a", "#b35427", "#267849"

    volume = np.linspace(0.01, 0.065, 500)
    for temperature, color in zip((150, 300, 600), (green, blue, orange)):
        left.plot(volume, pressure_kpa(volume, temperature), color=color,
                  lw=2.3, label=f"T = {temperature} K")
    left.set(title="Hold temperature fixed", xlabel=r"Volume $V$ (m$^3$)",
             ylabel=r"Absolute pressure $P$ (kPa)",
             xlim=(0.01, 0.065), ylim=(0, 515))
    left.set_xticks([0.01, 0.025, 0.05, 0.065])
    left.legend(loc="upper right", frameon=False, fontsize=10)
    p_reference = pressure_kpa(REFERENCE_VOLUME, 300)
    p_expanded = pressure_kpa(2 * REFERENCE_VOLUME, 300)
    left.scatter([REFERENCE_VOLUME, 2 * REFERENCE_VOLUME],
                 [p_reference, p_expanded], color=blue, s=38, zorder=5)
    left.annotate(f"0.025 m³\n{p_reference:.3f} kPa",
                  xy=(REFERENCE_VOLUME, p_reference), xytext=(0.017, 235),
                  arrowprops={"arrowstyle": "->", "color": blue}, fontsize=10)
    left.annotate(f"0.050 m³\n{p_expanded:.3f} kPa",
                  xy=(2 * REFERENCE_VOLUME, p_expanded), xytext=(0.046, 135),
                  arrowprops={"arrowstyle": "->", "color": blue}, fontsize=10)

    temperature = np.linspace(150, 650, 500)
    right.plot(temperature, pressure_kpa(REFERENCE_VOLUME, temperature),
               color=blue, lw=2.3)
    extrapolated = np.linspace(0, 150, 100)
    right.plot(extrapolated, pressure_kpa(REFERENCE_VOLUME, extrapolated),
               color=blue, lw=1.6, ls="--", alpha=0.55)
    right.set(title=r"Hold volume fixed: $V=0.025$ m$^3$",
              xlabel=r"Absolute temperature $T$ (K)",
              ylabel=r"Absolute pressure $P$ (kPa)",
              xlim=(0, 650), ylim=(0, 235))
    right.set_xticks([0, 150, 300, 450, 600])
    right.scatter([300, 600], [p_reference, 2 * p_reference],
                  color=[blue, orange], s=38, zorder=5)
    right.annotate(f"300 K\n{p_reference:.3f} kPa", xy=(300, p_reference),
                   xytext=(80, 125), fontsize=10,
                   arrowprops={"arrowstyle": "->", "color": blue})
    right.annotate(f"600 K\n{2 * p_reference:.3f} kPa", xy=(600, 2 * p_reference),
                   xytext=(375, 200), fontsize=10,
                   arrowprops={"arrowstyle": "->", "color": orange})
    right.text(65, 20, "Formal\nextrapolation", color="#555555", fontsize=9)

    for ax in (left, right):
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.29, 0.10, "Double V at fixed T: halve P", ha="center", color=blue)
    fig.text(0.755, 0.10, "Double T in kelvin at fixed V: double P",
             ha="center", color=blue)
    fig.text(0.5, 0.035,
             "Model state slices; extrapolation to zero temperature does not imply real-gas validity.",
             ha="center", fontsize=10, color="#555555")
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
