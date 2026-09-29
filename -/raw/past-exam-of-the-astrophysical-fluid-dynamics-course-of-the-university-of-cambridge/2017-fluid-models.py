"""Original overview of Q2 models; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.6), layout="constrained")
    fig.patch.set_facecolor("white")
    for ax in axes:
        ax.set_facecolor("white")
    ax = axes[0]
    for y in [-0.75, 0, 0.75]:
        ax.annotate("", xy=(9.5, y), xytext=(0.3, y), arrowprops={"arrowstyle": "->", "color": "#8a9faa", "lw": 1.6})
    x = np.linspace(0.8, 8.8, 700)
    y = 0.4 * np.sin(2 * np.pi * (x - 0.8) / 2)
    ax.plot(x, y, color="#a73e32", linewidth=2)
    ax.annotate("", xy=(x[-1], y[-1]), xytext=(x[-20], y[-20]), arrowprops={"arrowstyle": "->", "color": "#a73e32", "lw": 2})
    ax.text(5, 0.95, r"$\mathbf{B}$", ha="center", fontsize=14)
    ax.text(5, -1.02, "Helix projected onto a plane", ha="center", fontsize=9)
    ax.set(xlim=(0, 10), ylim=(-1.2, 1.2), title="Magnetic guidance of a particle")
    ax.axis("off")

    ax = axes[1]
    for radius in [0.3, 0.5, 0.7, 0.9]:
        ax.add_patch(Circle((0, 0), radius, fill=False, edgecolor="#b6c7d0", linewidth=1.4))
    ax.add_patch(Circle((0, 0), 0.12, color="#333333"))
    ax.annotate("", xy=(0.19, 0.12), xytext=(0.93, 0.12), arrowprops={"arrowstyle": "->", "color": "#17638d", "lw": 2.7})
    ax.annotate("", xy=(0.94, -0.17), xytext=(0.22, -0.17), arrowprops={"arrowstyle": "->", "color": "#ba6b23", "lw": 2.7})
    ax.text(0.54, 0.3, "Mass inward", fontsize=9, ha="center", color="#17638d", backgroundcolor="white")
    ax.text(0.45, -0.42, "Angular momentum\noutward", fontsize=9, ha="center", color="#9d5417", backgroundcolor="white")
    ax.set(xlim=(-1.08, 1.08), ylim=(-1.08, 1.08), title="Disk transport (face on)")
    ax.set_aspect("equal")
    ax.axis("off")

    ax = axes[2]
    radius = np.linspace(0, 1, 500)
    ax.plot(radius, np.sinc(radius), color="#24764f", linewidth=2.5)
    ax.scatter([0, 1], [1, 0], color="#24764f", s=22)
    ax.set(xlim=(0, 1), ylim=(0, 1.08), xlabel=r"Radius $r/R$", ylabel=r"Density $\rho/\rho_c$", title="Index-one polytrope")
    ax.text(0.11, 0.22, r"$\theta=\sin\xi/\xi,\quad R=\pi a$", fontsize=10)
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path("2017-fluid-models.png"), dpi=160, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
