"""Draw Paper 79's impermeable-channel Deacon cell at constant Coriolis parameter.

Requires caller-supplied MPLCONFIGDIR; writes basename PNG only to cwd.
"""

from pathlib import Path
import os

if not os.environ.get("MPLCONFIGDIR"):
    raise RuntimeError("Set MPLCONFIGDIR to a caller-owned cache directory")

import numpy as np
import matplotlib.pyplot as plt


width, height = 12, 6
y = np.linspace(0.0, 1.0, 241)
z = np.linspace(-1.0, 0.0, 301)
Y, Z = np.meshgrid(y, z)
h = 0.1  # h/H from the paper's representative depths.
s = np.maximum(Z + h, 0.0)
G = Z + 1.0 - (s / h) ** 2

# With constant positive A, Psi/A = sin(pi*y/L) G(z/H).
# Both plotted coordinates are normalized, so the common positive scale of
# their velocity components can be omitted without changing streamlines.
Psi = np.sin(np.pi * Y) * G
V = np.sin(np.pi * Y) * (2.0 * s / h**2 - 1.0)
W = np.pi * np.cos(np.pi * Y) * G
V[:, [0, -1]] = 0.0
W[[0, -1], :] = 0.0
assert np.all(V[:, [0, -1]] == 0.0)
assert np.all(W[[0, -1], :] == 0.0)
speed = np.hypot(V, W)

fig, ax = plt.subplots(figsize=(width, height), dpi=96)
ax.set_facecolor("white")
ax.streamplot(y, z, V, W, color=speed, cmap="viridis", density=1.25,
              linewidth=1.0, arrowsize=1.0)
ax.axhline(0.0, color="#35608d", linewidth=3)
ax.axhline(-h, color="#777777", linewidth=1, linestyle="--")
ax.text(0.02, 0.995, "surface wind stress", color="#234f7d", fontsize=12,
        ha="left", va="top", transform=ax.transAxes)
ax.annotate("northward", xy=(0.70, -0.045), xytext=(0.35, -0.045),
            arrowprops={"arrowstyle": "->", "color": "#234f7d"},
            color="#234f7d", fontsize=12, ha="center", va="center")
ax.annotate("southward deep return", xy=(0.25, -0.83), xytext=(0.62, -0.83),
            arrowprops={"arrowstyle": "->", "color": "#555555"},
            color="#555555", fontsize=12, ha="center", va="center")
ax.annotate("ascent", xy=(0.08, -0.36), xytext=(0.08, -0.65),
            arrowprops={"arrowstyle": "->", "color": "#222222"}, fontsize=12,
            ha="center")
ax.annotate("descent", xy=(0.92, -0.65), xytext=(0.92, -0.36),
            arrowprops={"arrowstyle": "->", "color": "#222222"}, fontsize=12,
            ha="center")
ax.text(0.5, -0.48, "Deacon cell", ha="center", va="center", fontsize=16,
        color="#222222", bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "none"})
ax.set_xlabel(r"northward coordinate $y/L$ (south to north)")
ax.set_ylabel(r"height $z/H$")
ax.set_xlim(0, 1)
ax.set_ylim(-1, 0)
ax.set_yticks([-1, -0.5, -h, 0], [r"$-1$ (bottom)", r"$-0.5$", r"$-h/H$", r"$0$ (surface)"])
ax.set_title("Clockwise wind-driven overturning")
fig.tight_layout()
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=96,
            facecolor="white", transparent=False)
plt.close(fig)
