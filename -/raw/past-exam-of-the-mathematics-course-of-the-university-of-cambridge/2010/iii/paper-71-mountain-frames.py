"""Sketch mountain-wave phase and energy directions; output to caller CWD.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, origin, delta, color, label, offset):
    end = np.asarray(origin) + delta
    ax.annotate("", end, origin,
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.5})
    ax.text(*(end + offset), label, color=color, fontsize=10,
            ha="center", va="center",
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.7), dpi=100)
    fig.set_facecolor("white")
    x, z = np.meshgrid(np.linspace(0, 4.4, 400), np.linspace(0, 3.2, 300))
    for ax in axes:
        ax.contour(x, z, x + 2 * z, levels=np.arange(-2, 13, 1),
                   colors="#a7b5c1", linewidths=1.2)
        ax.set(xlim=(0, 4.4), ylim=(0, 3.2), ylabel="Height z")
        ax.set_aspect("equal")
        ax.text(3.3, 0.85, "Wave crests", rotation=-27, color="#5c6974",
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    origin = np.array([2.05, 1.55])
    axes[0].plot(np.linspace(0, 4.4, 400),
                 0.08 + 0.05 * np.sin(2 * np.pi * np.linspace(0, 4.4, 400)),
                 color="black", lw=1.5)
    arrow(axes[0], origin, np.array([0.6, 1.2]), "#176a9e",
          "Energy: up and downwind", np.array([0.15, 0.22]))
    axes[0].scatter(*origin, s=20, color="black", zorder=5)
    axes[0].text(1.55, 1.3, "Phase pattern stationary", fontsize=10,
                 ha="center", bbox={"facecolor": "white", "edgecolor": "none"})
    axes[0].set(xlabel="Downwind coordinate x", title="Frame fixed to the hills")
    arrow(axes[1], origin, np.array([-1.2, 0.6]), "#176a9e",
          "Energy: upstream and up", np.array([0.15, 0.3]))
    arrow(axes[1], origin, np.array([-0.45, -0.9]), "#bc5138",
          "Phase: upstream and down", np.array([0.0, -0.28]))
    axes[1].scatter(*origin, s=20, color="black", zorder=5)
    axes[1].set(xlabel="Moving coordinate x′ = x − U₀t",
                title="Frame moving with the mean wind")
    fig.suptitle("Uniform mountain wave: m/k = 2; arrows show directions", fontsize=12)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "paper-71-mountain-frames.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
