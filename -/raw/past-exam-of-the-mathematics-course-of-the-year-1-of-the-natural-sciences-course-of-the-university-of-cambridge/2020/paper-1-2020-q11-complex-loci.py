"""Original Argand sketches; Python 3.14, NumPy and Matplotlib.

Dependencies are in root pyproject.toml; PNG output is in cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 4.9), layout="constrained")
    fig.set_facecolor("white")
    t = np.linspace(0, 2*np.pi, 700)
    axes[0].plot(np.sqrt(3)*np.cos(t), 1+2*np.sin(t), color="#176b9b", lw=2.2)
    axes[0].set_title("$a=4$: ellipse")
    axes[1].plot([0, 0], [0, 2], color="#176b9b", lw=4, zorder=3)
    axes[1].set_title("$a=2$: closed segment")
    for ax in axes:
        ax.axhline(0, color="0.5", lw=0.8)
        ax.axvline(0, color="0.5", lw=0.8)
        ax.scatter([0, 0], [0, 2], color="#b83c32", zorder=5)
        ax.annotate("$0$", (0, 0), xytext=(7, -14), textcoords="offset points")
        ax.annotate("$2i$", (0, 2), xytext=(7, 5), textcoords="offset points")
        ax.set(xlim=(-2.3, 2.3), ylim=(-1.4, 3.5), xlabel="$\\mathrm{Re}\\,z$",
               ylabel="$\\mathrm{Im}\\,z$", aspect="equal")
        ax.set_xticks([-2, -1, 0, 1, 2])
        ax.set_yticks([-1, 0, 1, 2, 3])
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
