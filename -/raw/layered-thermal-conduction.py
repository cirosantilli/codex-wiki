"""Plot two stipulated layers in perfect contact and their constant heat flux.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes layered-thermal-conduction.png in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    lengths = np.array([0.10, 0.10])
    conductivities = np.array([1.0, 4.0])
    area, hot, cold = 0.010, 40.0, 20.0
    resistances_per_area = lengths / conductivities
    flux = (hot - cold) / resistances_per_area.sum()
    rate = area * flux
    drops = flux * resistances_per_area
    interface = hot - drops[0]
    gradients = -flux / conductivities
    x1 = np.linspace(0.0, lengths[0], 101)
    x2 = np.linspace(lengths[0], lengths.sum(), 101)
    t1 = hot + gradients[0] * x1
    t2 = interface + gradients[1] * (x2 - lengths[0])
    assert np.allclose([flux, rate, interface], [160.0, 1.6, 24.0])
    assert np.allclose(drops, [16.0, 4.0])
    assert np.allclose(gradients, [-160.0, -40.0])
    assert np.isclose(t1[-1], t2[0]) and np.isclose(t2[-1], cold)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (tax, qax) = plt.subplots(2, 1, figsize=(8.2, 6.4), dpi=120,
                                  sharex=True, height_ratios=[1.5, 1])
    fig.subplots_adjust(left=0.12, right=0.96, bottom=0.18, top=0.83, hspace=0.22)
    fig.suptitle("Layers in series: a temperature kink, continuous heat flux", fontsize=14)
    fig.text(0.5, 0.91, "Each layer: L = 0.10 m    |    Shared area A = 0.010 m²",
             ha="center", fontsize=11)
    orange, blue = "#c44e28", "#216a99"
    tax.plot(x1, t1, color=orange, lw=3)
    tax.plot(x2, t2, color=blue, lw=3)
    tax.plot([0, 0.1, 0.2], [hot, interface, cold], "o", color="#303b43", ms=5)
    tax.annotate("40°C", (0, hot), xytext=(6, 8), textcoords="offset points")
    tax.annotate("Interface: 24°C", (0.1, interface), xytext=(16, 18),
                 textcoords="offset points", fontsize=10,
                 arrowprops={"arrowstyle": "->", "color": "#555555"})
    tax.annotate("20°C", (0.2, cold), xytext=(-5, 10),
                 textcoords="offset points", ha="right")
    tax.text(0.05, 43, "k₁ = 1 W/(m K)", ha="center", color=orange)
    tax.text(0.15, 43, "k₂ = 4 W/(m K)", ha="center", color=blue)
    tax.text(0.020, 23, "Drop: 16 K\nSlope: −160 K/m", fontsize=10, color=orange)
    tax.text(0.15, 34, "Drop: 4 K\nSlope: −40 K/m", ha="center", fontsize=10, color=blue)
    tax.set_ylabel("Temperature T (°C)")
    tax.set_ylim(17, 47)
    tax.set_yticks([20, 24, 30, 40])

    qax.plot([0, 0.2], [flux, flux], color="#24765c", lw=3)
    qax.text(0.1, 179, "q = 160 W/m² on both sides", ha="center", color="#24765c")
    qax.text(0.1, 53, "r₁ + r₂ = 0.100 + 0.025 = 0.125 m² K/W\n"
             "Q̇ = A q = 1.6 W; R₁ + R₂ = 12.5 K/W", ha="center", va="center",
             bbox={"facecolor": "white", "edgecolor": "#b8c3cc", "pad": 7})
    qax.set_ylabel("Heat flux q (W/m²)")
    qax.set_ylim(0, 220)
    qax.set_yticks([0, 80, 160])
    qax.set_xlabel("Position x (m): hot end → cold end", labelpad=8)
    for ax in (tax, qax):
        ax.axvspan(0, 0.1, color=orange, alpha=0.045)
        ax.axvspan(0.1, 0.2, color=blue, alpha=0.045)
        ax.axvline(0.1, color="#808080", lw=1, ls="--", zorder=0)
        ax.set_xlim(-0.004, 0.204)
        ax.set_xticks([0, 0.05, 0.10, 0.15, 0.20], ["0", "0.05", "0.10", "0.15", "0.20"])
        ax.grid(alpha=0.18)
    fig.text(0.5, 0.075, "One-dimensional steady state; perfect contact; constant k in each isotropic layer",
             ha="center", fontsize=9.5)
    fig.text(0.5, 0.035, "Fixed outer temperatures; no internal sources or side losses; stipulated properties",
             ha="center", fontsize=9.5)
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)
    print(f"q={flux:g} W/m²; Qdot={rate:g} W; interface={interface:g} °C; "
          f"drops={drops.tolist()} K; gradients={gradients.tolist()} K/m")


if __name__ == "__main__":
    main()
