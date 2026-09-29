"""Original Q11 contour sketches; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    theta = np.linspace(0, 2 * np.pi, 900)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), layout="constrained")
    fig.patch.set_facecolor("white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="#888888", linewidth=0.7)
        ax.axvline(0, color="#888888", linewidth=0.7)
        ax.set_aspect("equal")
        ax.set(xlabel=r"$x=\mathrm{Re}\,z$", ylabel=r"$y=\mathrm{Im}\,z$")
        ax.grid(alpha=0.15)
    for radius in [0.5, 1, 2, 3]:
        axes[0].plot(radius * np.cos(theta), radius * np.sin(theta), color="#17638d", linewidth=1.8)
        axes[0].text(radius * 0.70, radius * 0.70, f"$r={radius:g}$", fontsize=9, backgroundcolor="white")
    axes[0].set(xlim=(-3.4, 3.4), ylim=(-3.4, 3.4), title=r"$\mathrm{Re}\,\log z=\log r$")
    for level in [-1, -0.5, -0.25, 0.25, 0.5, 1]:
        centre = 1 / (2 * level)
        radius = abs(centre)
        colour = "#bd5337" if level < 0 else "#17638d"
        axes[1].plot(centre + radius * np.cos(theta), radius * np.sin(theta), color=colour, linewidth=1.8)
        axes[1].text(centre, radius + 0.08, f"$K={level:g}$", fontsize=9, ha="center", color=colour)
    axes[1].axvline(0, color="#333333", linewidth=1.2, linestyle="--")
    axes[1].text(0.1, -2.35, "$K=0$", fontsize=10)
    axes[1].set(xlim=(-4.4, 4.4), ylim=(-2.7, 2.7), title=r"$\mathrm{Re}(1/z)=K$")
    for ax in axes:
        ax.scatter(0, 0, s=35, facecolor="white", edgecolor="black", zorder=10)
    fig.savefig(Path("paper-1-complex-contours.png"), dpi=160, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
