"""Exact two-body Kepler energies; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    # Units: reduced mass m = semimajor axis a = coupling kappa = 1.
    eccentricity = 0.6
    phase = np.linspace(0.0, 1.0, 2401)
    mean_anomaly = 2 * np.pi * phase
    anomaly = mean_anomaly.copy()
    for _ in range(12):
        anomaly -= (anomaly - eccentricity * np.sin(anomaly) - mean_anomaly) / (
            1 - eccentricity * np.cos(anomaly)
        )
    radius = 1 - eccentricity * np.cos(anomaly)
    kinetic = 1 / radius - 0.5
    potential = -1 / radius
    # Integrate analytically using dt = (1 - e cos eta) d eta.
    residual = np.empty_like(phase)
    residual[0] = eccentricity / (1 - eccentricity)
    residual[1:] = eccentricity * np.sin(anomaly[1:]) / mean_anomaly[1:]
    boundary = np.empty_like(phase)
    boundary[0] = residual[0]
    boundary[1:] = (eccentricity * np.sin(anomaly[1:])) / (2 * np.pi * phase[1:])

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, (energy_ax, residual_ax) = plt.subplots(
        2, 1, figsize=(9, 6.8), sharex=True, gridspec_kw={"height_ratios": [1.5, 1]}
    )
    fig.patch.set_facecolor("white")
    energy_ax.plot(phase, kinetic, color="#1769aa", lw=2.2, label=r"$K(t)$")
    energy_ax.plot(phase, potential, color="#d35f16", lw=2.2, label=r"$U(t)$")
    energy_ax.axhline(-0.5, color="#333333", lw=1.7, label=r"$E=K+U=-0.5$")
    energy_ax.axhline(0.5, color="#1769aa", ls="--", lw=1.5, label=r"$\langle K\rangle_P=0.5$")
    energy_ax.axhline(-1, color="#d35f16", ls="--", lw=1.5, label=r"$\langle U\rangle_P=-1$")
    energy_ax.set_ylabel(r"Energy / $(\kappa/a)$")
    energy_ax.set_ylim(-2.8, 2.35)
    energy_ax.legend(loc="lower center", ncol=3, fontsize=10, framealpha=0.96)
    energy_ax.set_title("Kepler ellipse: varying energies, exact period averages", pad=12)

    residual_ax.plot(phase, residual, color="#1769aa", lw=3,
                     label=r"$2\langle K\rangle_T+\langle U\rangle_T$")
    residual_ax.plot(phase, boundary, color="#d35f16", ls=(0, (5, 4)), lw=1.8,
                     label=r"$[G(T)-G(0)]/T$")
    residual_ax.axhline(0, color="#444444", lw=0.8)
    quarter = len(phase) // 4
    residual_ax.scatter([0.25], [residual[quarter]], s=35, color="#222222", zorder=5)
    residual_ax.annotate(f"Quarter-period residual: {residual[quarter]:.4f}",
                         xy=(0.25, residual[quarter]), xytext=(0.39, 0.95),
                         arrowprops={"arrowstyle": "->", "color": "#444444"}, fontsize=10)
    residual_ax.set_ylabel(r"Virial residual / $(\kappa/a)$")
    residual_ax.set_xlabel(r"Elapsed time / orbital period, $T/P$")
    residual_ax.set_ylim(-0.23, 1.7)
    residual_ax.legend(loc="upper right", fontsize=10)
    for ax in (energy_ax, residual_ax):
        ax.set_facecolor("white")
        ax.axvspan(0, 0.25, color="#f4dfa5", alpha=0.32, zorder=0)
        ax.set_xlim(0, 1)
        ax.set_xticks(np.arange(0, 1.01, 0.125))
        ax.grid(alpha=0.18)
    fig.text(0.5, 0.015, "Original exact model: m = a = κ = 1, e = 0.6; shaded window T = P/4",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.045, 1, 1))
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
