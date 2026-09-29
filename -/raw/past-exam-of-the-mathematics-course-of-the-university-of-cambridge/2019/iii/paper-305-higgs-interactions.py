#!/usr/bin/env python3
"""Generate paper-305-higgs-interactions.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def straight(ax, center, angle, label, scalar=False):
    r0, r1 = 0.05, 0.42
    u = np.array([np.cos(angle), np.sin(angle)])
    a, b = center + r0 * u, center + r1 * u
    if scalar:
        ax.plot([a[0], b[0]], [a[1], b[1]], color="#b04a27", lw=2.5)
    else:
        t = np.linspace(0, 1, 160)
        n = np.array([-u[1], u[0]])
        xy = a[:, None] + (b - a)[:, None] * t + 0.018 * n[:, None] * np.sin(14 * np.pi * t)
        ax.plot(xy[0], xy[1], color="#2457a6", lw=2.0)
    pos = center + 0.48 * u
    ax.text(pos[0], pos[1], label, ha="center", va="center", fontsize=12)


def vertex(ax, scalar_count, vector_count, title):
    center = np.array([0.5, 0.48])
    count = scalar_count + vector_count
    angles = np.linspace(0, 2 * np.pi, count, endpoint=False) + np.pi / 8
    for i, angle in enumerate(angles):
        is_scalar = i < scalar_count
        straight(ax, center, angle, "$h$" if is_scalar else "$B^a$", scalar=is_scalar)
    ax.scatter(*center, s=32, color="black", zorder=4)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title(title, fontsize=14)


fig, axes = plt.subplots(2, 3, figsize=(11, 6.5), dpi=100)
for ax, spec in zip(
    axes.flat,
    [
        (3, 0, r"$h^3$"),
        (4, 0, r"$h^4$"),
        (1, 2, r"$hB^aB^a$"),
        (2, 2, r"$h^2B^aB^a$"),
        (0, 3, r"$\epsilon^{abc}(\partial B^a)B^bB^c$"),
        (0, 4, r"$g^2BB BB$"),
    ],
):
    vertex(ax, *spec)
fig.suptitle("Interaction vertices after complete SU(2) symmetry breaking", fontsize=17)
fig.tight_layout(rect=(0, 0, 1, 0.94))
fig.savefig(Path(Path(__file__).stem + ".png"), facecolor="white")
plt.close(fig)
