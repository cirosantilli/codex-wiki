"""Draw original coordinate slices of f(x,y)=x²+xy+2y².

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Write the matching opaque PNG to the current working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def height(x, y):
    return x * x + x * y + 2 * y * y


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    blue, orange = "#2166ac", "#c65102"
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.4, 4.7), dpi=120)
    fig.patch.set_facecolor("white")
    x = np.linspace(0.55, 1.45, 240)
    xx, yy = np.meshgrid(x, x)
    lines = left.contour(xx, yy, height(xx, yy), levels=np.arange(1.5, 8.6, 0.5),
                         colors="#a4a8ae", linewidths=0.9)
    left.clabel(lines, inline=True, fontsize=9, fmt="%g")
    left.plot(x, np.ones_like(x), color=blue, linewidth=3, label="Change x; hold y = 1")
    left.plot(np.ones_like(x), x, color=orange, linewidth=3, label="Change y; hold x = 1")
    left.scatter([1], [1], color="#111111", s=50, zorder=6)
    left.annotate("a = (1, 1)\nf(a) = 4", (1, 1), xytext=(1.12, 0.7),
                  arrowprops={"arrowstyle": "->", "color": "#333333"}, fontsize=11,
                  bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.95})
    left.set(xlabel="x", ylabel="y", xlim=(0.55, 1.45), ylim=(0.55, 1.45),
             title="Coordinate paths on the same surface")
    left.set_aspect("equal")
    left.legend(loc="upper left", fontsize=10, framealpha=0.97)

    t = np.linspace(-0.4, 0.4, 241)
    right.plot(t, 3*t+t*t, color=blue, linewidth=2.6, label=r"x slice: $3t+t^2$")
    right.plot(t, 3*t, color=blue, linestyle="--", linewidth=1.7, label="x tangent: 3t")
    right.plot(t, 5*t+2*t*t, color=orange, linewidth=2.6, label=r"y slice: $5t+2t^2$")
    right.plot(t, 5*t, color=orange, linestyle="--", linewidth=1.7, label="y tangent: 5t")
    right.scatter([0], [0], color="#111111", s=35, zorder=6)
    right.axhline(0, color="#bbbbbb", linewidth=0.8)
    right.axvline(0, color="#bbbbbb", linewidth=0.8)
    right.set(xlabel="Coordinate displacement t", ylabel="Height change from 4",
              title="Tangents give slopes 3 and 5", xlim=(-0.4, 0.4))
    right.grid(alpha=0.2)
    right.legend(loc="upper left", fontsize=10, framealpha=0.97)
    fig.suptitle(r"Partial derivatives of $f(x,y)=x^2+xy+2y^2$ at $(1,1)$", fontsize=16)
    fig.subplots_adjust(left=0.06, right=0.985, bottom=0.15, top=0.81, wspace=0.31)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
