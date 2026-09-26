#!/usr/bin/env python3
"""Draw representative streamlines for 2020 Part IB Paper 1, Question 17C."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT = Path(Path(__file__).stem + ".png")


alpha = 2 * np.pi / 3
gamma = np.pi / alpha
theta = np.linspace(0.025, alpha - 0.025, 900)

fig, ax = plt.subplots(figsize=(7.0, 4.8))
for r_min in (0.45, 0.8, 1.25, 1.8):
    radius = r_min * np.sin(gamma * theta) ** (-1 / gamma)
    visible = radius <= 4.8
    ax.plot(
        radius[visible] * np.cos(theta[visible]),
        radius[visible] * np.sin(theta[visible]),
        color="#1f5f99",
        linewidth=1.9,
    )

wall_radius = np.linspace(0, 5.0, 2)
for wall_angle in (0, alpha):
    ax.plot(
        wall_radius * np.cos(wall_angle),
        wall_radius * np.sin(wall_angle),
        color="0.15",
        linewidth=1.4,
    )

arc_theta = np.linspace(0, alpha, 100)
arc_radius = 0.42
ax.plot(arc_radius * np.cos(arc_theta), arc_radius * np.sin(arc_theta), color="0.3", linewidth=0.8)
ax.text(0.50 * np.cos(alpha / 2), 0.50 * np.sin(alpha / 2), r"$\alpha$", ha="center", va="center")
ax.text(4.5, -0.15, r"$\theta=0$", ha="right", va="top")
ax.text(4.5 * np.cos(alpha), 4.5 * np.sin(alpha) + 0.08, r"$\theta=\alpha$", ha="left", va="bottom")
ax.set_aspect("equal")
ax.set_xlim(-2.8, 5.1)
ax.set_ylim(-0.25, 4.7)
ax.axis("off")
fig.tight_layout()
fig.savefig(OUTPUT, dpi=160, facecolor="white")
