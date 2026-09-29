"""Draw synthetic Arrhenius plots and local apparent activation energies.

Output the matching PNG to CWD. Tested with Python 3.14,
matplotlib 3.10.7 and numpy 2.3.5. No laboratory data are used.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

R = 8.314462618  # J/(mol K), value used consistently in the article
E0 = 60000.0  # J/mol, synthetic exponent parameter
T0 = 300.0  # K
K0 = 0.1  # s^-1


def rate(temperature, power):
    return K0 * (temperature / T0) ** power * np.exp(
        E0 / R * (1 / T0 - 1 / temperature)
    )


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    temperature = np.linspace(280, 340, 401)
    samples = np.arange(280, 341, 10)
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.2, 5.0), dpi=110)
    fig.subplots_adjust(left=0.075, right=0.965, bottom=0.22, top=0.77, wspace=0.33)
    colors = ["#275f9e", "#bd6719"]
    for power, color in zip([0, 2], colors):
        left.plot(1000 / temperature, np.log(rate(temperature, power) / K0),
                  color=color, lw=2.5)
        left.scatter(1000 / samples, np.log(rate(samples, power) / K0),
                     color=color, s=27, zorder=3)
        right.plot(temperature, (E0 + power * R * temperature) / 1000,
                   color=color, lw=2.5)
    tangent_slope = -(E0 + 2 * R * T0) / (1000 * R)
    local_x = np.linspace(3.19, 3.48, 60)
    left.plot(local_x, tangent_slope * (local_x - 1000 / T0),
              color="#444444", ls="--", lw=1.5)
    left.scatter([1000 / T0], [0], facecolor="white", edgecolor="#333333",
                 s=65, zorder=4)
    left.annotate(f"300 K tangent\nslope {tangent_slope:.5f}",
                  xy=(3.40, tangent_slope * (3.40 - 1000 / T0)),
                  xytext=(3.19, -1.8), fontsize=10,
                  arrowprops={"arrowstyle": "->", "color": "#444444"})
    left.set(xlabel=r"$X=1000\,\mathrm{K}/T$", ylabel=r"$\ln[k(T)/k(300\,\mathrm{K})]$",
             xlim=(2.89, 3.62), ylim=(-2.5, 3.6))
    right.set(xlabel="Temperature T (K)",
              ylabel=r"Apparent $E_a$ (kJ/mol)", xlim=(280, 340), ylim=(58.5, 67.8))
    right.text(287, 60.35, r"$E_a=E_0=60$", color=colors[0])
    right.text(287, 66.0, r"$E_{a,\mathrm{app}}=E_0+2RT$", color=colors[1])
    right.scatter([300], [(E0 + 2 * R * 300) / 1000], color=colors[1], s=35)
    right.text(303, 64.2, "64.9887 at 300 K", color=colors[1], fontsize=10)
    for ax in [left, right]:
        ax.grid(alpha=0.17)
    fig.suptitle("Synthetic rates: same exponent parameter, different slopes", fontsize=16, y=0.97)
    fig.text(0.5, 0.855,
             "Blue: constant prefactor    Orange: prefactor ∝ (T/300 K)²\n"
             "Both: E₀ = 60 kJ/mol and k(300 K) = 0.100 s⁻¹", ha="center", fontsize=12)
    fig.text(0.5, 0.07,
             "Markers are model evaluations, not measured data.\n"
             "A local tangent and a line fitted across an interval need not give the same apparent energy.",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
