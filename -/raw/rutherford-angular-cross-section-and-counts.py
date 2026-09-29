"""Calculate an ideal Rutherford distribution; Python 3.14, NumPy 2.3.5.

Matplotlib 3.10.7. Run from _media to create the matching opaque white PNG.
Values are an original model, never historical measurements. Assumptions:
nonrelativistic point Coulomb scattering, heavy fixed target, thin foil,
small detector acceptance, unit efficiency, no screening or nuclear forces.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ENERGY_MEV = 5.0
Z_PROJECTILE = 2
Z_TARGET = 79
COULOMB_MEV_FM = 1.440  # stipulated rounded constant, not a precision determination
KAPPA_MEV_FM = Z_PROJECTILE * Z_TARGET * COULOMB_MEV_FM
A_FM = KAPPA_MEV_FM / (2 * ENERGY_MEV)
N_INCIDENT = 1e11
AREAL_DENSITY_M2 = 1e21
SOLID_ANGLE_SR = 1e-3
EFFICIENCY = 1.0


def differential_fm2_sr(theta_rad):
    """dσ/dΩ in fm²/sr for scattering angle in radians, 0 < theta <= pi."""
    return A_FM**2 / (4 * np.sin(np.asarray(theta_rad) / 2)**4)


def expected_counts(theta_rad):
    return (N_INCIDENT * AREAL_DENSITY_M2 * EFFICIENCY * SOLID_ANGLE_SR
            * differential_fm2_sr(theta_rad) * 1e-30)


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 6.1), facecolor="white")
    fig.subplots_adjust(left=0.09, right=0.97, bottom=0.19, top=0.73, wspace=0.29)
    fig.suptitle("Rutherford scattering: from cross-section to counts", fontsize=18, y=0.97)
    fig.text(0.5, 0.90, r"Calculated model, not measured data: $5.00\,$MeV $\alpha$ on gold ($z=2$, $Z=79$)",
             ha="center", fontsize=12)
    fig.text(0.5, 0.84,
             r"$N_{\rm inc}=10^{11}$, $n_s=10^{21}\,{\rm m}^{-2}$, $\Delta\Omega=10^{-3}\,$sr, $\eta=1$",
             ha="center", fontsize=12)
    angles = np.linspace(20, 160, 600)
    settings = np.array([30, 60, 90, 120, 150])
    cross_sections = differential_fm2_sr(np.deg2rad(settings)) / 100
    ax = axes[0]
    ax.semilogy(angles, differential_fm2_sr(np.deg2rad(angles)) / 100,
                color="#176a9c", linewidth=2.4)
    ax.scatter(settings, cross_sections, color="#176a9c", s=28, zorder=3)
    ax.set(xlim=(20, 160), ylim=(1, 1800), xlabel=r"Scattering angle $\theta$ (degrees)",
           ylabel=r"$d\sigma/d\Omega$ (barn/sr)", title="Angular law")
    ax.set_xticks([30, 60, 90, 120, 150])
    ax.grid(alpha=0.22, which="both")
    ax.text(0.47, 0.83, r"$\dfrac{\kappa^2}{16E^2}\csc^4(\theta/2)$",
            transform=ax.transAxes, fontsize=15)
    ax.annotate("90°: 5.18 barn/sr", xy=(90, cross_sections[2]), xytext=(66, 43),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#596572"})
    ax = axes[1]
    counts = expected_counts(np.deg2rad(settings))
    ax.bar(settings, counts, width=12, color="#3e896d", zorder=2)
    for angle, count in zip(settings, counts):
        ax.text(angle, count * 1.16, f"{count:.1f}", ha="center", fontsize=10)
    ax.set_yscale("log")
    ax.set(xlim=(15, 165), ylim=(8, 7000), xlabel=r"Detector setting $\theta$ (degrees)",
           ylabel="Expected signal counts per exposure", title="Same small detector at five settings")
    ax.set_xticks(settings)
    ax.grid(axis="y", alpha=0.22, which="both")
    ax.text(0.39, 0.78, r"$\mu=N_{\rm inc}n_s\eta\Delta\Omega\,\dfrac{d\sigma}{d\Omega}$",
            ha="center", transform=ax.transAxes, fontsize=12,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    fig.text(0.5, 0.085,
             "Heavy fixed point nucleus • single significant deflection • small detector patch • no energy loss",
             ha="center", fontsize=10.5, color="#596572")
    fig.text(0.5, 0.035,
             "Finite angular range only; forward screening and short-range nuclear effects are outside this model.",
             ha="center", fontsize=10.5, color="#596572")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
