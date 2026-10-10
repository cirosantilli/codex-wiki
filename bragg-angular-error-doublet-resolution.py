"""Chosen Bragg-error and equal-Gaussian doublet models, not measured spectra.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes the matching PNG in the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.3), dpi=110)
    fig.patch.set_facecolor("white")
    theta = np.linspace(8, 85, 400)
    angle_error = np.deg2rad(10/3600)
    axes[0].semilogy(theta, angle_error/np.tan(np.deg2rad(theta)),
                     color="#176b9c", lw=2.2, label="Angular term: 10 arcsec")
    axes[0].axhline(2e-5, color="#b44724", ls="--", label="Chosen spacing error: 20 ppm")
    for deg in (30, 70):
        y = angle_error/np.tan(np.deg2rad(deg))
        axes[0].plot(deg, y, "o", color="#176b9c")
        axes[0].annotate(f"{deg}°: {y*1e6:.1f} ppm", (deg, y), xytext=(-35, 16),
                         textcoords="offset points", fontsize=10)
    axes[0].set(xlabel=r"Bragg angle $\theta$ (degrees)",
                ylabel=r"Fractional error magnitude", title="Larger angles reduce angular error")
    axes[0].legend(loc="upper right", fontsize=9)
    axes[0].grid(alpha=0.2, which="both")
    d = 0.2000  # nm: chosen model plane spacing, not a historical crystal value
    wavelengths = np.array([0.2000, 0.2002])  # nm, invented example doublet
    centers = np.rad2deg(np.arcsin(wavelengths/(2*d)))
    mid = centers.mean()
    x = np.linspace(mid-0.12, mid+0.12, 1601)
    for sigma, color in ((0.040, "#888888"), (0.008, "#176b9c")):
        components = np.exp(-0.5*((x[:, None]-centers)/sigma)**2)
        axes[1].plot(x-mid, components.sum(axis=1), color=color, lw=2,
                     label=rf"$\sigma_\theta={sigma:.3f}^\circ$, $\Delta/\sigma={np.diff(centers)[0]/sigma:.2f}$")
        if sigma == 0.008:
            for col in components.T:
                axes[1].plot(x-mid, col, color=color, ls=":", lw=1)
    for c in centers:
        axes[1].axvline(c-mid, color="#b44724", ls="--", alpha=0.55, lw=1)
    axes[1].set(xlabel=r"Bragg-angle offset from midpoint (degrees)",
                ylabel="Response (each isolated peak = 1)",
                title="Same doublet, two assumed angular widths", ylim=(0, 2.12))
    axes[1].legend(fontsize=9, loc="upper right")
    axes[1].grid(alpha=0.2)
    fig.suptitle("Illustrative models • chosen d = 0.2000 nm, n = 1", fontsize=14, weight="bold")
    fig.text(0.5, 0.035,
             "Chosen lines: 0.2000 and 0.2002 nm. Equal Gaussian peaks; no noise or background.\n"
             "Two maxima appear for separation > 2σ. This is not the Rayleigh criterion.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.25, top=0.82, wspace=0.30)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
