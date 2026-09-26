#!/usr/bin/env python3
"""Generate the three phase portraits required by 2018 Part II Paper 1, Q31."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def vector_field(a, x, y):
    return 2 * x * (y - a), 1 - x**2 - y**2


fig, axes = plt.subplots(1, 3, figsize=(12, 4), constrained_layout=True)
x = np.linspace(-2.0, 2.0, 260)
y = np.linspace(-1.7, 1.7, 230)
X, Y = np.meshgrid(x, y)

for ax, a in zip(axes, (0.0, 0.5, 1.5)):
    U, V = vector_field(a, X, Y)
    speed = np.hypot(U, V)
    ax.streamplot(
        X,
        Y,
        U,
        V,
        density=1.15,
        color=np.log1p(speed),
        cmap="Blues",
        linewidth=0.75,
        arrowsize=0.8,
    )
    ax.axvline(0, color="#555555", linewidth=1.4, linestyle="--", label="invariant $x=0$")
    fixed = [(0.0, 1.0, "saddle" if a < 1 else "stable node"), (0.0, -1.0, "saddle")]
    if abs(a) < 1:
        q = np.sqrt(1 - a * a)
        kind = "center" if a == 0 else "stable focus"
        fixed.extend([(-q, a, kind), (q, a, kind)])
    for fx, fy, kind in fixed:
        color = {"saddle": "#d62728", "center": "#2ca02c", "stable focus": "#6f42c1", "stable node": "#111111"}[kind]
        marker = "x" if kind == "saddle" else "o"
        ax.scatter([fx], [fy], color=color, marker=marker, s=48, zorder=6)
        ax.annotate(kind, (fx, fy), xytext=(5, 5), textcoords="offset points", fontsize=7, color=color)
    if a == 0:
        t = np.linspace(0, 2 * np.pi, 500)
        ax.plot(np.sqrt(3) * np.cos(t), np.sin(t), color="#d62728", linewidth=1.6, label="$H=0$ separatrix")
    ax.set_title(f"$a={a:g}$")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.7, 1.7)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_aspect("equal")
    ax.grid(alpha=0.15)

output = Path(Path(__file__).stem + ".png")
fig.savefig(output, dpi=100, facecolor="white")
plt.close(fig)
