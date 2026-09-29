"""Illustrate y' + 2ty = t; tested with Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from the desired output directory; writes integrating-factor-variable-coefficient.png.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np


def main():
    t = np.linspace(0.0, 3.0, 601)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.3), dpi=120,
                             constrained_layout=True, facecolor="white")
    for initial, color in ((0.0, "#2176a5"), (1.0, "#bb4b20")):
        axes[0].plot(t, 0.5+(initial-0.5)*np.exp(-t*t), lw=2.7,
                     color=color, label=f"y(0) = {initial:g}", zorder=3)
        axes[0].scatter([0], [initial], color=color, s=26, zorder=4)
    axes[0].axhline(0.5, ls="--", color="#258568", lw=2,
                   label="constant particular solution: 1/2", zorder=3)
    axes[0].set(title=r"Direction field: $y'=t(1-2y)$", ylabel="state y",
                ylim=(-0.08, 1.15))
    axes[0].legend(loc="upper right", fontsize=8.7, framealpha=1)
    axes[1].plot(t, np.exp(-t*t), color="#2176a5", lw=2.7,
                 label=r"variable rate $a(t)=2t$: $e^{-t^2}$")
    axes[1].plot(t, np.exp(-2*t), color="#bb4b20", lw=2.3, ls="--",
                 label=r"constant rate $a(t)=2$: $e^{-2t}$")
    axes[1].scatter([2], [np.exp(-4)], color="#444444", zorder=4)
    axes[1].annotate("same accumulated rate at t = 2",
                     xy=(2, np.exp(-4)), xytext=(0.65, 0.32), fontsize=9,
                     arrowprops={"arrowstyle": "->", "color": "#555555"})
    axes[1].set(title="How much initial-data difference remains?",
                ylabel="fraction of initial difference", ylim=(-0.02, 1.05))
    axes[1].legend(loc="upper right", fontsize=9, framealpha=1)
    for ax in axes:
        ax.set(xlabel="time t", xlim=(-0.04, 3))
        ax.set_facecolor("white")
        ax.grid(alpha=0.15)
    # Draw equal-length segments in display coordinates, preserving dy/dt.
    fig.canvas.draw()
    grid_t, grid_y = np.meshgrid(np.linspace(0, 3, 20), np.linspace(0, 1, 11))
    points = np.column_stack((grid_t.ravel(), grid_y.ravel()))
    directions = np.column_stack((np.ones(len(points)),
                                  points[:, 0]*(1-2*points[:, 1])))
    display = axes[0].transData.transform(points)
    vectors = axes[0].transData.transform(points+directions)-display
    vectors /= np.linalg.norm(vectors, axis=1)[:, None]
    ends = np.stack((display-5*vectors, display+5*vectors), axis=1)
    segments = axes[0].transData.inverted().transform(ends.reshape(-1, 2)).reshape(-1, 2, 2)
    axes[0].add_collection(LineCollection(segments, colors="#aeb8c0",
                                         linewidths=0.9, zorder=1))
    fig.savefig(Path.cwd() / "integrating-factor-variable-coefficient.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
