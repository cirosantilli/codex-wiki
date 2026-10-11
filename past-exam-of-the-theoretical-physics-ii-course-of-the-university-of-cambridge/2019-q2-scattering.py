"""Render the dimensionless scattering curves derived for the 2019 paper.

Run from the mirrored media directory; the PNG is written to the working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11})
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), layout="constrained")
    fig.set_facecolor("white")

    x = np.linspace(0, 4 * np.pi, 1800)
    axes[0].plot(x, np.sinc(x / np.pi) ** 2, color="#2459a6", lw=2)
    tail = x[x >= 1]
    axes[0].plot(tail, 1 / tail**2, "--", color="0.5", lw=1, label=r"$1/(kR)^2$ envelope")
    axes[0].set(
        xlabel=r"Incident wave number $kR$",
        ylabel=r"$\sigma_0/(4\pi R^2)$",
        title="Hard-sphere S wave",
        xlim=(0, 4 * np.pi),
        ylim=(-0.025, 1.05),
        xticks=np.pi * np.arange(5),
        xticklabels=["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"],
    )
    axes[0].legend(fontsize=9)

    theta = np.linspace(0, np.pi, 2200)
    for k_radius, color in [(0.3, "#2459a6"), (3, "#d2731b"), (10, "#31834e")]:
        argument = 2 * k_radius * np.sin(theta / 2)
        intensity = np.sinc(argument / np.pi) ** 2
        axes[1].semilogy(np.degrees(theta), intensity, color=color, lw=1.5, label=fr"$kR={k_radius:g}$")
    axes[1].set(
        xlabel=r"Scattering angle $\theta$ (degrees)",
        ylabel=r"$(d\sigma_B/d\Omega)/(g^2R^2)$",
        title="Weak delta-shell Born scattering",
        xlim=(0, 180),
        ylim=(1e-5, 1.2),
        xticks=[0, 45, 90, 135, 180],
    )
    axes[1].legend(fontsize=9)
    for ax in axes:
        ax.grid(alpha=0.2)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
