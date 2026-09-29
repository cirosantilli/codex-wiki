"""Two-level trial energy and excited-state population for H = diag(0, 2).

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; writes an opaque white PNG in cwd.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    theta = np.linspace(-np.pi, np.pi, 801)
    population = np.sin(theta)**2
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.5), dpi=125)
    axes[0].plot(theta, 2 * population, color="#235f91", lw=2.6)
    axes[0].scatter([-np.pi, 0, np.pi], [0, 0, 0], color="#792f86",
                    s=40, zorder=5, clip_on=False)
    axes[0].scatter([np.pi / 4, np.pi / 2], [1, 2], color="#235f91", s=40)
    axes[0].annotate(r"$E=1$", (np.pi / 4, 1), xytext=(1.65, 0.8),
                     arrowprops={"arrowstyle": "->", "color": "#545454"})
    axes[0].set(xlim=(-np.pi, np.pi), ylim=(-0.1, 2.2),
                xlabel=r"Trial angle $\theta$ (radians)", ylabel=r"Energy $E(\theta)$",
                title=r"$E(\theta)=2\sin^2\theta$")
    axes[0].set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
                      [r"$-\pi$", r"$-\pi/2$", "0", r"$\pi/2$", r"$\pi$"])
    prob = np.linspace(0, 1, 100)
    axes[1].plot(prob, 2 * prob, color="#235f91", lw=2.6)
    axes[1].scatter([0, 0.5, 1], [0, 1, 2], color="#792f86", s=40, zorder=5)
    axes[1].set(xlim=(-0.04, 1.04), ylim=(-0.1, 2.2),
                xlabel=r"Excited-level probability $P_1=\sin^2\theta$",
                ylabel="Trial energy", title=r"Weighted mean: $E=0(1-P_1)+2P_1$")
    for ax in axes:
        ax.axhline(0, color="#545454", ls=":", lw=1.1)
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"$H=\mathrm{diag}(0,2)$, $|\psi_\theta\rangle=\cos\theta|0\rangle+\sin\theta|1\rangle$",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.035, "Ground energy 0 is attained exactly when the excited amplitude vanishes.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.22, top=0.78, wspace=0.32)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
