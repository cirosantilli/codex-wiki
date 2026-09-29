"""Plot the two allowed exterior equatorial photon radii for subextremal Kerr."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    spin = np.linspace(0.0, 0.9999, 1000)
    prograde = 2 * (1 + np.cos(2 * np.arccos(-spin) / 3))
    retrograde = 2 * (1 + np.cos(2 * np.arccos(spin) / 3))
    horizon = 1 + np.sqrt(1 - spin**2)

    fig, ax = plt.subplots(figsize=(7.4, 4.6), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.fill_between(spin, 0, horizon, color="#eeeeee", label="Inside outer horizon")
    ax.plot(spin, retrograde, color="#b44925", lw=2.4, label="Retrograde photon orbit")
    ax.plot(spin, prograde, color="#1763a6", lw=2.4, label="Prograde photon orbit")
    ax.plot(spin, horizon, color="#333333", lw=1.8, ls="--", label="Outer horizon")
    ax.scatter([0], [3], color="#333333", s=28, zorder=4)
    ax.annotate("Schwarzschild photon sphere", xy=(0, 3), xytext=(0.08, 3.65),
                fontsize=10, arrowprops={"arrowstyle": "-", "color": "#555555"})
    ax.set(xlim=(0, 1), ylim=(0.8, 4.15), xlabel=r"Spin $a/M$",
           ylabel=r"Boyer–Lindquist radius $r/M$",
           title="Equatorial circular photon orbits: discrete allowed radii")
    ax.grid(alpha=0.2)
    ax.legend(loc="lower left", fontsize=9, framealpha=1, facecolor="white")
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False,
                metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
