#!/usr/bin/env python3
"""Plot the curve in 2020 Part IB Paper 1, Question 11E."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT = Path(__file__).with_suffix(".svg")

plt.rcParams["svg.hashsalt"] = "codex-wiki"

x = np.linspace(-2.2, 2.2, 900)
z = np.linspace(-2.2, 2.2, 900)
xx, zz = np.meshgrid(x, z)
level = (xx**2 - 1) ** 2 + (zz**2 - 1) ** 2 - 5

fig, ax = plt.subplots(figsize=(6.2, 6.2))
ax.contour(xx, zz, level, levels=[0], colors=["#1f5f99"], linewidths=2.4)

# The positive squared coordinates at a meridional inflection point are
# (u, v) and (v, u), where these numerical values solve the level-set and
# zero-curvature equations simultaneously.
u = 0.3041992211341421
v = 3.125055593656238
points = []
for x_squared, z_squared in ((u, v), (v, u)):
    for x_sign in (-1, 1):
        for z_sign in (-1, 1):
            points.append(
                (x_sign * np.sqrt(x_squared), z_sign * np.sqrt(z_squared))
            )
px, pz = np.asarray(points).T
ax.scatter(px, pz, color="#b23a48", marker="o", s=35, zorder=3, label="inflection point")

ax.axhline(0, color="0.45", linewidth=0.8)
ax.axvline(0, color="0.45", linewidth=0.8)
ax.set_aspect("equal")
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_xlabel("$x$")
ax.set_ylabel("$z$", rotation=0)
ax.legend(loc="upper right", frameon=False)
fig.tight_layout()
fig.savefig(OUTPUT, metadata={"Date": None})
