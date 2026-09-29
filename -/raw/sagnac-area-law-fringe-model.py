"""Independent segment-sum model, not experimental measurements.

Tested with Python 3.14, numpy 2.3.5, matplotlib 3.10.7. Run from _media.
Each edge contributes 2 integral (Omega cross r) dot dr / (c lambda).
For rigid rotation the midpoint edge integral is exact at leading order.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


C = 299_792_458.0
WAVELENGTH = 633e-9


def segment_fringe_shift(vertices, omega):
    vertices = np.asarray(vertices, dtype=float)
    ends = np.roll(vertices, -1, axis=0)
    mids = (vertices + ends) / 2
    dl = ends - vertices
    # omega z-hat cross r, with signed omega in radians per second.
    velocity_per_omega = np.column_stack((-mids[:, 1], mids[:, 0]))
    circulation_per_omega = np.sum(velocity_per_omega * dl)
    return 2 * np.asarray(omega) * circulation_per_omega / (C * WAVELENGTH)


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    square = np.array([[-.15, -.15], [.15, -.15], [.15, .15], [-.15, .15]])
    rectangle = np.array([[-.20, -.10], [.20, -.10], [.20, .10], [-.20, .10]])
    omega = np.linspace(-50, 50, 501)
    fig = plt.figure(figsize=(10, 6.4), facecolor="white")
    grid = fig.add_gridspec(2, 2, width_ratios=[1, 2.55], hspace=.30, wspace=.25)
    fig.subplots_adjust(left=.08, right=.97, bottom=.18, top=.85)
    colors = ["#0067a4", "#ba4a10"]
    for row, (vertices, color, title) in enumerate(zip(
            [square, rectangle], colors,
            ["Square: 0.30 m × 0.30 m", "Rectangle: 0.40 m × 0.20 m"])):
        ax = fig.add_subplot(grid[row, 0])
        closed = np.vstack([vertices, vertices[0]])
        ax.fill(vertices[:, 0], vertices[:, 1], color=color, alpha=.10)
        ax.plot(closed[:, 0], closed[:, 1], color=color, lw=2)
        ax.set_aspect("equal")
        ax.set_xlim(-.26, .26)
        ax.set_ylim(-.22, .22)
        ax.axis("off")
        ax.set_title(title, fontsize=11)
        area = .09 if row == 0 else .08
        ax.text(0, 0, f"Area = {area:.2f} m²\nPerimeter = 1.20 m", ha="center", va="center", fontsize=10)
    ax = fig.add_subplot(grid[:, 1])
    for vertices, color, label in zip([square, rectangle], colors, ["Square", "Rectangle"]):
        shift = segment_fringe_shift(vertices, omega)
        ax.plot(omega, shift, color=color, lw=2.3, label=label)
        chosen = float(segment_fringe_shift(vertices, 10))
        ax.scatter([10], [chosen], color=color, zorder=4)
    ax.axhline(0, color="#777", lw=.8)
    ax.axvline(0, color="#777", lw=.8)
    ax.grid(alpha=.18)
    ax.set_xlabel(r"Signed rotation rate $\Omega$ (rad s$^{-1}$)")
    ax.set_ylabel(r"Signed fringe shift from rest $N=\Delta\phi/(2\pi)$")
    ax.set_xlim(-50, 50)
    ax.set_ylim(-.105, .105)
    ax.legend(loc="upper left")
    ax.text(.98, .08, r"$\lambda_0=633$ nm" + "\nSegment-sum calculation", transform=ax.transAxes,
            ha="right", va="bottom", fontsize=10)
    fig.suptitle("Same perimeter, different area: calculated Sagnac fringes", fontsize=16, y=.97)
    fig.text(.5, .90, "Leading-order vacuum model; all points and lines are predictions, not measured data", ha="center", fontsize=11)
    fig.text(.5, .075, r"At $\Omega=+10$ rad s$^{-1}$: square 0.01897 fringe; rectangle 0.01686 fringe.",
             ha="center", fontsize=11)
    fig.text(.5, .035, "Reversing +10 to −10 doubles the magnitude of the displacement from rest.", ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
