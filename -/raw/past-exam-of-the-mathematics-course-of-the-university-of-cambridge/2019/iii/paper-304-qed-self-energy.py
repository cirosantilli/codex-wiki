#!/usr/bin/env python3
"""Generate paper-304-qed-self-energy.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots(figsize=(11, 3.8), dpi=100)

left = np.array([0.06, 0.34])
v1 = np.array([0.34, 0.34])
v2 = np.array([0.66, 0.34])
right = np.array([0.94, 0.34])


def fermion_segment(a, b, arrow=True):
    ax.plot([a[0], b[0]], [a[1], b[1]], color="black", lw=2.6)
    if arrow:
        midpoint = 0.52 * a + 0.48 * b
        step = 0.12 * (b - a)
        ax.annotate(
            "",
            xy=midpoint + step,
            xytext=midpoint,
            arrowprops={"arrowstyle": "-|>", "lw": 1.9, "color": "black"},
        )


fermion_segment(left, v1)
fermion_segment(v1, v2)
fermion_segment(v2, right)

# A semicircular photon line with a transverse sinusoidal wiggle.
t = np.linspace(0.0, 1.0, 600)
center = (v1 + v2) / 2.0
radius = (v2[0] - v1[0]) / 2.0
angle = np.pi * (1.0 - t)
base_x = center[0] + radius * np.cos(angle)
base_y = v1[1] + 0.42 * np.sin(angle)
dx = np.gradient(base_x)
dy = np.gradient(base_y)
norm = np.hypot(dx, dy)
wiggle = 0.017 * np.sin(22.0 * np.pi * t)
x = base_x - dy / norm * wiggle
y = base_y + dx / norm * wiggle
ax.plot(x, y, color="#2457a6", lw=2.3)

ax.scatter([v1[0], v2[0]], [v1[1], v2[1]], color="black", s=42, zorder=4)
ax.text(0.17, 0.24, r"$p$", fontsize=15)
ax.text(0.485, 0.24, r"$k$", fontsize=15)
ax.text(0.81, 0.24, r"$p$", fontsize=15)
ax.text(0.485, 0.79, r"$p-k$", color="#2457a6", fontsize=15)
ax.text(0.50, 0.06, r"$\Sigma(\not p)$", ha="center", fontsize=17)
ax.set_title("One-loop fermion self-energy in QED", fontsize=17)
ax.set_xlim(0.0, 1.0)
ax.set_ylim(0.0, 1.05)
ax.axis("off")
fig.tight_layout()
fig.savefig(Path(Path(__file__).stem + ".png"), facecolor="white")
plt.close(fig)
