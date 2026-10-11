"""Original spiral sketches; Python 3.14, NumPy and Matplotlib from root pyproject.

Writes the PNG basename in cwd. Endpoints use -pi < Arg(z) <= pi.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def point(t):
    return np.exp(t)*np.cos(t), np.exp(t)*np.sin(t)


def main():
    theta = np.linspace(-np.pi, np.pi, 1800)
    x, y = point(theta)
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), layout="constrained")
    fig.set_facecolor("white")
    for ax in axes:
        ax.plot(x, y, color="#176b9b", lw=2)
        ax.axhline(0, color="0.55", lw=0.8)
        ax.axvline(0, color="0.55", lw=0.8)
        ax.set(xlabel="$\\mathrm{Re}\\,z$", ylabel="$\\mathrm{Im}\\,z$", aspect="equal")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.12)
    axes[0].set(xlim=(-25, 3.3), ylim=(-1.2, 9), title="One turn: $r=e^{\\theta}$")
    axes[0].scatter([-np.exp(np.pi)], [0], color="#b83c32", zorder=5)
    axes[0].annotate("$-e^{\\pi}$ (included)", (-np.exp(np.pi), 0), xytext=(8, 14),
                     textcoords="offset points")
    axes[0].scatter([0], [np.exp(np.pi/2)], color="#176b9b", s=20)
    axes[0].annotate("$i e^{\\pi/2}$", (0, np.exp(np.pi/2)), xytext=(-50, 8),
                     textcoords="offset points")
    axes[0].annotate("", point(2.65), xytext=point(2.50),
                     arrowprops={"arrowstyle": "->", "color": "#176b9b", "lw": 2})
    axes[1].set(xlim=(-0.65, 1.85), ylim=(-0.6, 1.9), title="Enlargement near the origin")
    axes[1].scatter([-np.exp(-np.pi)], [0], s=45, edgecolors="#b83c32", facecolors="white", zorder=6)
    axes[1].annotate("$-e^{-\\pi}$ (excluded)", (-np.exp(-np.pi), 0), xytext=(-30, 43),
                     textcoords="offset points", arrowprops={"arrowstyle": "->", "lw": 0.8})
    axes[1].scatter([1, 0], [0, -np.exp(-np.pi/2)], color="#176b9b", s=20)
    axes[1].annotate("$1$", (1, 0), xytext=(8, -15), textcoords="offset points")
    axes[1].annotate("$-i e^{-\\pi/2}$", (0, -np.exp(-np.pi/2)), xytext=(10, -17),
                     textcoords="offset points")
    axes[1].annotate("", point(0.6), xytext=point(0.46),
                     arrowprops={"arrowstyle": "->", "color": "#176b9b", "lw": 2})
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
