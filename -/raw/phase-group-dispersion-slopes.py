"""Original analytical diagrams; no measured data.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; writes the matching PNG basename to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.8))
    fig.set_facecolor("white")
    fig.suptitle("Phase and group velocities are different slopes", fontsize=17, y=0.97)
    fig.subplots_adjust(left=0.065, right=0.99, bottom=0.25, top=0.77, wspace=0.36)
    k = np.linspace(0, 2.0, 700)
    models = [
        (1.0, "Nondispersive branch", r"$\Omega=K$", r"$c_g=c_p$"),
        (0.5, "Deep-water gravity limit", r"$\Omega=\sqrt{K}$", r"$c_g=\frac{1}{2}c_p$"),
        (1.5, "Deep-water capillary limit", r"$\Omega=K^{3/2}$", r"$c_g=\frac{3}{2}c_p$"),
    ]
    for ax, (power, title, formula, ratio) in zip(axes, models):
        ax.set_facecolor("white")
        ax.plot(k, k**power, color="#233c61", lw=2.8, label="dispersion branch")
        # At K=1 all three curves have Omega=1. The origin slope is 1.
        ax.plot([0, 1.85], [0, 1.85], color="#d55e00", lw=2,
                linestyle="--", label=r"origin slope $c_p$")
        tangent_k = np.linspace(0.28, 1.8, 200)
        ax.plot(tangent_k, 1 + power * (tangent_k - 1),
                color="#00866b", lw=2, linestyle=":", label=r"tangent slope $c_g$")
        ax.scatter([1], [1], color="#233c61", s=38, zorder=5)
        ax.axvline(1, color="#d6dce5", lw=1, zorder=0)
        ax.set(title=title + "\n" + formula, xlabel=r"normalized wavenumber $K$",
               ylabel=r"normalized angular frequency $\Omega$",
               xlim=(0, 2.05), ylim=(0, 2.95))
        ax.text(0.08, 0.87, ratio, transform=ax.transAxes, fontsize=15,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
        ax.set_xticks([0, 1, 2])
        ax.set_yticks([0, 1, 2])
        ax.spines[["right", "top"]].set_visible(False)
    handles, labels = axes[1].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 0.08),
               ncols=3, frameon=False, fontsize=11)
    fig.text(0.5, 0.023,
             "Analytical models, not measured data. Each panel uses its own normalization; slopes are evaluated at K = 1.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
