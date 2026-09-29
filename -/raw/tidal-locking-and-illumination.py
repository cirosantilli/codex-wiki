"""Generate tidal-locking-and-illumination.png in the current directory.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
Ideal circular orbit with perpendicular spin axis and parallel sunlight.
Neglect Earth's motion around the Sun, libration, eclipses and terrain.
No empirical lunar positions, shapes or surface features are represented.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(2, 2, figsize=(9.0, 8.0), dpi=110)
    fig.subplots_adjust(left=0.035, right=0.965, bottom=0.17, top=0.83,
                        hspace=0.26, wspace=0.13)
    orbit_radius, moon_radius = 1.55, 0.33
    samples = np.linspace(0, 2 * np.pi, 400)
    phases = np.arange(4) * np.pi / 2
    labels = ["0: marked patch in daylight", "T/4: patch at sunset",
              "T/2: marked patch in darkness", "3T/4: patch at sunrise"]
    for ax, f, title in zip(axes.flat, phases, labels):
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set(xlim=(-2.20, 2.20), ylim=(-2.00, 2.00))
        # Parallel arrows represent incident sunlight, from the distant left.
        for y in [-0.52, 0, 0.52]:
            ax.annotate("", xy=(2.10, y), xytext=(-2.10, y),
                        arrowprops={"arrowstyle": "->", "color": "#e7c665",
                                    "lw": 1.1}, zorder=0)
        ax.plot(orbit_radius * np.cos(samples), orbit_radius * np.sin(samples),
                color="#a5b2bb", linestyle="--", lw=1, zorder=1)
        ax.add_patch(Circle((0, 0), 0.31, facecolor="#367bad",
                            edgecolor="#205374", zorder=4))
        ax.text(0, -0.05, "Earth", color="white", ha="center", fontsize=10, zorder=5)
        centre = orbit_radius * np.array([np.cos(f), np.sin(f)])
        # The left hemisphere is lit at every orbital phase; gray is unlit.
        ax.add_patch(Circle(centre, moon_radius, facecolor="#656d78",
                            edgecolor="none", zorder=4))
        ax.add_patch(Wedge(centre, moon_radius, 90, 270, facecolor="white",
                           edgecolor="none", zorder=5))
        ax.add_patch(Circle(centre, moon_radius, fill=False, edgecolor="#48525e",
                            lw=1.4, zorder=6))
        theta = f + np.pi
        patch = centre + moon_radius * np.array([np.cos(theta), np.sin(theta)])
        ax.plot([centre[0], patch[0]], [centre[1], patch[1]],
                color="#df6b21", lw=1.8, zorder=7)
        ax.scatter(*patch, s=50, color="#df6b21", edgecolor="white", lw=0.7, zorder=8)
        ax.annotate("", xy=0.47 * centre / orbit_radius,
                    xytext=centre - 0.46 * centre / orbit_radius,
                    arrowprops={"arrowstyle": "->", "color": "#b95012", "lw": 1.2},
                    zorder=3)
        a0, a1 = -np.pi / 4, -np.pi / 4 + 0.25
        ax.annotate("", xy=orbit_radius * np.array([np.cos(a1), np.sin(a1)]),
                    xytext=orbit_radius * np.array([np.cos(a0), np.sin(a0)]),
                    arrowprops={"arrowstyle": "->", "color": "#65727d", "lw": 1.4},
                    zorder=2)
        ax.set_title(title, fontsize=12, pad=9)
    fig.suptitle("Facing Earth does not mean facing the Sun", fontsize=16, y=0.975)
    fig.text(0.5, 0.915, "Sun far to the left: parallel sunlight travels rightward in every snapshot",
             ha="center", fontsize=11)
    fig.text(0.5, 0.875, "Orange dot = one Earth-facing surface patch; white = directly lit, grey = unlit",
             ha="center", fontsize=10)
    fig.text(0.5, 0.10, "The patch always faces Earth. It turns once in space and alternates between day and night.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.061, "Fixed Sun direction; Earth's motion around the Sun, eclipses, terrain and libration are omitted.",
             ha="center", fontsize=9)
    fig.text(0.5, 0.028, "Circular-orbit cartoon with arbitrary sizes, not photographs or actual lunar positions.",
             ha="center", fontsize=9)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
