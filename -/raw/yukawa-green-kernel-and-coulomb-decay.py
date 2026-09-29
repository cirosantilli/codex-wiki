"""Plot a scalar Yukawa Green kernel and suppression ratios.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; writes the matching PNG to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.3), layout="constrained")
    x = np.linspace(0.16, 5, 800)
    axes[0].plot(x, 1 / x, color="#555555", linestyle="--", label="Unscreened: 1/x")
    axes[0].plot(x, np.exp(-x) / x, color="#006e9a", linewidth=2.3,
                 label=r"Yukawa: $e^{-x}/x$")
    axes[0].set(xlabel=r"Separation $x=\kappa r$", ylabel=r"Scaled kernel $4\pi G/\kappa$",
                xlim=(0, 5), ylim=(0, 4), title="A decaying point-source field")
    axes[0].legend(frameon=False)
    axes[0].text(0.97, 0.48, "Origin excluded\nNo physical core modeled",
                 transform=axes[0].transAxes, ha="right", color="#555555")
    x = np.linspace(0, 5, 801)
    axes[1].plot(x, np.exp(-x), color="#006e9a", linewidth=2.3,
                 label=r"Potential: $e^{-x}$")
    axes[1].plot(x, (1 + x) * np.exp(-x), color="#b74d14", linewidth=2.3,
                 label=r"Radial force: $(1+x)e^{-x}$")
    axes[1].axhline(1, color="#555555", linestyle="--", linewidth=1)
    axes[1].set(xlabel=r"Separation $x=\kappa r$", ylabel="Magnitude / unscreened magnitude",
                xlim=(0, 5), ylim=(0, 1.06), title="Same exponential scale, different ratios")
    axes[1].legend(frameon=True, facecolor="white", edgecolor="white",
                   framealpha=1, loc="upper right")
    for ax in axes:
        ax.grid(alpha=0.2)
    fig.suptitle("Yukawa screening compared with the Coulomb kernel", fontsize=14)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
