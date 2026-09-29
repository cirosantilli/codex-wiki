"""Show straight shear trajectories and the deformation of a material cross.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media: python ../shear-flow-vorticity.py
The matching-basename PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def main():
    gamma = 1.0  # s^-1
    time = 0.5  # s
    blue, orange, green = "#1766a0", "#b65016", "#22784b"
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.8), dpi=120)
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.30, top=0.79, wspace=0.34)
    fig.suptitle("Straight shear trajectories can carry clockwise local spin", fontsize=16, y=0.96)
    fig.text(0.5, 0.875,
             r"$\mathbf{u}=(\gamma y,0),\quad\gamma=1\ \mathrm{s^{-1}},\quad t=0.5\ \mathrm{s}$",
             ha="center", fontsize=14)

    ax = axes[0]
    x, y = np.meshgrid(np.linspace(-1.5, 1.5, 9), np.linspace(-1.0, 1.0, 7))
    ax.quiver(x, y, gamma * y, np.zeros_like(y), angles="xy", scale_units="xy",
              scale=3.6, color=blue, width=0.006, pivot="mid")
    for y0 in (-0.75, 0.75):
        ax.axhline(y0, color="#888888", linestyle=":", lw=1)
        x0 = -0.4
        endpoint = x0 + gamma * y0 * time
        ax.plot(x0, y0, "o", color=orange, mfc="white", ms=6)
        ax.annotate("", xy=(endpoint, y0), xytext=(x0, y0),
                    arrowprops={"arrowstyle": "->", "color": orange, "lw": 2.3})
        ax.plot(endpoint, y0, "o", color=orange, ms=5)
    ax.set(xlim=(-1.7, 1.7), ylim=(-1.2, 1.2), xlabel=r"$x$ (m)", ylabel=r"$y$ (m)")
    ax.set_title("Each particle stays at its initial height", fontsize=12, pad=12)
    ax.set_aspect("equal")

    ax = axes[1]
    s = np.linspace(-0.85, 0.85, 100)
    ax.plot(s, np.zeros_like(s), color="#999999", ls="--", lw=2)
    ax.plot(np.zeros_like(s), s, color="#999999", ls="--", lw=2)
    ax.plot(s, np.zeros_like(s), color=green, lw=3)
    ax.plot(gamma * time * s, s, color=orange, lw=3)
    ax.plot(0, 0, "o", color="#222222", ms=5)
    angle = np.arctan2(1.0, gamma * time)
    arc = np.linspace(np.pi / 2, angle, 60)
    ax.plot(0.63 * np.cos(arc), 0.63 * np.sin(arc), color=orange, lw=1.6)
    ax.annotate("", xy=(0.63 * np.cos(arc[-1]), 0.63 * np.sin(arc[-1])),
                xytext=(0.63 * np.cos(arc[-8]), 0.63 * np.sin(arc[-8])),
                arrowprops={"arrowstyle": "->", "color": orange, "lw": 1.6})
    ax.text(-0.62, 0.92, "26.565°\nclockwise", ha="center", va="top", fontsize=11, color=orange)
    ax.text(0.25, 0.12, "Horizontal line\nkeeps its angle", fontsize=9, color=green)
    ax.set(xlim=(-1.1, 1.1), ylim=(-1.1, 1.1), xlabel=r"$\delta x/\ell$", ylabel=r"$\delta y/\ell$")
    ax.set_aspect("equal")
    ax.set_title("Two initially perpendicular material lines", fontsize=12, pad=12)
    ax.legend(handles=[Line2D([], [], color="#999999", ls="--", lw=2, label="Initial cross"),
                       Line2D([], [], color=orange, lw=3, label="Vertical line after shear")],
              loc="lower left", fontsize=9, framealpha=1)
    fig.text(0.5, 0.19,
             r"$\omega_z=-\gamma=-1\ \mathrm{s^{-1}},\qquad\Omega_{{\rm spin},z}=-\gamma/2=-0.5\ \mathrm{s^{-1}}$",
             ha="center", fontsize=14)
    fig.text(0.5, 0.10,
             "Initial line rotation rates: horizontal 0; vertical −γ. Their mean is −γ/2.\n"
             "The material cross deforms; local spin describes the antisymmetric velocity gradient.",
             ha="center", fontsize=11, linespacing=1.5)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
