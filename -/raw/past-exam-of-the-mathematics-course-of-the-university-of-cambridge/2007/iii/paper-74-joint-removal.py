"""Original joint-removal phase planes; writes basename PNG to caller CWD."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def panel(ax, beta, coupling, title):
    grid = np.linspace(0, 2.5, 27)
    u, v = np.meshgrid(grid, grid)
    du, dv = 1 - beta * u - coupling * u * v, 1 - beta * v - coupling * u * v
    ax.streamplot(grid, grid, du, dv, color="#b6c0c8", linewidth=.7, density=.9, arrowsize=.8)
    t = np.linspace(.005, 2.5, 1000)
    if coupling == 0:
        ax.axvline(1 / beta, color="#276e9b", lw=2, label=r"$\dot u=0$")
        ax.axhline(1 / beta, color="#c87533", lw=2, label=r"$\dot v=0$")
        ax.scatter(1 / beta, 1 / beta, color="#327644", s=60, zorder=4)
    elif beta == 0:
        ax.plot(t, 1 / (coupling * t), color="#7564a0", lw=2.5, label="equilibrium curve")
        for d in [-1.5, -.7, 0, .7, 1.5]:
            u0 = (d + np.sqrt(d * d + 4 / coupling)) / 2
            v0 = (-d + np.sqrt(d * d + 4 / coupling)) / 2
            ax.scatter(u0, v0, s=40, color="#7564a0", zorder=4)
    else:
        ax.plot(1 / (beta + coupling * t), t, color="#276e9b", lw=2, label=r"$\dot u=0$")
        ax.plot(t, 1 / (beta + coupling * t), color="#c87533", lw=2, label=r"$\dot v=0$")
        mu = 2 / (beta + np.sqrt(beta * beta + 4 * coupling))
        ax.scatter(mu, mu, s=60, color="#327644", zorder=4)
    ax.set(xlim=(0, 2.5), ylim=(0, 2.5), xlabel=r"$u=\langle X_1\rangle$", ylabel=r"$v=\langle X_2\rangle$", title=title)
    ax.set_aspect("equal")
    ax.legend(fontsize=8, loc="upper right")
    ax.spines[["top", "right"]].set_visible(False)


def main():
    fig, axes = plt.subplots(1, 3, figsize=(11.8, 4.3), constrained_layout=True, facecolor="white")
    for ax, args in zip(axes, [(1, 0, r"Independent removal: $C=0$"), (0, 1, r"Joint removal only: $\beta=0$"), (1, 1, r"Both mechanisms: $\beta=C=1$")]):
        panel(ax, *args)
    fig.suptitle(r"Mean-field joint removal: phase planes with $\lambda=1$", fontsize=15)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
