"""Threshold radial energy; Python 3.14, NumPy and Matplotlib."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0.29, 1.06, 1200)
    potential = x + 1.0 / (6.0 * x**2)
    level = 7.0 / 6.0
    fig, ax = plt.subplots(figsize=(7.8, 4.9), dpi=100, facecolor="white")
    ax.set_facecolor("white")
    ax.axvspan(1.0, 1.06, color="#eeeeee")
    ax.plot(x, potential, color="#1263a0", lw=2.5,
            label=r"$(U_J+Mgl)/(Mgl)=x+1/(6x^2)$")
    ax.axhline(level, color="#ba5223", ls="--", lw=1.8,
               label=r"Threshold energy: $(E+Mgl)/(Mgl)=7/6$")
    allowed = (x >= 0.5) & (x <= 1.0)
    ax.fill_between(x, potential, level, where=allowed,
                    color="#6ab7ad", alpha=0.42)
    ax.scatter([0.5, 1.0], [level, level], color="#222222", s=28, zorder=4)
    ax.axvline(1.0, color="#666666", lw=1)
    ax.annotate("Initial radial turning point", xy=(0.5, level),
                xytext=(0.35, 1.56), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.annotate("Hanging mass reaches table", xy=(1.0, level),
                xytext=(0.69, 1.77), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.text(0.74, 1.085, "Accessible radii", ha="center", fontsize=10)
    ax.text(1.027, 1.42, "Beyond the table boundary", rotation=90,
            ha="center", va="center", fontsize=9, color="#555555")
    ax.set_xlim(0.29, 1.06)
    ax.set_ylim(1.0, 2.35)
    ax.set_xlabel(r"Tabletop radius $x=r/l$", fontsize=11)
    ax.set_ylabel("Dimensionless radial potential / energy", fontsize=11)
    ax.set_title("Radial energy at the just-reaching threshold", fontsize=13, pad=12)
    ax.grid(alpha=0.2)
    ax.legend(loc="upper right", frameon=True, fontsize=9)
    fig.tight_layout(pad=1.6)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False,
                metadata={"Software": "Codex Wiki"})
    plt.close(fig)


if __name__ == "__main__":
    main()
