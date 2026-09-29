"""Original quadratic-potential streamlines and dye map; Python 3.14."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.2), layout="constrained")
    grid = np.linspace(-2, 2, 151)
    x, y = np.meshgrid(grid, grid)
    for ax, alpha in zip(axes[:2], (0.0, np.pi/3)):
        ux = 2*(x*np.cos(alpha)-y*np.sin(alpha))
        uy = -2*(x*np.sin(alpha)+y*np.cos(alpha))
        ax.streamplot(grid, grid, ux, uy, color="#126782", density=0.9,
                      linewidth=0.9, arrowsize=1.1)
        for angle in (-alpha/2, -alpha/2+np.pi/2):
            ax.plot([-2.8*np.cos(angle), 2.8*np.cos(angle)],
                    [-2.8*np.sin(angle), 2.8*np.sin(angle)], color="#d16b18", lw=1.4, ls="--")
        ax.plot(0, 0, "ko", ms=4)
        ax.set_title(r"$w=\beta z^2$" if alpha == 0 else r"$w=\beta z^2e^{i\pi/3}$")
    ax = axes[2]
    alpha = np.pi/3
    bt = 0.3
    ax.add_patch(Ellipse((0, 0), 2, 2, facecolor="#126782", edgecolor="#126782", alpha=0.17,
                        label=r"$t=0$: circle, area $\pi R^2$"))
    ax.add_patch(Ellipse((0, 0), 2*np.exp(2*bt), 2*np.exp(-2*bt),
                        angle=-alpha*90/np.pi, facecolor="#d16b18", edgecolor="#d16b18", alpha=0.30,
                        label=r"$\beta t=0.3$: ellipse, area $\pi R^2$"))
    ax.plot([-1.8, 1.8], [1.8*np.tan(alpha/2), -1.8*np.tan(alpha/2)], "--", color="0.4", lw=1)
    ax.set_title(r"Pure advection: $\alpha=\pi/3$")
    ax.legend(loc="upper center", fontsize=8.4)
    for ax in axes:
        ax.set(xlim=(-2, 2), ylim=(-2, 2), aspect="equal", xlabel=r"$x/R$", ylabel=r"$y/R$")
        ax.axhline(0, color="0.75", lw=0.6)
        ax.axvline(0, color="0.75", lw=0.6)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
