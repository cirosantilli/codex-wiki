#!/usr/bin/env python3
"""Generate paper-316-projected-orbit.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


inclination = np.deg2rad(68)
node = np.deg2rad(32)
phase = np.linspace(0, 2 * np.pi, 600)
e1 = np.array((np.cos(node), np.sin(node), 0.0))
e2 = np.array((-np.sin(node) * np.cos(inclination), np.cos(node) * np.cos(inclination), np.sin(inclination)))
orbit = np.outer(np.cos(phase), e1) + np.outer(np.sin(phase), e2)
planet_phase = np.deg2rad(58)
planet = np.cos(planet_phase) * e1 + np.sin(planet_phase) * e2

fig = plt.figure(figsize=(10.0, 5.2), layout="constrained")
ax3 = fig.add_subplot(1, 2, 1, projection="3d")
grid = np.linspace(-1.1, 1.1, 2)
gx, gy = np.meshgrid(grid, grid)
ax3.plot_surface(gx, gy, np.zeros_like(gx), color="#c7e9f1", alpha=0.32, shade=False)
ax3.plot(orbit[:, 0], orbit[:, 1], orbit[:, 2], color="#1f77b4", linewidth=2.6)
ax3.plot([0, e1[0]], [0, e1[1]], [0, 0], color="black", linewidth=1.8)
ax3.scatter(*planet, color="#d62728", s=55)
ax3.scatter([0], [0], [0], marker="*", color="#ffbf00", s=130)
ax3.text(*(1.08 * e1), "ascending node")
ax3.text(*(1.08 * planet), "planet")
ax3.set(xlabel="North $x$", ylabel="East $y$", zlabel="line of sight $z$", title="Inclined circular orbit")
ax3.set_box_aspect((1, 1, 0.85))

ax = fig.add_subplot(1, 2, 2)
ax.plot(orbit[:, 0], orbit[:, 1], color="#1f77b4", linewidth=2.6)
ax.plot([-1.1 * e1[0], 1.1 * e1[0]], [-1.1 * e1[1], 1.1 * e1[1]], color="black", linewidth=1.2, linestyle="--", label="nodal line")
ax.scatter([planet[0]], [planet[1]], color="#d62728", s=55, zorder=4)
ax.scatter([0], [0], marker="*", color="#ffbf00", s=130, zorder=4)
ax.annotate("projected planet", planet[:2], planet[:2] + np.array((0.12, 0.2)), arrowprops={"arrowstyle": "->"})
ax.set(xlabel="North $x$", ylabel="East $y$", title="Projection on the sky", xlim=(-1.25, 1.25), ylim=(-1.25, 1.25), aspect="equal")
ax.grid(alpha=0.18)
ax.legend(loc="lower right")
fig.savefig(Path(Path(__file__).stem + ".png"), dpi=100, facecolor="white")
plt.close(fig)
