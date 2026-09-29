"""Compare a first-order crossing with a detour around a critical endpoint.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; writes this script's basename.png to the working directory.
This original dimensionless PT cartoon represents no named material.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, start, end, color):
    ax.annotate("", end, start,
                arrowprops={"arrowstyle": "-|>", "color": color,
                            "lw": 2, "mutation_scale": 15}, zorder=7)


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.10, right=0.98, bottom=0.16, top=0.87)
    theta = np.linspace(0.25, 4.15, 850)
    pressure = np.linspace(0.08, 6.7, 750)
    t, p = np.meshgrid(theta, pressure)
    liquid, gas = np.array([0.88, 0.95, 0.92]), np.array([1.0, 0.94, 0.86])
    width = np.maximum(0.02, 1.5 * (t - 3.0))
    weight = 0.5 * (1.0 + np.tanh((p - (2.0 * t - 1.0)) / width))
    weight[t <= 3.0] = (p[t <= 3.0] > (2.0 * t[t <= 3.0] - 1.0))
    weight[t < 1.0] = 0.0  # No stable liquid below the stipulated triple temperature.
    rgb = gas + weight[..., None] * (liquid - gas)
    solid = ((p >= 1.0) & (t < 1.0 + 0.1 * (p - 1.0))) | (
        (p < 1.0) & (t <= 1.0) & (p > np.exp(t - 1.0)))
    rgb[solid] = [0.91, 0.93, 0.96]
    ax.imshow(rgb, origin="lower", extent=(0.25, 4.15, 0.08, 6.7), aspect="auto", zorder=0)
    sub_t, vap_t, melt_p = np.linspace(0.25, 1, 200), np.linspace(1, 3, 300), np.linspace(1, 6.7, 250)
    ax.plot(sub_t, np.exp(sub_t - 1), color="#444444", lw=2)
    ax.plot(vap_t, 2 * vap_t - 1, color="#444444", lw=2)
    ax.plot(1 + 0.1 * (melt_p - 1), melt_p, color="#444444", lw=2)
    ax.plot([3, 3], [0.08, 5], ls="--", color="#aaaaaa", lw=1)
    ax.plot([0.25, 3], [5, 5], ls="--", color="#aaaaaa", lw=1)
    ax.scatter([1, 3], [1, 5], color="#222222", s=45, zorder=6)
    direct, detour = "#c05d00", "#1565b5"
    ax.plot([1.6, 3.6], [3, 3], color=direct, lw=3, zorder=5)
    ax.plot([1.6, 1.6, 3.6, 3.6], [3, 6, 6, 3], color=detour, lw=3, zorder=5)
    arrow(ax, (2.5, 3), (2.88, 3), direct)
    arrow(ax, (1.6, 3.8), (1.6, 4.45), detour)
    arrow(ax, (2.35, 6), (2.9, 6), detour)
    arrow(ax, (3.6, 4.65), (3.6, 4.0), detour)
    ax.scatter([1.6, 3.6], [3, 3], color="#222222", s=48, zorder=8)
    ax.scatter([2], [3], s=90, facecolor="white", edgecolor=direct, lw=2, zorder=9)
    ax.text(1.65, 2.66, "A (1.6, 3)", fontsize=10, ha="right")
    ax.text(3.65, 2.66, "B (3.6, 3)", fontsize=10, ha="center")
    ax.text(0.64, 3.2, "Solid", color="#34485f", ha="center")
    ax.text(2.08, 4.6, "Liquid", color="#176749", ha="center")
    ax.text(2.95, 1.4, "Gas", color="#965b13", ha="center")
    ax.text(2.6, 6.2, "Detour: no first-order crossing", color=detour, ha="center", fontsize=11)
    ax.annotate("Crossing (2, 3)", (2, 3), (2.15, 2.1), color=direct,
                fontsize=10, arrowprops={"arrowstyle": "-", "color": direct})
    ax.annotate("Critical point\n(3, 5)", (3, 5), (3.15, 5.23), fontsize=10)
    ax.text(1.07, 0.72, "Triple point", fontsize=10)
    ax.set(xlim=(0.25, 4.15), ylim=(0.08, 6.7),
           xlabel=r"Temperature coordinate $\theta=T/T_*$",
           ylabel=r"Pressure coordinate $\pi=p/p_*$")
    ax.set_xticks([1, 1.6, 2, 3, 3.6, 4])
    ax.set_yticks([1, 3, 5, 6])
    fig.suptitle("Liquid to gas: two paths with the same endpoints", fontsize=15, y=0.97)
    fig.text(0.5, 0.91, "Original dimensionless cartoon • no measured data or equation of state",
             ha="center", fontsize=10, color="#505050")
    fig.text(0.5, 0.035, "Orange: π = 3.  Blue: up to π = 6, across to θ = 3.6, then down to π = 3.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
