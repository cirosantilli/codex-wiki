"""Illustrate a hypothetical Michelson displacement count (Python 3.14)."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(9.6, 6.2), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 1, height_ratios=(1.05, 1.3))
    ax = fig.add_subplot(grid[0])
    ax.set(xlim=(0, 10), ylim=(0, 3.3))
    ax.axis("off")
    ax.set_title("Moving one mirror adds distance on both passes", loc="left", weight="bold")
    ax.plot([1.3, 1.8], [1.0, 2.0], color="0.3", lw=5)
    ax.text(0.2, 0.35, "Beam splitter")
    for y, direction in [(1.7, (2.2, 6.5)), (1.35, (6.5, 2.2))]:
        ax.annotate("", xy=(direction[1], y), xytext=(direction[0], y),
                    arrowprops={"arrowstyle": "->", "color": "#166da0", "lw": 2})
    ax.text(3.6, 1.95, "Outward path")
    ax.text(3.6, 0.9, "Return path")
    ax.plot([6.8, 6.8], [0.8, 2.4], lw=4, color="0.4")
    ax.plot([8.4, 8.4], [0.8, 2.4], lw=4, color="#b04e00")
    ax.text(6.8, 0.35, "Initial mirror", ha="center")
    ax.text(8.5, 0.35, "Final mirror", ha="center", color="#b04e00")
    ax.annotate("", xy=(8.4, 2.7), xytext=(6.8, 2.7),
                arrowprops={"arrowstyle": "<->", "color": "#b04e00"})
    ax.text(7.6, 2.9, r"$\Delta L$", ha="center", color="#b04e00")
    ax.text(0.2, 2.8, r"Fixed medium: $\lambda=\lambda_0/n$" + "\n" +
            r"$\Delta N=2\Delta L/\lambda$", va="top")
    ax = fig.add_subplot(grid[1])
    wavelength_nm = 600.0
    x_um = np.linspace(0, 1.2, 1201)
    cycles = 2 * x_um * 1000 / wavelength_nm
    ax.plot(x_um, 0.5 * (1 + np.cos(2 * np.pi * cycles)), color="#166da0", lw=2)
    for k in range(5):
        x = k * wavelength_nm / 2000
        ax.plot(x, 1, "o", color="#b04e00", ms=5)
        ax.text(x, 1.055, f"{k}", ha="center", color="#b04e00")
    ax.annotate("", xy=(0.3, 0.53), xytext=(0, 0.53),
                arrowprops={"arrowstyle": "<->", "color": "0.25"})
    ax.text(0.15, 0.59, "300 nm\none cycle", ha="center", fontsize=10)
    ax.set(xlabel=r"Mirror displacement $\Delta L$ (µm)",
           ylabel=r"Normalized intensity $I/I_{\max}$", xlim=(-0.02, 1.23), ylim=(-0.04, 1.21))
    ax.set_title("Hypothetical 600 nm source: count bright-to-bright cycles", loc="left", fontsize=12)
    ax.grid(alpha=0.2)
    fig.suptitle("Michelson displacement ruler", fontsize=16, weight="bold")
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
