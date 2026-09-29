"""Original Euclidean Killing fields; run from _media to write the PNG there.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Arrows use one common scale within both panels and keep relative magnitudes.
"""

from pathlib import Path
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/codex-wiki-matplotlib")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.4), layout="constrained")
    points = np.linspace(-2, 2, 9)
    x, y = np.meshgrid(points, points)
    blue, orange = "#1769aa", "#c45412"
    theta = np.linspace(0, 2 * np.pi, 500)
    for ax in axes:
        ax.set(xlim=(-2.6, 2.6), ylim=(-2.6, 2.6), xlabel="$x$", ylabel="$y$")
        ax.set_aspect("equal")
        ax.set_xticks(range(-2, 3))
        ax.set_yticks(range(-2, 3))
        ax.grid(alpha=0.17)
        ax.axhline(0, color="#bbbbbb", lw=0.7)
        ax.axvline(0, color="#bbbbbb", lw=0.7)
    for yy in [-1.75, -0.75, 0.75, 1.75]:
        axes[0].plot([-2.6, 2.6], [yy, yy], color=orange, alpha=0.5, lw=1.4)
    axes[0].quiver(x, y, np.ones_like(x), np.zeros_like(y), color=blue,
                   angles="xy", scale_units="xy", scale=4, width=0.006,
                   pivot="mid", zorder=3)
    axes[0].set_title("Translation: $K=\\partial_x$\nFlow orbits are horizontal lines", pad=12)
    for radius in [0.75, 1.5, 2.25]:
        axes[1].plot(radius * np.cos(theta), radius * np.sin(theta),
                     color=orange, alpha=0.65, lw=1.4)
    axes[1].quiver(x, y, -y, x, color=blue, angles="xy", scale_units="xy",
                   scale=4, width=0.006, pivot="mid", zorder=3)
    axes[1].scatter([0], [0], color=blue, s=22, zorder=4)
    axes[1].set_title("Rotation: $K=-y\\partial_x+x\\partial_y$\nFlow orbits are circles", pad=12)
    fig.suptitle("Two infinitesimal symmetries of the Euclidean plane", fontsize=16)
    fig.supxlabel("Blue arrows: Killing field (common scale).  Orange curves: symmetry flow orbits.",
                  fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
