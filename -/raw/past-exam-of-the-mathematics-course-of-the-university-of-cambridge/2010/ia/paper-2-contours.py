"""Contour sketch for Paper 2, Question 8A.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Uses the caller's MPLCONFIGDIR unchanged. Writes only the PNG basename
in the current working directory, so Make can run it inside _media.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    grid = np.linspace(-0.42, 1.3, 650)
    x, y = np.meshgrid(grid, grid)
    values = x * y * (1 - x - y)
    fig, ax = plt.subplots(figsize=(7.6, 6.4), dpi=125, facecolor="white")
    ax.set_facecolor("white")
    negative = ax.contour(
        x, y, values, levels=[-0.12, -0.06, -0.025, -0.008],
        colors="#2563a6", linestyles="dashed", linewidths=1.05,
    )
    positive = ax.contour(
        x, y, values, levels=[0.008, 0.02, 0.03, 0.035],
        colors="#b94f14", linestyles="solid", linewidths=1.1,
    )
    ax.clabel(negative, fontsize=8, inline=True, fmt="%.3g")
    ax.clabel(positive, fontsize=8, inline=True, fmt="%.3g")
    ax.axvline(0, color="#222222", linewidth=1.7)
    ax.axhline(0, color="#222222", linewidth=1.7)
    ax.plot(grid, 1 - grid, color="#222222", linewidth=1.7)
    for point, offset, text in [
        ((0, 0), (9, -22), "(0, 0): saddle"),
        ((1, 0), (7, -22), "(1, 0): saddle"),
        ((0, 1), (9, 9), "(0, 1): saddle"),
        ((1 / 3, 1 / 3), (17, 15), "(1/3, 1/3)\nlocal maximum: 1/27"),
    ]:
        ax.plot(*point, "o", color="#161616", markersize=5)
        ax.annotate(
            text, point, xytext=offset, textcoords="offset points",
            fontsize=9, arrowprops={"arrowstyle": "-", "color": "#555555"},
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.93},
        )
    ax.text(-0.34, 1.22, "Black: zero contours\nOrange: positive; blue dashed: negative",
            fontsize=9, bbox={"facecolor": "white", "edgecolor": "none"})
    ax.set(xlim=(-0.42, 1.3), ylim=(-0.42, 1.3), xlabel="x", ylabel="y",
           title="Contours of f(x, y) = xy(1 - x - y)")
    ax.set_aspect("equal")
    fig.tight_layout()
    fig.savefig(Path("paper-2-contours.png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
