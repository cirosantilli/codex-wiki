"""Illustrate a stipulated 0.5 kg ice-to-water heating budget at 1 atm.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes sensible-and-latent-heating-curve.png to the current directory.
Rounded constant parameters are model assumptions, not precision data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    mass, c_ice, latent, c_water = 0.5, 2.1, 334.0, 4.18
    q_ice = mass * c_ice * 10.0
    q_melt = mass * latent
    q_water = mass * c_water * 20.0
    plateau_end = q_ice + q_melt
    total = plateau_end + q_water
    heat = np.unique(np.r_[np.linspace(0.0, total, 1500), q_ice, 94.0, plateau_end])
    temperature = np.where(
        heat < q_ice, -10.0 + heat / (mass * c_ice),
        np.where(heat <= plateau_end, 0.0, (heat - plateau_end) / (mass * c_water)),
    )
    liquid_fraction = np.clip((heat - q_ice) / q_melt, 0.0, 1.0)
    assert np.allclose([q_ice, q_melt, q_water, total], [10.5, 167.0, 41.8, 219.3])
    recovered = (mass * c_ice * (np.minimum(temperature, 0.0) + 10.0)
                 + q_melt * liquid_fraction
                 + mass * c_water * np.maximum(temperature, 0.0))
    assert np.allclose(recovered, heat)
    midpoint = np.flatnonzero(heat == 94.0)[0]
    assert temperature[midpoint] == 0.0 and liquid_fraction[midpoint] == 0.5

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(9.5, 5.3), dpi=120)
    fig.subplots_adjust(left=0.09, right=0.97, bottom=0.28, top=0.80)
    fig.suptitle("Heating ice to water: most of the heat goes into melting", fontsize=15)
    fig.text(0.5, 0.88, "Illustrative 0.5 kg closed sample at fixed pressure, 1 atm", ha="center")
    blue, orange, green = "#216a99", "#b8531c", "#24765c"
    for low, high, color in [(0.0, q_ice, blue), (q_ice, plateau_end, orange),
                             (plateau_end, total, green)]:
        selected = (heat >= low) & (heat <= high)
        ax.plot(heat[selected], temperature[selected], color=color, lw=3)
    ax.axvspan(q_ice, plateau_end, color=orange, alpha=0.07)
    for boundary in (q_ice, plateau_end):
        ax.axvline(boundary, color="#777777", ls=":", lw=1)
    ax.plot([0, q_ice, 94, plateau_end, total], [-10, 0, 0, 0, 20],
            "o", color="#343b43", ms=4)
    ax.annotate("Ice warms: −10 → 0 °C\n10.5 kJ sensible heat",
                xy=(q_ice / 2, -5), xytext=(27, -12), color=blue,
                arrowprops={"arrowstyle": "->", "color": blue}, fontsize=10)
    ax.text(94, 17, "Ice + water at 0 °C\n167 kJ latent heat", ha="center", color=orange)
    ax.annotate("94 kJ total: half liquid by mass", xy=(94, 0), xytext=(94, 8),
                ha="center", fontsize=10, color=orange,
                arrowprops={"arrowstyle": "->", "color": orange})
    ax.annotate("Water warms: 0 → 20 °C\n41.8 kJ sensible heat",
                xy=(195, (195 - plateau_end) / (mass * c_water)), xytext=(132, 26),
                color=green, fontsize=10,
                arrowprops={"arrowstyle": "->", "color": green})
    ax.text(q_ice + 3, -2.5, "10.5 kJ", fontsize=9, color="#555555")
    ax.text(plateau_end - 3, -2.5, "177.5 kJ", ha="right", fontsize=9, color="#555555")
    ax.set(xlim=(-3, 225), ylim=(-16, 32), yticks=[-10, 0, 10, 20, 30],
           xticks=[0, 50, 100, 150, 200, total],
           xlabel="Total supplied heat Q = ΔH from the initial ice (kJ)",
           ylabel="Temperature (°C)")
    ax.set_xticklabels(["0", "50", "100", "150", "200", "219.3"])
    ax.grid(alpha=0.16)
    fig.text(0.5, 0.15, "Stipulated constants: c_ice = 2.1; c_water = 4.18 kJ/(kg K); Lf = 334 kJ/kg",
             ha="center", fontsize=10)
    fig.text(0.5, 0.095, "Quasistatic heating; only pressure–volume work; no heat loss or material loss",
             ha="center", fontsize=10)
    fig.text(0.5, 0.04, "Total: 10.5 + 167 + 41.8 = 219.3 kJ; melting uses 76.2%", ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)
    print(f"Stages: {q_ice:g} + {q_melt:g} + {q_water:g} = {total:g} kJ")


if __name__ == "__main__":
    main()
