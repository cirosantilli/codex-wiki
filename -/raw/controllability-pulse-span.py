"""Analytic double-integrator timing diagram; no measured data.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../controllability-pulse-span.py
Outputs controllability-pulse-span.png to CWD.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
All coordinates are dimensionless. Only NumPy and Matplotlib are required.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def trajectory(t):
    """Exact p,v for u=+1 on [0,1), then -1 on [1,2]."""
    q = np.maximum(t - 1, 0)
    return t**2 / 2 - q**2, t - 2 * q


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.9), layout="constrained")
    fig.set_facecolor("white")
    blue, orange = "#176b9a", "#cc7024"
    fig.suptitle("One input, two endpoint directions: double integrator at T = 2", fontsize=15)
    left, middle, right = axs
    left.plot([0, 1, 1, 2], [1, 1, -1, -1], color=blue, lw=3)
    left.axhline(0, color="#999999", lw=0.8)
    left.set(xlim=(-0.06, 2.06), ylim=(-1.45, 1.55), xlabel="Time t", ylabel="Acceleration input u", title="Accelerate, then brake")
    left.set_xticks([0, 1, 2])
    left.set_yticks([-1, 0, 1])
    left.text(0.5, 1.18, "+1", ha="center", color=blue)
    left.text(1.5, -1.25, "−1", ha="center", color=blue)

    t = np.linspace(0, 2, 801)
    p, v = trajectory(t)
    middle.plot(p[t <= 1], v[t <= 1], color=blue, lw=3)
    middle.plot(p[t >= 1], v[t >= 1], color=orange, lw=3)
    middle.scatter([0, 0.5, 1], [0, 1, 0], c=["#333333", blue, orange], s=35, zorder=4)
    middle.annotate("Start (0, 0)", (0, 0), xytext=(0.04, -0.16), fontsize=10)
    middle.annotate("Switch (½, 1)", (0.5, 1), xytext=(0.15, 1.16), fontsize=10)
    middle.annotate("Rest again\n(1, 0)", (1, 0), xytext=(0.64, 0.16), fontsize=10)
    for j, color in [(240, blue), (560, orange)]:
        middle.annotate("", (p[j + 20], v[j + 20]), (p[j], v[j]), arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
    middle.set(xlim=(-0.09, 1.14), ylim=(-0.26, 1.4), xlabel="Position p", ylabel="Velocity v", title="Analytic state path")
    middle.set_xticks([0, 0.5, 1])

    # Endpoint contributions of unit-amplitude inputs on the two halves.
    endpoint_map = np.array([[1.5, 0.5], [1, 1]])
    assert np.isclose(np.linalg.det(endpoint_map), 1)
    assert np.allclose(endpoint_map @ [1, -1], [1, 0])
    for column, color in zip(endpoint_map.T, [blue, orange]):
        right.annotate("", column, (0, 0), arrowprops={"arrowstyle": "->", "color": color, "lw": 3})
    right.annotate("First half\n(3/2, 1)", (1.5, 1), xytext=(1.34, 1.2), ha="center", fontsize=10, color=blue)
    right.annotate("Second half\n(1/2, 1)", (0.5, 1), xytext=(0.28, 1.2), ha="center", fontsize=10, color=orange)
    right.plot([1.5, 1], [1, 0], ls="--", color=orange, lw=1.7)
    right.scatter([0, 1], [0, 0], color="#333333", s=30, zorder=4)
    right.text(0.96, -0.16, "Difference = (1, 0)", ha="center", fontsize=10)
    right.text(0.85, -0.54, "det = 1 → rank 2\nReal amplitudes span the plane", ha="center", fontsize=10, bbox={"facecolor": "white", "edgecolor": "#cccccc", "boxstyle": "round,pad=0.3"})
    right.set(xlim=(-0.26, 1.96), ylim=(-0.76, 1.68), xlabel="Final position p(2)", ylabel="Final velocity v(2)", title="Two independent contributions")
    right.set_aspect("equal", adjustable="box")
    for ax in axs:
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, -0.005, "Analytic mathematical example • dimensionless coordinates • no measurements", ha="center", fontsize=10)
    fig.savefig(Path.cwd() / "controllability-pulse-span.png", dpi=120, facecolor="white", transparent=False, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
