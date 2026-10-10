"""Original fixed-step paths on a quadratic; Python 3.14, matplotlib 3.10.7."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 6.0), dpi=120)
    fig.patch.set_facecolor("white")
    grid_x = np.linspace(-0.4, 2.55, 320)
    grid_y = np.linspace(-2.25, 2.25, 420)
    x, y = np.meshgrid(grid_x, grid_y)
    energy = (x * x + 9 * y * y) / 2
    for ax, eta, steps, color in zip(
        axes, (0.2, 0.25), (10, 3), ("#176c9c", "#bd4729"), strict=True
    ):
        k = np.arange(steps + 1)
        points = np.column_stack((2 * (1 - eta) ** k, (1 - 9 * eta) ** k))
        contours = ax.contour(x, y, energy, levels=[0.5, 2, 6.5, 12, 20],
                              colors="#b5bdc5", linewidths=0.9)
        ax.clabel(contours, inline=True, fontsize=9, fmt="%g")
        ax.contour(x, y, energy, levels=[6.5], colors="#75838e", linewidths=1.4)
        ax.plot(points[:, 0], points[:, 1], "o-", color=color, lw=1.5,
                ms=4.5, zorder=4)
        for start, end in zip(points[:-1], points[1:], strict=True):
            ax.annotate("", xy=end, xytext=start,
                        arrowprops={"arrowstyle": "->", "color": color, "lw": 1.3},
                        zorder=5)
        ax.plot(0, 0, "*", ms=13, color="#252b30", zorder=6)
        ax.annotate(r"$x_0=(2,1)$", xy=points[0], xytext=(-68, 18),
                    textcoords="offset points", fontsize=11,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
        ax.annotate(r"$x_1$", xy=points[1], xytext=(8, -13),
                    textcoords="offset points", color=color, fontsize=12)
        ax.axhline(0, color="#dfe3e6", lw=0.8)
        ax.axvline(0, color="#dfe3e6", lw=0.8)
        ax.set(xlim=(-0.4, 2.55), ylim=(-2.25, 2.25), xlabel=r"$x_1$", ylabel=r"$x_2$")
        ax.set_aspect("equal")
        factors = "0.8, −0.8" if eta == 0.2 else "0.75, −1.25"
        ax.set_title(f"η = {eta:g}: {steps} updates\ncoordinate factors {factors}",
                     color=color, fontsize=12, pad=10)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"Fixed-step gradient descent on $f(x)=\frac{1}{2}(x_1^2+9x_2^2)$",
                 fontsize=15, y=0.98)
    fig.text(0.5, 0.025,
             "Exact constructed iterates; gray ellipses are energy levels. Same scale in both panels.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.08, right=0.96, top=0.83, bottom=0.13, wspace=0.32)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
