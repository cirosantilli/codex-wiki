"""Generate gaussian-beam-waist-and-divergence.png in CWD.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
Vacuum scalar paraxial Gaussian model; all plotted lengths are physical.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    wavelength = 632.8e-9
    waists = np.array([0.500e-3, 0.250e-3])
    ranges = np.pi * waists**2 / wavelength
    angles = wavelength / (np.pi * waists)
    colors = ["#2166ac", "#c45b15"]
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.8), dpi=100)
    fig.subplots_adjust(left=.08, right=.98, bottom=.28, top=.79, wspace=.30)
    near = np.linspace(-1.6, 1.6, 801)
    far = np.linspace(0, 6, 801)
    for waist, rayleigh, angle, color in zip(waists, ranges, angles, colors):
        label = rf"$w_0={waist * 1e3:.3f}$ mm"
        width = waist * np.sqrt(1 + (near / rayleigh)**2)
        axes[0].plot(near, width * 1e3, color=color, lw=2.3, label=label)
        axes[0].plot(near, -width * 1e3, color=color, lw=2.3)
        for sign in [-1, 1]:
            axes[0].scatter([sign * rayleigh], [np.sqrt(2) * waist * 1e3],
                            s=48, facecolor="white", edgecolor=color, lw=1.8, zorder=4)
        axes[1].plot(far, waist * np.sqrt(1 + (far / rayleigh)**2) * 1e3,
                     color=color, lw=2.3)
        axes[1].plot(far, angle * far * 1e3, color=color, ls="--", lw=1.5)
    axes[0].axhline(0, color="0.65", lw=.8)
    axes[0].axvline(0, color="0.65", lw=.8, ls=":")
    axes[0].set(xlim=(-1.6, 1.6), ylim=(-1.5, 1.5), xlabel="Axial distance z (m)",
                ylabel=r"Signed contour $\pm w(z)$ (mm)", title="Waist and Rayleigh range")
    axes[0].legend(loc="lower center", fontsize=10, framealpha=.95)
    axes[0].text(.24, .95, r"Circles: $z=\pm z_R$, $w=\sqrt{2}w_0$",
                 transform=axes[0].transAxes, va="top", fontsize=10)
    axes[1].set(xlim=(0, 6), ylim=(0, 5.2), xlabel="Axial distance z (m)",
                ylabel="Beam radius w(z) (mm)", title="Far-field divergence")
    axes[1].legend(handles=[Line2D([0], [0], color="0.25", lw=2.3, label="Exact model radius"),
                            Line2D([0], [0], color="0.25", ls="--", lw=1.5,
                                   label=r"Asymptote $w=\theta z$")],
                   loc="upper left", fontsize=10)
    for ax in axes:
        ax.grid(alpha=.18)
    fig.suptitle("A smaller waist spreads faster", fontsize=16, y=.97)
    fig.text(.5, .88, r"Fundamental Gaussian beam in vacuum; $\lambda=632.8$ nm",
             ha="center", fontsize=12)
    for index, color in enumerate(colors):
        fig.text(.5, .12 - index * .055,
                 f"Waist {waists[index] * 1e3:.3f} mm:  Rayleigh range {ranges[index]:.6f} m;  "
                 f"half-angle {angles[index] * 1e3:.6f} mrad", ha="center", color=color)
    fig.savefig("gaussian-beam-waist-and-divergence.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
