"""Gaussian-windowed cosine toy: orientation tuning and phase sensitivity.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Writes only orientation-selectivity-angle-phase.png to CWD.
All parameters are chosen; this is neither a fit nor measured tuning data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


OUTPUT = Path("orientation-selectivity-angle-phase.png")
SX, SY, Q = .5, 1., np.pi


def angular_drive(theta):
    """Exact full-plane integral, normalized to the aligned phase-zero response."""
    theta = np.deg2rad(theta)
    a = np.exp(-.5 * Q**2 * (SX**2 * (np.sin(theta) - 1)**2
                             + SY**2 * np.cos(theta)**2))
    b = np.exp(-.5 * Q**2 * (SX**2 * (np.sin(theta) + 1)**2
                             + SY**2 * np.cos(theta)**2))
    return (a + b) / (1 + np.exp(-2 * SX**2 * Q**2))


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig = plt.figure(figsize=(9, 6.7), dpi=120, facecolor="white")
    grid = fig.add_gridspec(2, 4, height_ratios=(.85, 1.25), left=.09, right=.965,
                           bottom=.16, top=.82, hspace=.65, wspace=.75)
    fig.suptitle("Same filter, different angle or phase", fontsize=16, weight="bold", y=.97)
    fig.text(.5, .915, "Gaussian-windowed cosine toy • arbitrary spatial units • no biological data",
             ha="center", fontsize=10.5)
    x, y = np.meshgrid(np.linspace(-2, 2, 241), np.linspace(-2, 2, 241))
    kernel = np.exp(-.5 * ((x / SX)**2 + (y / SY)**2)) * np.cos(Q * x)
    ax = fig.add_subplot(grid[0, 0])
    ax.imshow(kernel, origin="lower", extent=(-2, 2, -2, 2), cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_title("A. Filter K", fontsize=11, weight="bold")
    ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2])
    ax.set_xlabel("x (red +, blue −)", fontsize=9); ax.set_ylabel("y")
    for column, theta in enumerate((0, 60, 90), start=1):
        t = np.deg2rad(theta)
        stimulus = np.cos(Q * (x * np.sin(t) - y * np.cos(t)))
        ax = fig.add_subplot(grid[0, column])
        ax.imshow(stimulus, origin="lower", extent=(-2, 2, -2, 2), cmap="gray", vmin=-1, vmax=1)
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_title(f"Stripes: θ = {theta}°", fontsize=10)
        ax.set_xlabel(f"R = {angular_drive(theta):.4f}", fontsize=10)
    theta = np.linspace(0, 180, 721)
    ax = fig.add_subplot(grid[1, :2])
    ax.plot(theta, angular_drive(theta), color="#1d6696", linewidth=2,
            label="Phase φ = 0")
    ax.plot(theta, np.zeros_like(theta), "--", color="#b96720", linewidth=1.6,
            label="φ = π/2 or π: rectified R = 0")
    for angle in (0, 60, 90, 120, 180):
        ax.plot(angle, angular_drive(angle), "o", color="#1d6696", markersize=4)
    ax.set(xlim=(0, 180), ylim=(-.04, 1.12), xticks=[0, 45, 90, 135, 180],
           xlabel="Stripe angle θ from horizontal (degrees)", ylabel="Normalized toy output R")
    ax.set_title("B. Angle sweep at fixed phase", fontsize=11, weight="bold", pad=11)
    ax.legend(frameon=False, fontsize=8.5, loc="upper left")
    phase = np.linspace(0, 2 * np.pi, 721)
    ax = fig.add_subplot(grid[1, 2:])
    ax.plot(phase / np.pi, np.cos(phase), "--", color="#697789", linewidth=1.7,
            label="Signed drive D = cos φ")
    ax.plot(phase / np.pi, np.maximum(0, np.cos(phase)), color="#1d6696", linewidth=2,
            label="Output R = max(0, D)")
    ax.set(xlim=(0, 2), ylim=(-1.12, 1.12), xticks=[0, .5, 1, 1.5, 2],
           xticklabels=["0", "π/2", "π", "3π/2", "2π"],
           xlabel="Spatial phase φ at θ = 90°", ylabel="Normalized drive / output")
    ax.set_title("C. Shift stripes without rotating", fontsize=11, weight="bold", pad=11)
    ax.legend(frameon=True, facecolor="white", edgecolor="white", fontsize=8.5, loc="upper right")
    for ax in fig.axes[-2:]:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(color="#e4e8ed", linewidth=.6)
    fig.text(.5, .045, "Chosen parameters: σx = 0.5, σy = 1, q = π. Curves use full-plane integrals; image panels show a crop.",
             ha="center", fontsize=9.5)
    fig.savefig(OUTPUT, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
