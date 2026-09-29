"""Synthetic sightline and absorption; no measured data or cosmological fit.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Output is the script basename with .png in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


LAMBDA_ALPHA = 1215.67  # vacuum angstroms; Rauch (1998), section 1
C_KMS = 299792.458
SELECTED_Z = np.array([2.0, 2.35, 2.7])
COLORS = ["#0072B2", "#B34F00", "#7B3294"]


def model():
    """Gaussian Doppler optical depths, no damping, velocities or noise."""
    wavelength = np.linspace(3500.0, 5000.0, 60001)
    tau = np.zeros_like(wavelength)
    # Additional weak components are deliberately invented, evenly specified.
    weak_z = np.array([1.91, 1.94, 1.965, 2.03, 2.07, 2.11, 2.15, 2.19,
                       2.24, 2.28, 2.32, 2.39, 2.43, 2.48, 2.52, 2.57,
                       2.62, 2.66, 2.75, 2.80, 2.86, 2.92, 2.97])
    for index, z in enumerate(weak_z):
        center = LAMBDA_ALPHA * (1 + z)
        b = 25.0 + 5.0 * (index % 4)  # km/s, illustrative Doppler widths
        v = C_KMS * (wavelength / center - 1)
        tau += (0.25 + 0.13 * (index % 5)) * np.exp(-(v / b) ** 2)
    for z in SELECTED_Z:
        center = LAMBDA_ALPHA * (1 + z)
        v = C_KMS * (wavelength / center - 1)
        tau += 1.6 * np.exp(-(v / 35.0) ** 2)
    # A uniform toy optical depth only within the displayed foreground band.
    smooth_tau = np.where(wavelength < LAMBDA_ALPHA * 4, 2.0, 0.0)
    return wavelength, tau, np.exp(-tau), np.exp(-smooth_tau)


def main():
    wavelength, tau, transmission, smooth = model()
    assert np.all(tau >= 0)
    assert np.all((transmission > 0) & (transmission <= 1))
    assert np.all(SELECTED_Z < 3.0)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 1, figsize=(9.4, 6.6),
                             gridspec_kw={"height_ratios": [1, 1.5]})
    fig.patch.set_facecolor("white")
    fig.suptitle("One atomic transition, many foreground redshifts", fontsize=16)
    geometry, spectrum = axes
    geometry.set_xlim(-0.3, 10.3)
    geometry.set_ylim(-0.65, 1.65)
    geometry.axis("off")
    geometry.plot([0, 10], [0.25, 0.25], color="#64748b", lw=1.4)
    geometry.annotate("", xy=(0.1, 0.25), xytext=(9.8, 0.25),
                      arrowprops={"arrowstyle": "->", "lw": 2, "color": "#64748b"})
    geometry.text(5, 1.35, "Light travels toward the observer", ha="center")
    geometry.scatter([0, 10], [0.25, 0.25], s=[85, 140], color=["#222222", "#228833"])
    geometry.text(0, -0.25, "Observer\nz = 0", ha="center")
    geometry.text(10, -0.25, "Quasar\nz = 3", ha="center")
    for x, z, color in zip([2.4, 5.0, 7.6], SELECTED_Z, COLORS, strict=True):
        geometry.add_patch(Rectangle((x - 0.25, -0.1), 0.5, 0.75,
                                     facecolor=color, alpha=0.18, edgecolor=color))
        geometry.text(x, 0.85, f"Selected region\nz = {z:g}", ha="center", color=color)
        geometry.text(x, -0.25, f"{LAMBDA_ALPHA * (1 + z):.1f} Å", ha="center", color=color)
    geometry.text(5, -0.58, "Positions and region sizes schematic; other foreground gas omitted",
                  ha="center", fontsize=10)
    spectrum.plot(wavelength, transmission, color="#0072B2", lw=1.3,
                  label="Structured toy optical depth (26 components)")
    spectrum.plot(wavelength, smooth, color="#B34F00", lw=2, ls="--",
                  label="Uniform toy optical depth: τ = 2")
    for z, color in zip(SELECTED_Z, COLORS, strict=True):
        center = LAMBDA_ALPHA * (1 + z)
        spectrum.annotate(f"z = {z:g}", xy=(center, np.exp(-1.6)),
                          xytext=(center, 0.52), ha="center", color=color,
                          arrowprops={"arrowstyle": "->", "color": color, "lw": 1})
    emission = LAMBDA_ALPHA * 4
    spectrum.axvline(emission, color="#228833", lw=1.3, ls=":")
    spectrum.text(emission - 20, 0.64, "Quasar Lyα\nposition", ha="right", color="#228833")
    spectrum.set(xlim=(3500, 5000), ylim=(0, 1.13),
                 xlabel="Observed vacuum wavelength (Å)", ylabel="Continuum-normalized transmission")
    spectrum.legend(loc="upper left", fontsize=9, framealpha=1)
    spectrum.grid(alpha=0.15)
    fig.text(0.5, 0.025, "SYNTHETIC, not measured data · no noise, instrument response or proximity effect",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.06, 1, 0.95))
    fig.savefig(Path(__file__).stem + ".png", dpi=115, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
