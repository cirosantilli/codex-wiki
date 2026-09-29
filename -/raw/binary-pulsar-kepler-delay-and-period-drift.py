"""Chosen Kepler timing model and secular drift; no observations or historical fit.

Python 3.14, NumPy, Matplotlib. Run from _media. Newton's iteration is
independently checked against bisection and Kepler-equation residuals.
"""
from pathlib import Path
import json

import matplotlib.pyplot as plt
import numpy as np


def eccentric_anomaly(mean, eccentricity):
    E = np.asarray(mean, dtype=float).copy()
    for _ in range(16):
        E -= (E - eccentricity * np.sin(E) - mean) / (1 - eccentricity * np.cos(E))
    return E


def delay(mean, eccentricity, omega, x):
    E = eccentric_anomaly(mean, eccentricity)
    return x * (np.sin(omega) * (np.cos(E) - eccentricity)
                + np.sqrt(1 - eccentricity**2) * np.cos(omega) * np.sin(E))


def checks():
    e, x, omega, pb = 0.6, 2.0, np.deg2rad(40), 28800.0
    mean = np.linspace(0, 2 * np.pi, 1001)
    E = eccentric_anomaly(mean, e)
    residual = float(np.max(np.abs(E - e * np.sin(E) - mean)))
    # Bracketing is a different root-finding algorithm; f' >= 1-e > 0.
    lo, hi = np.zeros_like(mean), np.full_like(mean, 2 * np.pi)
    for _ in range(60):
        mid = (lo + hi) / 2
        left = mid - e * np.sin(mid) < mean
        lo = np.where(left, mid, lo); hi = np.where(left, hi, mid)
    agreement = float(np.max(np.abs(E - (lo + hi) / 2)))
    assert residual < 2e-14 and agreement < 3e-14
    assert np.max(np.abs(delay(mean, 0, omega, x) - x * np.sin(mean + omega))) < 2e-15
    assert abs(np.ptp(delay(np.array([0, 2 * np.pi]), e, omega, x))) < 2e-14
    # Finite differences independently check dz/dt against the anomaly derivative.
    test = np.linspace(0.03, 2 * np.pi - 0.03, 301)
    Et = eccentric_anomaly(test, e)
    h = 1e-5
    fd = (delay(test + h, e, omega, x) - delay(test - h, e, omega, x)) / (2*h)
    analytic = x * (-np.sin(omega)*np.sin(Et) + np.sqrt(1-e*e)*np.cos(omega)*np.cos(Et)) / (1-e*np.cos(Et))
    derivative_error = float(np.max(np.abs(fd - analytic)))
    assert derivative_error < 4e-9
    # Direct orbital-plane rotation equals the analytic projected delay.
    projected = x * (np.sin(omega)*(np.cos(E)-e) + np.cos(omega)*np.sqrt(1-e*e)*np.sin(E))
    assert np.max(np.abs(projected - delay(mean, e, omega, x))) < 2e-15
    year = 365.25 * 86400
    t = 20 * year; pdot = -2e-12
    shift = 0.5 * pdot / pb * t*t
    # Integrate cycles exactly for P(t)=Pb+pdot*t, then convert excess cycles to seconds.
    excess = (np.log1p(pdot*t/pb) - pdot*t/pb) / pdot
    exact_shift = -pb * excess
    assert abs(exact_shift - shift) < 2e-6
    G, c, solar_mass = 6.67430e-11, 299792458.0, 1.98847e30
    mass_function = 4*np.pi**2*(c*x)**3/(G*pb**2)/solar_mass
    print(json.dumps({"kepler_max_residual_rad": residual, "newton_bisection_max_difference_rad": agreement,
                      "delay_derivative_max_error_s_per_rad": derivative_error,
                      "mass_function_solar_masses": mass_function,
                      "period_change_after_20_years_ms": pdot*t*1000,
                      "periastron_time_shift_after_20_years_s": shift,
                      "exact_linear_period_integral_shift_s": exact_shift}))


def main():
    checks()
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(2, 1, figsize=(8.8, 7.1), layout="constrained")
    phase = np.linspace(0, 1, 801); mean = 2*np.pi*phase
    omega, x = np.deg2rad(40), 2.0
    axes[0].plot(phase, delay(mean, 0.6, omega, x), color="#246799", lw=2.5, label=r"eccentricity $e=0.6$")
    axes[0].plot(phase, delay(mean, 0, omega, x), color="#9a6125", lw=1.7, ls="--", label=r"circular comparison $e=0$")
    axes[0].axhline(0, color="0.7", lw=0.8)
    axes[0].set(xlabel=r"mean orbital phase $M/(2\pi)$", ylabel=r"geometric delay $\Delta_R$ (s)", xlim=(0, 1),
                title=r"Chosen orbit: $x=2$ s, $P_b=8$ h, $\omega=40^\circ$")
    axes[0].legend(loc="upper right", fontsize=10)
    years = np.linspace(0, 20, 301); t = years * 365.25 * 86400
    shift = 0.5 * (-2e-12) / 28800 * t*t
    axes[1].plot(years, shift, color="#246799", lw=2.5)
    axes[1].axhline(0, color="0.5", lw=1, ls="--")
    axes[1].set(xlabel="elapsed time (Julian years)", ylabel="periastron time shift (s)", xlim=(0, 20),
                title=r"Separately chosen secular model: $\dot P_b=-2\times10^{-12}$ s/s")
    axes[1].annotate(f"earlier by {abs(shift[-1]):.2f} s\nperiod shorter by 1.26 ms", xy=(20, shift[-1]),
                     xytext=(8.8, -7), arrowprops={"arrowstyle": "->", "color": "#246799"}, fontsize=10.5)
    for ax in axes:
        ax.grid(alpha=0.18); ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Illustrative timing models — no historical data or fit", fontsize=14)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
