"""Chosen two-channel angular profiles; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media: output is this script's basename with a .png suffix in CWD.
No experimental data are used.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (ax, angular) = plt.subplots(1, 2, figsize=(10, 4.4), layout="constrained")
    angles = [0, 60, 90, 120, 180]
    colors = ["#264d8b", "#167d96", "#397d33", "#ad6a12", "#943b66"]
    for degrees, color in zip(angles, colors):
        z = 1 + 1j * np.cos(np.deg2rad(degrees))
        ax.annotate("", xy=(z.real, z.imag), xytext=(0, 0),
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
        ax.text(1.04, z.imag, f"{degrees}°", color=color, va="center")
    ax.axhline(0, color="0.7", lw=0.8)
    ax.axvline(0, color="0.7", lw=0.8)
    ax.plot([1, 1], [-1, 1], ":", color="0.65")
    ax.set(xlim=(-0.12, 1.55), ylim=(-1.3, 1.3), aspect="equal",
           xlabel=r"Real part of $h$", ylabel=r"Imaginary part of $h$",
           title=r"Angular factor $h(\theta)=1+i\cos\theta$")
    ax.text(0.03, 0.97, r"$g_1=\sqrt{3/(16\pi)}\,h$", transform=ax.transAxes, va="top")

    theta = np.linspace(0, np.pi, 721)
    density1 = (9 / 25) * 3 / (16 * np.pi) * (1 + np.cos(theta) ** 2)
    density2 = np.full_like(theta, (16 / 25) / (4 * np.pi))
    angular.axvspan(0, 60, color="#e7eff6", label="Accepted cone")
    angular.plot(np.rad2deg(theta), density1, lw=2.5, color="#264d8b",
                 label=r"Channel 1: $(9/25)|g_1|^2$")
    angular.plot(np.rad2deg(theta), density2, lw=2.5, color="#ad6a12",
                 label=r"Channel 2: $(16/25)|g_2|^2$")
    angular.set(xlim=(0, 180), ylim=(0, 0.068), xticks=[0, 60, 90, 120, 180],
                xlabel=r"Scattering angle $\theta$ (degrees)",
                ylabel=r"Joint density $dP_i/d\Omega$ (sr$^{-1}$)",
                title="Squared amplitudes × channel flux weight")
    angular.legend(loc="upper center", fontsize=9, framealpha=1)
    angular.grid(axis="y", alpha=0.2)
    fig.suptitle("Chosen scattering model: complex amplitudes → angular intensity", fontsize=14)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
