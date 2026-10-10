"""Original half-life plots for prescribed kinetic models, not observations.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media to write the matching opaque PNG into the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    k_obs, initial = 0.50, 0.020  # L mol^-1 s^-1 and mol L^-1
    time = np.linspace(0.0, 750.0, 1001)
    concentration = initial / (1.0 + k_obs * initial * time)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.8), layout="constrained")
    blue, orange = "#2375a4", "#ca6230"
    axes[0].plot(time, concentration, color=blue, lw=2.3)
    halving_times = np.array([0.0, 100.0, 300.0, 700.0])
    levels = initial / 2.0 ** np.arange(4)
    axes[0].scatter(halving_times, levels, color=blue, zorder=3, s=35)
    for end, level in zip(halving_times[1:], levels[1:]):
        axes[0].plot([0, end, end], [level, level, 0], ls=":", lw=1, color=blue, alpha=0.7)
    for start, end in zip(halving_times[:-1], halving_times[1:]):
        axes[0].annotate("", xy=(end, 0.0165), xytext=(start, 0.0165),
                         arrowprops={"arrowstyle": "<->", "color": orange})
        axes[0].text((start + end) / 2.0, 0.0172, f"{end-start:.0f} s",
                     ha="center", color=orange, fontsize=10)
    axes[0].set(title="Successive halving intervals: 100, 200, 400 s",
                xlabel="Time since mixing (s)", ylabel=r"$[A]$ (mol L$^{-1}$)",
                xlim=(-15, 750), ylim=(0, 0.022))
    starts = np.linspace(0.005, 0.050, 501)
    axes[1].plot(starts, 1.0 / (k_obs * starts), color=blue, lw=2.3,
                 label=r"Second order: $1/(k_{\rm obs}[A]_0)$")
    axes[1].axhline(100, color=orange, ls="--", lw=2,
                    label="First order: ln 2 / k₁ = 100 s")
    axes[1].scatter([initial], [100], color=blue, zorder=3, s=45)
    axes[1].set(title="First half-life versus initial concentration",
                xlabel=r"$[A]_0$ (mol L$^{-1}$)", ylabel="First half-life (s)",
                xlim=(0.005, 0.050), ylim=(0, 430))
    axes[1].legend(loc="upper right", fontsize=10, frameon=False)
    axes[1].text(0.04, 0.05, "kₒᵦₛ = 0.50 L mol⁻¹ s⁻¹\nk₁ = ln 2 / (100 s)",
                 transform=axes[1].transAxes, fontsize=10)
    for ax in axes:
        ax.grid(alpha=0.18)
    fig.suptitle("Second-order half-lives lengthen as concentration falls"
                 "\nOriginal models with chosen parameters; no measured data", fontsize=12)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
