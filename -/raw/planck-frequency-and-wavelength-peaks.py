"""One 6000 K Planck spectrum in frequency and wavelength coordinates.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes planck-frequency-and-wavelength-peaks.png into the working directory.
Peak equations use standard-library bisection, with no SciPy dependency.
"""

import math

import matplotlib.pyplot as plt
import numpy as np


H = 6.62607015e-34
K_B = 1.380649e-23
C = 299792458.0
TEMPERATURE = 6000.0


def positive_peak_root(exponent):
    lo, hi = 1.0, float(exponent)
    for _ in range(100):
        mid = (lo + hi) / 2
        if exponent * (-math.expm1(-mid)) - mid > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def b_nu(frequency_hz):
    return (2 * H * frequency_hz**3 / C**2
            / np.expm1(H * frequency_hz / (K_B * TEMPERATURE)))


def b_lambda(wavelength_m):
    return (2 * H * C**2 / wavelength_m**5
            / np.expm1(H * C / (wavelength_m * K_B * TEMPERATURE)))


def main():
    x_nu, x_lambda = (positive_peak_root(m) for m in (3, 5))
    nu_peak = x_nu * K_B * TEMPERATURE / H
    lambda_peak = H * C / (K_B * TEMPERATURE * x_lambda)
    converted_lambda = C / nu_peak
    converted_nu = C / lambda_peak
    assert math.isclose(converted_lambda * 1e6, 0.84990713825, rel_tol=1e-10)
    assert math.isclose(lambda_peak * 1e6, 0.482961992531, rel_tol=1e-10)

    # Check both density transformation and equal power in matching finite bands.
    band_lambda = np.linspace(0.4e-6, 0.8e-6, 20001)
    assert np.allclose(b_lambda(band_lambda),
                       b_nu(C / band_lambda) * C / band_lambda**2,
                       rtol=5e-14, atol=0)
    band_nu = np.linspace(C / band_lambda[-1], C / band_lambda[0], 20001)
    wavelength_integral = np.trapezoid(b_lambda(band_lambda), band_lambda)
    frequency_integral = np.trapezoid(b_nu(band_nu), band_nu)
    assert math.isclose(wavelength_integral, frequency_integral, rel_tol=1e-8)
    for peak, density in ((nu_peak, b_nu), (lambda_peak, b_lambda)):
        assert density(peak) > density(peak * 0.99)
        assert density(peak) > density(peak * 1.01)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (freq_ax, wave_ax) = plt.subplots(1, 2, figsize=(11.2, 5.7), dpi=120)
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.26, top=0.79, wspace=0.34)
    fig.suptitle("Same 6000 K radiation: the peak depends on spectral coordinates",
                 fontsize=15)
    blue, orange = "#245caa", "#a14b15"
    nu_thz = np.linspace(1, 1500, 2400)
    lambda_um = np.linspace(0.1, 3, 2400)
    # Per Hz -> per THz multiplies by 1e12; per m -> per um by 1e-6.
    freq_ax.plot(nu_thz, b_nu(nu_thz * 1e12) * 1e12 / 1e4, color=blue, lw=2.6)
    wave_ax.plot(lambda_um, b_lambda(lambda_um * 1e-6) * 1e-6 / 1e6,
                 color=orange, lw=2.6)
    freq_ax.set(title="Equal-width frequency bins", xlim=(0, 1500), ylim=(0, 11),
                xlabel="Frequency ν (THz)", ylabel="Bν (10⁴ W m⁻² sr⁻¹ THz⁻¹)")
    wave_ax.set(title="Equal-width wavelength bins", xlim=(0.1, 3), ylim=(0, 36),
                xlabel="Wavelength λ (μm)", ylabel="Bλ (10⁶ W m⁻² sr⁻¹ μm⁻¹)")
    for ax, own, other, own_y, other_y, color in (
        (freq_ax, nu_peak / 1e12, converted_nu / 1e12,
         b_nu(nu_peak) * 1e12 / 1e4, b_nu(converted_nu) * 1e12 / 1e4, blue),
        (wave_ax, lambda_peak * 1e6, converted_lambda * 1e6,
         b_lambda(lambda_peak) * 1e-6 / 1e6,
         b_lambda(converted_lambda) * 1e-6 / 1e6, orange),
    ):
        ax.vlines(own, 0, own_y, color=color, linestyle=":", lw=1.3)
        ax.plot(own, own_y, "o", color=color, ms=7)
        ax.vlines(other, 0, other_y, color="#555b62", linestyle="--", lw=1.4)
        ax.plot(other, other_y, "o", mfc="white", mec="#555b62", ms=7)
        ax.grid(alpha=0.18)
    freq_ax.annotate(f"Bν peak\n{nu_peak / 1e12:.3f} THz",
                     (nu_peak / 1e12, b_nu(nu_peak) * 1e12 / 1e4),
                     xytext=(17, 6), textcoords="offset points", color=blue)
    wave_ax.annotate(f"Bλ peak\n{lambda_peak * 1e6:.6f} μm",
                     (lambda_peak * 1e6, b_lambda(lambda_peak) * 1e-6 / 1e6),
                     xytext=(20, 4), textcoords="offset points", color=orange)
    freq_ax.annotate("c / λpeak\n620.737 THz", (converted_nu / 1e12,
                     b_nu(converted_nu) * 1e12 / 1e4), xytext=(35, -10),
                     textcoords="offset points", color="#555b62",
                     arrowprops={"arrowstyle": "-", "color": "#555b62"})
    wave_ax.annotate(f"c / νpeak\n{converted_lambda * 1e6:.6f} μm",
                     (converted_lambda * 1e6, b_lambda(converted_lambda) * 1e-6 / 1e6),
                     xytext=(65, 8), textcoords="offset points", color="#555b62",
                     arrowprops={"arrowstyle": "-", "color": "#555b62"})
    fig.text(0.5, 0.115, r"$B_\lambda = B_\nu(c/\lambda)\,c/\lambda^2$", ha="center",
             fontsize=16)
    fig.text(0.5, 0.045,
             "Filled dots: each panel's maximum · open dots: the other peak, converted",
             ha="center", fontsize=11)
    fig.savefig("planck-frequency-and-wavelength-peaks.png", facecolor="white",
                transparent=False)
    plt.close(fig)
    print(f"x_nu={x_nu:.12f}; x_lambda={x_lambda:.12f}")
    print(f"nu_peak={nu_peak / 1e12:.9f} THz; lambda_peak={lambda_peak * 1e6:.9f} um")
    print(f"c/nu_peak={converted_lambda * 1e6:.9f} um; "
          f"c/lambda_peak={converted_nu / 1e12:.9f} THz")
    print(f"0.4–0.8 um band: {wavelength_integral:.9g} W m^-2 sr^-1; "
          f"relative coordinate-integral difference "
          f"{abs(wavelength_integral / frequency_integral - 1):.3g}")


if __name__ == "__main__":
    main()
