#!/usr/bin/env python3
"""Compute original transonic accretion profiles; write the PNG basename to cwd.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (+dfsg1).
Dependencies are already listed in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def profiles(radius):
    """Return u/c_s and rho/rho_inf on the reservoir-fed transonic branch."""
    radius = np.asarray(radius)
    rhs = 4*np.log(radius)+4/radius-3
    high_branch = radius < 1
    lower = np.where(high_branch, 0, -rhs-2)
    higher = np.where(high_branch, np.log(rhs+1)+2, 0)
    for _ in range(80):
        middle = (lower+higher)/2
        value = np.exp(middle)-middle
        move_lower = np.where(high_branch, value < rhs, value > rhs)
        lower = np.where(move_lower, middle, lower)
        higher = np.where(move_lower, higher, middle)
    log_w = np.where(abs(radius-1) < 1e-12, 0, (lower+higher)/2)
    speed = np.exp(log_w/2)
    density = np.exp(1.5)/(radius**2*speed)
    return speed, density


def main():
    radius = np.unique(np.r_[np.geomspace(.03, 100, 700), 1.])
    speed, density = profiles(radius)
    fig, axes = plt.subplots(1, 2, figsize=(8.0, 3.8), dpi=120, facecolor="white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_xlabel(r"Radius $x=r/r_s$")
        ax.set_xlim(.03, 100)
        ax.grid(which="both", alpha=.14)
        ax.spines[["top", "right"]].set_visible(False)
        ax.axvline(1, color=".65", lw=.9, linestyle=":")
    axes[0].loglog(radius, speed, color="#0072b2", lw=2.2, label="Accretion speed")
    inside = radius[radius < .15]
    axes[0].loglog(inside, 2/np.sqrt(inside), "--", color=".4", lw=1.3,
                   label=r"Inner free-fall limit $2/\sqrt{x}$")
    axes[0].scatter([1], [1], color="#0072b2", s=24, zorder=4)
    axes[0].set_ylabel(r"Inward speed $u/c_s$")
    axes[0].set_title("Subsonic outside, supersonic inside")
    axes[0].legend(loc="lower left", fontsize=8, frameon=False)
    axes[1].loglog(radius, density, color="#d55e00", lw=2.2)
    axes[1].axhline(1, color=".5", lw=.9, linestyle="--")
    axes[1].scatter([1], [np.exp(1.5)], color="#d55e00", s=24, zorder=4)
    axes[1].annotate(r"$\rho_s/\rho_\infty=e^{3/2}$", xy=(1, np.exp(1.5)),
                     xytext=(2.1, 18), fontsize=9,
                     arrowprops={"arrowstyle": "->", "color": ".4"})
    axes[1].set_ylabel(r"Density $\rho/\rho_\infty$")
    axes[1].set_title("Compression toward the accretor")
    fig.tight_layout()
    fig.savefig(Path(__file__).stem+".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
