"""Original planar rotation schematic and Brownian toy paths; Python 3.14.

Run from the output directory. Requires numpy 2.3.5 and matplotlib 3.10.7.
All paths are simulated, and all correlation curves are exact model curves.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    blue, orange, green = "#176b9b", "#c65b17", "#368366"
    fig = plt.figure(figsize=(11.2, 7.4), dpi=100, layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=(0.85, 1.25))
    ax = fig.add_subplot(grid[0, 0])
    ax.set(xlim=(-0.3, 4.4), ylim=(-0.9, 1.05), aspect="equal")
    ax.axis("off")
    ax.set_title("A marked end makes an arrow", loc="left", weight="bold")
    for x, angle in [(0.55, 30), (3.1, 210)]:
        ax.add_patch(Ellipse((x, 0.05), 1.45, 0.42, angle=angle,
                             facecolor="#dcecf5", edgecolor=blue, lw=1.7))
        theta = np.deg2rad(angle)
        end = (x + 0.55 * np.cos(theta), 0.05 + 0.55 * np.sin(theta))
        ax.plot(*end, "o", color=orange, ms=8)
        ax.add_patch(FancyArrowPatch((x, 0.05), end, arrowstyle="->",
                                     mutation_scale=13, color=blue, lw=1.5))
    ax.text(1.8, 0.05, r"$\ne$", ha="center", fontsize=23)
    ax.text(0.55, -0.73, r"$\phi$", ha="center")
    ax.text(3.1, -0.73, r"$\phi+\pi$", ha="center")
    ax = fig.add_subplot(grid[0, 1])
    ax.set(xlim=(-0.3, 4.4), ylim=(-0.9, 1.05), aspect="equal")
    ax.axis("off")
    ax.set_title("An unmarked long axis is a director", loc="left", weight="bold")
    for x, angle in [(0.55, 30), (3.1, 210)]:
        ax.add_patch(Ellipse((x, 0.05), 1.45, 0.42, angle=angle,
                             facecolor="#e2f0e9", edgecolor=green, lw=1.7))
        theta = np.deg2rad(angle)
        dx, dy = 0.58 * np.cos(theta), 0.58 * np.sin(theta)
        ax.plot([x-dx, x+dx], [0.05-dy, 0.05+dy], color=green, lw=1.5)
    ax.text(1.8, 0.05, "=", ha="center", fontsize=23)
    ax.text(1.8, -0.73, r"$\phi\equiv\phi+\pi$ (same visible shape)", ha="center")
    ax = fig.add_subplot(grid[1, 0])
    dr, dt = 0.25, 0.01
    t = np.arange(601) * dt
    rng = np.random.default_rng(74319)
    for color in (blue, orange, green):
        phi = np.r_[0.0, np.cumsum(rng.normal(0, np.sqrt(2*dr*dt), len(t)-1))]
        ax.plot(t, phi, lw=1.3, color=color)
    ax.axhline(0, lw=0.7, color="#aaaaaa")
    ax.set(xlabel="Time (s)", ylabel=r"Unwrapped angle $\phi(t)-\phi(0)$ (rad)",
           xlim=(0, 6), title="Three simulated planar Brownian paths")
    ax.text(0.04, 0.97, r"$D_r=0.25\ \mathrm{s}^{-1}$, $\Delta t=0.01$ s",
            transform=ax.transAxes, va="top", fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    ax = fig.add_subplot(grid[1, 1])
    ax.plot(t, np.exp(-dr*t), color=blue, lw=2.4,
            label=r"Arrow: $\langle\cos\Delta\phi\rangle=e^{-D_rt}$")
    ax.plot(t, np.exp(-4*dr*t), color=green, lw=2.4,
            label=r"Axis: $\langle\cos2\Delta\phi\rangle=e^{-4D_rt}$")
    ax.axvline(2, color="#999999", lw=0.8, ls=":")
    for factor, color, label in [(1, blue, "0.607"), (4, green, "0.135")]:
        value = np.exp(-factor*dr*2)
        ax.plot(2, value, "o", color=color)
        ax.annotate(label, (2, value), (2.2, value+0.04), color=color)
    ax.set(xlabel="Lag time (s)", ylabel="Orientational correlation",
           xlim=(0, 6), ylim=(0, 1.08), title="Exact ensemble curves for the same planar model")
    ax.legend(loc="upper right", fontsize=10, frameon=False)
    fig.suptitle("Planar rotational diffusion: identify what you can see", fontsize=16, weight="bold")
    fig.supxlabel("Toy simulations and analytic curves, not experimental measurements", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
