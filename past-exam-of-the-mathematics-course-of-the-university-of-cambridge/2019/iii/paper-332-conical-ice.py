"""Plot steady and draining conical ice profiles; write PNG to cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    # Dimensionless units A=D=ell=1; M is volume/(2*pi*cos(alpha)).
    nodes, weights = np.polynomial.legendre.leggauss(500)
    s = 0.75 * (nodes + 1)
    steady = np.cbrt(s / 2 - s * s / 3)
    mass = 0.75 * np.sum(weights * s * steady)
    x = np.linspace(0.0, 1.5, 600)
    h = np.cbrt(np.maximum(x / 2 - x * x / 3, 0.0))
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.3), dpi=100, facecolor="white")
    axes[0].fill_between(x, 0, h, color="#1766aa", alpha=0.18)
    axes[0].plot(x, h, color="#1766aa", lw=2.5)
    axes[0].axvline(1, color="#d87922", ls="--", label="Snowline")
    axes[0].axvline(1.5, color="0.45", ls=":", label="Steady terminus")
    axes[0].set(xlim=(0, 1.8), ylim=(0, 0.72), xlabel=r"Along-slope distance $x/\ell$",
                ylabel=r"Thickness $h/(A\ell/D)^{1/3}$", title="Steady snowfall balanced by ablation")
    axes[0].legend(frameon=False, loc="upper right", fontsize=9)
    colors = ["#1766aa", "#d87922", "#38966b"]
    for age, color in zip([1.0, 4.0, 16.0], colors):
        nose = (125 * mass * mass * age / 4) ** 0.2
        xx = np.linspace(0, nose, 400)
        hh = np.sqrt(xx / (5 * age))
        axes[1].plot(xx, hh, color=color, lw=2.3, label=rf"Virtual age $\tau={age:g}$")
        axes[1].plot([nose, nose], [hh[-1], 0], color=color, lw=2.3)
    axes[1].set(xlim=(0, nose * 1.1), ylim=(0, 0.72), xlabel=r"Along-slope distance $x/\ell$",
                ylabel=r"Thickness $h/(A\ell/D)^{1/3}$", title="Conserved volume; finite-height moving front")
    axes[1].legend(frameon=False, fontsize=9)
    for ax in axes:
        ax.grid(alpha=0.2)
    fig.suptitle("Conical ice current: steady profile and long-time similarity family", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
