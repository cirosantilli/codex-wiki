"""Local coexistence tangents from stipulated data.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.6))
    fig.subplots_adjust(left=0.09, right=0.96, bottom=0.34, top=0.77, wspace=0.34)
    fig.suptitle(r"Coexistence slope: $dp/dT=L/(T\,\Delta v)$", y=0.97, fontsize=19)
    fig.text(0.5, 0.88, "Local tangents from stipulated inputs; not measured phase diagrams",
             ha="center", fontsize=12)
    vapor_slope = 40000 * 10000 / (8.314 * 300**2) / 1000
    water_slope = 334000 / (273.15 * (1 / 1000 - 1 / 917)) / 1e6
    models = [
        (axes[0], np.linspace(-2, 2, 100), vapor_slope, 1,
         "Liquid → gas: positive volume jump", "Pressure change (kPa)", "#146a92"),
        (axes[1], np.linspace(-0.08, 0.08, 100), water_slope, 1 / water_slope,
         "Ice → water: negative volume jump", "Pressure change (MPa)", "#a74828"),
    ]
    for ax, dt, slope, step_t, title, ylabel, color in models:
        ax.plot(dt, slope * dt, color=color, lw=3)
        ax.axhline(0, color="0.65", lw=0.8)
        ax.axvline(0, color="0.65", lw=0.8)
        step_p = slope * step_t
        ax.plot([0, step_t, step_t], [0, 0, step_p], "--", color="0.3", lw=1.5)
        ax.scatter([0, step_t], [0, step_p], color=color, s=32, zorder=4)
        ax.set(title=title, xlabel="Temperature change (K)", ylabel=ylabel)
        ax.grid(alpha=0.15)
        if ax is axes[0]:
            ax.text(0.55, -0.23, "+1 K", ha="center")
            ax.text(1.08, 0.20, "+0.535\nkPa", fontsize=11)
        else:
            ax.set_xticks([-0.08, -0.04, 0, 0.04, 0.08])
            ax.text(-0.038, -0.25, "−0.0740 K", ha="center", fontsize=11)
            ax.text(-0.069, 0.32, "+1\nMPa", fontsize=11)
    fig.text(0.09, 0.20,
             r"$T=300\ \mathrm{K},\quad L_m=40.0\ \mathrm{kJ\,mol^{-1}}$" "\n"
             r"$\Delta v_m\simeq RT/p=0.24942\ \mathrm{m^3\,mol^{-1}}$" "\n"
             r"$dp/dT=+0.5346\ \mathrm{kPa\,K^{-1}}$", fontsize=12, va="top")
    fig.text(0.59, 0.20,
             r"$T_m=273.15\ \mathrm{K},\quad L=334\ \mathrm{kJ\,kg^{-1}}$" "\n"
             r"$\Delta v=1/1000-1/917=-9.0513\!\times\!10^{-5}\ \mathrm{m^3\,kg^{-1}}$" "\n"
             r"$dT_m/dp=-0.07402\ \mathrm{K\,MPa^{-1}}$", fontsize=11, va="top")
    fig.text(0.5, 0.035, "Positive latent heat: the sign of the slope follows the sign of the volume jump.",
             ha="center", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
