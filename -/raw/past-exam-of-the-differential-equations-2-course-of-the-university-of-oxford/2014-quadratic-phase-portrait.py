"""Phase sketch for a quadratic planar system; PNG output is in the CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 as declared in
the repository pyproject.toml. Invariant manifolds are numerical sketches
from small eigenvector displacements, using an adaptive-step RK4 trace.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def field(z):
    x, y = z
    return np.array([x * (1.0 - x - y), 2.0 - 2.0 * x - y])


def trace(seed, direction, bounds):
    z = np.array(seed, dtype=float)
    points = [z.copy()]
    xmin, xmax, ymin, ymax = bounds
    for _ in range(14000):
        speed = np.linalg.norm(field(z))
        if speed < 1.0e-9:
            break
        dt = direction * 0.008 / max(1.0, speed)
        k1 = field(z)
        k2 = field(z + dt * k1 / 2)
        k3 = field(z + dt * k2 / 2)
        k4 = field(z + dt * k3)
        z = z + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        points.append(z.copy())
        if not (xmin <= z[0] <= xmax and ymin <= z[1] <= ymax):
            break
    return np.array(points)


def flow_arrow(ax, points, color):
    length = np.r_[0, np.cumsum(np.linalg.norm(np.diff(points, axis=0), axis=1))]
    if length[-1] < 0.2:
        return
    z = points[np.searchsorted(length, 0.55 * length[-1])]
    velocity = field(z)
    velocity = velocity / np.linalg.norm(velocity)
    ax.annotate("", xy=z + 0.09 * velocity, xytext=z - 0.09 * velocity,
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": 1.8})


def main():
    bounds = (-0.5, 2.2, -1.2, 3.5)
    xmin, xmax, ymin, ymax = bounds
    x = np.linspace(xmin, xmax, 240)
    y = np.linspace(ymin, ymax, 260)
    xx, yy = np.meshgrid(x, y)
    u = xx * (1 - xx - yy)
    v = 2 - 2 * xx - yy
    speed = np.hypot(u, v)
    denominator = np.maximum(speed, 1.0e-12)

    fig, ax = plt.subplots(figsize=(6.5, 6.0), layout="constrained")
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    ax.streamplot(x, y, u / denominator, v / denominator, color="#b7bec4",
                  linewidth=0.65, density=1.35, arrowsize=0.8, zorder=1)
    ax.axvline(0, color="#4c7592", ls="--", lw=1.2,
               label="x nullclines: x=0, y=1-x")
    ax.plot(x, 1 - x, color="#4c7592", ls="--", lw=1.2)
    ax.plot(x, 2 - 2 * x, color="#b17b24", ls="--", lw=1.2,
            label="y nullcline: y=2-2x")

    saddle = np.array([1.0, 0.0])
    for name, eigenvector, direction, color in [
        ("Stable manifold", [1, np.sqrt(2)], -1, "#7e3d9b"),
        ("Unstable manifold", [1, -np.sqrt(2)], 1, "#c94336"),
    ]:
        eig = np.array(eigenvector) / np.linalg.norm(eigenvector)
        for sign in [-1, 1]:
            points = trace(saddle + sign * 1.0e-4 * eig, direction, bounds)
            ax.plot(points[:, 0], points[:, 1], color=color, lw=2.0,
                    label=name if sign == -1 else None, zorder=3)
            flow_arrow(ax, points, color)

    ax.scatter([0], [2], color="#1967ac", s=55, zorder=5)
    ax.scatter([1], [0], color="black", s=55, marker="x", zorder=5)
    ax.annotate("Stable improper node\n(0, 2)", (0, 2), xytext=(12, 12),
                textcoords="offset points", fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.85})
    ax.annotate("Saddle (1, 0)", (1, 0), xytext=(12, 6),
                textcoords="offset points", fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.85})
    ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax), xlabel="x", ylabel="y",
           title="Nullclines, flow directions and saddle manifolds")
    ax.set_aspect("equal")
    ax.legend(loc="upper right", fontsize=8, framealpha=0.95)
    ax.grid(alpha=0.12)
    fig.savefig(Path("2014-quadratic-phase-portrait.png"), dpi=135, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
