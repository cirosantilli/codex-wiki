"""Plot the stipulated steady bar and distinguish heat flux from heat rate.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes fourier-conduction-steady-bar.png in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    length, area, conductivity = 0.10, 0.010, 2.0
    hot, cold = 40.0, 20.0  # Celsius; differences have the same size in kelvin.
    x = np.linspace(0.0, length, 201)
    gradient = (cold - hot) / length
    temperature = hot + gradient * x
    flux = -conductivity * gradient
    rate = area * flux
    assert np.allclose([gradient, flux, rate], [-200.0, 400.0, 4.0])

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (tax, qax) = plt.subplots(2, 1, figsize=(8.2, 6.4), dpi=120,
                                  sharex=True, height_ratios=[1.4, 1])
    fig.subplots_adjust(left=0.12, right=0.96, bottom=0.18, top=0.84, hspace=0.22)
    fig.suptitle("Steady conduction: falling temperature, constant heat flux", fontsize=14)
    fig.text(0.5, 0.91, "L = 0.10 m    |    A = 0.010 m²    |    k = 2 W/(m K)",
             ha="center", fontsize=11)
    tax.plot(x, temperature, color="#c44e28", lw=3)
    tax.fill_between(x, 18, temperature, color="#c44e28", alpha=0.08)
    tax.plot([0, length], [hot, cold], "o", color="#c44e28", ms=6)
    tax.annotate("40°C", (0, hot), xytext=(6, 8), textcoords="offset points")
    tax.annotate("20°C", (length, cold), xytext=(-6, 8),
                 textcoords="offset points", ha="right")
    tax.text(0.058, 32, "dT/dx = −200 K/m", color="#9a3e20", ha="center")
    tax.annotate("", xy=(0.087, 45), xytext=(0.013, 45),
                 arrowprops={"arrowstyle": "->", "lw": 2, "color": "#216a99"})
    tax.text(0.05, 46.3, "Heat flows from hot to cold", ha="center", color="#216a99")
    tax.set_ylabel("Temperature T (°C)")
    tax.set_ylim(18, 50)
    tax.set_yticks([20, 30, 40])

    qax.plot(x, np.full_like(x, flux), color="#216a99", lw=3)
    qax.text(0.05, 440, "q = −k dT/dx = 400 W/m²", ha="center", color="#216a99")
    qax.text(0.05, 115, "Rate through the whole cross section:\n"
             "Q̇ = A q = 0.010 m² × 400 W/m² = 4 W", ha="center", va="center",
             bbox={"facecolor": "white", "edgecolor": "#b8c3cc", "pad": 7})
    qax.set_ylabel("Heat flux q (W/m²)")
    qax.set_ylim(0, 520)
    qax.set_yticks([0, 200, 400])
    qax.set_xlabel("Position x (m): hot end → cold end", labelpad=8)
    for ax in (tax, qax):
        ax.set_xlim(-0.002, 0.102)
        ax.set_xticks([0, 0.025, 0.050, 0.075, 0.100],
                      ["0", "0.025", "0.050", "0.075", "0.100"])
        ax.grid(alpha=0.18)
    fig.text(0.5, 0.075, "One-dimensional steady state; constant k and A; fixed end temperatures",
             ha="center", fontsize=10)
    fig.text(0.5, 0.035, "No internal sources or side losses; stipulated isotropic material",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)
    print(f"gradient={gradient:g} K/m; q={flux:g} W/m²; Qdot={rate:g} W")


if __name__ == "__main__":
    main()
