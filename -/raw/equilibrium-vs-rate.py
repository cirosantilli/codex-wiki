"""Compare relaxation speeds and the shared ideal-mixture free-energy minimum.

Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp python ../equilibrium-vs-rate.py
Writes an opaque white PNG to the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    kf, kr = 0.3, 0.1
    ratio = kf / kr
    x_eq = ratio / (1.0 + ratio)
    time = np.linspace(0.0, 14.0, 561)
    base = x_eq * (1.0 - np.exp(-(kf + kr) * time))
    faster = x_eq * (1.0 - np.exp(-2.0 * (kf + kr) * time))
    x = np.linspace(0.0, 1.0, 1001)

    def free_energy(fraction):
        fraction = np.asarray(fraction)
        other = 1.0 - fraction
        return (fraction * np.log(np.maximum(fraction, np.finfo(float).tiny))
                + other * np.log(np.maximum(other, np.finfo(float).tiny))
                - fraction * np.log(ratio))

    excess = free_energy(x) - free_energy(x_eq)
    assert np.allclose(faster, x_eq * (1.0 - np.exp(-(kf + kr) * (2.0 * time))))
    assert np.isclose(x_eq, 0.75)
    assert np.isclose(x[np.argmin(excess)], x_eq)
    assert np.all(excess >= -1e-12)
    assert np.isclose(free_energy(x_eq), -np.log(4.0))
    driving = np.log(x[1:-1] / (1 - x[1:-1])) - np.log(ratio)
    net = kf * (1 - x[1:-1]) - kr * x[1:-1]
    assert np.all(driving * net <= 1e-12)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (speed, potential) = plt.subplots(1, 2, figsize=(10.0, 4.6), dpi=120)
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.19, top=0.79, wspace=0.32)
    fig.suptitle("Same equilibrium and free energy; twice the approach speed", fontsize=14)
    blue, orange, green = "#236a9e", "#bc542c", "#257653"
    speed.plot(time, base, color=blue, lw=2.5, label=r"0.3 / 0.1 s$^{-1}$; $\tau=2.5$ s")
    speed.plot(time, faster, color=orange, lw=2.5, ls="--", label=r"0.6 / 0.2 s$^{-1}$; $\tau=1.25$ s")
    speed.axhline(x_eq, color=green, ls=":", lw=1.5)
    speed.text(6.5, 0.77, "[B]eq = 0.75 M", color=green)
    speed.set(xlabel="Time (s)", ylabel="[B] (M)", xlim=(0, 14), ylim=(0, 0.87))
    speed.set_title("Approach from pure A", fontsize=12)
    speed.legend(loc="lower right", fontsize=9, frameon=False)
    potential.plot(x, excess, color="#654994", lw=2.5)
    potential.scatter([x_eq], [0], color=green, s=45, zorder=3)
    potential.axvline(x_eq, color=green, ls=":", lw=1)
    potential.annotate("Minimum at x = 0.75\nfor both rate pairs", xy=(x_eq, 0),
                       xytext=(0.48, 0.48), color=green,
                       arrowprops={"arrowstyle": "->", "color": green})
    potential.set(xlabel=r"B fraction: $x=[\mathrm{B}]/([\mathrm{A}]+[\mathrm{B}])$",
                  ylabel=r"$(F-F_{\rm eq})/(nRT)$", xlim=(0, 1), ylim=(-0.06, 1.5))
    potential.set_title("Ideal mixture at fixed T and V", fontsize=12)
    for axis in (speed, potential):
        axis.grid(alpha=0.16)
    fig.text(0.52, 0.045, r"Shared $K=3$: $F/(nRT)=(1-x)\ln(1-x)+x\ln x-x\ln3$ + constant",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / "equilibrium-vs-rate.png", transparent=False)
    plt.close(fig)
    print(f"K={ratio:g}; equilibrium fraction={x_eq:g}; relaxation times=2.5, 1.25 s")


if __name__ == "__main__":
    main()
