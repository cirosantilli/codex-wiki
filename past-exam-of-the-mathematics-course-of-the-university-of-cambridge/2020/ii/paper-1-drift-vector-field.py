#!/usr/bin/env python3
"""Plot the linear drift field in 2020 Part II Paper 1, Question 6B."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT = Path(__file__).with_suffix(".svg")

plt.rcParams["svg.hashsalt"] = "codex-wiki"

x1, x2 = np.meshgrid(np.linspace(-1, 1, 17), np.linspace(-1, 1, 17))
a1 = -x1 + x2
a2 = -2 * x1 - x2
speed = np.hypot(a1, a2)

fig, ax = plt.subplots(figsize=(6.2, 6.2))
ax.streamplot(
    x1,
    x2,
    a1,
    a2,
    color=speed,
    cmap="viridis",
    density=1.15,
    linewidth=1.2,
    arrowsize=1.05,
)
ax.scatter([0], [0], color="#b23a48", s=32, zorder=3)
ax.axhline(0, color="0.55", linewidth=0.7)
ax.axvline(0, color="0.55", linewidth=0.7)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect("equal")
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$", rotation=0)
fig.tight_layout()
fig.savefig(OUTPUT, metadata={"Date": None})
