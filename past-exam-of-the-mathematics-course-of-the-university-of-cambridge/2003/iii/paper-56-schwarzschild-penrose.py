"""Schwarzschild radial conformal diagram; Python 3.14, NumPy/Matplotlib.

Write the opaque PNG basename to the caller's current directory. The caller
may supply MPLCONFIGDIR; this generator does not override it.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

fig, ax = plt.subplots(figsize=(8.6, 6.4), dpi=140, facecolor="white")
ax.set_facecolor("white")
# Coordinates are (4X/pi, 4T/pi); null slopes remain +/-1.
regions = [
    ([(0, 0), (1, 1), (2, 0), (1, -1)], "#eef5ff"),
    ([(0, 0), (-1, 1), (-2, 0), (-1, -1)], "#eef5ff"),
    ([(0, 0), (1, 1), (-1, 1)], "#fff0ed"),
    ([(0, 0), (1, -1), (-1, -1)], "#fff7e6"),
]
for vertices, color in regions:
    ax.add_patch(Polygon(vertices, closed=True, facecolor=color, edgecolor="none"))
for side in (-1, 1):
    ax.plot([side, 2 * side, side], [1, 0, -1], color="#264d77", lw=2)
    ax.plot([side, 0, side], [1, 0, -1], color="#47624c", lw=1.7, ls="--")
# The r=0 singularities are spacelike, represented by jagged lines.
x = np.linspace(-1, 1, 101)
for side in (-1, 1):
    y = side * (1 + 0.025 * np.where(np.arange(len(x)) % 2, 1, -1))
    ax.plot(x, y, color="#a02525", lw=1.8)
ax.scatter([0], [0], s=24, color="#47624c", zorder=5)
ax.text(0, 0.53, "II: black-hole interior", ha="center", fontsize=11)
ax.text(0, -0.55, "IV: white-hole interior", ha="center", fontsize=11)
ax.text(1.1, 0, "I\nright exterior", ha="center", va="center", fontsize=11)
ax.text(-1.1, 0, "III\nleft exterior", ha="center", va="center", fontsize=11)
ax.text(0, 1.15, r"$r=0$: future singularity", ha="center", fontsize=11, color="#a02525")
ax.text(0, -1.22, r"$r=0$: past singularity", ha="center", fontsize=11, color="#a02525")
for side in (-1, 1):
    ax.text(1.63 * side, 0.51, r"$\mathscr{I}^{+}$", fontsize=16, ha="center")
    ax.text(1.63 * side, -0.60, r"$\mathscr{I}^{-}$", fontsize=16, ha="center")
    ax.text(2.13 * side, 0, r"$i^0$", ha="center", va="center", fontsize=14)
    ax.text(1.09 * side, 1.1, r"$i^+$", ha="center", fontsize=14)
    ax.text(1.09 * side, -1.18, r"$i^-$", ha="center", fontsize=14)
ax.text(0.42, 0.3, "future horizon", rotation=45, fontsize=9, color="#36543c")
ax.text(0.42, -0.43, "past horizon", rotation=-45, fontsize=9, color="#36543c")
ax.annotate("bifurcation sphere", xy=(0, 0), xytext=(-0.32, -0.18),
            ha="right", fontsize=9, arrowprops={"arrowstyle": "-", "color": "#47624c"})
ax.set_title("Maximally extended Schwarzschild spacetime", fontsize=15, pad=15)
ax.text(0, -1.47, "Null directions have slopes +/-1. Each interior point represents a two-sphere.",
        ha="center", fontsize=9)
ax.set_aspect("equal")
ax.set_xlim(-2.45, 2.45)
ax.set_ylim(-1.62, 1.42)
ax.axis("off")
fig.tight_layout()
fig.savefig(Path.cwd() / "paper-56-schwarzschild-penrose.png", facecolor="white", transparent=False)
plt.close(fig)
