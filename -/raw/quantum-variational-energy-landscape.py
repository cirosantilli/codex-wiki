"""Analytic Gaussian trial energy landscapes; opaque PNG in cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Build with: make _media/quantum-variational-energy-landscape.png
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    a = np.linspace(0.55, 3.5, 1201)
    kinetic = a / 4
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.9))
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.29, top=0.78,
                        wspace=0.29)
    fig.suptitle("Minimize energy within the Gaussian trial family", fontsize=15, y=0.97)
    fig.text(0.5, 0.87, r"$\psi_a=(a/\pi)^{1/4}e^{-ax^2/2}$; $a>0$, $\hbar=m=1$",
             ha="center")
    specs = ((1 / (4 * a), 1.0, 0.5, "#226f9c",
              r"Harmonic: $V=x^2/2$", (0, 1.05)),
             (3 / (4 * a**2), 6**(1 / 3), 3 * 6**(1 / 3) / 8, "#754694",
              r"Quartic: $V=x^4$", (0, 2.8)))
    for ax, (potential, optimum, best, color, title, limits) in zip(axes, specs):
        ax.plot(a, kinetic + potential, color=color, lw=2.7, label="Total trial energy")
        ax.plot(a, kinetic, color="#216e9b", ls="--", lw=1.6, label="Kinetic energy")
        ax.plot(a, potential, color="#c88229", ls="--", lw=1.6, label="Potential energy")
        ax.plot([optimum, optimum], [0, best], color="0.45", ls=":", lw=1.2)
        ax.scatter([optimum], [best], s=45, color=color, zorder=5)
        ax.set(xlabel=r"Trial parameter $a$ (larger means narrower)", ylabel="Energy",
               xlim=(0.55, 3.5), ylim=limits)
        ax.set_title(title, fontsize=12)
        ax.grid(alpha=0.15)
    axes[0].annotate("a = 1\nExact ground energy = 0.5", xy=(1, 0.5),
                     xytext=(1.45, 0.91), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": "0.3"})
    axes[1].annotate(r"$a=6^{1/3}\approx1.8171$" "\nTrial minimum = 0.681420",
                     xy=(specs[1][1], specs[1][2]), xytext=(1.4, 2.05), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": "0.3"})
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 0.085),
               ncol=3, frameon=False, fontsize=10)
    fig.text(0.5, 0.025, "The quartic minimum is an upper bound on the true ground energy; no exact quartic value is plotted.",
             ha="center", fontsize=9.5)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130,
                transparent=False, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
