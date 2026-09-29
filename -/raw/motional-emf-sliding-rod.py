"""Sliding rod: signed flux, charge force, and current; PNG output in cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    length, speed, field = 0.50, 2.0, 0.40
    velocity = np.array([speed, 0.0, 0.0])
    magnetic = np.array([0.0, 0.0, field])
    charge_drive = np.cross(velocity, magnetic)
    bottom_to_top = np.array([0.0, length, 0.0])
    signed_emf = charge_drive @ bottom_to_top
    np.testing.assert_allclose(charge_drive, [0.0, -0.80, 0.0])
    np.testing.assert_allclose(signed_emf, -0.40)
    # Separate finite-difference flux check, using an arbitrarily chosen x(0).
    t = np.linspace(0.0, 1.0, 101)
    flux = field * length * (0.30 + speed * t)
    np.testing.assert_allclose(-np.diff(flux) / np.diff(t), signed_emf, atol=1e-14)
    # Downward conventional current gives a leftward magnetic force.
    np.testing.assert_allclose(np.cross(-bottom_to_top, magnetic), [-0.20, 0.0, 0.0])

    blue, orange, green = "#176997", "#bd5723", "#337b56"
    plt.rcParams.update({"font.size": 11})
    fig, ax = plt.subplots(figsize=(9.5, 5.4), dpi=120, facecolor="white")
    rod_x = 1.1
    ax.add_patch(Rectangle((0, 0), rod_x, length, facecolor="#edf5fa", edgecolor="none"))
    ax.add_patch(Rectangle((0.7, 0), rod_x - 0.7, length, facecolor="#f9e8cc", edgecolor="none"))
    for x in np.linspace(0.14, 1.7, 10):
        for y in (0.09, 0.25, 0.41):
            ax.plot(x, y, "o", ms=7, mfc="white", mec=blue, mew=1.2)
            ax.plot(x, y, ".", ms=2, color=blue)
    wire = "#59636c"
    ax.plot([0, 1.75], [0, 0], color=wire, lw=3)
    ax.plot([0, 1.75], [length, length], color=wire, lw=3)
    ax.plot([0, 0], [0, 0.17], color=wire, lw=3)
    ax.plot([0, 0], [0.33, length], color=wire, lw=3)
    ax.add_patch(Rectangle((-0.035, 0.17), 0.07, 0.16, facecolor="white", edgecolor=wire, lw=2))
    ax.text(-0.10, 0.25, "R", ha="right", va="center")
    ax.plot([0.7, 0.7], [0, length], color="#9ca6ad", lw=2, ls="--")
    ax.plot([rod_x, rod_x], [0, length], color=wire, lw=7, solid_capstyle="round")
    # Actual clockwise current: right on top, down rod, left on bottom, up left.
    for start, end in (((0.35, length), (0.6, length)), ((rod_x, 0.38), (rod_x, 0.12)),
                       ((0.6, 0), (0.35, 0)), ((0, 0.35), (0, 0.46))):
        ax.annotate("", end, start, arrowprops={"arrowstyle": "->", "lw": 3, "color": orange})
    ax.annotate("", (1.72, 0.65), (rod_x, 0.65),
                arrowprops={"arrowstyle": "->", "lw": 2.5, "color": green})
    ax.text(1.41, 0.72, "v = 2.0 m/s", ha="center", color=green)
    ax.annotate("", (0.72, -0.23), (1.10, -0.23),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": orange})
    ax.text(0.91, -0.31, "Magnetic braking force", ha="center", color=orange, fontsize=10)
    ax.annotate("", (-0.24, length), (-0.24, 0),
                arrowprops={"arrowstyle": "<->", "color": wire})
    ax.text(-0.31, 0.25, "ℓ = 0.50 m", ha="center", va="center", rotation=90)
    ax.annotate("", (rod_x, -0.09), (0, -0.09), arrowprops={"arrowstyle": "<->", "color": wire})
    ax.text(0.55, -0.15, "x(t): area A = ℓx grows", ha="center", fontsize=10)
    ax.text(rod_x, length + 0.065, "−", ha="center", va="center", fontsize=18, color=blue)
    ax.text(rod_x, -0.035, "+", ha="center", va="top", fontsize=18, color=blue)
    ax.text(0.89, 0.86, "B = 0.40 T out of page (dots)", ha="center", color=blue, fontsize=12)
    ax.text(0.89, 0.98, "U-shaped stationary return path; right rod slides", ha="center", fontsize=11)

    ax.text(2.05, 0.85, "Sign check", fontsize=13, weight="bold")
    ax.text(2.05, 0.60, "Positive normal: out of page\nPositive loop: counterclockwise", fontsize=11, linespacing=1.6)
    ax.text(2.05, 0.37, "v × B points down\nBottom end positive (isolated rod)", fontsize=11, color=blue, linespacing=1.6)
    ax.text(2.05, 0.13, "Φ = Bℓx increases\nEmf (CCW) = −Bℓv = −0.40 V", fontsize=11, linespacing=1.6)
    ax.text(2.05, -0.11, "Closed resistive loop:\ncurrent clockwise, down the rod", fontsize=11, color=orange, linespacing=1.6)
    ax.set(xlim=(-0.48, 3.73), ylim=(-0.39, 1.07), aspect="equal")
    ax.axis("off")
    fig.suptitle("Motion increases flux even in a constant magnetic field", fontsize=15, y=0.96)
    fig.text(0.5, 0.07, "Blue ± labels show isolated-rod polarity; orange arrows show closed-loop current. Neglect self-inductance.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.015, right=0.985, top=0.86, bottom=0.14)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
