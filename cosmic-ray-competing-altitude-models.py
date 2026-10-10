"""Generate hypothetical altitude attenuation curves and a density confound.

Run from _media. Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Pure illustrative attenuation: no fitted Hess data and no shower production.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def altitude_model(height_km):
    """Return ground, extraterrestrial, fixed-gas and vented responses."""
    x = np.exp(-np.asarray(height_km) / 8)
    ground = 0.8 * np.exp(-(1 - x) / 0.08)
    extraterrestrial = 6.0 * np.exp(-x / 0.45)
    fixed = 0.15 + ground + extraterrestrial
    return ground, extraterrestrial, fixed, fixed * x


def draw():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.8), dpi=120, facecolor="white")
    fig.subplots_adjust(top=0.77, bottom=0.24, left=0.075, right=0.975, wspace=0.27)
    fig.suptitle("Competing altitude trends and the gas-density confound", fontsize=17, y=0.96)
    fig.text(0.5, 0.875, "Hypothetical attenuation model • no shower production • no Hess data points",
             ha="center", fontsize=11, color="#555555")
    z = np.linspace(0, 6, 501)
    ground, extraterrestrial, fixed, vented = altitude_model(z)
    ax = axes[0]
    ax.plot(z, fixed, color="#bb4d21", lw=2.8, label="Ground + extraterrestrial + B")
    ax.plot(z, ground + 0.15, color="#245d8d", lw=2.5, label="Ground only + B")
    ax.plot(z, extraterrestrial, color="#38815b", lw=2, ls="--", label="Extraterrestrial component E")
    ax.axhline(0.15, color="#888888", lw=1, ls=":")
    x_min = (1 / 0.08 - np.log(0.8 * 0.45 / (6 * 0.08))) / (1 / 0.08 + 1 / 0.45)
    z_min = -8 * np.log(x_min)
    q_min = altitude_model(z_min)[2]
    ax.annotate("Model minimum\n1.13 km", xy=(z_min, q_min), xytext=(2.9, 0.62),
                arrowprops={"arrowstyle": "->", "color": "#555555"}, ha="center", fontsize=10)
    ax.set(title="Competing source hypotheses", ylabel="Fixed-gas response (arbitrary units)", ylim=(0, 2.35))
    ax.legend(loc="upper left", fontsize=8.5, framealpha=1)

    ax = axes[1]
    ax.plot(z, fixed / fixed[0], color="#bb4d21", lw=2.8, label="Fixed detector gas density")
    ax.plot(z, vented / vented[0], color="#245d8d", lw=2.5, label="Vented, no density correction")
    ax.plot(z, np.exp(-z / 8), color="#777777", ls=":", lw=1.8, label=r"Gas density ratio $\rho/\rho_0$")
    ax.set(title="Same mixed radiation field", ylabel="Response / own ground response", ylim=(0.4, 1.55))
    ax.legend(loc="upper left", fontsize=8.5, framealpha=1)
    ax.text(5.85, fixed[-1] / fixed[0] + 0.04, f"{fixed[-1] / fixed[0]:.2f}",
            color="#bb4d21", ha="right", fontsize=11)
    ax.text(5.85, vented[-1] / vented[0] + 0.04, f"{vented[-1] / vented[0]:.2f}",
            color="#245d8d", ha="right", fontsize=11)
    for ax in axes:
        ax.set(xlabel="Altitude above ground (km)", xlim=(0, 6))
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.135, r"$H=8$ km,   $G_0=0.8$,   $E_{\rm top}=6$,   $B=0.15$,   "
             r"$\Lambda_g/X_0=0.08$,   $\Lambda_e/X_0=0.45$", ha="center", fontsize=11)
    fig.text(0.5, 0.065, "The vented model assumes response ∝ gas density; dividing by density recovers the fixed-gas curve.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    draw()
