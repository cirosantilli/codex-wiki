#!/usr/bin/env python3
"""Generate paper-301-compton-diagrams.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def line_with_arrow(ax, a, b, label=None):
    ax.plot([a[0], b[0]], [a[1], b[1]], color="black", lw=2.3)
    x = 0.55 * a[0] + 0.45 * b[0]
    y = 0.55 * a[1] + 0.45 * b[1]
    ax.annotate("", xy=(x + 0.10 * (b[0] - a[0]), y + 0.10 * (b[1] - a[1])), xytext=(x, y), arrowprops={"arrowstyle": "-|>", "lw": 1.8})
    if label:
        ax.text((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 - 0.12, label, ha="center", fontsize=12)


def photon(ax, a, b, label=None):
    t = np.linspace(0, 1, 220)
    dx, dy = b[0] - a[0], b[1] - a[1]
    norm = np.hypot(dx, dy)
    wiggle = 0.033 * np.sin(18 * np.pi * t)
    x = a[0] + dx * t - dy / norm * wiggle
    y = a[1] + dy * t + dx / norm * wiggle
    ax.plot(x, y, color="#2457a6", lw=2)
    if label:
        ax.text((a[0] + b[0]) / 2 + 0.06, (a[1] + b[1]) / 2 + 0.06, label, color="#2457a6", fontsize=12)


def diagram(ax, channel):
    left, v1, v2, right = (0.05, 0.35), (0.34, 0.43), (0.66, 0.57), (0.95, 0.65)
    line_with_arrow(ax, left, v1, r"$p$")
    line_with_arrow(ax, v1, v2, r"$p+q$" if channel == "s" else r"$p-q'$" )
    line_with_arrow(ax, v2, right, r"$p'$")
    if channel == "s":
        photon(ax, (0.10, 0.92), v1, r"$q,\epsilon$")
        photon(ax, v2, (0.90, 0.92), r"$q',\epsilon'^*$")
    else:
        photon(ax, (0.10, 0.92), v2, r"$q,\epsilon$")
        photon(ax, v1, (0.90, 0.92), r"$q',\epsilon'^*$")
    ax.scatter([v1[0], v2[0]], [v1[1], v2[1]], s=30, color="black", zorder=4)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title(("$s$ channel" if channel == "s" else "$u$ channel"), fontsize=15)


fig, axes = plt.subplots(1, 2, figsize=(12, 4.3), dpi=100)
diagram(axes[0], "s")
diagram(axes[1], "u")
fig.suptitle("Tree-level Compton scattering", fontsize=17)
fig.tight_layout(rect=(0, 0, 1, 0.90))
fig.savefig(Path(Path(__file__).stem + ".png"), facecolor="white")
plt.close(fig)
