#!/usr/bin/env python3
"""Plot the two derived torsional mode eigenvalues and their limits.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (+dfsg1 build),
matching the repository pyproject.toml. Writes the PNG basename into cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    ratio = np.geomspace(.03, 100, 700)
    high = .5 + 1 / ratio + np.sqrt(.25 + 1 / ratio**2)
    # Product of eigenvalues is 1/R; this avoids subtractive cancellation.
    low = (1 / ratio) / high
    fig, ax = plt.subplots(figsize=(7.2, 4.0), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.loglog(ratio, high, color="#0072b2", linewidth=2.3, label=r"Higher mode $\omega_+^2$")
    ax.loglog(ratio, low, color="#d55e00", linewidth=2.3, label=r"Lower mode $\omega_-^2$")
    ax.hlines(.5, .03, .6, colors="0.5", linestyles=":", linewidth=1)
    ax.hlines(1, 3, 100, colors="0.5", linestyles=":", linewidth=1)
    small = np.geomspace(.03, .15, 100)
    large = np.geomspace(10, 100, 100)
    ax.loglog(small, 2 / small, ":", color="0.5", linewidth=1)
    ax.loglog(large, 1 / large, ":", color="0.5", linewidth=1)
    ax.text(.055, .62, r"$\omega_-^2\to\omega_0^2/2$", fontsize=10)
    ax.text(.05, 12, r"$\omega_+^2\sim2\omega_0^2/R$", fontsize=10)
    ax.text(15, 1.38, r"$\omega_+^2\to\omega_0^2$", fontsize=10)
    ax.text(9, .032, r"$\omega_-^2\sim\omega_0^2/R$", fontsize=10)
    ax.set(xlim=(.03, 100), ylim=(.008, 90), xlabel=r"Length ratio $R=\ell_2/\ell_1$",
           ylabel=r"Squared frequency $\omega^2/\omega_0^2$", title="Coupled torsional pendulums: both mode limits")
    ax.grid(which="both", alpha=.17)
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
