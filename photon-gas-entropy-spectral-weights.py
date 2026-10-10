"""Original analytic two-polarization photon spectra; no measurement data.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: the PNG is written into CWD, using this script's stem.
Exact SI constants, vacuum dispersion E=h*nu, chemical potential zero.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


H = 6.62607015e-34  # J s
K_B = 1.380649e-23  # J/K
C = 299792458.0  # m/s
ZETA_3 = 1.2020569031595943
TEMPERATURE = 2.725  # K, stipulated illustration, not a fitted measurement


def energy_spectrum(frequency_hz, temperature):
    """Stored radiation energy per volume per Hz, including both polarizations."""
    return (8 * np.pi * H * frequency_hz**3 / C**3
            / np.expm1(H * frequency_hz / (K_B * temperature)))


def spectral_fractions(x):
    """Fractions of total photon number and energy per dimensionless dx."""
    occupation = 1 / np.expm1(x)
    return (x**2 * occupation / (2 * ZETA_3),
            15 * x**3 * occupation / np.pi**4)


def main():
    a_r = 8 * np.pi**5 * K_B**4 / (15 * H**3 * C**3)
    u = a_r * TEMPERATURE**4
    n = 16 * np.pi * ZETA_3 * (K_B * TEMPERATURE / (H * C))**3
    # Broad-domain numerical checks are independent of the plotting window.
    x_check = np.linspace(1e-7, 60, 180001)
    f_n, f_u = spectral_fractions(x_check)
    assert np.isclose(np.trapezoid(f_n, x_check), 1, rtol=1e-8)
    assert np.isclose(np.trapezoid(f_u, x_check), 1, rtol=1e-8)
    nu_check = x_check * K_B * TEMPERATURE / H
    assert np.isclose(np.trapezoid(energy_spectrum(nu_check, TEMPERATURE),
                                 nu_check) / u, 1, rtol=1e-8)
    mean_x = np.trapezoid(x_check * f_n, x_check)
    assert np.isclose(mean_x, u / (n * K_B * TEMPERATURE), rtol=1e-8)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.6, 4.7), dpi=110)
    fig.subplots_adjust(left=0.085, right=0.975, bottom=0.19, top=0.78, wspace=0.30)
    fig.suptitle("Photon gas: spectral energy and photon counting", fontsize=16, y=0.97)
    fig.text(0.5, 0.89, "Analytic equilibrium model · two polarizations · μγ = 0",
             ha="center", fontsize=11)
    blue, orange = "#2265a3", "#bb5a1b"
    nu_ghz = np.linspace(0.001, 650, 2200)
    # Per Hz -> per GHz; the plotted ordinate is in units of 1e-16 J m^-3 GHz^-1.
    per_ghz = energy_spectrum(nu_ghz * 1e9, TEMPERATURE) * 1e9
    left.plot(nu_ghz, per_ghz / 1e-16, color=blue, lw=2.5)
    left.fill_between(nu_ghz, per_ghz / 1e-16, color=blue, alpha=0.12)
    left.set(xlim=(0, 650), ylim=(0, 1.8), xlabel="Frequency ν (GHz)",
             ylabel="Energy density per GHz\n(10⁻¹⁶ J m⁻³ GHz⁻¹)",
             title=f"Stipulated T = {TEMPERATURE} K")
    left.text(0.97, 0.91, "Full spectral integral:\n"
              f"u = {u / 1e-14:.4f} × 10⁻¹⁴ J m⁻³",
              transform=left.transAxes, ha="right", va="top", fontsize=10)
    left.grid(alpha=0.18)

    x = np.linspace(0.001, 12, 1800)
    f_n, f_u = spectral_fractions(x)
    right.plot(x, f_n, color=orange, lw=2.5, label="Photon number fraction")
    right.plot(x, f_u, color=blue, lw=2.5, label="Energy fraction")
    right.set(xlim=(0, 12), ylim=(0, 0.31), xlabel=r"Scaled frequency x = hν / (k$_B$T)",
              ylabel="Fraction per unit x", title="Same photons, different weights")
    right.legend(loc="upper right", frameon=False, fontsize=10)
    right.text(0.97, 0.60, "Each full integral = 1\n\nMean photon energy:\n"
               r"2.7012 k$_B$T",
               transform=right.transAxes, ha="right", va="top", fontsize=10)
    right.grid(alpha=0.18)
    fig.text(0.5, 0.045, "Original model curves, not FIRAS data · integrals extend to infinite frequency",
             ha="center", fontsize=10)
    output = Path(__file__).with_suffix('.png').name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"{output}: a_R={a_r:.12g}; u={u:.12g}; n_gamma={n:.12g}; mean_x={mean_x:.12g}")


if __name__ == "__main__":
    main()
