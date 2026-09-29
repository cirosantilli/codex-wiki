"""Original local bifurcation diagrams and schematic Hopf-cycle portraits."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def parameters(ax, sigma):
    ax.axhline(0, color="#46545e", lw=1.7)
    ax.plot([0, 0], [0, .4], color="#ba613c", lw=2.5)
    ax.text(.015, .31, "$H_0$", color="#ba613c")
    ax.text(.42, .012, "pitchfork", fontsize=8)
    if sigma == -1:
        k = np.linspace(-.7, 0, 100)
        ax.plot(k, k / 2, color="#7763a5", lw=2.5)
        ax.text(-.52, -.24, "$H_\\pm$", color="#7763a5")
        ax.text(-.65, -.34, "pair stable below\nthis Hopf line", fontsize=8)
        ax.text(.12, -.26, "origin saddle;\nnonzero pair unstable", fontsize=8)
    else:
        ax.text(-.62, -.22, "origin saddle;\nno other equilibria", fontsize=8)
        ax.text(.11, -.22, "origin saddle;\nno periodic orbits", fontsize=8)
        ax.text(-.67, .08, "origin stable;\ntwo saddles", fontsize=8)
        ax.text(.11, .08, "origin unstable;\ntwo saddles", fontsize=8)
    ax.set(xlim=(-.7, .7), ylim=(-.4, .4), xlabel=r"$\kappa$", ylabel=r"$\lambda$", title=r"$s\gg1$" if sigma == 1 else r"$s\ll1$")
    ax.scatter([0], [0], color="#303a43", s=25, zorder=4)
    ax.spines[["top", "right"]].set_visible(False)


def portrait(ax, sigma, lam, kap, title, cycle=None):
    grid = np.linspace(-1.05, 1.05, 24)
    q, p = np.meshgrid(grid, grid)
    force = -lam * q + kap * p + sigma * q**3 - 2 * sigma * q**2 * p
    ax.streamplot(grid, grid, p, force, color="#bdc5cc", linewidth=.65, density=.7, arrowsize=.7)
    equilibria = [0.0]
    if lam / sigma > 0:
        equilibria += [-np.sqrt(lam / sigma), np.sqrt(lam / sigma)]
    for q0 in equilibria:
        determinant = lam if q0 == 0 else -2 * lam
        tr = kap - 2 * sigma * q0**2
        if determinant < 0:
            ax.scatter(q0, 0, marker="X", color="#935648", s=38, zorder=5)
        else:
            ax.scatter(q0, 0, facecolors="#32754d" if tr < 0 else "white", edgecolors="#32754d" if tr < 0 else "#a24744", s=38, zorder=5)
    theta = np.linspace(0, 2 * np.pi, 600)
    if cycle == "origin":
        radius = np.sqrt(2 * abs(kap))
        ax.plot(radius * np.cos(theta), -np.sqrt(lam) * radius * np.sin(theta), "-" if sigma == 1 else "--", color="#276e9b", lw=1.8)
    elif cycle == "wells":
        radius = np.sqrt(kap - 2 * lam)
        for q0 in equilibria[1:]:
            ax.plot(q0 + radius * np.cos(theta), -np.sqrt(-2 * lam) * radius * np.sin(theta), color="#276e9b", lw=1.8)
    ax.set(xlim=(-1.05, 1.05), ylim=(-1.05, 1.05), xlabel="$q$", ylabel="$p$", title=title)
    ax.tick_params(labelsize=7)
    ax.set_aspect("equal")
    ax.spines[["top", "right"]].set_visible(False)


def main():
    fig = plt.figure(figsize=(14, 10.4), facecolor="white", constrained_layout=True)
    gs = fig.add_gridspec(3, 1, height_ratios=[.8, 1, 1])
    top = gs[0, 0].subgridspec(1, 2)
    middle = gs[1, 0].subgridspec(1, 4)
    bottom = gs[2, 0].subgridspec(1, 5)
    parameters(fig.add_subplot(top[0, 0]), 1)
    parameters(fig.add_subplot(top[0, 1]), -1)
    cases = [
        (1, -.25, -.12, r"$\lambda<0$: saddle", None),
        (1, .25, -.025, r"$\lambda>0,\ \kappa<0$", None),
        (1, .25, .015, r"$\lambda>0,\ \kappa>0$", "origin"),
        (1, -.25, .12, r"$\lambda<0$: saddle", None),
        (-1, .25, -.015, r"$\lambda>0,\ \kappa<0$", "origin"),
        (-1, .25, .015, r"$\lambda>0,\ \kappa>0$", None),
        (-1, -.25, -.52, r"$\kappa<2\lambda<0$", None),
        (-1, -.25, -.48, r"$2\lambda<\kappa<0$", "wells"),
        (-1, -.25, .12, r"$\lambda<0,\ \kappa>0$", None),
    ]
    for index, case in enumerate(cases):
        grid = middle if index < 4 else bottom
        col = index if index < 4 else index - 4
        portrait(fig.add_subplot(grid[0, col]), *case)
    fig.suptitle("Local double-zero bifurcations and neighboring phase portraits\nMiddle row: large s. Bottom row: small s. Solid cycles stable; dashed cycle unstable.\nCycle outlines use leading Hopf amplitudes; global termination curves are not shown.", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
