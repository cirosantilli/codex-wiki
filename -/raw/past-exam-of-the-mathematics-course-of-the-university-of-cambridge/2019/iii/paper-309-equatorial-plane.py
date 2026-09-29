#!/usr/bin/env python3
"""Generate paper-309-equatorial-plane.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


fig = plt.figure(figsize=(9, 6), dpi=100, facecolor="white")
ax = fig.add_subplot(111, projection="3d")

# A representative orbital plane through the symmetry centre.
normal = np.array([0.45, -0.35, 0.82])
normal = normal / np.linalg.norm(normal)
trial = np.array([1.0, 0.0, 0.0])
u = trial - np.dot(trial, normal) * normal
u = u / np.linalg.norm(u)
v = np.cross(normal, u)

radius = 1.45
corners = [
    radius * (sx * u + sy * v)
    for sx, sy in [(-1, -1), (1, -1), (1, 1), (-1, 1)]
]
plane = Poly3DCollection(
    [corners],
    facecolors="#7db7d8",
    edgecolors="#477c9b",
    linewidths=1.2,
    alpha=0.28,
)
ax.add_collection3d(plane)

angle = np.linspace(0.0, 2.0 * np.pi, 500)
orbit = 1.05 * np.cos(angle)[:, None] * u + 0.68 * np.sin(angle)[:, None] * v
ax.plot(orbit[:, 0], orbit[:, 1], orbit[:, 2], color="#9d2f2f", lw=2.8)

ax.scatter([0], [0], [0], color="black", s=35)
ax.text(0.04, 0.04, 0.04, "symmetry centre", fontsize=10)

arrow_length = 1.25
ax.quiver(
    0,
    0,
    0,
    *(arrow_length * normal),
    color="#56358c",
    linewidth=2.2,
    arrow_length_ratio=0.14,
)
tip = 1.34 * normal
ax.text(tip[0], tip[1], tip[2], r"fixed angular momentum $\mathbf{L}$", color="#56358c", fontsize=11)

axis_length = 1.65
ax.plot([-axis_length, axis_length], [0, 0], [0, 0], color="#555555", lw=0.8)
ax.plot([0, 0], [-axis_length, axis_length], [0, 0], color="#555555", lw=0.8)
ax.plot([0, 0], [0, 0], [-axis_length, axis_length], color="#555555", lw=0.8)
ax.text(axis_length, 0, 0, "$x$", fontsize=11)
ax.text(0, axis_length, 0, "$y$", fontsize=11)
ax.text(0, 0, axis_length, "$z$", fontsize=11)

ax.text(
    -1.35,
    -1.15,
    -0.85,
    "A spatial rotation makes this fixed plane the equatorial plane",
    fontsize=10,
)
ax.set_title("Planarity of a geodesic in a spherically symmetric spacetime", pad=14, fontsize=13)
ax.set_xlim(-1.7, 1.7)
ax.set_ylim(-1.7, 1.7)
ax.set_zlim(-1.7, 1.7)
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=23, azim=-52)
ax.set_axis_off()
fig.tight_layout()
fig.savefig(Path(Path(__file__).stem + ".png"), facecolor="white")
plt.close(fig)
