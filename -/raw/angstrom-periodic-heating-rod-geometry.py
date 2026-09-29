"""Original periodic-heating geometry; Python 3.14, matplotlib 3.10.7.

Run from _media: MPLBACKEND=Agg python ../angstrom-periodic-heating-rod-geometry.py
The dimensions are illustrative, not a reconstruction of a particular apparatus.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(10, 5.8), dpi=120)
    ax.set(xlim=(-0.08, 1.05), ylim=(-0.55, 0.78))
    ax.axis("off")
    ax.set_title("Ångström method: one periodic input, two local thermometers", pad=14)
    ax.add_patch(Rectangle((0.04, 0.16), 0.87, 0.18, facecolor="#e6c58d", edgecolor="#6c4e1c", lw=1.6))
    ax.add_patch(Rectangle((-0.015, 0.10), 0.075, 0.30, facecolor="#e99b8f", edgecolor="#a53927"))
    ax.text(0.02, 0.50, "Heater / cooler\nat x = 0", ha="center", color="#a53927")
    ax.text(0.49, 0.25, "Uniform rod: conductivity k, diffusivity α = k/(ρcₚ)", ha="center")
    ax.text(0.94, 0.27, "Far end\nx = L", ha="left", va="center")
    for x, lab, col in [(0.27, "1", "#146c94"), (0.57, "2", "#7c3f96")]:
        ax.plot(x, 0.34, "o", color=col, ms=8)
        level = 0.68 if lab == "1" else 0.60
        ax.plot([x, x, 0.69], [0.34, level, level], color=col, lw=1.5)
        ax.text(x, 0.42, f"x{lab}", ha="center", color=col)
    ax.add_patch(Rectangle((0.69, 0.56), 0.26, 0.16, facecolor="#f2f5f7", edgecolor="#4c5863"))
    ax.text(0.82, 0.64, "Synchronized\nrecorder", ha="center", va="center")
    ax.annotate("", xy=(0.57, 0.06), xytext=(0.27, 0.06), arrowprops={"arrowstyle": "<->", "color": "#333333"})
    ax.text(0.42, -0.015, "Measured spacing Δx", ha="center")
    for x in [0.16, 0.43, 0.71, 0.85]:
        ax.add_patch(FancyArrowPatch((x, 0.16), (x, -0.13), arrowstyle="->", mutation_scale=12, color="#8b6c42"))
    ax.text(0.51, -0.20, "Possible side losses to surroundings at T∞", ha="center", color="#72532b")
    ax.text(0.51, -0.29, "Insulate; keep the cross-section nearly isothermal; test far-end influence", ha="center", fontsize=10)
    t = np.linspace(0, 2*np.pi, 200)
    ax.plot(-0.05 + 0.10*t/(2*np.pi), -0.18 + 0.045*np.cos(t), color="#a53927", lw=2)
    ax.text(0, -0.34, "Periodic drive", ha="center", color="#a53927", fontsize=10)
    ax.text(0.49, -0.44, "Fit the same frequency at both sensors: amplitude ratio A₁/A₂ and phase lag Δφ", ha="center", fontsize=11)
    fig.tight_layout()
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
