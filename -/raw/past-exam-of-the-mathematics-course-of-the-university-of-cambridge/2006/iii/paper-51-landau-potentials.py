"""Landau minima; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.

Emit the PNG basename in caller CWD; respect caller MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axs = plt.subplots(1, 2, figsize=(8.2, 3.6), dpi=160, facecolor="white")
    m = np.unique(np.r_[np.linspace(-1.35, 1.35, 700), 0, -np.sqrt(.6), np.sqrt(.6)])
    for r, color in [(.6, "#3182bd"), (0., "#6a51a3"), (-.6, "#e6550d")]:
        axs[0].plot(m, r*m*m/2 + m**4/4, color=color, label=fr"$r={r:g}$")
        roots = np.array([0.]) if r >= 0 else np.array([-np.sqrt(-r), np.sqrt(-r)])
        axs[0].scatter(roots, r*roots**2/2 + roots**4/4, color=color, s=22, zorder=5)
    axs[0].set(title=r"Continuous onset: $u=1$", xlabel=r"Order parameter $M$",
               ylabel=r"Potential $V(M)$", ylim=(-.13, .65))
    axs[0].legend(fontsize=8, loc="upper center")
    roots = np.array([-np.sqrt(.75), 0., np.sqrt(.75)])
    m = np.unique(np.r_[np.linspace(-1.25, 1.25, 900), roots, -.5, .5])
    v = m*m*(m*m-.75)**2/6
    axs[1].plot(m, v, color="#238b45")
    axs[1].scatter(roots, np.zeros(3), color="#238b45", s=30, zorder=5)
    axs[1].set(title=r"First-order coexistence: $u=-1, v=1$", xlabel=r"Order parameter $M$",
               ylabel=r"Potential $V(M)$", ylim=(-.016, .11))
    axs[1].text(0, .085, r"$r=3/16$: three equal minima", ha="center", fontsize=9)
    axs[1].annotate(r"$M=0$", xy=(0, 0), xytext=(0, .037), ha="center",
                    arrowprops={"arrowstyle": "->", "color": "0.4"}, fontsize=9)
    axs[1].text(roots[0], -.012, r"$-\sqrt{3/4}$", ha="center", fontsize=9)
    axs[1].text(roots[2], -.012, r"$+\sqrt{3/4}$", ha="center", fontsize=9)
    for ax in axs:
        ax.set_facecolor("white")
        ax.axhline(0, color="0.65", lw=.6)
        ax.grid(alpha=.16)
    fig.tight_layout()
    fig.savefig(Path("paper-51-landau-potentials.png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
