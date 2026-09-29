"""Generate einstein-solid-heat-capacity.png in the current working directory.

Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
This is the vibrational heat capacity of an ideal fixed-frequency Einstein solid.
Negative exponentials avoid overflow; expm1 preserves small-x accuracy.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def heat_capacity_ratio(temperature_ratio):
    """Return C_V/(3 N k_B) for positive finite T/theta_E."""
    temperature_ratio = np.asarray(temperature_ratio, dtype=float)
    if np.any(~np.isfinite(temperature_ratio)) or np.any(temperature_ratio <= 0):
        raise ValueError("T/theta_E must be positive and finite")
    x = 1.0 / temperature_ratio
    # Squaring only after the decaying exponential avoids x**2 overflow.
    return (x * np.exp(-0.5 * x) / (-np.expm1(-x))) ** 2


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    temperature_ratio = np.linspace(0.02, 3.0, 1500)
    cases = np.array([0.1, 0.5, 1.0, 2.0])
    values = heat_capacity_ratio(cases)
    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    fig.subplots_adjust(left=0.11, right=0.97, bottom=0.15, top=0.85)
    ax.axhline(1, color="#555555", ls="--", lw=1.6,
               label="Classical Dulong–Petit limit")
    ax.plot(temperature_ratio, heat_capacity_ratio(temperature_ratio),
            color="#247aa6", lw=2.5, label="Einstein solid")
    ax.scatter(cases, values, color="#d58526", edgecolor="white", s=65, zorder=4)
    label_positions = [(0.32, 0.18), (0.24, 0.46), (1.05, 0.68), (2.03, 0.80)]
    for ratio, value, position in zip(cases, values, label_positions):
        ax.annotate(rf"$T/\theta_E={ratio:g}$" + "\n" +
                    rf"$C_V/(3Nk_B)={value:.5f}$",
                    xy=(ratio, value), xytext=position, fontsize=10,
                    ha="left", va="center",
                    arrowprops={"arrowstyle": "-", "color": "#77532b", "lw": 1},
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.set(xlim=(0, 3.05), ylim=(0, 1.13),
           xlabel=r"Temperature ratio $T/\theta_E$",
           ylabel=r"Vibrational heat capacity $C_V/(3Nk_B)$")
    ax.set_title("Einstein solid: quantum freeze-out and the classical limit\n"
                 r"$3N$ independent oscillators, one fixed frequency; "
                 r"$\theta_E=\hbar\omega/k_B$", fontsize=12, pad=13)
    ax.legend(loc="upper left", facecolor="white", edgecolor="none",
              framealpha=1, fontsize=10)
    ax.set_axisbelow(True)
    ax.grid(alpha=0.2)
    fig.savefig(Path.cwd() / "einstein-solid-heat-capacity.png", dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
