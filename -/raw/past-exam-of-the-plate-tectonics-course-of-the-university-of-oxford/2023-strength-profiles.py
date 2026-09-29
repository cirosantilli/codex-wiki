"""Illustrative strength envelopes; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.

These are conceptual piecewise curves, not fitted India/Pacific observations.
The PNG is always written to CWD, independently of the script's location.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    fig, axs = plt.subplots(1, 2, figsize=(9, 5.8), dpi=100, sharey=True)
    fig.patch.set_facecolor("white")
    curves = [
        ("Continental interior (India)", [0, 15, 25, 38, 38.1, 52, 75, 110, 150, 180], [0, 220, 50, 15, 340, 460, 260, 95, 15, 2], 38),
        ("Old oceanic plate (central Pacific)", [0, 7, 7.1, 28, 44, 65, 90, 120, 180], [0, 90, 105, 490, 310, 100, 10, 2, 1], 7),
    ]
    for ax, (title, z, sigma, moho) in zip(axs, curves):
        ax.set_facecolor("white")
        ax.axhspan(0, moho, color="#e8d7c0", alpha=0.65)
        ax.axhspan(moho, 180, color="#e7edf3", alpha=0.65)
        ax.plot(sigma, z, color="#214c6b", lw=2.6)
        ax.fill_betweenx(z, 0, sigma, color="#6b9abd", alpha=0.28)
        ax.axhline(moho, color="#765b43", ls="--", lw=1.1)
        ax.text(575, moho + 4, f"Moho ~{moho} km", ha="right", va="top", fontsize=9)
        ax.set(xlim=(0, 600), ylim=(180, 0), xlabel="Sustained differential stress (MPa)", title=title)
        ax.set_xticks([0, 200, 400, 600])
        ax.grid(axis="x", alpha=0.2)
    axs[0].set_ylabel("Depth below solid surface (km)")
    axs[0].annotate("Frictional upper crust", (160, 11), (280, 8), fontsize=9, arrowprops={"arrowstyle": "->"})
    axs[0].annotate("Weak lower crust", (25, 32), (255, 32), fontsize=9, arrowprops={"arrowstyle": "->"})
    axs[0].annotate("Stronger mantle", (425, 57), (285, 79), fontsize=9, arrowprops={"arrowstyle": "->"})
    axs[0].text(170, 137, "Cold cratonic mantle can\nretain strength to greater depth", fontsize=9)
    axs[1].annotate("Thin mafic crust", (70, 5), (235, 14), fontsize=9, arrowprops={"arrowstyle": "->"})
    axs[1].annotate("Mantle strength peak", (480, 29), (205, 52), fontsize=9, arrowprops={"arrowstyle": "->"})
    axs[1].text(150, 108, "Hotter deep rock flows\nat lower stress", fontsize=9)
    fig.suptitle("Rock strength: friction strengthens; temperature promotes creep", fontsize=12.5, y=0.98)
    fig.text(0.045, 0.025, "Illustrative profiles only: depths and stresses depend on geotherm, composition, water and strain rate.", fontsize=9)
    fig.subplots_adjust(left=0.085, right=0.98, top=0.88, bottom=0.14, wspace=0.16)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
