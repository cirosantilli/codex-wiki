"""Original ideal-field comparison; Python 3.14, matplotlib 3.10.7.

Run from _media; the drawing is functional, not a historical reconstruction.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.6), facecolor="white")
    blue, red, grey = "#176a97", "#b44736", "#4d5965"
    for ax in axes:
        ax.set(xlim=(-2.6, 2.6), ylim=(-2.4, 2.8), aspect="equal")
        ax.axis("off")
        for z in (-1.35, 1.35):
            ax.add_patch(Rectangle((-.8, z-.10), 1.6, .20,
                                   facecolor="#dde5eb", edgecolor=grey, lw=1.5))
        for x in (-1.25, 1.25):
            ax.add_patch(Rectangle((x-.13, -.5), .26, 1,
                                   facecolor="#dde5eb", edgecolor=grey, lw=1.5))
        ax.add_patch(Circle((0, 0), .085, color="#201f25", zorder=5))
        ax.text(0, 1.65, "endcap", ha="center", color=grey, fontsize=10)
        ax.text(1.5, -.75, "ring section", ha="center", color=grey, fontsize=10)
        ax.text(-.18, -.28, "charge Q", ha="right", fontsize=10)
    ax = axes[0]
    ax.set_title("Paul trap: oscillating electric field", fontsize=13, pad=18)
    ax.text(0, 2.18, r"$\Phi\propto-\cos(\Omega t)(x^2+y^2-2z^2)$",
            ha="center", fontsize=12)
    for sign in (-1, 1):
        ax.add_patch(FancyArrowPatch((sign*.95, 0), (sign*.3, 0),
                                   arrowstyle="->", mutation_scale=14, color=blue, lw=2))
        ax.add_patch(FancyArrowPatch((0, sign*.3), (0, sign*1.05),
                                   arrowstyle="->", mutation_scale=14, color=red, lw=2))
    ax.text(-2.4, .6, r"phase $\Omega t=\pi$", fontsize=10, color=grey)
    ax.text(0, -1.8, "Electric focusing reverses each half-cycle.",
            ha="center", fontsize=11)
    ax.text(0, -2.18, "Small q: slow oscillation + RF micromotion",
            ha="center", fontsize=11, color=blue)
    ax = axes[1]
    ax.set_title("Penning trap: static electric + magnetic fields", fontsize=13, pad=18)
    ax.text(0, 2.18, r"$Q\Phi=\frac{m\omega_z^2}{2}[z^2-(x^2+y^2)/2]$",
            ha="center", fontsize=12)
    for sign in (-1, 1):
        ax.add_patch(FancyArrowPatch((0, sign*1.05), (0, sign*.3),
                                   arrowstyle="->", mutation_scale=14, color=blue, lw=2))
    for x in (-2.05, 2.05):
        ax.annotate("", (x, 1.3), (x, -1.05),
                    arrowprops={"arrowstyle": "->", "color": "#6b4aa5", "lw": 2})
    ax.text(1.8, 1.55, r"$\mathbf{B}$", fontsize=14, color="#6b4aa5")
    theta = np.linspace(0, 2*np.pi, 200)
    ax.plot(.63*np.cos(theta), .20*np.sin(theta), color="#6b4aa5", lw=2)
    ax.text(-1.0, .80, "axial E\nrestoring force", fontsize=10, color=blue,
            ha="center")
    ax.text(0, -1.8, "Magnetic bending confines transverse motion.",
            ha="center", fontsize=11)
    ax.text(0, -2.18, r"Ideal model: $\omega_c^2>2\omega_z^2>0$",
            ha="center", fontsize=11, color="#6b4aa5")
    fig.suptitle("Two ways around static electric confinement", fontsize=16, y=.99)
    fig.text(.5, .025, "Schematic meridional sections; arrows show forces on the chosen charge. Not to scale.",
             ha="center", fontsize=10, color=grey)
    fig.subplots_adjust(left=.02, right=.98, bottom=.10, top=.84, wspace=.08)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
