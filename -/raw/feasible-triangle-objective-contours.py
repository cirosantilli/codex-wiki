"""Plot the feasible triangle and squared-distance contours; save basename.png to CWD.

Tested: Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


def main():
    target = np.array([2.0, 2.0])
    normal = np.ones(2)
    optimum = target - ((normal @ target - 3) / (normal @ normal)) * normal
    assert np.allclose(optimum, [1.5, 1.5])
    assert np.isclose(np.sum((optimum - target) ** 2), 0.5)
    assert np.allclose(2 * (optimum - target) + normal, 0)

    grid = np.linspace(-0.4, 3.5, 450)
    x, y = np.meshgrid(grid, grid)
    f = (x - 2) ** 2 + (y - 2) ** 2
    mask = (x >= 0) & (y >= 0) & (x + y <= 3)
    assert np.all(f[mask] >= 0.5 - 1e-12)
    assert np.allclose(f, ((x + y - 4) ** 2 + (x - y) ** 2) / 2)

    plt.rcParams.update({"font.size": 11})
    fig, ax = plt.subplots(figsize=(7.4, 6.0), layout="constrained", facecolor="white")
    ax.set_facecolor("white")
    ax.add_patch(Polygon([(0, 0), (3, 0), (0, 3)], facecolor="#dcefe5",
                         edgecolor="#247654", lw=2, zorder=2))
    cs = ax.contour(x, y, f, levels=[0.5, 1, 2, 4], colors="#648cb0",
                    linewidths=[2, 1, 1, 1], zorder=3)
    ax.clabel(cs, fmt=lambda v: f"f = {v:g}", fontsize=9,
              manual=[(2.5, 2.5), (2.95, 2.05), (2.85, 3.1), (0.2, 2.85)])
    ax.plot([1.5, 2], [1.5, 2], color="#ce7d20", lw=2.5, zorder=4)
    ax.scatter([2, 1.5], [2, 1.5], c=["#b44f47", "#247654"], s=65, zorder=5)
    ax.scatter([1], [1], color="#57636b", s=35, zorder=5)
    box = {"facecolor": "white", "edgecolor": "none", "pad": 3}
    ax.annotate("Unconstrained optimum (2, 2)\nf = 0; infeasible", (2, 2),
                xytext=(0.8, 3.22), fontsize=10, bbox=box,
                arrowprops={"arrowstyle": "->", "color": "#b44f47"})
    ax.annotate("Constrained optimum (1.5, 1.5)\nf = 0.5", (1.5, 1.5),
                xytext=(1.65, 0.35), fontsize=10, bbox=box,
                arrowprops={"arrowstyle": "->", "color": "#247654"})
    ax.annotate("(1, 1): feasible\nf = 2", (1, 1), xytext=(0.13, 0.27),
                fontsize=10, bbox=box, arrowprops={"arrowstyle": "->"})
    ax.text(0.14, 1.65, "Feasible region F\nx ≥ 0, y ≥ 0\nx + y ≤ 3", fontsize=10,
            color="#205f44", bbox=box)
    ax.text(2.45, 0.93, "x + y = 3", rotation=-45, color="#205f44", fontsize=10)
    # Perpendicular displacement to the active edge.
    p = optimum
    tangent = np.array([-1.0, 1.0]) / np.sqrt(2)
    outward = normal / np.sqrt(2)
    corner = np.array([p + .14 * tangent, p + .14 * (tangent + outward), p + .14 * outward])
    ax.plot(*corner.T, color="#5e6369", lw=1, zorder=4)
    ax.set(xlim=(-.2, 3.5), ylim=(-.2, 3.6), aspect="equal", xlabel="x", ylabel="y",
           title="Feasibility selects points; the objective ranks them")
    ax.set_xticks([0, 1, 2, 3])
    ax.set_yticks([0, 1, 2, 3])
    ax.grid(alpha=.15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
