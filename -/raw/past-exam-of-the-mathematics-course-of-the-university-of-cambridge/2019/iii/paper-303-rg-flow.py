#!/usr/bin/env python3
"""Generate paper-303-rg-flow.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# A representative perturbative ratio b/c. Changing it moves the interacting
# fixed point without changing the local flow topology discussed in the answer.
b = 0.12
c = 1.0
g_star = np.sqrt(b / c)
x_star = (-1.0 + np.sqrt(1.0 + 4.0 * g_star**2)) / 2.0


def beta(point):
    """Return (d(mu^2/Lambda^2)/ds, dg/ds)."""
    x, g = point
    return np.array(
        [2.0 * x - 2.0 * g**2 / (1.0 + x), b * g**2 - c * g**4]
    )


def backward_branch(sign):
    """Trace one branch of the stable manifold backward from the fixed point."""
    a = 2.0 + 2.0 * g_star**2 / (1.0 + x_star) ** 2
    cross = -4.0 * g_star / (1.0 + x_star)
    stable = 2.0 * b * g_star - 4.0 * c * g_star**3
    tangent = np.array([-cross / (a - stable), 1.0])
    tangent /= np.linalg.norm(tangent)
    point = np.array([x_star, g_star]) + sign * 2.0e-4 * tangent
    points = [point.copy()]
    dt = -0.03
    for _ in range(10000):
        k1 = beta(point)
        k2 = beta(point + dt * k1 / 2.0)
        k3 = beta(point + dt * k2 / 2.0)
        k4 = beta(point + dt * k3)
        point = point + dt * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        if not (-0.28 <= point[0] <= 0.72 and 0.0 <= point[1] <= 0.86):
            break
        points.append(point.copy())
    return np.array(points)


x = np.linspace(-0.25, 0.68, 150)
g = np.linspace(0.002, 0.82, 150)
xx, gg = np.meshgrid(x, g)
uu = 2.0 * xx - 2.0 * gg**2 / (1.0 + xx)
vv = b * gg**2 - c * gg**4
speed = np.hypot(uu, vv)
uu /= np.maximum(speed, 1.0e-12)
vv /= np.maximum(speed, 1.0e-12)

fig, ax = plt.subplots(figsize=(11, 6.5), dpi=100)
ax.streamplot(
    xx,
    gg,
    uu,
    vv,
    density=(1.35, 1.15),
    linewidth=0.9,
    arrowsize=1.15,
    color="#56708a",
)

g_curve = np.linspace(0.0, 0.82, 500)
x_mass = (-1.0 + np.sqrt(1.0 + 4.0 * g_curve**2)) / 2.0
ax.plot(x_mass, g_curve, "--", color="#d77c21", lw=2.0, label=r"$\beta_{\mu^2}=0$")
ax.axhline(g_star, color="#7650a8", ls=":", lw=2.0, label=r"$\beta_g=0$ at $g=g_*$")

for sign in (-1.0, 1.0):
    branch = backward_branch(sign)
    ax.plot(branch[:, 0], branch[:, 1], color="#b3262e", lw=2.7)
ax.plot([], [], color="#b3262e", lw=2.7, label="tuned critical trajectory")

ax.scatter([0.0, x_star], [0.0, g_star], s=75, color="black", zorder=5)
ax.annotate("Gaussian fixed point", (0.0, 0.0), xytext=(0.035, 0.075), fontsize=11)
ax.annotate(
    "interacting fixed point",
    (x_star, g_star),
    xytext=(x_star + 0.07, g_star + 0.075),
    arrowprops={"arrowstyle": "->", "lw": 1.1},
    fontsize=11,
)

ax.set_xlim(-0.25, 0.68)
ax.set_ylim(0.0, 0.82)
ax.set_xlabel(r"$\mu^2/\Lambda^2$", fontsize=13)
ax.set_ylabel(r"$g$", fontsize=13)
ax.set_title(r"Representative RG flow for $b/c=0.12$ (arrows point toward the infrared)", fontsize=14)
ax.grid(alpha=0.16)
ax.legend(loc="upper left", framealpha=0.95)
fig.tight_layout()
fig.savefig(Path(Path(__file__).stem + ".png"), facecolor="white")
plt.close(fig)
