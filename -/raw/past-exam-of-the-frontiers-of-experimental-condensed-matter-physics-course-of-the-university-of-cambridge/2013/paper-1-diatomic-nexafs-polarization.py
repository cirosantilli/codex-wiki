"""Ideal dipole factors for stipulated orientations; no source spectra are copied."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    angle = np.linspace(0, 90, 361)
    alpha = np.deg2rad(angle)
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.2), sharey=True, layout="constrained")
    for ax, tilt in zip(axes, [90, 35]):
        beta = np.deg2rad(tilt)
        sigma = np.cos(beta)**2*np.cos(alpha)**2+.5*np.sin(beta)**2*np.sin(alpha)**2
        pi = 1-sigma
        ax.plot(angle, pi, label=r"Summed $\pi^*$ geometry", color="tab:blue", lw=2)
        ax.plot(angle, sigma, label=r"$\sigma^*$ geometry", color="tab:orange", lw=2)
        ax.set(xlabel="Electric-field angle to surface normal (degrees)",
               title=f"Molecular-axis tilt {tilt}°; random azimuth", xlim=(0, 90), ylim=(-.03, 1.03))
        ax.set_xticks([0, 45, 90]); ax.grid(alpha=.2)
        ax.text(.5, .08, "Normal field at left; tangential field at right",
                transform=ax.transAxes, ha="center", fontsize=9)
    axes[0].set_ylabel("Dimensionless orientation factor")
    axes[0].legend(loc="center right", frameon=False)
    fig.suptitle("Original orientation model; resonance matrix elements and spectra are not fitted")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
