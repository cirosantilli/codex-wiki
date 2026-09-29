"""Original radial approximate-identity diagram; PNG written to CWD.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from math import exp, lgamma, log, pi
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    radii = np.linspace(0, 1, 20001)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), dpi=100)
    fig.set_facecolor("white")
    for n in (1, 4, 16, 64):
        coefficient = exp(log(2) - 1.5 * log(pi) + lgamma(n + 1.5) - lgamma(n + 1))
        density = coefficient * (1 - radii**4)**n
        radial_mass = 2 * pi * radii * density
        cumulative = np.concatenate(([0], np.cumsum(
            (radial_mass[1:] + radial_mass[:-1]) * np.diff(radii) / 2)))
        if not np.isclose(cumulative[-1], 1, atol=1e-7):
            raise ValueError(f"Incorrect normalization for n={n}: {cumulative[-1]}")
        axes[0].plot(radii, density, lw=2, label=f"n = {n}")
        axes[1].plot(radii, cumulative, lw=2, label=f"n = {n}")
    axes[0].set(xlabel="Radius r", ylabel="Density gₙ(r)",
                title="The density grows near the origin", xlim=(0, 1), ylim=(0, None))
    axes[1].set(xlabel="Radius r", ylabel="Mass inside the disk of radius r",
                title="Unit mass concentrates into smaller disks",
                xlim=(0, 1), ylim=(0, 1.04))
    for ax in axes:
        ax.grid(alpha=0.2)
        ax.legend(fontsize=9)
    fig.suptitle("A radial approximate identity: gₙ(r) = cₙ(1 − r⁴)ⁿ", fontsize=13)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "paper-9-radial-approximate-identity.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
