"""Stipulated circular-disk correlation model, with no measured points.

Python 3.14; numpy 2.3.5; matplotlib 3.10.7. No SciPy.
Run from _media to write basename.png in the current directory.
J1 uses a convergent power series, independently checked against angular
quadrature of the disk transform. The example uses a rectangular count gate,
not the bandpass electronics of the historical Sirius experiment.
"""

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def j1_series(x):
    term = x / 2
    terms = [term]
    for k in range(1, 200):
        term *= -(x * x / 4) / (k * (k + 1))
        terms.append(term)
        if abs(term) < 1e-18:
            return math.fsum(terms)
    raise ArithmeticError("J1 series did not converge")


def coherence(x):
    return 1.0 if x == 0 else 2 * j1_series(x) / x


def disk_quadrature(x, n=20000):
    # 4/pi integral from 0 to pi/2 cos(x sin u) cos²u du.
    # Simpson quadrature, independently integrating the projected disk.
    u = np.linspace(0, math.pi / 2, n + 1)
    y = np.cos(x * np.sin(u)) * np.cos(u) ** 2
    return (4 / math.pi) * (math.pi / 2 / n / 3) * (
        y[0] + y[-1] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum())


def first_zero():
    lo, hi = 3.0, 4.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if j1_series(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    theta = 5e-3 * math.pi / 648000  # five milliarcseconds in radians
    wavelength = 500e-9
    x0 = first_zero()
    baseline_zero = x0 * wavelength / (math.pi * theta)
    checks = [abs(coherence(x) - disk_quadrature(x)) for x in np.linspace(0, 8, 33)]
    assert max(checks) < 5e-13
    assert abs(x0 - 3.8317059702075125) < 2e-14
    assert abs(coherence(0.01) - (1 - 0.01 ** 2 / 8 + 0.01 ** 4 / 192)) < 1e-15
    tau0, gate, rho = 1.0, 50.0, 0.8  # picoseconds; stipulated, not instrument data
    beta = 2 * tau0 / gate - 2 * (tau0 / gate) ** 2 * (1 - math.exp(-gate / tau0))
    amplitude = rho * rho * beta  # one selected polarization
    baseline = np.linspace(0, 50, 801)
    gamma = np.array([coherence(math.pi * b * theta / wavelength) for b in baseline])
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(2, 1, figsize=(9.4, 7.1), sharex=True,
                             gridspec_kw={"height_ratios": [1.2, 1]}, facecolor="white")
    upper, lower = axes
    upper.plot(baseline, gamma, color="#bd6020", lw=2, label=r"Signed field coherence $\gamma(B)$")
    upper.plot(baseline, gamma ** 2, color="#176b94", lw=2.3, label=r"Squared visibility $V^2=|\gamma|^2$")
    upper.axhline(0, color="#7d858a", lw=0.8)
    upper.set(ylabel="Normalized optical quantities", ylim=(-0.21, 1.09))
    upper.legend(loc="upper right", frameon=False, fontsize=10)
    upper.text(28, 0.36, "Sign reversal survives in γ;\nintensity correlations retain |γ|².", fontsize=10)
    lower.plot(baseline, 1 + amplitude * gamma ** 2, color="#664095", lw=2.3)
    lower.axhline(1, color="#7d858a", lw=0.8)
    lower.set(xlabel="Projected baseline B (m)", ylabel=r"Gate-averaged $g^{(2)}_{\rm obs}(B,0)$",
              ylim=(0.998, 1.029), xlim=(0, 50))
    lower.text(27.7, 1.019, "One polarization; independent backgrounds\n"
               r"$\rho_1=\rho_2=0.8$; $|g_t^{(1)}(u)|^2=e^{-|u|/\tau_0}$" + "\n"
               r"$\tau_0=1$ ps; rectangular gate $T=50$ ps" + "\n"
               rf"$\beta={beta:.4f}$; excess at B = 0: {amplitude:.6f}", fontsize=10)
    for ax in axes:
        ax.axvline(baseline_zero, color="#42614c", ls="--", lw=1.2)
        ax.grid(alpha=0.18)
    upper.annotate(f"First zero: {baseline_zero:.3f} m", xy=(baseline_zero, 0), xytext=(6, -0.16),
                   arrowprops={"arrowstyle": "->", "color": "#42614c"}, color="#42614c", fontsize=10)
    fig.suptitle("Stipulated uniform stellar disk: diameter 5 mas, wavelength 500 nm", fontsize=13)
    fig.text(0.5, 0.015, "Calculated curves only — no measured points or fit to Sirius", ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.035, 1, 0.955), h_pad=1.2)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print({"series_quadrature_max_abs_error": float(max(checks)), "first_j1_zero": x0,
           "first_zero_m": baseline_zero, "theta_rad": theta, "beta": beta,
           "zero_baseline_g2": 1 + amplitude,
           "at_10m": {"x": math.pi * 10 * theta / wavelength,
                       "visibility_squared": coherence(math.pi * 10 * theta / wavelength) ** 2,
                       "observed_g2": 1 + amplitude * coherence(math.pi * 10 * theta / wavelength) ** 2}})


if __name__ == "__main__":
    main()
