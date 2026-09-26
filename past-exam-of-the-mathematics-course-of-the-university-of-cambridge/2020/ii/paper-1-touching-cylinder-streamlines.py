#!/usr/bin/env python3
"""Plot the Stokes streamlines in 2020 Part II Paper 1, Question 39B."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT = Path(__file__).with_suffix(".svg")

plt.rcParams["svg.hashsalt"] = "codex-wiki"

a = 1.0
x = np.linspace(-2.15, 2.15, 700)
y = np.linspace(-0.08, 4.15, 700)
xx, yy = np.meshgrid(x, y)
r = np.hypot(xx, yy)
sin_theta = np.divide(yy, r, out=np.zeros_like(r), where=r > 0)

inside_outer = xx**2 + (yy - 2 * a) ** 2 <= (2 * a) ** 2
outside_inner = xx**2 + (yy - a) ** 2 >= a**2
fluid = inside_outer & outside_inner & (r > 1e-5)

psi = np.full_like(r, np.nan)
psi[fluid] = (
    sin_theta[fluid]
    / r[fluid]
    * (r[fluid] - 2 * a * sin_theta[fluid])
    * (r[fluid] - 4 * a * sin_theta[fluid])
)

fig, ax = plt.subplots(figsize=(6.4, 6.4))
levels = np.linspace(np.nanmin(psi) * 0.94, np.nanmin(psi) * 0.08, 12)
ax.contour(xx, yy, psi, levels=np.sort(levels), colors="#176b87", linewidths=1.05)

angle = np.linspace(0, 2 * np.pi, 600)
ax.plot(a * np.cos(angle), a + a * np.sin(angle), color="0.12", linewidth=2)
ax.plot(2 * a * np.cos(angle), 2 * a + 2 * a * np.sin(angle), color="0.12", linewidth=2)
ax.scatter([0], [2 * np.sqrt(2) * a], color="#c75146", s=34, zorder=4)
ax.annotate(
    "stagnation point",
    (0, 2 * np.sqrt(2) * a),
    xytext=(0.45, 3.1),
    arrowprops={"arrowstyle": "->", "color": "0.3"},
)
ax.set_aspect("equal")
ax.set_xlim(-2.15, 2.15)
ax.set_ylim(-0.08, 4.15)
ax.set_xlabel("$x/a$")
ax.set_ylabel("$y/a$")
fig.tight_layout()
fig.savefig(OUTPUT, metadata={"Date": None})
