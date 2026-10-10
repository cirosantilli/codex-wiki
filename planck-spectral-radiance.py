"""Ideal wavelength spectra at three stipulated temperatures.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes planck-spectral-radiance.png into the current working directory.
Constants are exact SI values; this is a model, not measured data.
"""

import math

import matplotlib.pyplot as plt
import numpy as np


H = 6.62607015e-34  # J s
K_B = 1.380649e-23  # J/K
C = 299792458.0  # m/s


def positive_peak_root(exponent):
    """Bisect m(1-exp(-x))-x on [1,m], excluding its endpoint root at 0."""
    lo, hi = 1.0, float(exponent)
    for _ in range(100):
        mid = (lo + hi) / 2
        if exponent * (-math.expm1(-mid)) - mid > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def b_lambda(wavelength_m, temperature):
    return (2 * H * C**2 / wavelength_m**5
            / np.expm1(H * C / (wavelength_m * K_B * temperature)))


def main():
    x_peak = positive_peak_root(5)
    displacement = H * C / (K_B * x_peak)
    temperatures = (3000, 4500, 6000)
    peaks_um = np.array([displacement / t * 1e6 for t in temperatures])
    assert np.allclose(peaks_um, [0.9659239851, 0.6439493234, 0.4829619925])
    for t, peak_um in zip(temperatures, peaks_um):
        peak = peak_um * 1e-6
        assert b_lambda(peak, t) > b_lambda(peak * 0.99, t)
        assert b_lambda(peak, t) > b_lambda(peak * 1.01, t)
    wavelength_um = np.linspace(0.1, 3.0, 2200)
    wavelength_m = wavelength_um * 1e-6
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(9.4, 5.3), dpi=130)
    fig.subplots_adjust(left=0.115, right=0.965, bottom=0.19, top=0.84)
    fig.suptitle("Planck's law: temperature sets the whole spectrum", fontsize=16)
    for t, peak_um, color in zip(temperatures, peaks_um,
                                ("#a14b15", "#237850", "#245caa")):
        # B_lambda per metre -> per micrometre: multiply by 1e-6.
        radiance_per_um = b_lambda(wavelength_m, t) * 1e-6
        ax.plot(wavelength_um, radiance_per_um / 1e6, color=color, lw=2.6,
                label=f"{t} K  ·  peak {peak_um * 1000:.0f} nm")
        peak_y = b_lambda(peak_um * 1e-6, t) * 1e-6 / 1e6
        ax.plot(peak_um, peak_y, "o", ms=6, color=color)
        ax.vlines(peak_um, 0, peak_y, color=color, linestyle=":", lw=1.2)
    ax.set(xlim=(0.1, 3.0), ylim=(0, 35),
           xlabel="Wavelength λ (μm)",
           ylabel="Bλ (10⁶ W m⁻² sr⁻¹ μm⁻¹)")
    ax.set_xticks([0.1, 0.5, 1, 1.5, 2, 2.5, 3])
    ax.grid(alpha=0.18)
    ax.legend(frameon=False, loc="upper right", fontsize=12)
    fig.text(0.5, 0.035,
             "Ideal equilibrium spectra · markers maximize radiance per unit wavelength",
             ha="center", fontsize=11)
    fig.savefig("planck-spectral-radiance.png", facecolor="white", transparent=False)
    plt.close(fig)
    print(f"x_lambda={x_peak:.12f}; b={displacement:.12g} m K")
    for t, peak_um in zip(temperatures, peaks_um):
        print(f"T={t} K: lambda_peak={peak_um * 1000:.6f} nm; "
              f"B_lambda(0.5 um)={b_lambda(0.5e-6, t) * 1e-6:.6g} per um")


if __name__ == "__main__":
    main()
