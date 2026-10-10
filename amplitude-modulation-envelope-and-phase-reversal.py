"""Original AM model; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes this script's basename as an opaque white PNG.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    cycles = np.linspace(0, 2, 8001)
    theta = 2 * np.pi * cycles
    fig, axes = plt.subplots(2, 1, figsize=(10, 6.4), sharex=True)
    for ax, m in zip(axes, (0.5, 1.4), strict=True):
        q = 1 + m * np.cos(theta)
        signal = q * np.cos(20 * theta)
        envelope = np.abs(q)
        ax.fill_between(cycles, -2.65, 2.65, where=q < 0,
                        color="#f4e1f0", interpolate=True)
        ax.plot(cycles, signal, color="#266ba3", lw=1.0, label=r"voltage $s/A$")
        ax.plot(cycles, envelope, color="#d87516", lw=2.2, label=r"bounds $\pm |q|$")
        ax.plot(cycles, -envelope, color="#d87516", lw=2.2)
        ax.plot(cycles, q, color="#863a96", lw=1.8, ls=(0, (5, 3)),
                label=r"signed factor $q=1+m\cos(\Omega t)$")
        ax.axhline(0, color="#777777", lw=0.7)
        ax.set_ylim(-2.65, 2.65)
        ax.set_xlim(0, 2)
        ax.set_yticks([-2, -1, 0, 1, 2])
        ax.set_ylabel("Voltage / carrier peak A")
        ax.set_title(f"m = {m:g}" + (" : positive factor, faithful envelope" if m < 1
                                      else " : envelope folds at sign changes"), loc="left")
        ax.grid(alpha=0.16)
        if m > 1:
            ax.annotate(r"$q<0$: carrier phase flips by $\pi$",
                        xy=(0.50, -0.4), xytext=(0.50, -1.35), fontsize=10, ha="center",
                        arrowprops={"arrowstyle": "->", "color": "#863a96"},
                        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.92},
                        color="#702980")
    axes[0].legend(loc="lower center", ncols=3, fontsize=9, framealpha=1)
    axes[1].set_xticks(np.arange(0, 2.01, 0.25))
    axes[1].set_xlabel(r"Time in message cycles: $\Omega t/(2\pi)$")
    fig.suptitle("Amplitude modulation: signed factor versus nonnegative envelope", fontsize=14)
    fig.text(0.5, 0.018, r"Original linear model; $\omega_c/\Omega=20$. Calculated curves, not measured traces.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.095, right=0.985, top=0.875, bottom=0.125, hspace=0.30)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
