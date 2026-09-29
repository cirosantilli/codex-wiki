"""Plot original stipulated attenuation models, not measured material data.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5; run from _media.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.9), dpi=120, facecolor="white")
    blue, orange = "#1768a2", "#b64a18"
    x = np.linspace(0, 12, 401)
    half = np.log(2) / 0.4
    ax = axes[0]
    ax.plot(x, np.exp(-0.4 * x), color=blue, lw=2.5,
            label=r"$T=e^{-0.40x}$")
    ax.plot([0, half, half], [0.5, 0.5, 0], ls="--", color="#777777", lw=1)
    ax.scatter([half, 2.5], [0.5, np.exp(-1)], color=[blue, orange], zorder=4)
    ax.annotate("Half-value layer\n1.73 mm → 0.500", (half, 0.5), (4.1, 0.68),
                arrowprops={"arrowstyle": "->", "color": "#777777"}, fontsize=10)
    ax.annotate("2.50 mm → 0.368", (2.5, np.exp(-1)), (4.1, 0.41),
                arrowprops={"arrowstyle": "->", "color": orange}, fontsize=10, color=orange)
    ax.set(title="One photon energy", xlabel="Thickness x (mm)",
           ylabel="Transmission T", xlim=(0, 12), ylim=(0, 1.03))
    ax.legend(loc="upper right", frameon=False)
    ax = axes[1]
    mixture = 0.5 * np.exp(-0.4 * x) + 0.5 * np.exp(-0.1 * x)
    ax.semilogy(x, mixture, color=blue, lw=2.5,
                label=r"$\frac{1}{2}e^{-0.40x}+\frac{1}{2}e^{-0.10x}$")
    ax.semilogy(x, np.exp(-0.25 * x), color=orange, lw=2, ls="--",
                label=r"$e^{-0.25x}$ (same initial slope)")
    t5 = 0.5 * np.exp(-2) + 0.5 * np.exp(-0.5)
    ax.scatter([5, 5], [t5, np.exp(-1.25)], color=[blue, orange], zorder=4)
    ax.text(5.5, t5 * 1.08, "0.371", color=blue, fontsize=10)
    ax.text(5.5, np.exp(-1.25) * 0.56, "0.287", color=orange, fontsize=10)
    ax.set(title="Equal-weight two-energy mixture", xlabel="Thickness x (mm)",
           ylabel="Transmission T (log scale)", xlim=(0, 12), ylim=(0.04, 1.1))
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    for ax in axes:
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Narrow-beam attenuation: a model with stated limits", fontsize=16)
    fig.text(0.5, 0.025, "Stipulated coefficients in mm⁻¹ • fixed geometry and linear detector • background subtracted • no accepted scatter",
             ha="center", fontsize=9, color="#444444")
    fig.tight_layout(rect=(0, 0.06, 1, 0.94), w_pad=2)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
