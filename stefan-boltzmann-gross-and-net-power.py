"""Plot emitted exitance and two-way enclosure exchange.

Run from _media; writes stefan-boltzmann-gross-and-net-power.png to CWD.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
All curves use stipulated model parameters, not experimental data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


SIGMA = 5.670374419e-8  # Approximate SI value, W m^-2 K^-4.
EPSILON, AREA, WALL_T = 0.8, 0.01, 300.0


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    temperature = np.linspace(200, 650, 451)
    exitance = SIGMA * temperature**4
    emitted = EPSILON * AREA * exitance
    absorbed = EPSILON * AREA * SIGMA * WALL_T**4
    net = emitted - absorbed
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.8, 4.8))
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.21, top=0.82, wspace=0.30)
    fig.suptitle("Emission grows as T⁴; net exchange subtracts absorbed power", fontsize=15, y=0.97)
    ax.plot(temperature, exitance / 1000, color="#b35415", lw=2.5)
    ax.set(title="Blackbody: total outward hemisphere",
           xlabel="Absolute surface temperature T (K)",
           ylabel="Radiant exitance Mᵦ (kW / m²)", xlim=(200, 650), ylim=(0, 10.5))
    for t, xytext in [(300, (255, 2.0)), (600, (440, 8.4))]:
        m = SIGMA * t**4 / 1000
        ax.scatter(t, m, color="#b35415", zorder=4, s=35)
        ax.annotate(f"{t} K: {m:.3f} kW / m²", xy=(t, m), xytext=xytext,
                    arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    ax.text(0.05, 0.95, "300 → 600 K: ×16 emission", transform=ax.transAxes, va="top", fontsize=10)
    bx.plot(temperature, emitted, label="Emitted: εσAT⁴", color="#b35415", lw=2.5)
    bx.axhline(absorbed, label="Absorbed: εσATₛ⁴", color="#24689d", lw=2, ls="--")
    bx.plot(temperature, net, label="Net outward: εσA(T⁴ − Tₛ⁴)", color="#6c4292", lw=2.5)
    bx.axhline(0, color="#777777", lw=0.8)
    bx.axvline(WALL_T, color="#777777", lw=0.8, ls=":")
    bx.scatter([WALL_T, 500], [0, EPSILON * AREA * SIGMA * (500**4 - WALL_T**4)],
               color="#6c4292", zorder=5, s=35)
    bx.annotate("Equal temperatures:\nnet = 0", xy=(300, 0), xytext=(335, 14),
                arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    bx.annotate("500 K: net 24.68 W", xy=(500, EPSILON * AREA * SIGMA * (500**4 - WALL_T**4)),
                xytext=(380, 38), arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    bx.set(title="Grey surface in black walls at Tₛ = 300 K",
           xlabel="Absolute surface temperature T (K)", ylabel="Power (W)",
           xlim=(200, 650), ylim=(-6, 85))
    bx.legend(loc="upper left", frameon=False, fontsize=9)
    for axis in (ax, bx):
        axis.grid(alpha=0.18)
    fig.text(0.5, 0.035, "Model curves • ε = 0.8, emitting area A = 0.01 m² • Full view of black isothermal walls",
             ha="center", fontsize=10, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
