#!/usr/bin/env python3
"""Generate paper-3-hyperboloid-geodesics.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


z = np.linspace(-1.65, 1.65, 90)
phi = np.linspace(0, 2 * np.pi, 130)
zz, pp = np.meshgrid(z, phi)
radius = np.sqrt(1 + zz**2)
xx = radius * np.cos(pp)
yy = radius * np.sin(pp)

fig = plt.figure(figsize=(9.0, 6.5), layout="constrained")
ax = fig.add_subplot(projection="3d")
ax.plot_wireframe(xx, yy, zz, rstride=10, cstride=9, color="0.72", linewidth=0.5, alpha=0.72)
ax.plot(np.cos(phi), np.sin(phi), np.zeros_like(phi), color="#9467bd", linewidth=3, label="waist geodesic")
for sign, color in ((1, "#1f77b4"), (-1, "#1f77b4")):
    ax.plot(sign * np.sqrt(1 + z**2), np.zeros_like(z), z, color=color, linewidth=2.7)
t = np.linspace(-1.5, 1.5, 120)
ax.plot(np.ones_like(t), t, t, color="#d62728", linewidth=2.7, label="intersecting ruling geodesics")
ax.plot(np.ones_like(t), -t, t, color="#d62728", linewidth=2.7)
ax.scatter([1], [0], [0], color="black", s=35)
ax.text(1.06, 0.05, 0.08, "right-angle intersection")
ax.set(xlabel="$x$", ylabel="$y$", zlabel="$z$", title="Plane-section geodesics on $x^2+y^2-z^2=1$")
ax.set_box_aspect((1, 1, 1.05))
ax.legend(loc="upper left")
fig.savefig(Path(Path(__file__).stem + ".png"), dpi=100, facecolor="white")
plt.close(fig)
