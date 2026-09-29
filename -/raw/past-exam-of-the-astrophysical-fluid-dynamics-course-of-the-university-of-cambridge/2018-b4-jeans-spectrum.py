#!/usr/bin/env python3
"""Plot the derived static Jeans spectrum; write the PNG basename to cwd.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (+dfsg1).
Dependencies are already listed in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    q = np.linspace(0, 2, 600)
    long = np.linspace(.001, 1, 400)
    fig, axes = plt.subplots(1, 2, figsize=(8.0, 3.8), dpi=120, facecolor="white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_xlabel(r"Wavenumber $k/k_J$")
        ax.grid(alpha=.16)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].plot(q, q*q-1, lw=2.2, color="#0072b2")
    axes[0].fill_between(q[q<1], -1.15, 0, color="#d55e00", alpha=.08)
    axes[0].axhline(0, color=".4", lw=.9)
    axes[0].axvline(1, color=".5", lw=.9, linestyle=":")
    axes[0].text(.15, -.55, "Growing / decaying", fontsize=9, color="#a33f00")
    axes[0].text(1.15, .55, "Acoustic\noscillations", fontsize=9, color="#0072b2")
    axes[0].set(xlim=(0, 2), ylim=(-1.15, 3.15),
                ylabel=r"$\omega^2/(4\pi G\rho_0)$", title="Pressure versus self-gravity")
    axes[1].plot(long, np.sqrt(1-long**2), color="#d55e00", lw=2.2)
    axes[1].scatter([0], [1], facecolor="white", edgecolor="#d55e00", s=35, zorder=4)
    axes[1].annotate(r"Supremum as $k\to0^+$", xy=(.02, 1),
                     xytext=(.24, .72), fontsize=9,
                     arrowprops={"arrowstyle": "->", "color": ".4"})
    axes[1].set(xlim=(0, 1.02), ylim=(0, 1.08),
                ylabel=r"Growth rate $s/\sqrt{4\pi G\rho_0}$",
                title="Longest available scales grow fastest")
    fig.tight_layout()
    fig.savefig(Path(__file__).stem+".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
