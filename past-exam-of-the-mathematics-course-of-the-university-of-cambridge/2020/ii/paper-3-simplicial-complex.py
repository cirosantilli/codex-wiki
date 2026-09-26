#!/usr/bin/env python3
"""Draw the simplicial complex in 2020 Part II Paper 3, Question 20."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


OUTPUT = Path(__file__).with_suffix(".svg")
plt.rcParams["svg.hashsalt"] = "codex-wiki"

vertices = {
    "v1": (-1.15, 0.0),
    "v2": (1.15, 0.0),
    "v3": (0.0, 1.65),
    "v4": (0.0, -1.5),
}

fig, ax = plt.subplots(figsize=(5.8, 5.8))
filled = Polygon(
    [vertices["v1"], vertices["v2"], vertices["v3"]],
    closed=True,
    facecolor="#b9dced",
    edgecolor="#176b87",
    linewidth=2.4,
)
ax.add_patch(filled)

for first, second in [("v1", "v4"), ("v2", "v4")]:
    x = [vertices[first][0], vertices[second][0]]
    y = [vertices[first][1], vertices[second][1]]
    ax.plot(x, y, color="#176b87", linewidth=2.4)

label_offsets = {
    "v1": (-0.19, -0.20),
    "v2": (0.07, -0.20),
    "v3": (0.07, 0.08),
    "v4": (0.07, -0.02),
}
for name, (x, y) in vertices.items():
    ax.scatter([x], [y], s=35, color="#173f5f", zorder=3)
    dx, dy = label_offsets[name]
    ax.text(x + dx, y + dy, f"${name[0]}_{name[1]}$", fontsize=13)

ax.text(0.0, 0.54, "filled 2-simplex", color="#176b87", ha="center", fontsize=11)
ax.text(0.0, -0.62, "unfilled", color="#555555", ha="center", fontsize=11)
ax.set_aspect("equal")
ax.set_xlim(-1.55, 1.55)
ax.set_ylim(-1.8, 2.0)
ax.set_axis_off()
fig.tight_layout()
fig.savefig(OUTPUT, metadata={"Date": None}, transparent=True)
