"""Exact bounded reachable region and invariant shared-input line.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../reachability-bounded-and-shared.py
Outputs reachability-bounded-and-shared.png to CWD.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
The curves are analytic toy predictions, not measurements. T=2, |u|<=1.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def position_bounds(v, duration):
    center = duration * v / 2
    radius = (duration**2 - v**2) / 4
    return center - radius, center + radius


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 4.8), layout="constrained")
    fig.set_facecolor("white")
    fig.suptitle("Reachable endpoints depend on both dynamics and allowed inputs", fontsize=15)
    blue, orange, red = "#176b9a", "#cc7024", "#b32939"
    left, right = axs
    v = np.linspace(-2, 2, 1001)
    lower, upper = position_bounds(v, 2)
    assert np.all(lower <= upper)
    assert np.allclose(position_bounds(np.array([0]), 2), [[-1], [1]])
    left.fill_betweenx(v, lower, upper, color="#d6eaf5")
    left.plot(upper, v, color=blue, lw=2.3, label="+1 first, −1 last")
    left.plot(lower, v, color=orange, lw=2.3, label="−1 first, +1 last")
    left.plot([-1, 1], [0, 0], color="#333333", lw=2)
    left.scatter([-1, 0, 1], [0, 0, 0], s=30, color="#333333", zorder=4)
    left.scatter([1.5], [0], s=60, marker="x", color=red, lw=2, zorder=5)
    left.annotate("(3/2, 0)\nunreachable", (1.5, 0), xytext=(1.22, -0.72), ha="center", fontsize=10, color=red, arrowprops={"arrowstyle": "->", "color": red})
    left.annotate("Rest-to-rest interval [−1, 1]", (0, 0), xytext=(-0.22, 0.64), ha="center", fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"}, bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    left.set(title="Double integrator: rank 2\nT = 2, |u| ≤ 1", xlabel="Final position p", ylabel="Final velocity v", xlim=(-2.45, 2.45), ylim=(-2.45, 2.45))
    left.legend(loc="lower left", fontsize=9, framealpha=1)

    # A=0, B=(1,1)^T: only the diagonal direction is influenced.
    shared_matrix = np.array([[1, 0], [1, 0]])
    assert np.linalg.matrix_rank(shared_matrix) == 1
    q = np.array([-3, 3])
    right.plot(q, q, "--", color="#888888", lw=2, label="Unrestricted inputs: entire line")
    right.plot([-2, 2], [-2, 2], color=blue, lw=4, label="|u| ≤ 1: only the segment")
    right.scatter([-2, 0, 2], [-2, 0, 2], color=blue, s=30, zorder=4)
    right.scatter([1], [0], marker="x", color=red, s=60, lw=2, zorder=5)
    right.annotate("(1, 0) unreachable\nat every duration", (1, 0), xytext=(1.07, -1.3), ha="center", fontsize=10, color=red, arrowprops={"arrowstyle": "->", "color": red})
    right.text(-2.75, 2.25, "Invariant: z₁ − z₂ = 0\nrange C = span{(1, 1)}", fontsize=10, va="top", bbox={"facecolor": "white", "edgecolor": "none"})
    right.set(title="Shared input: rank 1\nż₁ = ż₂ = u, start at zero", xlabel="Final state z₁", ylabel="Final state z₂", xlim=(-3, 3), ylim=(-3, 3))
    right.legend(loc="lower left", fontsize=9, framealpha=1)
    for ax in axs:
        ax.set_facecolor("white")
        ax.axhline(0, color="#bbbbbb", lw=0.7, zorder=0)
        ax.axvline(0, color="#bbbbbb", lw=0.7, zorder=0)
        ax.grid(alpha=0.18)
        ax.set_aspect("equal", adjustable="box")
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, -0.008, "Analytic mathematical examples • dimensionless coordinates • no measurements", ha="center", fontsize=10)
    fig.savefig(Path.cwd() / "reachability-bounded-and-shared.png", dpi=120, facecolor="white", transparent=False, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
