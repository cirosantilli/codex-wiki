#!/usr/bin/env python3
"""Generate paper-2-gradient-flow.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def potential(x, y):
    return x**3 - 3 * x + (x + 1) * y**2


def velocity(point):
    x, y = point
    return np.array((-(3 * x**2 - 3 + y**2), -2 * y * (x + 1)))


def rk4(point, step):
    k1 = velocity(point)
    k2 = velocity(point + step * k1 / 2)
    k3 = velocity(point + step * k2 / 2)
    k4 = velocity(point + step * k3)
    return point + step * (k1 + 2 * k2 + 2 * k3 + k4) / 6


x = np.linspace(-1.75, 2.35, 420)
y = np.linspace(-1.7, 1.7, 360)
xx, yy = np.meshgrid(x, y)
uu = -(3 * xx**2 - 3 + yy**2)
vv = -2 * yy * (xx + 1)
zz = potential(xx, yy)

trajectory = [np.array((2.0, 1.0))]
for _ in range(900):
    trajectory.append(rk4(trajectory[-1], 0.004))
trajectory = np.asarray(trajectory)

fig, ax = plt.subplots(figsize=(8.0, 6.0), layout="constrained")
levels = np.array([-4, -3, -2.4, -2.1, -2.01, -1.8, -1, 0, 1, 2, 4, 7, 11])
contours = ax.contour(xx, yy, zz, levels=levels, colors="0.55", linewidths=0.8)
ax.clabel(contours, fontsize=7, inline=True)
speed = np.hypot(uu, vv)
ax.streamplot(x, y, uu, vv, color=np.log1p(speed), cmap="Blues", density=1.15, linewidth=0.8, arrowsize=0.8)
ax.plot(trajectory[:, 0], trajectory[:, 1], color="#d62728", linewidth=2.7, label="trajectory from $(2,1)$")
ax.scatter([1, -1], [0, 0], s=55, c=["black", "#ff7f0e"], zorder=5)
ax.annotate("minimum $(1,0)$", (1, 0), (1.16, -0.28), arrowprops={"arrowstyle": "->"})
ax.annotate("degenerate critical point $(-1,0)$", (-1, 0), (-1.62, 0.38), arrowprops={"arrowstyle": "->"})
ax.scatter([2], [1], marker="*", s=130, color="#d62728", zorder=6)
ax.set(xlabel="$x$", ylabel="$y$", xlim=(x.min(), x.max()), ylim=(y.min(), y.max()), title="Contours of $U$ and the descending gradient flow $\\dot x=-U_x$, $\\dot y=-U_y$")
ax.set_aspect("equal")
ax.legend(loc="lower right")
fig.savefig(Path(Path(__file__).stem + ".png"), dpi=100, facecolor="white")
plt.close(fig)
