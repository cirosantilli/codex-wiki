"""Ideal finite-row diffraction; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media. Hypothetical row, not a fit or experimental dataset.
The direct complex sum avoids removable singularities of the sine quotient.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

H = 6.62607015e-34
E_CHARGE = 1.602176634e-19
E_MASS = 9.1093837139e-31
N_SITES = 12
ROW_SPACING = 0.250e-9


def model_intensity(phi, wavelength, n_sites=N_SITES, spacing=ROW_SPACING):
    """Intensity relative to its normal-direction value, phi in radians."""
    delta = 2 * np.pi * spacing * np.sin(np.asarray(phi)) / wavelength
    phase = np.asarray(delta)[..., None] * np.arange(n_sites)
    return np.abs(np.exp(1j * phase).sum(axis=-1) / n_sites) ** 2


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (geometry, intensity) = plt.subplots(1, 2, figsize=(10.8, 5),
                                             gridspec_kw={"width_ratios": [1, 1.35]})
    fig.subplots_adjust(left=0.04, right=0.98, bottom=0.21, top=0.73, wspace=0.17)
    fig.suptitle("Electron diffraction: a finite row adds scattering phases", y=0.96, fontsize=15)
    fig.text(0.5, 0.86, "Hypothetical model • 12 equal sites • d = 0.250 nm • no measured data", ha="center")

    geometry.set(xlim=(-2.5, 2.8), ylim=(-0.6, 3.5), aspect="equal")
    geometry.axis("off")
    geometry.plot([-2.25, 2.25], [0, 0], color="#777777", lw=1)
    geometry.scatter(np.arange(-2, 3), np.zeros(5), color="#555555", s=70, zorder=5)
    for x in [-1, 0, 1]:
        geometry.annotate("", (x, 0.15), (x, 2.35),
                          arrowprops={"arrowstyle": "->", "color": "#2367a2", "lw": 1.7})
    geometry.text(-2.4, 2.9, "Incident plane wave\n(normal to the row)", color="#2367a2")
    phi = np.deg2rad(35)
    direction = np.array([np.sin(phi), np.cos(phi)])
    for x in [0, 1]:
        end = np.array([x, 0]) + 2.75 * direction
        geometry.annotate("", end, (x, 0.08),
                          arrowprops={"arrowstyle": "->", "color": "#b44b28", "lw": 1.7})
    geometry.plot([0, 0], [0, 2.6], "--", color="#777777", lw=1)
    geometry.add_patch(Arc((0, 0), 1.45, 1.45, theta1=55, theta2=90, color="#333333"))
    geometry.text(0.15, 0.87, r"$\phi$", fontsize=14)
    geometry.text(-0.3, 2.6, "Outward normal", fontsize=10, ha="center")
    geometry.text(1.2, 3.05, "Outgoing\ndirection", color="#b44b28", fontsize=10)
    geometry.annotate("", (1, -0.30), (0, -0.30), arrowprops={"arrowstyle": "<->", "color": "#333333"})
    geometry.text(0.5, -0.52, r"$d$", ha="center", fontsize=13)
    geometry.text(-2.4, -1.1, r"Adjacent phase difference: $\delta=kd\sin\phi$", fontsize=11)
    geometry.text(-2.4, -1.48, "Arrows show directions, not particle trajectories.", fontsize=9)

    angles = np.linspace(-70, 70, 5001)
    for voltage, color in [(54, "#2367a2"), (100, "#b44b28"), (400, "#248048")]:
        wavelength = H / np.sqrt(2 * E_MASS * E_CHARGE * voltage)
        first = np.rad2deg(np.arcsin(wavelength / ROW_SPACING))
        intensity.plot(angles, model_intensity(np.deg2rad(angles), wavelength),
                       color=color, lw=1.7, label=f"{voltage} V; first order ±{first:.1f}°")
    intensity.set(xlabel=r"Angle $\phi$ from outward normal (degrees)",
                  ylabel=r"Calculated intensity $I(\phi)/I(0)$", xlim=(-70, 70), ylim=(0, 1.09))
    intensity.set_xticks([-60, -30, 0, 30, 60])
    intensity.grid(alpha=0.2)
    handles, labels = intensity.get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, 0.82),
               ncol=3, fontsize=10, frameon=False)
    fig.text(0.5, 0.04, r"Peak condition: $d\sin\phi=m\lambda$; increasing voltage moves a fixed order toward the normal.",
             fontsize=10, ha="center")
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
