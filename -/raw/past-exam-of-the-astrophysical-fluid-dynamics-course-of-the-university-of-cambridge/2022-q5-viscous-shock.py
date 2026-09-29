#!/usr/bin/env python3
"""Plot the derived Burgers shock and explain its width conventions.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (+dfsg1 build),
as declared in the repository pyproject.toml. Writes the PNG basename to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    coordinate = np.linspace(-4, 4, 700)
    velocity = -np.tanh(coordinate)
    fig, ax = plt.subplots(figsize=(7.2, 3.6), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.axhline(1, color="0.6", linestyle=":", linewidth=1)
    ax.axhline(-1, color="0.6", linestyle=":", linewidth=1)
    ax.axhline(0, color="0.85", linewidth=0.8)
    ax.plot(coordinate, velocity, color="#0072b2", linewidth=2.6,
            label=r"$u=V-(\Delta u/2)\tanh(\xi/\ell)$")
    tangent = np.linspace(-1.12, 1.12, 100)
    ax.plot(tangent, -tangent, "--", color="#b66f00", linewidth=1.4, label="Central tangent")
    ax.annotate("", xy=(-1, -1.22), xytext=(1, -1.22),
                arrowprops={"arrowstyle": "<->", "color": "0.25"})
    ax.text(0, -1.29, r"Jump / maximum gradient: $\delta=2\ell=8\nu/\Delta u$",
            va="top", ha="center", fontsize=9)
    ax.text(-3.7, 1.05, r"$u_L$", fontsize=11)
    ax.text(3.25, -0.96, r"$u_R$", fontsize=11)
    ax.set(xlim=(-4, 4), ylim=(-1.55, 1.3), xlabel=r"Moving coordinate $\xi/\ell=(x-Vt)/\ell$",
           ylabel=r"Velocity $(u-V)/(\Delta u/2)$", title=r"Viscous shock: $\ell=4\nu/\Delta u$")
    ax.set_yticks([-1, 0, 1])
    ax.grid(alpha=0.15)
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
