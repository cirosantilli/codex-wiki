"""Original diagram of the free three-mass chain, middle mass 2m.

Tested with Python 3.14, NumPy 2.3 and Matplotlib 3.10.
Run from the mirrored _media directory; output is written to cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


def spring(ax, left, right, y):
    xs = np.linspace(left, right, 49)
    ys = np.zeros_like(xs)
    ys[3:-3] = 0.085 * np.sin(np.linspace(0, 12 * np.pi, len(xs) - 6))
    ax.plot(xs, y + ys, color="#8b95a5", lw=1.7, zorder=1)


fig, axes = plt.subplots(3, 1, figsize=(8.2, 5.5), facecolor="white")
positions = np.array([0.0, 2.0, 4.0])
shapes = [(1, 1, 1), (1, 0, -1), (1, -1, 1)]
frequencies = [r"$\omega=0$", r"$\omega=\Omega$", r"$\omega=\sqrt{2}\,\Omega$"]
labels = ["Free translation", "End masses move oppositely", "End masses move together"]
for ax, shape, frequency, label in zip(axes, shapes, frequencies, labels):
    ax.set_facecolor("white")
    spring(ax, 0.15, 1.79, 0)
    spring(ax, 2.21, 3.85, 0)
    for j, (x, component) in enumerate(zip(positions, shape)):
        radius = 0.21 if j == 1 else 0.15
        ax.add_patch(Circle((x, 0), radius, facecolor="#e3eaf3", edgecolor="#294e76", lw=1.7, zorder=3))
        ax.text(x, 0, "$2m$" if j == 1 else "$m$", ha="center", va="center", fontsize=11, zorder=4)
        if component:
            ax.add_patch(FancyArrowPatch((x - 0.26 * component, 0.40), (x + 0.26 * component, 0.40), arrowstyle="-|>", mutation_scale=15, lw=2, color="#b44822"))
        else:
            ax.text(x, 0.4, "fixed", ha="center", va="center", color="#5d6675", fontsize=10)
        ax.text(x, -0.42, f"{component:+d}" if component else "0", ha="center", va="center", fontsize=11, color="#294e76")
    ax.text(-0.8, 0.13, frequency, ha="right", va="center", fontsize=15)
    ax.text(5.0, 0.13, label, ha="left", va="center", fontsize=11)
    ax.set_xlim(-2.1, 8.0)
    ax.set_ylim(-0.7, 0.75)
    ax.set_aspect("equal")
    ax.axis("off")
fig.suptitle(r"Three free masses: mode shapes for $\mu=2$, $\Omega=\sqrt{k/m}$", fontsize=15, y=0.98)
fig.text(0.5, 0.025, "Arrows indicate signed modal displacement; numbers give relative amplitudes.", ha="center", fontsize=10)
fig.subplots_adjust(top=0.90, bottom=0.10, left=0.015, right=0.99, hspace=0.12)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=145, facecolor="white")
plt.close(fig)
