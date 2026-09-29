"""Original evanescent decay model; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media; writes this script's basename.png to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    n1, n2, wavelength = 1.5, 1.0, 633.0  # lengths in nanometres
    critical = np.degrees(np.arcsin(n2 / n1))
    kappa = 2*np.pi/wavelength * np.sqrt(n1*n1*np.sin(np.radians(50))**2 - n2*n2)
    delta = 1/kappa
    colors = ["#285b94", "#a54825"]
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.2), dpi=100)
    fig.patch.set_facecolor("white")
    fig.suptitle("Evanescent penetration: amplitude and squared field", fontsize=17, y=0.97)
    z = np.linspace(0, 650, 601)
    ax = axes[0]
    ax.plot(z, np.exp(-kappa*z), color=colors[0], lw=2.8, label=r"Amplitude $e^{-z/\delta}$")
    ax.plot(z, np.exp(-2*kappa*z), color=colors[1], lw=2.8, label=r"Squared field $e^{-2z/\delta}$")
    ax.axhline(np.exp(-1), color="#6b737c", ls=":", lw=1.2)
    ax.text(627, np.exp(-1)+0.024, r"$1/e$", ha="right", color="#606870", fontsize=12)
    for depth, color in zip([delta, delta/2], colors):
        ax.plot([depth, depth], [0, np.exp(-1)], color=color, ls="--", lw=1.5)
        ax.plot(depth, np.exp(-1), "o", color=color, ms=6)
    ax.annotate(f"δ = {delta:.3f} nm", (delta, np.exp(-1)), xytext=(290, 0.53),
                arrowprops=dict(arrowstyle="->", color=colors[0]), color=colors[0], fontsize=11)
    ax.annotate(f"δ/2 = {delta/2:.3f} nm", (delta/2, np.exp(-1)), xytext=(210, 0.18),
                arrowprops=dict(arrowstyle="->", color=colors[1]), color=colors[1], fontsize=11)
    ax.set(xlim=(0, 650), ylim=(0, 1.04), xlabel="Distance z into the lower-index medium (nm)",
           ylabel="Envelope normalized to its surface value", title="50° incidence: two different 1/e depths")
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    ax = axes[1]
    angles = np.linspace(critical+0.01, 89.9, 1400)
    depths = wavelength / (2*np.pi*np.sqrt(n1*n1*np.sin(np.radians(angles))**2-n2*n2))
    ax.plot(angles, depths, color=colors[0], lw=2.8, label=r"Amplitude depth $\delta$")
    ax.plot(angles, depths/2, color=colors[1], lw=2.8, label=r"Squared-field depth $\delta/2$")
    ax.axvline(critical, color="#6b737c", ls=":", lw=1.4)
    ax.annotate(r"$\delta\to\infty$ at $\theta_c^+$", (42.05, 630), xytext=(52, 580),
                arrowprops=dict(arrowstyle="->", color="#606870"), color="#606870", fontsize=12)
    ax.plot([50, 50], [0, delta], color="#8b9198", ls=":", lw=1)
    ax.plot(50, delta, "o", color=colors[0], ms=6)
    ax.plot(50, delta/2, "o", color=colors[1], ms=6)
    ax.annotate("50°", (50, delta), xytext=(55, 267), fontsize=11,
                arrowprops=dict(arrowstyle="->", color="#606870"))
    ax.set(xlim=(40, 90), ylim=(0, 680), xlabel="Angle of incidence θ (degrees from normal)",
           ylabel="1/e depth (nm)", title=f"Critical angle θc = {critical:.4f}°")
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
        ax.spines[["right", "top"]].set_visible(False)
        ax.tick_params(labelsize=10)
    fig.text(0.5, 0.08, "Constructed model: n₁ = 1.5, n₂ = 1, λ₀ = 633 nm • lossless, isotropic, nonmagnetic media", ha="center", fontsize=11)
    fig.text(0.5, 0.035, "Squared field and tangential energy flow decay together; outgoing normal average power is zero.", ha="center", fontsize=10, color="#505963")
    fig.subplots_adjust(left=0.075, right=0.98, top=0.82, bottom=0.22, wspace=0.27)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
