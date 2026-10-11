#!/usr/bin/env python3
"""Plot good-conductor field profiles; write the PNG basename to cwd.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (+dfsg1).
Dependencies are already listed in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    depth = np.linspace(0, 7, 800)
    envelope = np.exp(-depth)
    fig, ax = plt.subplots(figsize=(7.0, 3.9), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.plot(depth, envelope*np.cos(depth), color="#0072b2", lw=2.2,
            label=r"$E_x/E_0=e^{-q}\cos q$")
    ax.plot(depth, envelope*np.cos(depth+np.pi/4), color="#d55e00", lw=2.2,
            label=r"$H_y/H_0=e^{-q}\cos(q+\pi/4)$")
    ax.plot(depth, envelope, "--", color=".5", lw=1, label=r"Envelopes $\pm e^{-q}$")
    ax.plot(depth, -envelope, "--", color=".5", lw=1)
    ax.axhline(0, color=".6", lw=.8)
    ax.set(xlim=(0, 7), ylim=(-1.04, 1.04), xlabel=r"Depth $q=z/\delta$",
           ylabel="Field / its own peak surface phasor amplitude",
           title="Electric and magnetic fields in the metal at t = 0")
    ax.grid(alpha=.15)
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path(__file__).stem+".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
