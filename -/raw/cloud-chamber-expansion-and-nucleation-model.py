"""Original stipulated water-vapor model, not historical data.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
No ion-dependent nucleation calculation or measured detector calibration.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

T0 = 293.15
P0 = 2339.0
GAMMA = 1.40
LM = 45000.0
R = 8.314
SIGMA = 0.075
VL = 2.99e-29
KB = 1.380649e-23


def state(expansion):
    temperature = T0 * np.asarray(expansion) ** (1.0 - GAMMA)
    actual = P0 * np.asarray(expansion) ** (-GAMMA)
    saturation = P0 * np.exp(LM / R * (1.0 / T0 - 1.0 / temperature))
    return temperature, actual, saturation, actual / saturation


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.9), layout="constrained", facecolor="white")
    fig.suptitle("Expansion promotes supersaturation; a neutral drop still faces a barrier", fontsize=15)
    expansion = np.linspace(1, 1.17, 350)
    temperature, actual, saturation, ratio = state(expansion)
    blue, orange = "#247caa", "#bb641c"

    ax = axes[0]
    ax.plot(expansion, actual / 1000, color=blue, lw=2.4, label=r"Actual $p_v$")
    ax.plot(expansion, saturation / 1000, color=orange, lw=2.4, label=r"Equilibrium $p_{\rm sat}$")
    ax.fill_between(expansion, saturation / 1000, actual / 1000, color=blue, alpha=.09)
    ax.set(title="A  Cooling beats dilution", xlabel=r"Expansion ratio $V/V_0$", ylabel="Water-vapor pressure (kPa)", ylim=(.6, 2.5))
    ax.legend(frameon=False, loc="lower left", fontsize=10)
    ax.text(.97, .96, "293.15 K → 275.31 K", transform=ax.transAxes, ha="right", va="top", fontsize=10)

    ax = axes[1]
    ax.plot(expansion, ratio, color=blue, lw=2.4)
    ax.axhline(1, color="#657581", lw=1, ls="--")
    selected = state(1.15)
    ax.scatter([1.15], [selected[3]], color=blue, s=35, zorder=3)
    ax.annotate("1.15: S = 2.3772", (1.15, selected[3]), xytext=(1.025, 2.57),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": blue})
    ax.set(title="B  Supersaturated vapor", xlabel=r"Expansion ratio $V/V_0$", ylabel=r"Saturation ratio $S=p_v/p_{\rm sat}$", ylim=(.85, 2.85))
    ax.text(.05, .08, "No droplet depletion\nor latent-heat feedback", transform=ax.transAxes, fontsize=10, color="#526573")

    ax = axes[2]
    radius = np.linspace(0, 3.6e-9, 500)
    for lam, color in [(1.10, orange), (1.15, blue)]:
        t, _, _, s = state(lam)
        driving = KB * t * np.log(s)
        free_energy = 4 * np.pi * SIGMA * radius**2 - (4 * np.pi / 3) * radius**3 * driving / VL
        critical = 2 * SIGMA * VL / driving
        barrier = 4 * np.pi * SIGMA * critical**2 / 3
        ax.plot(radius * 1e9, free_energy / (KB * t), color=color, lw=2, label=fr"$V/V_0={lam:.2f}$")
        ax.scatter([critical * 1e9], [barrier / (KB * t)], s=25, color=color, zorder=3)
    ax.set(title="C  Neutral-drop comparison", xlabel="Drop radius (nm)", ylabel=r"Formation free energy $\Delta G/(k_B T)$", ylim=(-100, 370), xlim=(0, 3.6))
    ax.axhline(0, color="#657581", lw=1)
    ax.legend(frameon=False, fontsize=10)
    ax.text(.05, .08, "Dots: critical nuclei\nIon hydration omitted", transform=ax.transAxes, fontsize=10, color="#526573")

    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=.18)
    fig.supxlabel("Stipulated water constants • ideal adiabatic carrier gas • constant latent heat and surface tension • no measured traces", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
