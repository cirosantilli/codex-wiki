#!/usr/bin/env python3
"""Generate paper-301-vacuum-bubbles.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, PathPatch
from matplotlib.path import Path as MplPath


def tadpole(ax, x, y, angle, radius=0.18):
    dx, dy = radius * np.cos(angle), radius * np.sin(angle)
    cx, cy = x + dx, y + dy
    ax.add_patch(Arc((cx, cy), 2 * radius, 1.45 * radius, angle=np.degrees(angle), theta1=0, theta2=360, lw=2.0, color="#2457a6"))


def connectors(ax, a, b, n):
    offsets = np.linspace(-0.24, 0.24, n)
    for off in offsets:
        verts = [a, ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + off), b]
        path = MplPath(verts, [MplPath.MOVETO, MplPath.CURVE3, MplPath.CURVE3])
        ax.add_patch(PathPatch(path, fill=False, lw=1.9, color="#2457a6"))


def setup(ax, title):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=13)


fig, axes = plt.subplots(2, 2, figsize=(12, 6.5), dpi=100)

ax = axes[0, 0]
setup(ax, r"order $\lambda$: one vertex, three tadpoles")
v = (0.5, 0.48)
for angle in (np.pi / 2, 7 * np.pi / 6, 11 * np.pi / 6):
    tadpole(ax, *v, angle, 0.21)
ax.scatter([v[0]], [v[1]], s=48, color="black", zorder=5)
ax.text(0.5, 0.08, r"$15/6!=1/48$", ha="center", fontsize=12)

for ax, r, pos, coeff in [
    (axes[0, 1], 2, (0.30, 0.70), r"$4050/[2(6!)^2]=1/256$"),
    (axes[1, 0], 4, (0.28, 0.72), r"$5400/[2(6!)^2]=1/192$"),
    (axes[1, 1], 6, (0.26, 0.74), r"$720/[2(6!)^2]=1/1440$"),
]:
    setup(ax, rf"order $\lambda^2$: $r={r}$ connecting lines")
    a, b = (pos[0], 0.50), (pos[1], 0.50)
    connectors(ax, a, b, r)
    loops = (6 - r) // 2
    angles = [np.pi / 2, 3 * np.pi / 2]
    for j in range(loops):
        tadpole(ax, *a, angles[j], 0.14)
        tadpole(ax, *b, angles[j], 0.14)
    ax.scatter([a[0], b[0]], [a[1], b[1]], s=44, color="black", zorder=5)
    ax.text(0.5, 0.08, coeff, ha="center", fontsize=11)

fig.suptitle(r"Connected vacuum-bubble types in $-\lambda\phi^6/6!$ theory", fontsize=16)
fig.tight_layout(rect=(0, 0, 1, 0.93))
fig.savefig(Path(Path(__file__).stem + ".png"), facecolor="white")
plt.close(fig)
