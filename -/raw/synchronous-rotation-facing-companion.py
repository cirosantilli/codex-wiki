"""Generate synchronous-rotation-facing-companion.png in the current directory.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
Circular-orbit geometry cartoon, not an ephemeris or observed lunar states.
The colored hemispheres and marker indicate material orientation, not light.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
import numpy as np


def marked_body(ax, centre, theta, radius=0.32):
    """Draw a body with a marked material direction at inertial angle theta."""
    angle = np.degrees(theta)
    ax.add_patch(Circle(centre, radius, facecolor="#d5e7f2",
                        edgecolor="none", zorder=3))
    ax.add_patch(Wedge(centre, radius, angle - 90, angle + 90,
                       facecolor="#ffe1bf", edgecolor="none", zorder=4))
    ax.add_patch(Circle(centre, radius, fill=False, edgecolor="#4b5964",
                        linewidth=1.3, zorder=5))
    tip = centre + radius * np.array([np.cos(theta), np.sin(theta)])
    ax.annotate("", xy=tip, xytext=centre,
                arrowprops={"arrowstyle": "->", "color": "#b95012", "lw": 1.8},
                zorder=6)
    ax.scatter(*tip, s=30, color="#b95012", edgecolor="white",
               linewidth=0.6, zorder=7)


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 6.0), dpi=110)
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.18, top=0.80, wspace=0.12)
    phases = np.arange(4) * np.pi / 2
    labels = ["0", "T/4", "T/2", "3T/4"]
    orbit_radius = 1.65
    samples = np.linspace(0, 2 * np.pi, 400)
    for ax, synchronous in zip(axes, [True, False]):
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set(xlim=(-2.45, 2.45), ylim=(-2.35, 2.35))
        ax.plot(orbit_radius * np.cos(samples), orbit_radius * np.sin(samples),
                color="#a9b4bc", linestyle="--", lw=1)
        ax.add_patch(Circle((0, 0), 0.38, facecolor="#687d91", zorder=3))
        ax.text(0, -0.62, "Companion", ha="center", color="#34495b")
        for f, label in zip(phases, labels):
            direction = np.array([np.cos(f), np.sin(f)])
            centre = orbit_radius * direction
            theta = f + np.pi if synchronous else np.pi
            marked_body(ax, centre, theta)
            ax.text(*(2.20 * direction), label, ha="center", va="center")
        a0, a1 = -np.pi / 3, -np.pi / 3 + 0.25
        ax.annotate("", xy=orbit_radius * np.array([np.cos(a1), np.sin(a1)]),
                    xytext=orbit_radius * np.array([np.cos(a0), np.sin(a0)]),
                    arrowprops={"arrowstyle": "->", "color": "#65727d", "lw": 1.7})
        ax.annotate("", xy=(-1.35, -2.02), xytext=(-2.10, -2.02),
                    arrowprops={"arrowstyle": "->", "color": "#65727d", "lw": 1.2})
        ax.text(-1.73, -2.25, "Fixed direction in space", ha="center", fontsize=9)
        if synchronous:
            ax.set_title("Synchronous: one spin per orbit", fontsize=13, pad=14)
            ax.text(0.5, -0.07, r"$\theta=f+\pi$: same marked face points inward",
                    transform=ax.transAxes, ha="center", fontsize=11)
        else:
            ax.set_title("No spin: fixed orientation in space", fontsize=13, pad=14)
            ax.text(0.5, -0.07, r"$\theta=\pi$: different faces point inward",
                    transform=ax.transAxes, ha="center", fontsize=11)
    fig.suptitle("Facing a companion requires rotation in space", fontsize=16, y=0.97)
    fig.text(0.5, 0.885, "Four snapshots of each circular orbit; orange dot = the same surface patch",
             ha="center", fontsize=11)
    fig.text(0.5, 0.055, "Material colors do not show sunlight. Spin axes point out of the page; sizes are arbitrary.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.023, "Geometry cartoons, not photographs or measured lunar states.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
