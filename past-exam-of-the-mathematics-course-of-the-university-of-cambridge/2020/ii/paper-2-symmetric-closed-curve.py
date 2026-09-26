#!/usr/bin/env python3
"""Draw a rotationally symmetric closed space curve for 2020 Part II Paper 2."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT = Path(Path(__file__).stem + ".png")

parameter = np.linspace(0.0, 2.0 * np.pi, 900)
major_radius = 2.0
minor_radius = 0.58
frequency = 2
radius = major_radius + minor_radius * np.cos(frequency * parameter)
x = radius * np.cos(parameter)
y = radius * np.sin(parameter)
z = minor_radius * np.sin(frequency * parameter)

fig = plt.figure(figsize=(7.0, 5.8))
ax = fig.add_subplot(111, projection="3d")
ax.plot(x, y, z, color="#176b87", linewidth=2.6)

# Show the half-turn symmetry axis and a faint copy of the rotated curve.
ax.plot([0.0, 0.0], [0.0, 0.0], [-1.1, 1.1], color="#555555", linewidth=1.1)
ax.text(0.0, 0.0, 1.2, "$z$", color="#555555", fontsize=12)
ax.quiver(0.0, -0.15, 0.86, 0.0, 0.55, 0.0, color="#c75146", arrow_length_ratio=0.25, linewidth=1.7)
ax.text(0.0, 0.46, 0.9, "rotation by $\\pi$", color="#c75146", fontsize=11)

ax.set_xlim(-2.8, 2.8)
ax.set_ylim(-2.8, 2.8)
ax.set_zlim(-1.15, 1.25)
ax.set_box_aspect((1.0, 1.0, 0.52))
ax.view_init(elev=58, azim=-55)
ax.set_axis_off()
fig.tight_layout()
fig.savefig(OUTPUT, dpi=160, facecolor="white")
