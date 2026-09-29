#!/usr/bin/env python3
"""Generate paper-333-beta-drift.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


tau = np.linspace(0, 12 * np.pi, 2400)
beta = 0.11
x = 1 - np.cos(tau) + beta * (np.sin(tau) - 0.25 * np.sin(2 * tau) - 0.5 * tau)
y = np.sin(tau) + beta * (np.cos(tau) - 1 + 0.5 * np.sin(tau) ** 2)
centres_x = 1 - beta * np.arange(0, 13, 2) * np.pi / 2

fig, ax = plt.subplots(figsize=(9.0, 4.8), layout="constrained")
ax.plot(x, y, color="#1f77b4", linewidth=2.1)
ax.scatter([x[0]], [y[0]], color="#d62728", s=65, zorder=4, label="initial parcel position")
ax.plot(centres_x, np.zeros_like(centres_x), color="#d95f02", linestyle="--", linewidth=1.5, label="westward motion of loop centres")
for index in range(120, len(tau) - 20, 420):
    ax.annotate("", (x[index + 18], y[index + 18]), (x[index], y[index]), arrowprops={"arrowstyle": "->", "color": "#1f77b4", "lw": 1.6})
ax.annotate("westward beta drift", (centres_x[-1], 0), (centres_x[-1] + 1.0, -1.25), arrowprops={"arrowstyle": "->", "color": "#d95f02"})
ax.axhline(0, color="0.75", linewidth=0.8)
ax.set(xlabel="$x f_0/V$ (eastward)", ylabel="$y f_0/V$ (northward)", title="Inertial loops on a beta plane", aspect="equal")
ax.grid(alpha=0.18)
ax.legend(loc="upper right")
fig.savefig(Path(Path(__file__).stem + ".png"), dpi=100, facecolor="white")
plt.close(fig)
