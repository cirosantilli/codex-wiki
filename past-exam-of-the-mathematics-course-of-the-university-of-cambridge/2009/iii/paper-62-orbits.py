"""Closed and precessing bound orbits; output basename to the caller's CWD.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
The precession is enlarged to make the geometry visible, not fitted to Mercury.
"""
import os
import tempfile

if "MPLCONFIGDIR" not in os.environ:
    os.environ["MPLCONFIGDIR"] = tempfile.mkdtemp(prefix="paper-62-mpl-")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    eccentricity = 0.5
    alpha = np.sqrt(0.9)
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 4.3), layout="constrained")
    theta = np.linspace(0, 2 * np.pi, 1600)
    radius = (1 - eccentricity**2) / (1 + eccentricity * np.cos(theta))
    axes[0].plot(radius * np.cos(theta), radius * np.sin(theta), color="#1565a6", lw=2)
    axes[0].scatter([1 - eccentricity], [0], s=32, color="#b52828", zorder=5)
    axes[0].annotate("fixed perihelion", (0.5, 0), (0.7, -0.55), fontsize=9,
                     arrowprops={"arrowstyle": "->", "color": "#b52828"})
    axes[0].set_title(r"Closed ellipse: $\alpha=1$", fontsize=12)
    colors = plt.colormaps["viridis"](np.linspace(0.1, 0.88, 6))
    for j, color in enumerate(colors):
        theta = np.linspace(2 * np.pi * j / alpha, 2 * np.pi * (j + 1) / alpha, 1200)
        radius = (1 - eccentricity**2) / (1 + eccentricity * np.cos(alpha * theta))
        axes[1].plot(radius * np.cos(theta), radius * np.sin(theta), color=color, lw=1.25)
        periangle = 2 * np.pi * j / alpha
        axes[1].scatter([0.5 * np.cos(periangle)], [0.5 * np.sin(periangle)],
                        s=24, color=color, edgecolor="white", linewidth=0.4, zorder=6)
    axes[1].annotate("successive perihelia", (0.5, 0), (0.55, -0.75), fontsize=9,
                     arrowprops={"arrowstyle": "->", "color": "#444444"})
    axes[1].set_title(r"Precessing rosette: $\alpha=\sqrt{0.9}$", fontsize=12)
    for ax in axes:
        ax.scatter([0], [0], marker="*", s=130, color="#ecb934", edgecolor="#604800", zorder=7)
        ax.axhline(0, lw=0.5, color="#bdbdbd", zorder=0)
        ax.axvline(0, lw=0.5, color="#bdbdbd", zorder=0)
        ax.set(xlim=(-1.7, 1.7), ylim=(-1.7, 1.7), xlabel=r"$x/a$", ylabel=r"$y/a$")
        ax.set_aspect("equal")
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"Bound orbits with $e=0.5$: an attractive inverse-cube term advances the apsides", fontsize=11)
    fig.savefig("paper-62-orbits.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
