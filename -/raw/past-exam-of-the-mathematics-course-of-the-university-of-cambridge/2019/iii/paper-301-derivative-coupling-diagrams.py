#!/usr/bin/env python3
"""Generate paper-301-derivative-coupling-diagrams.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def fermion(ax, a, b, label=None, arrow=True):
    ax.plot([a[0], b[0]], [a[1], b[1]], color="black", lw=2.2)
    if arrow:
        x = 0.58 * a[0] + 0.42 * b[0]
        y = 0.58 * a[1] + 0.42 * b[1]
        dx = (b[0] - a[0]) * 0.12
        dy = (b[1] - a[1]) * 0.12
        ax.annotate("", xy=(x + dx, y + dy), xytext=(x, y), arrowprops={"arrowstyle": "-|>", "lw": 1.8, "color": "black"})
    if label:
        ax.text((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + 0.12, label, ha="center", fontsize=12)


def scalar(ax, a, b, label=None):
    t = np.linspace(0, 1, 180)
    x = a[0] + (b[0] - a[0]) * t
    y = a[1] + (b[1] - a[1]) * t
    dx, dy = b[0] - a[0], b[1] - a[1]
    norm = np.hypot(dx, dy)
    x += -dy / norm * 0.035 * np.sin(14 * np.pi * t)
    y += dx / norm * 0.035 * np.sin(14 * np.pi * t)
    ax.plot(x, y, color="#2457a6", lw=2.0)
    if label:
        ax.text((a[0] + b[0]) / 2 + 0.08, (a[1] + b[1]) / 2 + 0.08, label, color="#2457a6", fontsize=12)


fig, axes = plt.subplots(1, 3, figsize=(12, 5), dpi=100)
for ax in axes:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")

ax = axes[0]
fermion(ax, (0.08, 0.50), (0.92, 0.50), r"fermion momentum $p$")
scalar(ax, (0.50, 0.93), (0.50, 0.50), r"$k$")
ax.scatter([0.5], [0.5], s=32, color="black", zorder=4)
ax.text(0.50, 0.26, r"vertex $-\lambda\gamma^\mu k_\mu$", ha="center", fontsize=13)
ax.set_title("Derivative vertex", fontsize=14)

ax = axes[1]
scalar(ax, (0.10, 0.50), (0.48, 0.50), r"$\phi(p)$")
fermion(ax, (0.48, 0.50), (0.92, 0.78), r"$\psi(q_2)$")
fermion(ax, (0.92, 0.22), (0.48, 0.50), r"$\bar\psi(q_1)$")
ax.scatter([0.48], [0.5], s=32, color="black", zorder=4)
ax.text(0.52, 0.08, r"$\mathcal{M}\propto\bar u(q_2)\,\gamma^\mu p_\mu\,v(q_1)=0$", ha="center", fontsize=12)
ax.set_title("Decay amplitude", fontsize=14)

ax = axes[2]
ax.axvline(0.50, color="#c43c39", lw=1.7, ls="--")
ax.text(0.50, 0.95, "cut", color="#c43c39", ha="center", fontsize=11)
scalar(ax, (0.06, 0.50), (0.30, 0.50))
fermion(ax, (0.30, 0.50), (0.50, 0.74), arrow=True)
fermion(ax, (0.50, 0.26), (0.30, 0.50), arrow=True)
scalar(ax, (0.94, 0.50), (0.70, 0.50))
fermion(ax, (0.50, 0.74), (0.70, 0.50), arrow=True)
fermion(ax, (0.70, 0.50), (0.50, 0.26), arrow=True)
ax.scatter([0.30, 0.70], [0.50, 0.50], s=28, color="black", zorder=4)
ax.text(0.50, 0.10, r"$\sum |\mathcal{M}|^2=0$", ha="center", fontsize=13)
ax.set_title("Amplitude times conjugate", fontsize=14)

fig.suptitle("Derivative coupling to the Dirac current", fontsize=16)
fig.tight_layout(rect=(0, 0, 1, 0.93))
fig.savefig(Path(Path(__file__).stem + ".png"), facecolor="white")
plt.close(fig)
