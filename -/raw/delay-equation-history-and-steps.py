"""Exact polynomial method-of-steps diagram; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media; writes delay-equation-history-and-steps.png in the CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch


def exact(t):
    """y'=y(t-1), history 1, restricted to -1 <= t <= 3."""
    t = np.asarray(t)
    return 1 + np.maximum(t, 0) + np.maximum(t - 1, 0) ** 2 / 2 + np.maximum(t - 2, 0) ** 3 / 6


def main():
    probes = np.array([0.2, 0.8, 1.3, 1.8, 2.2, 2.7])
    derivative = 1 + np.maximum(probes - 1, 0) + np.maximum(probes - 2, 0) ** 2 / 2
    assert np.allclose(derivative, exact(probes - 1), rtol=0, atol=1e-14)
    assert np.allclose(exact([0, 1, 2, 3]), [1, 2, 7 / 2, 37 / 6])

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig = plt.figure(figsize=(8, 5.5), dpi=120, facecolor="white")
    grid = fig.add_gridspec(2, 1, height_ratios=[3.1, 1], hspace=0.42)
    ax = fig.add_subplot(grid[0])
    lower = fig.add_subplot(grid[1])
    colors = ["#636b74", "#2468ad", "#c66b13", "#287e60"]
    labels = ["Given history", "Step 1", "Step 2", "Step 3"]
    for index, (start, color, label) in enumerate(zip(range(-1, 3), colors, labels)):
        t = np.linspace(start, start + 1, 181)
        ax.axvspan(start, start + 1, color=color, alpha=0.065)
        ax.plot(t, exact(t), color=color, lw=2.8, ls="--" if index == 0 else "-")
        ax.text(start + 0.5, 6.6, label, ha="center", color=color, weight="bold", fontsize=10)
    for t, label in [(1, "$2$"), (2, "$7/2$"), (3, "$37/6$")]:
        ax.plot(t, exact(t), "o", color="#263442", ms=4)
        ax.annotate(label, (t, exact(t)), xytext=(-10, 10), textcoords="offset points", ha="right")
    ax.plot([0.5, 1.5], exact([0.5, 1.5]), "o", color="#263442", ms=5, zorder=5)
    tangent_t = np.array([1.13, 1.87])
    ax.plot(tangent_t, 21 / 8 + 1.5 * (tangent_t - 1.5), color="#263442", lw=1.2, ls=":")
    ax.annotate("Read the past: $y(1/2)=3/2$", (0.5, 1.5), xytext=(-0.85, 3.6),
                arrowprops={"arrowstyle": "->", "color": "#263442"}, fontsize=10)
    ax.annotate("Slope now: $y'(3/2)=3/2$", (1.5, 21 / 8), xytext=(0.55, 5.05),
                arrowprops={"arrowstyle": "->", "color": "#263442"}, fontsize=10)
    ax.axvline(0, color="#8a8a8a", lw=0.8)
    ax.set(xlim=(-1.08, 3.13), ylim=(0.5, 7), xticks=range(-1, 4), ylabel="$y(t)$", xlabel="Time $t$ (delay = 1)")
    ax.grid(axis="y", alpha=0.16)
    ax.set_title("A known past builds the future: $y'(t)=y(t-1)$", pad=17, fontsize=14)

    lower.set(xlim=(-1.08, 3.13), ylim=(-0.1, 1.5))
    lower.axis("off")
    formulas = ["Given: $y=1$", "$y'=1$", "$y'=t$", "$y'=t+(t-2)^2/2$"]
    for start, color, label in zip(range(-1, 3), colors, formulas):
        lower.plot([start + 0.06, start + 0.94], [0.6, 0.6], color=color, lw=5, solid_capstyle="round")
        lower.text(start + 0.5, 0.28, label, ha="center", va="top", fontsize=10, color=color)
        lower.text(start + 0.5, 1.18, f"[{start}, {start + 1}]", ha="center", fontsize=10)
    for boundary in [0, 1, 2]:
        lower.add_patch(FancyArrowPatch((boundary - 0.35, 0.84), (boundary + 0.35, 0.84),
                                       connectionstyle="arc3,rad=-0.5", arrowstyle="->", mutation_scale=13,
                                       color="#3d4650", lw=1.2))
    fig.subplots_adjust(left=0.08, right=0.975, top=0.88, bottom=0.07)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
