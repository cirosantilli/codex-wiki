"""Draw the half-space projection example; save basename.png to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/convex-mpl python3 ../convex-projection-optimization.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    a = np.array([2.0, 1.0])
    normal = np.ones(2)
    multiplier = (normal @ a - 1) / (normal @ normal)
    optimum = a - multiplier * normal
    objective = 0.5 * np.sum((optimum - a) ** 2)
    assert np.allclose(optimum, [1, 0])
    assert multiplier == 1 and objective == 1
    assert np.isclose(normal @ optimum, 1)
    assert np.allclose(optimum - a + multiplier * normal, 0)
    # Check the exact square-completion certificate on a grid, including
    # points on both sides of the constraint boundary.
    grid = np.linspace(-2.0, 3.4, 351)
    x, y = np.meshgrid(grid, grid)
    f = 0.5 * ((x - a[0]) ** 2 + (y - a[1]) ** 2)
    g = x + y - 1
    certificate = 1 + 0.5 * ((x - 1) ** 2 + y ** 2)
    assert np.allclose(f + multiplier * g, certificate)
    assert np.all(f[g <= 0] >= 1 - 1e-12)

    plt.rcParams.update({"font.size": 11})
    fig, ax = plt.subplots(figsize=(7.1, 5.8), layout="constrained", facecolor="white")
    ax.fill_between(grid, -2, 1 - grid, color="#d8eee8", alpha=1)
    contours = ax.contour(x, y, f, levels=[0.25, 0.5, 1, 2, 3],
                          colors="#447ca5", linewidths=1.2)
    ax.clabel(contours, inline=True, fmt="f = %g", fontsize=9)
    ax.plot(grid, 1 - grid, color="#26765c", lw=2.3)
    ax.plot([optimum[0], a[0]], [optimum[1], a[1]],
            color="#d17a24", lw=2.8)
    ax.scatter(*a, color="#b94f42", s=60, zorder=5)
    ax.scatter(*optimum, color="#26765c", s=60, zorder=5)
    ax.annotate("Target (2, 1)\nf = 0; infeasible", a, xytext=(2.2, 1.5),
                fontsize=10, bbox={"facecolor": "white", "edgecolor": "none", "pad": 2},
                arrowprops={"arrowstyle": "->", "color": "#b94f42"})
    ax.annotate("Optimum (1, 0)\nf = 1; multiplier = 1", optimum,
                xytext=(1.7, -0.8), fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2},
                arrowprops={"arrowstyle": "->", "color": "#26765c"})
    ax.text(-1.65, -1.35, "Feasible half-space\nx + y ≤ 1", color="#205e49")
    ax.text(-1.55, 2.78, "Boundary: x + y = 1", color="#205e49", fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    # Mark orthogonality of the displacement to the boundary tangent.
    tangent = np.array([-1, 1]) / np.sqrt(2)
    outward = normal / np.sqrt(2)
    corner = np.array([optimum + 0.17 * tangent,
                       optimum + 0.17 * (tangent + outward),
                       optimum + 0.17 * outward])
    ax.plot(*corner.T, color="#4c5357", lw=1)
    ax.axhline(0, color="#a1a8ac", lw=0.6)
    ax.axvline(0, color="#a1a8ac", lw=0.6)
    ax.set(xlim=(-1.8, 3.4), ylim=(-1.8, 3.1), aspect="equal",
           xlabel="x", ylabel="y", title="The first feasible contour touches at (1, 0)")
    ax.grid(alpha=0.16)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Projection {optimum.tolist()}, multiplier {multiplier:g}, objective {objective:g}")


if __name__ == "__main__":
    main()
