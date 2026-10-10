"""Synthetic Doppler absorption and Gaussian instrumental convolution.

No measurements or fitted physical density. Optical-depth areas are arbitrary.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Output is the script basename with .png in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


C_KMS = 299792.458
K_B = 1.380649e-23  # SI
M_H = 1.6735575e-27  # kg, adequate neutral hydrogen mass approximation
VELOCITY = np.linspace(-200.0, 200.0, 8001)


def thermal_b(temperature):
    return np.sqrt(2 * K_B * temperature / M_H) / 1000


def optical_depth(v, center, b, area):
    # Integral tau dv equals area, corresponding to a fixed neutral column.
    return area / (np.sqrt(np.pi) * b) * np.exp(-((v - center) / b) ** 2)


def instrument(flux, resolving_power):
    """Convolve FLUX with unit-area Gaussian; assume continuum beyond grid."""
    dv = VELOCITY[1] - VELOCITY[0]
    sigma = C_KMS / resolving_power / np.sqrt(8 * np.log(2))
    radius = int(np.ceil(6 * sigma / dv))
    offsets = np.arange(-radius, radius + 1) * dv
    kernel = np.exp(-0.5 * (offsets / sigma) ** 2)
    kernel /= kernel.sum()
    padded = np.pad(flux, radius, constant_values=1.0)
    return np.convolve(padded, kernel, mode="valid")


def model():
    cold_tau = optical_depth(VELOCITY, 0, thermal_b(10000), 6.0)
    hot_tau = optical_depth(VELOCITY, 0, thermal_b(30000), 6.0)
    cold, hot = np.exp(-cold_tau), np.exp(-hot_tau)
    pair_tau = sum(optical_depth(VELOCITY, center, 8.0, 12.0) for center in [-12, 12])
    pair = np.exp(-pair_tau)
    return cold_tau, hot_tau, cold, hot, instrument(cold, 10000), pair, instrument(pair, 45000), instrument(pair, 10000)


def main():
    cold_tau, hot_tau, cold, hot, blurred, pair, fine_pair, coarse_pair = model()
    assert abs(np.trapezoid(cold_tau, VELOCITY) - 6) < 1e-10
    assert abs(np.trapezoid(hot_tau, VELOCITY) - 6) < 1e-10
    assert np.all((coarse_pair > 0) & (coarse_pair <= 1 + 1e-14))
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 1, figsize=(9.4, 7.0), sharex=True)
    fig.patch.set_facecolor("white")
    fig.suptitle("Line shape carries information, but broadening can hide it", fontsize=15)
    axes[0].plot(VELOCITY, cold, color="#0072B2", lw=2, label="10,000 K, intrinsic")
    axes[0].plot(VELOCITY, hot, color="#B34F00", lw=2, label="30,000 K, intrinsic")
    axes[0].plot(VELOCITY, blurred, color="#7B3294", ls="--", lw=2,
                 label="10,000 K + instrument R = 10,000")
    axes[0].set(ylim=(0.70, 1.025), ylabel="Normalized transmission")
    axes[0].set_title("A. Same neutral column: hotter gas spreads the optical depth", loc="left", fontsize=12)
    axes[0].legend(loc="lower right", fontsize=10)
    axes[1].plot(VELOCITY, pair, color="#64748b", lw=1.5, ls=":", label="Intrinsic two-component model")
    axes[1].plot(VELOCITY, fine_pair, color="#0072B2", lw=2, label="Instrument R = 45,000")
    axes[1].plot(VELOCITY, coarse_pair, color="#B34F00", lw=2, label="Instrument R = 10,000")
    for center in [-12, 12]:
        axes[1].axvline(center, color="#64748b", lw=0.8, ls=":")
    axes[1].set(xlim=(-80, 80), ylim=(0.35, 1.04),
                xlabel="Velocity relative to chosen line center (km/s)", ylabel="Normalized transmission")
    axes[1].set_title("B. Two Doppler cores, b = 8 km/s, separated by 24 km/s", loc="left", fontsize=12)
    axes[1].legend(loc="lower right", fontsize=10)
    for ax in axes:
        ax.grid(alpha=0.17)
    fig.text(0.5, 0.025, "SYNTHETIC, not measured data · Gaussian instrument FWHM = c/R · no noise or damping wings",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.06, 1, 0.95))
    fig.savefig(Path(__file__).stem + ".png", dpi=115, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
