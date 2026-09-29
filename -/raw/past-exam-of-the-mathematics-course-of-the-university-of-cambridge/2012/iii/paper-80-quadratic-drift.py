"""Quadratic ice-drift calculation from the explicit force balance.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Still water, no pressure slope or pack forces, wind speed much greater
than ice speed, no intrinsic boundary-layer turning. The drag convention
is rho*C*|v|*v. Effective air and water areas are taken equal. Only the
basename PNG is written to the caller's cwd; MPLCONFIGDIR is respected.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def drift(wind, mass_per_area):
    a = 1.3 * 1.5e-3 * wind**2
    b = 1025 * 4e-3
    coriolis = mass_per_area * 1.4e-4
    speed2 = 2 * a**2 / (coriolis**2 + np.sqrt(coriolis**4 + 4*b*b*a*a))
    speed = np.sqrt(speed2)
    angle = np.degrees(np.arctan2(coriolis, b*speed))
    return speed, angle


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    wind = np.linspace(1, 30, 350)
    fig, axes = plt.subplots(1, 2, figsize=(10.5001, 4.5001), dpi=100)
    for mu, label, color in [(900, "Thin floe: μ = 900 kg/m²", "#225ea8"),
                              (1e5, "Deep berg: μ = 100,000 kg/m²", "#d95f0e")]:
        u, theta = drift(wind, mu)
        axes[0].plot(wind, u, label=label, color=color, lw=2.5)
        axes[1].plot(wind, theta, label=label, color=color, lw=2.5)
    axes[0].set_ylabel("Ice speed relative to still water (m/s)")
    axes[0].set_title("Quadratic-drag equilibrium speed")
    axes[1].set_ylabel("Magnitude of wind-relative turning (degrees)")
    axes[1].set_ylim(0, 95)
    axes[1].set_title("Mass per drag area controls turning")
    for ax in axes:
        ax.set_xlabel("Wind speed (m/s)")
        ax.set_xlim(1, 30)
        ax.grid(alpha=0.20)
    axes[0].legend(loc="upper left", fontsize=9)
    fig.text(0.5, 0.025, "Equal drag areas; |f| = 1.4×10⁻⁴ s⁻¹; quadratic stresses; no ocean current or intrinsic drag turning.",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=0.075, right=0.985, bottom=0.22, top=0.89, wspace=0.30)
    fig.savefig(Path("paper-80-quadratic-drift.png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
