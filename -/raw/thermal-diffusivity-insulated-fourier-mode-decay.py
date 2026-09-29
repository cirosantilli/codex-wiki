"""Original insulated-bar model; run from _media. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    length = 0.010
    conductivity, density = 2.0, 1000.0
    capacities = (1000.0, 4000.0)
    colors = ("#196ca3", "#bf5620")
    x = np.linspace(0, length, 601)
    times = np.linspace(0, 60, 601)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), layout="constrained")
    fig.suptitle("Same conductivity, different thermal storage", fontsize=15)
    axes[0].plot(x * 1000, np.cos(np.pi * x / length), color="#555555", ls="--", label="Both at t = 0")
    for capacity, color, letter in zip(capacities, colors, ("A", "B")):
        alpha = conductivity / (density * capacity)
        tau = 1 / (alpha * (np.pi / length) ** 2)
        fraction = np.exp(-10 / tau)
        label = rf"{letter}: $\rho c$ = {density * capacity / 1e6:g} MJ m$^{{-3}}$ K$^{{-1}}$"
        axes[0].plot(x * 1000, fraction * np.cos(np.pi * x / length), color=color, lw=2.5, label=f"{letter} at t = 10 s")
        axes[1].plot(times, np.exp(-times / tau), color=color, lw=2.5, label=label)
        axes[1].scatter([10], [fraction], color=color, s=35, zorder=3)
        axes[1].annotate(f"{letter}: {fraction:.3f}", (10, fraction), xytext=(15, 8), textcoords="offset points", color=color)
    axes[0].set(xlabel="Position x (mm)", ylabel=r"$(T-\overline{T})/A_0$", title="Insulated ends; spatial mode n = 1", xlim=(0, 10), ylim=(-1.12, 1.12))
    axes[1].axvline(10, color="#888888", ls=":", lw=1)
    axes[1].set(xlabel="Time t (s)", ylabel=r"Remaining amplitude $A(t)/A_0$", title=r"$A(t)/A_0 = \exp[-\alpha(\pi/L)^2t]$", xlim=(0, 60), ylim=(0, 1.08))
    for axis in axes:
        axis.grid(alpha=0.2)
        axis.legend(loc="upper right", fontsize=9)
    fig.text(0.5, -0.02, "Stipulated material models: k = 2 W/(m K), density = 1000 kg/m³, L = 10 mm; no measured data", ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
