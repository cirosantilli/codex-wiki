"""Draw the original divider and its terminal equivalent; run from _media."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np


def wire(ax, *points, **kwargs):
    ax.plot(*zip(*points), color="#253444", linewidth=1.8, **kwargs)


def resistor(ax, start, end, label, offset=(0, 0.33), color="#253444"):
    start, end = np.array(start), np.array(end)
    direction = end - start
    normal = np.array([-direction[1], direction[0]]) / np.linalg.norm(direction)
    points = [start, start + 0.2 * direction]
    for k in range(9):
        points.append(start + (0.25 + 0.0625 * k) * direction
                      + (0.11 * (-1) ** k if k not in (0, 8) else 0) * normal)
    points += [start + 0.8 * direction, end]
    ax.plot(*zip(*points), color=color, linewidth=1.8)
    midpoint = (start + end) / 2 + offset
    ax.text(*midpoint, label, ha="center", va="center", fontsize=11, color=color)


def supply(ax, x, voltage):
    wire(ax, (x, 0.8), (x, 1.55))
    wire(ax, (x, 2.45), (x, 3.2))
    ax.add_patch(Circle((x, 2), 0.45, edgecolor="#253444", facecolor="white", lw=1.8))
    ax.text(x, 2.18, "+", ha="center", va="center", fontsize=13)
    ax.text(x, 1.80, "−", ha="center", va="center", fontsize=13)
    ax.text(x - 0.65, 2, voltage, ha="center", va="center", fontsize=12)


def terminals_and_load(ax):
    wire(ax, (3.0, 3.2), (4.2, 3.2))
    wire(ax, (3.0, 0.8), (4.2, 0.8))
    resistor(ax, (4.2, 3.2), (4.2, 0.8), r"$R_L$", offset=(0.46, 0), color="#b54c2b")
    for y, label in [(3.2, "a"), (0.8, "b")]:
        ax.plot(3.0, y, "o", ms=5, color="#253444")
        ax.text(3.02, y + (0.16 if y > 2 else -0.26), label, fontsize=12)
    ax.annotate("", xy=(4.0, 3.45), xytext=(3.35, 3.45),
                arrowprops={"arrowstyle": "->", "color": "#b54c2b", "lw": 1.6})
    ax.text(3.66, 3.67, r"$I$ delivered", ha="center", color="#b54c2b", fontsize=11)
    ax.text(3.15, 2, "+\n\n$V$\n\n−", va="center", ha="center", fontsize=12)
    ax.add_patch(Rectangle((-0.87, 0.38), 3.68, 3.02, fill=False,
                           edgecolor="#6e8497", linestyle="--", linewidth=1.2))


fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.8), facecolor="white")
for ax in axes:
    ax.set_aspect("equal")
    ax.set_xlim(-1.08, 4.9)
    ax.set_ylim(-0.05, 4.3)
    ax.axis("off")
    ax.set_facecolor("white")
    terminals_and_load(ax)

ax = axes[0]
supply(ax, 0, "12 V")
resistor(ax, (0, 3.2), (2.4, 3.2), r"$R_1=2\,\mathrm{k\Omega}$")
wire(ax, (2.4, 3.2), (3.0, 3.2))
resistor(ax, (2.4, 3.2), (2.4, 0.8), r"$R_2=4\,\mathrm{k\Omega}$", offset=(-0.85, 0))
wire(ax, (0, 0.8), (3.0, 0.8))
ax.plot(2.4, 3.2, "o", ms=4, color="#253444")
ax.plot(2.4, 0.8, "o", ms=4, color="#253444")
ax.set_title("Original 12 V divider", fontsize=14, pad=8)
ax.text(1.9, 0, r"With $R_L=4\,\mathrm{k\Omega}$: $V=6$ V, $I=1.5$ mA",
        ha="center", fontsize=11)

ax = axes[1]
supply(ax, 0, "8 V")
resistor(ax, (0, 3.2), (2.4, 3.2), r"$R_{\mathrm{th}}=\frac{4}{3}\,\mathrm{k\Omega}$")
wire(ax, (2.4, 3.2), (3.0, 3.2))
wire(ax, (0, 0.8), (3.0, 0.8))
ax.set_title("Thévenin equivalent at a, b", fontsize=14, pad=8)
ax.text(1.9, 0, r"Same $V$ and $I$ for each connected load", ha="center", fontsize=11)
fig.tight_layout(pad=1.5)
fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white", transparent=False)
plt.close(fig)
