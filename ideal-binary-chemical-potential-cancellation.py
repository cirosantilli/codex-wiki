"""Ideal binary mixture: chemical potentials and Gibbs-Duhem cancellation.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
All curves are original calculations; no experimental data are used.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    x = np.linspace(0.025, 0.975, 500)
    blue, orange = "#2368a2", "#bd5b19"
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), dpi=110)
    fig.subplots_adjust(left=0.085, right=0.975, bottom=0.19, top=0.77, wspace=0.38)
    fig.suptitle("Ideal binary mixture: two changing potentials, one constraint", y=0.97,
                 fontsize=15)
    fig.text(0.5, 0.865, r"Fixed $T,p$; $x=x_A$, $x_B=1-x$; pure-component references subtracted",
             ha="center", fontsize=12)
    ax = axes[0]
    ax.plot(x, np.log(x), color=blue, lw=2.5, label=r"A: $\ln x$")
    ax.plot(x, np.log1p(-x), color=orange, lw=2.5, label=r"B: $\ln(1-x)$")
    ax.axvline(0.25, color="0.65", lw=1, ls=":")
    ax.scatter([0.25, 0.25], [np.log(0.25), np.log(0.75)], color=[blue, orange], zorder=4)
    ax.set(xlim=(0, 1), ylim=(-3.8, 0.15), xlabel=r"Mole fraction $x$",
           ylabel=r"$(\mu_i-\mu_i^*)/(RT)$", title="Chemical-potential shifts")
    ax.legend(loc="lower center", frameon=False)
    ax.grid(alpha=0.15)
    ax = axes[1]
    ax.plot(x, np.ones_like(x), color=blue, lw=2.5, label=r"$x\,\mu_A'/(RT)=+1$")
    ax.plot(x, -np.ones_like(x), color=orange, lw=2.5, label=r"$(1-x)\,\mu_B'/(RT)=-1$")
    ax.plot(x, np.zeros_like(x), color="0.2", lw=2, ls="--", label="Sum = 0")
    ax.set(xlim=(0, 1), ylim=(-1.7, 1.7), xlabel=r"Mole fraction $x$",
           ylabel="Weighted derivative / RT", title="Weighted slopes cancel")
    ax.set_yticks([-1, 0, 1])
    ax.grid(alpha=0.15)
    ax.text(0.045, 1.24, r"$x\,\mu_A'/(RT)=+1$", color=blue, fontsize=11)
    ax.text(0.045, -1.48, r"$(1-x)\,\mu_B'/(RT)=-1$", color=orange, fontsize=11)
    ax.text(0.73, 0.18, "Sum = 0", color="0.2", fontsize=11)
    fig.text(0.27, 0.055, r"At $x=1/4$: slopes $4RT$ and $-4RT/3$", ha="center", fontsize=11)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
