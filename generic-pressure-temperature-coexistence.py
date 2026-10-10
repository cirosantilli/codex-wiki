"""Draw a generic dimensionless PT coexistence cartoon, not material data.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; writes this script's basename.png to the working directory.
The stipulated curves describe topology only, not an equation of state.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.10, right=0.98, bottom=0.16, top=0.87)
    theta = np.linspace(0.25, 4.15, 850)
    pressure = np.linspace(0.08, 6.7, 750)
    t, p = np.meshgrid(theta, pressure)
    liquid = np.array([0.88, 0.95, 0.92])
    gas = np.array([1.0, 0.94, 0.86])
    # Smooth background beyond the endpoint; no extra fluid boundary.
    width = np.maximum(0.02, 1.5 * (t - 3.0))
    weight = 0.5 * (1.0 + np.tanh((p - (2.0 * t - 1.0)) / width))
    weight[t <= 3.0] = (p[t <= 3.0] > (2.0 * t[t <= 3.0] - 1.0))
    weight[t < 1.0] = 0.0  # No stable liquid below the stipulated triple temperature.
    rgb = gas + weight[..., None] * (liquid - gas)
    solid = ((p >= 1.0) & (t < 1.0 + 0.1 * (p - 1.0))) | (
        (p < 1.0) & (t <= 1.0) & (p > np.exp(t - 1.0)))
    rgb[solid] = [0.91, 0.93, 0.96]
    ax.imshow(rgb, origin="lower", extent=(0.25, 4.15, 0.08, 6.7),
              aspect="auto", interpolation="nearest", zorder=0)
    sub_t = np.linspace(0.25, 1.0, 200)
    vap_t = np.linspace(1.0, 3.0, 300)
    melt_p = np.linspace(1.0, 6.7, 250)
    ax.plot(sub_t, np.exp(sub_t - 1.0), color="#303a47", lw=2.3)
    ax.plot(vap_t, 2.0 * vap_t - 1.0, color="#303a47", lw=2.3)
    ax.plot(1.0 + 0.1 * (melt_p - 1.0), melt_p, color="#303a47", lw=2.3)
    ax.scatter([1.0, 3.0], [1.0, 5.0], s=[55, 65], color="#202631", zorder=5)
    ax.text(0.64, 3.65, "Solid", ha="center", weight="bold", color="#34485f")
    ax.text(2.12, 5.7, "Liquid", ha="center", weight="bold", color="#176749")
    ax.text(2.95, 1.6, "Gas", ha="center", weight="bold", color="#965b13")
    ax.text(3.65, 6.05, "Connected\nfluid region", ha="center", fontsize=11)
    arrow = {"arrowstyle": "-", "color": "#555555", "lw": 1}
    ax.annotate("Triple point (1, 1)\nThree distinct phases", (1, 1), (1.55, 0.45),
                fontsize=10, arrowprops=arrow)
    ax.annotate("Critical point (3, 5)\nLiquid and gas merge", (3, 5), (3.12, 3.6),
                fontsize=10, arrowprops=arrow)
    ax.text(0.34, 0.22, "Sublimation", fontsize=10)
    ax.text(1.19, 3.6, "Melting", rotation=83, fontsize=10)
    ax.text(1.74, 3.16, "Liquid–gas coexistence", rotation=31, fontsize=10)
    ax.set(xlim=(0.25, 4.15), ylim=(0.08, 6.7),
           xlabel=r"Temperature coordinate $\theta=T/T_*$",
           ylabel=r"Pressure coordinate $\pi=p/p_*$")
    ax.set_xticks([1, 2, 3, 4])
    ax.set_yticks([1, 2, 3, 4, 5, 6])
    fig.suptitle("One-component pressure–temperature phase diagram", fontsize=15, y=0.97)
    fig.text(0.5, 0.91, "Original dimensionless cartoon • no measured data or equation of state",
             ha="center", fontsize=10, color="#505050")
    fig.text(0.5, 0.035, "Curves: sublimation  π = exp(θ − 1); vaporization  π = 2θ − 1; melting  θ = 1 + 0.1(π − 1)",
             ha="center", fontsize=9)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
