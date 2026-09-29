"""Project ideal Zeeman dipoles; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media. Traces and angular factors are calculated, not measured.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10.8, 7.2), facecolor="white")
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.1], hspace=0.62, wspace=0.3)
    side = fig.add_subplot(gs[0, 0])
    axial = fig.add_subplot(gs[0, 1])
    angular = fig.add_subplot(gs[1, :])
    green, blue = "#21754c", "#235fb0"
    fig.suptitle("The same transitions look different from different directions", fontsize=17, y=0.97)
    for ax in [side, axial]:
        ax.set(xlim=(-2.5, 2.5), ylim=(-1.45, 1.45), aspect="equal")
        ax.axis("off")
    side.set_title(r"Across $\mathbf{B}$: three frequencies", fontsize=13)
    side.annotate("", xy=(-2.1, 1.0), xytext=(-2.1, -0.7),
                  arrowprops={"arrowstyle": "->", "lw": 2, "color": "#333333"})
    side.text(-2.1, -1.0, r"$\mathbf{B}$", ha="center")
    side.annotate("", xy=(-0.6, 0.8), xytext=(-0.6, -0.8),
                  arrowprops={"arrowstyle": "<->", "lw": 3, "color": green})
    side.text(-0.6, -1.2, r"$\pi$: $\mathbf{E}\parallel\mathbf{B}$", ha="center", color=green)
    side.annotate("", xy=(1.9, 0), xytext=(0.4, 0),
                  arrowprops={"arrowstyle": "<->", "lw": 3, "color": blue})
    side.text(1.15, -1.2, r"$\sigma^\pm$: $\mathbf{E}\perp\mathbf{B}$", ha="center", color=blue)
    axial.set_title(r"Along $\mathbf{B}$: two frequencies", fontsize=13)
    axial.text(-2.0, 0.1, r"$\odot$", ha="center", fontsize=28)
    axial.text(-2.0, -0.6, r"$\mathbf{B}$", ha="center")
    t = np.linspace(0, 2 * np.pi, 241)
    for center, rotation, label in [(-0.6, 1, r"$\sigma^-$"), (1.3, -1, r"$\sigma^+$")]:
        axial.plot(center + 0.57 * np.cos(t), 0.57 * np.sin(t), color=blue, lw=2)
        a, b = 0.25, 0.25 + rotation * 0.65
        axial.annotate("", xy=(center + 0.57 * np.cos(b), 0.57 * np.sin(b)),
                       xytext=(center + 0.57 * np.cos(a), 0.57 * np.sin(a)),
                       arrowprops={"arrowstyle": "-|>", "lw": 2, "color": blue})
        axial.text(center, -0.92, label, ha="center", color=blue)
    axial.text(0.3, -1.4, r"$\pi$ absent; opposite rotations (convention dependent)", ha="center", fontsize=10)
    degrees = np.linspace(0, 90, 361)
    theta = np.deg2rad(degrees)
    angular.plot(degrees, np.sin(theta) ** 2, color=green, lw=2.5,
                 label=r"$\pi$: $\sin^2\theta$")
    angular.plot(degrees, (1 + np.cos(theta) ** 2) / 2, color=blue, lw=2.5,
                 label=r"Each $\sigma$: $(1+\cos^2\theta)/2$")
    angular.set(xlim=(0, 90), ylim=(0, 1.08), xticks=[0, 30, 60, 90],
                xlabel=r"Viewing angle $\theta$ from the magnetic field (degrees)",
                ylabel="Angular intensity factor")
    angular.grid(alpha=0.18)
    angular.spines[["top", "right"]].set_visible(False)
    angular.legend(loc="center right", frameon=True, facecolor="white", framealpha=1)
    fig.text(0.5, 0.025, "Calculated for equal dipole magnitudes • state populations and transition strengths are separate",
             ha="center", fontsize=11, color="#444444")
    fig.subplots_adjust(left=0.105, right=0.96, bottom=0.13, top=0.85)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
