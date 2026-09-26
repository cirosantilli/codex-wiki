#!/usr/bin/env python3
"""Draw the magnetic-field helix in 2019 IA Paper 4, question 10(a)."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT = Path(__file__).with_suffix(".svg")
plt.rcParams["svg.hashsalt"] = "codex-wiki"

# Dimensionless coordinates with v/Omega = 1. The initial point is (1, 0, 0),
# the guiding-centre axis is x = 2, y = 0, and the equal parallel and
# perpendicular speeds give a pitch of 2*pi radii per turn.
t = np.linspace(0.0, 4.0 * np.pi, 800)
x = 2.0 - np.cos(t)
y = np.sin(t)
z = t

fig = plt.figure(figsize=(6.4, 5.2))
ax = fig.add_subplot(projection="3d")
ax.plot(x, y, z, color="#225f8b", linewidth=2.2)
ax.plot([2, 2], [0, 0], [0, 4 * np.pi], color="#777777", linestyle="--", linewidth=1)
ax.scatter([1], [0], [0], color="#a14b2a", s=30, depthshade=False)
ax.text(0.9, 0.0, -0.65, "$\\mathbf{x}(0)=(1,0,0)$", color="#a14b2a")
ax.quiver(1, 0, 0, 0, 0.8, 0.8, color="#a14b2a", arrow_length_ratio=0.16)
ax.text(0.95, 0.85, 0.95, "$\\dot{\\mathbf{x}}(0)$", color="#a14b2a")
ax.text(2.05, 0.05, 4 * np.pi, "guiding-centre axis", color="#555555")
ax.set(xlabel="$x$", ylabel="$y$", zlabel="$z$")
ax.set_xlim(0.7, 3.3)
ax.set_ylim(-1.3, 1.3)
ax.set_zlim(0, 4 * np.pi)
ax.view_init(elev=20, azim=-58)
ax.set_box_aspect((1, 1, 2.4))
fig.tight_layout()
fig.savefig(OUTPUT, metadata={"Date": None})
