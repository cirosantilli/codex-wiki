"""Pressure and logarithmic plots of a stipulated constant-latent-heat model.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    gas_constant, latent_heat, reference_t, reference_p = 8.314, 40000, 300, 10
    temperature = np.linspace(280, 340, 400)
    log_ratio = latent_heat / gas_constant * (1 / reference_t - 1 / temperature)
    pressure = reference_p * np.exp(log_ratio)
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.8, 5.6))
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.21, top=0.75, wspace=0.32)
    fig.suptitle("Idealized vapor pressure: one model, two views", fontsize=19, y=0.97)
    fig.text(0.5, 0.87,
             r"$L_m=40.0\ \mathrm{kJ\,mol^{-1}},\quad p_1=10.0\ \mathrm{kPa},\quad T_1=300\ \mathrm{K}$",
             ha="center", fontsize=14)
    left.plot(temperature, pressure, color="#146a92", lw=3, label="Integrated model")
    slope = reference_p * latent_heat / (gas_constant * reference_t**2)
    left.plot(temperature, reference_p + slope * (temperature - reference_t),
              "--", color="0.45", lw=1.6, label="Tangent at 300 K")
    left.set(xlabel="Temperature (K)", ylabel="Saturation pressure (kPa)",
             title="Curved on ordinary axes", xlim=(280, 340), ylim=(0, 75))
    left.legend(loc="upper left", fontsize=10, frameon=False)
    right.plot(1000 / temperature, log_ratio, color="#146a92", lw=3)
    right.set(xlabel=r"Inverse temperature $1/T$ ($10^{-3}\ \mathrm{K^{-1}}$)",
              ylabel=r"$\ln(p/p_1)$", title="Linear at constant latent heat")
    for temp, offset in [(300, (-18, 14)), (330, (-50, 14))]:
        logr = latent_heat / gas_constant * (1 / reference_t - 1 / temp)
        p = reference_p * np.exp(logr)
        left.scatter(temp, p, color="#a74828", s=35, zorder=5)
        right.scatter(1000 / temp, logr, color="#a74828", s=35, zorder=5)
        left.annotate(f"{temp} K\n{p:.2f} kPa", (temp, p), xytext=offset,
                      textcoords="offset points", fontsize=11)
        right.annotate(f"{temp} K", (1000 / temp, logr), xytext=(10, -20),
                       textcoords="offset points", fontsize=11)
    for ax in (left, right):
        ax.grid(alpha=0.18)
    fig.text(0.5, 0.095,
             r"$\ln(p/p_1)=(L_m/R)(1/T_1-1/T)$; slope against $1/T$: $-L_m/R=-4811.16\ \mathrm{K}$",
             ha="center", fontsize=13)
    fig.text(0.5, 0.04, "Stipulated pure-substance model over 280–340 K; not experimental water data.",
             ha="center", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
