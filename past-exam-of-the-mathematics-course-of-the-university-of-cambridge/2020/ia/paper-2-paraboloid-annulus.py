#!/usr/bin/env python3
"""Generate paper-2-paraboloid-annulus.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


theta = np.linspace(0.0, 2.0 * np.pi, 180)
radius = np.linspace(1.0, 2.0, 60)
theta_grid, radius_grid = np.meshgrid(theta, radius)
x = radius_grid * np.cos(theta_grid)
y = radius_grid * np.sin(theta_grid)
z = 5.0 - radius_grid**2

fig = plt.figure(figsize=(7.2, 5.8), layout="constrained")
ax = fig.add_subplot(projection="3d")
ax.plot_surface(x, y, z, color="#5aa9e6", alpha=0.7, linewidth=0)
for r, height, label in ((1.0, 4.0, "$r=1,z=4$"), (2.0, 1.0, "$r=2,z=1$")):
    ax.plot(r * np.cos(theta), r * np.sin(theta), height, color="black", linewidth=2.0)
    ax.text(r, 0.0, height + 0.15, label)
ax.quiver(0.0, 0.0, 2.4, 0.0, 0.0, 1.0, length=0.65, color="#d62728")
ax.text(0.05, 0.05, 3.05, "upward orientation", color="#d62728")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")
ax.set_title(r"$z=5-x^2-y^2$, $1<z<4$")
ax.set_box_aspect((1.0, 1.0, 0.85))
ax.view_init(elev=25.0, azim=-55.0)

output = Path(Path(__file__).stem + ".png")
fig.savefig(output, dpi=160, facecolor="white")
plt.close(fig)
