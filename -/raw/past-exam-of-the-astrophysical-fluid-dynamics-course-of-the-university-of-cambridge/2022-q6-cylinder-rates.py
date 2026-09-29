#!/usr/bin/env python3
"""Compute cylinder mode rates, using the derived dispersion relation.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (+dfsg1 build),
as declared in the repository pyproject.toml. Writes the PNG basename to cwd.
No source diagram is traced or embedded. K0 uses its convergent real integral
(DLMF 10.32.9); I1 uses its power series (DLMF 10.25.2).
"""
from pathlib import Path
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def k0(x):
    """K0(x) for positive real x, from integral exp(-x cosh(t)) dt."""
    if x <= 0:
        raise ValueError("x must be positive")
    t = np.linspace(0.0, 16.0, 4097)
    return float(np.trapezoid(np.exp(-x * np.cosh(t)), t))


def i1(x):
    term = x / 2.0
    total = term
    for j in range(1, 100):
        term *= x * x / (4 * j * (j + 1))
        total += term
        if abs(term) < 1e-16 * abs(total):
            return total
    raise ArithmeticError("I1 series did not converge")


def dispersion_rhs(kappa):
    i0 = float(np.i0(kappa))
    return kappa * i1(kappa) / i0 * (k0(kappa) * i0 - 0.5)


def critical_kappa():
    low, high = 0.1, 2.0
    for _ in range(65):
        mid = (low + high) / 2
        if k0(mid) * np.i0(mid) > 0.5:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def fastest_kappa():
    low, high = 0.05, critical_kappa()
    ratio = (math.sqrt(5) - 1) / 2
    c = high - ratio * (high - low)
    d = low + ratio * (high - low)
    fc, fd = dispersion_rhs(c), dispersion_rhs(d)
    for _ in range(80):
        if fc > fd:
            high, d, fd = d, c, fc
            c = high - ratio * (high - low)
            fc = dispersion_rhs(c)
        else:
            low, c, fc = c, d, fd
            d = low + ratio * (high - low)
            fd = dispersion_rhs(d)
    return (low + high) / 2


def main():
    critical = critical_kappa()
    fastest = fastest_kappa()
    lambda_crit = 2 * np.pi / critical
    lambda_peak = 2 * np.pi / fastest
    wavelength = np.unique(np.r_[np.linspace(4.0, 32.0, 900), lambda_crit, lambda_peak])
    rhs = np.array([dispersion_rhs(2 * np.pi / value) for value in wavelength])
    rhs[np.abs(wavelength - lambda_crit) < 1e-12] = 0.0
    growth = np.where(rhs >= 0, np.sqrt(np.maximum(rhs, 0)), np.nan)
    oscillation = np.where(rhs <= 0, np.sqrt(np.maximum(-rhs, 0)), np.nan)
    peak_rate = math.sqrt(dispersion_rhs(fastest))
    fig, ax = plt.subplots(figsize=(7.2, 3.9), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.axvspan(4, lambda_crit, color="#e69f00", alpha=0.09)
    ax.axvspan(lambda_crit, 32, color="#0072b2", alpha=0.055)
    ax.plot(wavelength, oscillation, color="#b66f00", linewidth=2.3,
            label=r"Stable: $\omega/\sqrt{4\pi G\rho}$")
    ax.plot(wavelength, growth, color="#0072b2", linewidth=2.3,
            label=r"Unstable: $\sigma/\sqrt{4\pi G\rho}$")
    ax.axvline(lambda_crit, color="0.4", linestyle="--", linewidth=1)
    ax.plot(lambda_peak, peak_rate, "o", color="#0072b2", markersize=5)
    ax.annotate(f"Fastest growth\n$\\lambda/R={lambda_peak:.2f}$", xy=(lambda_peak, peak_rate),
                xytext=(17, 0.31), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "0.3"})
    ax.annotate(f"Threshold {lambda_crit:.2f}", xy=(lambda_crit, 0),
                xytext=(8, 0.045), fontsize=9, color="0.3",
                arrowprops={"arrowstyle": "->", "color": "0.4"})
    ax.set(xlim=(4, 32), ylim=(0, 0.46), xlabel=r"Axial wavelength $\lambda/R$",
           ylabel="Dimensionless rate", title="Self-gravitating cylinder: mode growth and oscillation")
    ax.grid(alpha=0.18)
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)
    print(f"kappa_crit={critical:.10f}; lambda_crit/R={lambda_crit:.10f}")
    print(f"kappa_fastest={fastest:.10f}; lambda_fastest/R={lambda_peak:.10f}")
    print(f"F_max={peak_rate**2:.10f}; sigma/sqrt(4*pi*G*rho)={peak_rate:.10f}")


if __name__ == "__main__":
    main()
