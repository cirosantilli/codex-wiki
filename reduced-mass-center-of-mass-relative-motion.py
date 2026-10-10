"""Draw a two-particle coordinate split; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes the matching PNG basename to the current directory.
All curves use stipulated dimensionless parameters, not experimental data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    blue, orange, green = "#1765a0", "#b84b17", "#21804a"
    fig = plt.figure(figsize=(10, 6), layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=(0.9, 1.4))
    geometry = fig.add_subplot(grid[0, :])
    geometry.set(xlim=(-1.12, 0.75), ylim=(-0.7, 0.78))
    geometry.axis("off")
    geometry.set_title("One pair, two coordinates: centre R and separation r", pad=10)
    geometry.plot([-0.75, 0.25], [0, 0], color="#707070", lw=2, zorder=1)
    geometry.scatter([-0.75, 0.25], [0, 0], s=[400, 750], c=[blue, orange], zorder=3)
    geometry.scatter([0], [0], marker="x", color=green, s=90, lw=3, zorder=4)
    geometry.text(-0.75, 0.3, r"$m_1$ at $x_1=R-3r/4$", ha="center", color=blue)
    geometry.text(0.25, 0.3, r"$m_2=3m_1$ at $x_2=R+r/4$", ha="center", color=orange)
    geometry.text(0, -0.22, r"$R$", ha="center", color=green)
    geometry.annotate("", xy=(0.25, -0.48), xytext=(-0.75, -0.48),
                      arrowprops={"arrowstyle": "->", "lw": 2, "color": "#333333"})
    geometry.text(-0.25, -0.65, r"$r=x_2-x_1$  (arrow from body 1 to body 2)", ha="center")
    tau = np.linspace(0, 4 * np.pi, 500)
    extension = 0.3 * np.cos(tau)
    center = 0.08 * tau
    x1 = center - 0.75 * (1 + extension)
    x2 = center + 0.25 * (1 + extension)
    lab = fig.add_subplot(grid[1, 0])
    lab.plot(tau, x1, color=blue, lw=2, label=r"$x_1/\ell$")
    lab.plot(tau, x2, color=orange, lw=2, label=r"$x_2/\ell$")
    lab.plot(tau, center, color=green, lw=2, ls="--", label=r"$R/\ell$")
    lab.set(title="Laboratory positions: drift + vibration", ylabel="Position / equilibrium length")
    lab.legend(loc="upper left", fontsize=10)
    internal = fig.add_subplot(grid[1, 1])
    internal.plot(tau, -0.75 * extension, color=blue, lw=2, label=r"$u_1=-3s/4$")
    internal.plot(tau, 0.25 * extension, color=orange, lw=2, label=r"$u_2=s/4$")
    internal.axhline(0, color="#777777", lw=1)
    internal.set(title="Internal displacements: translation removed",
                 ylabel=r"Displacement from equilibrium / $\ell$", ylim=(-0.31, 0.31))
    internal.legend(loc="upper left", fontsize=10)
    for ax in (lab, internal):
        ax.set(xlabel=r"Phase time $\tau=\omega t$", xlim=(0, 4 * np.pi))
        ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi],
                      ["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
        ax.grid(alpha=0.2)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
