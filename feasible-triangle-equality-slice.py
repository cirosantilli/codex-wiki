"""Plot an equality slice and objective geometry; save basename.png to CWD.

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
    equality_normal = np.array([1.0, -1.0])
    line_projection = target + (1 - equality_normal @ target) * equality_normal / 2
    assert np.allclose(line_projection, [2.5, 1.5])
    assert sum(line_projection) > 3
    t = np.linspace(0, 1, 501)
    q = (t - 1) ** 2 + (t - 2) ** 2
    assert np.all(4 * t - 6 < 0) and q[-1] == 1
    optimum = np.array([2.0, 1.0])
    assert np.allclose(2 * (optimum - target) + np.ones(2) - equality_normal, 0)

    grid = np.linspace(-.3, 3.6, 450)
    x, y = np.meshgrid(grid, grid)
    f = (x - 2) ** 2 + (y - 2) ** 2
    assert np.allclose(f + (x + y - 3) - (x - y - 1), (x - 2) ** 2 + (y - 1) ** 2 + 1)

    plt.rcParams.update({"font.size": 11})
    fig, ax = plt.subplots(figsize=(7.4, 6.0), layout="constrained", facecolor="white")
    ax.set_facecolor("white")
    ax.add_patch(Polygon([(0, 0), (3, 0), (0, 3)], facecolor="#edf5ef",
                         edgecolor="#86a68f", lw=1.4, zorder=2))
    cs = ax.contour(x, y, f, levels=[.5, 1, 2, 5], colors="#7798b7",
                    linewidths=[1, 2, 1, 1], zorder=3)
    ax.clabel(cs, fmt=lambda v: f"f = {v:g}", fontsize=9,
              manual=[(1.5, 2.5), (2.7, 2.7), (.65, 2.25), (.17, .73)])
    ax.plot(grid, grid - 1, "--", color="#b78855", lw=1.4, zorder=3)
    ax.plot([1, 2], [0, 1], color="#a96020", lw=4, zorder=4)
    ax.plot([2, 2], [1, 2], color="#ce7d20", lw=2, zorder=4)
    ax.scatter([1, 2], [0, 1], c="#a96020", s=65, zorder=5)
    ax.scatter([2], [2], c="#b44f47", s=55, zorder=5)
    ax.scatter([2.5], [1.5], facecolors="white", edgecolors="#a96020", s=65, zorder=5)
    ax.scatter([1.5], [1.5], marker="x", c="#247654", s=55, zorder=5)
    box = {"facecolor": "white", "edgecolor": "none", "pad": 3}
    ax.annotate("Target (2, 2)\nf = 0", (2, 2), xytext=(2.7, 3.15),
                fontsize=10, bbox=box, arrowprops={"arrowstyle": "->", "color": "#b44f47"})
    ax.annotate("New optimum (2, 1)\nf = 1", (2, 1), xytext=(2.3, .25),
                fontsize=10, bbox=box, arrowprops={"arrowstyle": "->", "color": "#a96020"})
    ax.annotate("Nearest point on entire line\n(2.5, 1.5): violates x + y ≤ 3", (2.5, 1.5),
                xytext=(1.45, -.15), fontsize=9, bbox=box,
                arrowprops={"arrowstyle": "->", "color": "#a96020"})
    ax.annotate("Old optimum (1.5, 1.5)\nviolates x − y = 1", (1.5, 1.5),
                xytext=(.05, 2.93), fontsize=10, bbox=box,
                arrowprops={"arrowstyle": "->", "color": "#247654"})
    ax.text(.1, 1.65, "Original triangle F", color="#587460", fontsize=10, bbox=box)
    ax.text(2.91, 2.35, "x − y = 1", rotation=45, color="#9c5c24", fontsize=10)
    ax.annotate("(1, 0)", (1, 0), xytext=(.33, .18), fontsize=10, bbox=box)
    ax.set(xlim=(-.2, 3.6), ylim=(-.35, 3.6), aspect="equal", xlabel="x", ylabel="y",
           title="An added equality leaves only a feasible segment")
    ax.set_xticks([0, 1, 2, 3])
    ax.set_yticks([0, 1, 2, 3])
    ax.grid(alpha=.15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
