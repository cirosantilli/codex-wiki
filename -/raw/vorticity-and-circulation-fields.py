"""Compare solid rotation and a potential line vortex; write a PNG in the CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media: python ../vorticity-and-circulation-fields.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    omega = 1.0  # s^-1
    strength = 1.0  # m^2 s^-1
    blue, orange = "#1766a0", "#b65016"
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(2, 2, figsize=(10, 8), dpi=120)
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.09, top=0.85,
                        hspace=0.47, wspace=0.30)
    fig.suptitle("Circular paths do not determine local fluid spin", fontsize=17, y=0.98)
    fig.text(0.5, 0.925,
             r"$\Omega=1\ \mathrm{s^{-1}},\quad K=1\ \mathrm{m^2\,s^{-1}}$; counterclockwise loops",
             ha="center", fontsize=13)
    theta = np.linspace(0.0, 2.0 * np.pi, 361)
    grid = np.linspace(-1.45, 1.45, 13)
    x, y = np.meshgrid(grid, grid)
    radius_squared = x * x + y * y
    keep = radius_squared >= 0.30**2
    for ax, kind, color in zip(axes[0], ("rotation", "vortex"), (blue, orange)):
        if kind == "rotation":
            u, v = -omega * y, omega * x
            title = r"Solid-body rotation: $\mathbf{u}=(-\Omega y,\Omega x)$"
        else:
            # Evaluate only outside the excluded origin; do not regularize the field.
            u = -strength * y[keep] / radius_squared[keep]
            v = strength * x[keep] / radius_squared[keep]
            title = r"Potential line vortex: $\mathbf{u}=K\mathbf{e}_\theta/r$"
        qx, qy = (x, y) if kind == "rotation" else (x[keep], y[keep])
        ax.quiver(qx, qy, u, v, color=color, angles="xy", scale_units="xy",
                  scale=7.5, width=0.005, pivot="mid")
        ax.plot(np.cos(theta), np.sin(theta), "--", color="#333333", lw=1.4)
        for angle in (0.35, 3.5):
            ax.annotate("", xy=(np.cos(angle + 0.18), np.sin(angle + 0.18)),
                        xytext=(np.cos(angle - 0.18), np.sin(angle - 0.18)),
                        arrowprops={"arrowstyle": "->", "color": "#222222", "lw": 2,
                                    "connectionstyle": "arc3,rad=0.15"})
        ax.text(-1.47, -1.43, r"Dashed loop: $R=1\ \mathrm{m}$", fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 1})
        if kind == "vortex":
            ax.plot(0, 0, marker="o", ms=7, mfc="white", mec="#333333", mew=1.5)
            ax.annotate("Excluded origin", xy=(0.02, 0.02), xytext=(0.45, 0.35),
                        fontsize=10, bbox={"facecolor": "white", "edgecolor": "none"},
                        arrowprops={"arrowstyle": "->", "color": "#333333"})
        ax.set(xlim=(-1.6, 1.6), ylim=(-1.6, 1.6), xlabel=r"$x$ (m)", ylabel=r"$y$ (m)")
        ax.set_aspect("equal")
        ax.set_title(title, fontsize=12, pad=12)
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])

    r = np.linspace(0.2, 1.6, 200)
    ax = axes[1, 0]
    ax.plot(r, 2 * omega * np.ones_like(r), color=blue, lw=2.5, label="Solid rotation")
    ax.plot(r, np.zeros_like(r), color=orange, lw=2.5, label="Potential line vortex")
    ax.set(xlabel=r"Radius $r$ (m)", ylabel=r"$\omega_z$ ($\mathrm{s^{-1}}$)",
           ylim=(-0.25, 2.55), xlim=(0.2, 1.6), yticks=[0, 1, 2])
    ax.set_title(r"Local curl in the fluid ($r>0$)", pad=10)
    ax.legend(loc="center", fontsize=10, framealpha=1)
    ax.grid(alpha=0.2)

    ax = axes[1, 1]
    ax.plot(r, 2 * np.pi * omega * r**2, color=blue, lw=2.5,
            label=r"Solid rotation: $2\pi\Omega R^2$")
    ax.plot(r, 2 * np.pi * strength * np.ones_like(r), color=orange, lw=2.5,
            label=r"Potential line vortex: $2\pi K$")
    ax.plot(1, 2 * np.pi, "o", color="#222222", ms=6)
    ax.annotate(r"Both: $\Gamma=2\pi$ at $R=1$", xy=(1, 2 * np.pi),
                xytext=(0.32, 10), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#333333"})
    ax.set(xlabel=r"Loop radius $R$ (m)", ylabel=r"$\Gamma$ ($\mathrm{m^2\,s^{-1}}$)",
           ylim=(0, 18), xlim=(0.2, 1.6))
    ax.set_title("Circulation around the whole loop", pad=10)
    ax.legend(loc="upper left", fontsize=9, framealpha=1)
    ax.grid(alpha=0.2)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
