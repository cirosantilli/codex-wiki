"""Original second-order disappearance models; no measured data.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media to write the matching opaque PNG into the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    k_obs = 0.50  # L mol^-1 s^-1, species disappearance convention
    time = np.linspace(0.0, 400.0, 801)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.5), layout="constrained")
    colors = ("#2375a4", "#ca6230", "#33845b")
    for initial, color in zip((0.010, 0.020, 0.040), colors):
        concentration = initial / (1.0 + k_obs * initial * time)
        half_time = 1.0 / (k_obs * initial)
        label = rf"$[A]_0={initial:.3f}$ mol L$^{{-1}}$"
        axes[0].plot(time, concentration, color=color, lw=2.3, label=label)
        axes[0].scatter([half_time], [initial / 2], color=color, s=40, zorder=3)
        axes[0].annotate(f"{half_time:.0f} s", (half_time, initial / 2),
                         xytext=(9, 5), textcoords="offset points", color=color)
        axes[1].plot(time, 1.0 / concentration, color=color, lw=2.3)
        axes[1].scatter([half_time], [2.0 / initial], color=color, s=40, zorder=3)
    axes[0].set(title="Remaining concentration", xlabel="Time (s)",
                ylabel=r"$[A]$ (mol L$^{-1}$)", xlim=(0, 400), ylim=(0, 0.043))
    axes[0].legend(loc="upper right", fontsize=10, frameon=False)
    axes[1].set(title="Reciprocal concentration", xlabel="Time (s)",
                ylabel=r"$1/[A]$ (L mol$^{-1}$)", xlim=(0, 400), ylim=(0, 325))
    axes[1].text(0.04, 0.95, "Shared slope: 0.50 L mol⁻¹ s⁻¹\nIntercept: 1/[A]₀",
                 transform=axes[1].transAxes, va="top", fontsize=10,
                 bbox={"facecolor": "white", "edgecolor": "none", "alpha": 1})
    for ax in axes:
        ax.grid(alpha=0.18)
    fig.suptitle(r"Second-order disappearance: $-d[A]/dt=k_{\rm obs}[A]^2$"
                 "\nChosen model parameters; dots mark first half-lives, not measurements", fontsize=12)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
