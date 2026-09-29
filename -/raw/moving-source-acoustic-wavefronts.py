"""Original weak-wave geometry; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes moving-source-acoustic-wavefronts.png to the CWD.
Circles are axial sections of spherical fronts, not measured shock images.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5), dpi=120,
                             facecolor="white")
    ages = np.arange(0.5, 3.01, 0.5)
    colors = plt.cm.Blues(np.linspace(0.40, 0.88, len(ages)))
    for ax, mach in zip(axes, (0.5, 2.0)):
        ax.set_facecolor("white")
        for age, color in zip(ages, colors):
            ax.add_patch(Circle((-mach * age, 0), age, fill=False,
                                lw=1.7, edgecolor=color))
            ax.plot(-mach * age, 0, ".", color=color, ms=5)
        ax.axhline(0, color="#c0c6cd", lw=0.8, zorder=0)
        ax.plot(0, 0, "o", color="#202b36", ms=7, zorder=5)
        ax.annotate("source now", (0, 0), (0.1, -1.5),
                    arrowprops={"arrowstyle": "-", "color": "#202b36"},
                    fontsize=10)
        ax.annotate("", (1.9, 0.7), (0.2, 0.7),
                    arrowprops={"arrowstyle": "->", "lw": 1.8,
                                "color": "#202b36"})
        ax.text(1.05, 1.02, r"motion $U$", ha="center", fontsize=10)
        ax.set_aspect("equal")
        ax.set_xlim(-9.4, 3.1)
        ax.set_ylim(-3.65, 3.65)
        ax.set_xticks([-8, -6, -4, -2, 0, 2])
        ax.set_yticks([-3, 0, 3])
        ax.set_xlabel(r"$x/(cT)$")
        ax.set_title(rf"$M={mach:g}$: " +
                     ("subsonic" if mach < 1 else "supersonic"), pad=15)
        if mach > 1:
            slope = 1 / np.sqrt(mach**2 - 1)
            xs = np.linspace(-6.2, 0, 300)
            for sign in (-1, 1):
                ax.plot(xs, sign * (-xs) * slope, color="#c64632",
                        lw=2.2, zorder=4)
            ax.add_patch(Arc((0, 0), 2.6, 2.6, theta1=150, theta2=180,
                             lw=1.6, color="#c64632"))
            ax.text(-2.15, 0.24, r"$\mu=30^\circ$", color="#a63223",
                    fontsize=10, zorder=6, bbox={"facecolor": "white", "edgecolor": "none",
                                       "pad": 1.5})
            ax.text(-9.0, 3.28, "Mach cone section", color="#a63223",
                    fontsize=10, zorder=6, bbox={"facecolor": "white", "edgecolor": "none",
                                       "pad": 1.5})
        else:
            ax.text(-8.7, 3.12, "fronts reach ahead of source", fontsize=10,
                    color="#285580")
    axes[0].set_ylabel(r"$y/(cT)$")
    fig.suptitle("Sound fronts emitted by a moving point", fontsize=17,
                 y=0.96)
    fig.text(0.5, 0.145,
             r"At $t=0$: center $(U\tau,0)$; radius $-c\tau$; "
             r"release times $\tau/T=-0.5,-1,\ldots,-3$.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.083,
             "Axial sections of 3D spherical fronts in uniform resting gas.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.035,
             "Weak linear-wave model; no measured shock or sonic-boom strength.",
             ha="center", fontsize=10, color="#525b65")
    fig.subplots_adjust(left=0.065, right=0.985, bottom=0.255, top=0.83,
                        wspace=0.16)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
