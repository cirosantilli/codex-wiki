"""Original free-electron Compton curves; Python 3.14, matplotlib 3.10.7, numpy 2.3.5."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

ENERGY_KEV = 70.0
REST_ENERGY_KEV = 511.0  # stipulated rounded input, not a precision constant
COMPTON_PM = 2.426


def main():
    degrees = np.linspace(0, 180, 721)
    factor = 1 - np.cos(np.deg2rad(degrees))
    energy = ENERGY_KEV / (1 + ENERGY_KEV / REST_ENERGY_KEV * factor)
    points = np.array([0, 60, 90, 180])
    point_factor = 1 - np.cos(np.deg2rad(points))
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.1), layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("Compton recoil: outgoing photon energy and wavelength increase", fontsize=15)
    axes[0].plot(degrees, energy, color="#126f9b", lw=2.6)
    axes[0].scatter(points, ENERGY_KEV / (1 + ENERGY_KEV / REST_ENERGY_KEV * point_factor),
                    color="#126f9b", s=35, zorder=3, clip_on=False)
    axes[0].set(ylabel="Outgoing photon energy E′ (keV)", ylim=(52, 72),
                title="Photon energy decreases")
    axes[1].plot(degrees, COMPTON_PM * factor, color="#a64e16", lw=2.6)
    axes[1].scatter(points, COMPTON_PM * point_factor, color="#a64e16", s=35,
                    zorder=3, clip_on=False)
    axes[1].set(ylabel="Wavelength increase λ′ − λ (pm)", ylim=(-0.25, 5.15),
                title="Wavelength increases")
    for ax in axes:
        ax.set(xlabel="Photon deflection θ (degrees)", xlim=(0, 180), xticks=[0, 60, 90, 120, 180])
        ax.grid(alpha=0.24)
        ax.spines[["top", "right"]].set_visible(False)
    fig.supxlabel("E = 70 keV; mₑc² = 511 keV; λC = 2.426 pm (chosen rounded inputs)\n"
                  "Free electron initially at rest • Calculated curves and points, not measured data",
                  fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
