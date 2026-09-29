"""Render the orbit sketch to the current working directory.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5,
as specified by the repository pyproject.toml.
"""
from pathlib import Path
import os
import tempfile

# Keep Matplotlib's writable cache in a fresh task-owned namespace.
if "MPLCONFIGDIR" not in os.environ:
    os.environ["MPLCONFIGDIR"] = tempfile.mkdtemp(
        prefix="2016-ia-paper-4-primary-figure-cache-"
    )
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

alpha = 0.5
eccentricity = np.sqrt(1 + 4 * alpha**2)
beta = np.arctan(2 * alpha)
limit = np.arccos(-1 / eccentricity)
fig, ax = plt.subplots(figsize=(8, 5.6), dpi=100, facecolor="white")
ax.set_facecolor("white")

y = np.linspace(-4.4, 4.4, 900)
ax.plot(1 - y**2 / 4, y, color="#2166ac", lw=2,
        label="Original parabola")

def new_orbit(angles):
    radii = 2 / (1 + eccentricity * np.cos(angles))
    return radii * np.cos(angles - beta), radii * np.sin(angles - beta)

past = np.linspace(-limit + 0.06, beta, 900)
future = np.linspace(beta, limit - 0.06, 900)
ax.plot(*new_orbit(past), color="#d95f02", ls="--", lw=1.5, alpha=0.8,
        label="New conic: earlier continuation")
ax.plot(*new_orbit(future), color="#d95f02", lw=2.3,
        label="After impulse: hyperbola")

peri_radius = 2 / (1 + eccentricity)
peri = peri_radius * np.array([np.cos(beta), -np.sin(beta)])
ax.plot([0, peri[0]], [0, peri[1]], color="#777777", ls=":", lw=1.3)
ax.scatter(*peri, color="#d95f02", s=26, zorder=5)
ax.annotate("New periapsis", peri, xytext=(-1.4, -1.4),
            arrowprops={"arrowstyle": "-", "color": "#777777"}, fontsize=10)
ax.scatter([0], [0], color="#e6ab02", edgecolor="#555555", s=95, zorder=6)
ax.annotate("Sun (focus)", (0, 0), xytext=(-1.55, 0.25), fontsize=10)
ax.scatter([1], [0], color="#222222", s=28, zorder=7)
ax.annotate("Impulse point\n(1, 0)", (1, 0), xytext=(1.15, -0.6), fontsize=10)
ax.annotate("", (1, 1.1), (1, 0),
            arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#2166ac"})
ax.text(0.55, 0.9, r"$V$", color="#2166ac", fontsize=12)
ax.annotate("", (1.85, 0), (1, 0),
            arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#333333"})
ax.text(1.35, 0.18, r"$\alpha V$", fontsize=12)
ax.axhline(0, color="#bbbbbb", lw=0.7, zorder=0)
ax.axvline(0, color="#bbbbbb", lw=0.7, zorder=0)
ax.set_xlim(-4.2, 3.2)
ax.set_ylim(-3.5, 3.5)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel(r"$x/d$")
ax.set_ylabel(r"$y/d$")
ax.set_title(r"Outward radial impulse: $\alpha=1/2$, new eccentricity $\sqrt{2}$")
ax.legend(loc="upper left", fontsize=9, framealpha=1)
fig.tight_layout()
destination = Path.cwd() / "paper-4-comet-orbits.png"
fig.savefig(destination, facecolor="white", transparent=False, dpi=100)
plt.close(fig)
print(destination)
