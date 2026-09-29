"""Pointwise limits and exact supremum errors; Python 3.14, matplotlib/numpy.

Run from _media to save the basename PNG in the current working directory.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, 1, 1001)
    n = np.arange(1, 36)
    threshold = int(np.ceil(np.log(.01) / np.log(.8)))
    assert threshold == 21
    assert .8**20 > .01 > .8**21
    assert np.allclose((2.0**(-1/n))**n, .5)
    colors = ["#1976a3", "#d17624", "#38834d", "#8856a7"]
    fig, axes = plt.subplots(1, 2, figsize=(11, 5), dpi=120)
    ax = axes[0]
    for k, color in zip([1, 5, 20, 50], colors):
        ax.plot(x, x**k, color=color, lw=1.8, label=f"n = {k}")
    ax.plot([0, 1], [0, 0], color="#202c35", lw=2.8, ls="--",
            label="Pointwise limit (open at x = 1)")
    ax.scatter([1], [0], s=64, facecolors="white", edgecolors="#202c35",
               linewidths=2, zorder=6)
    ax.scatter([1], [1], s=50, color="#202c35", zorder=6)
    ax.annotate("f(1) = 1", (1, 1), xytext=(.57, .96), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#202c35"})
    ax.annotate("f(x) = 0 for x < 1", (.45, 0), xytext=(.15, .14), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#202c35"})
    ax.axvline(.8, color="#777777", lw=1, ls=":")
    ax.text(.79, .56, "a = 0.8", rotation=90, ha="right", fontsize=10)
    ax.set(xlim=(-.02, 1.06), ylim=(-.06, 1.07), xlabel="Input x", ylabel="Function value")
    ax.set_title(r"$f_n(x)=x^n$: each input has its own waiting time", fontsize=11)
    ax.legend(loc="upper left", fontsize=9, frameon=False)
    ax.grid(alpha=.15)
    ax = axes[1]
    ax.semilogy(n, np.ones_like(n), color=colors[0], lw=2.3, label=r"$x^n$ on $[0,1]$: $E_n=1$")
    ax.semilogy(n, .8**n, color=colors[2], lw=2.3, label=r"$x^n$ on $[0,0.8]$: $E_n=0.8^n$")
    ax.semilogy(n, 1/(n+1), color=colors[1], lw=2.3, label=r"$x/(n+1)$ on $[0,1]$: $E_n=1/(n+1)$")
    ax.axhline(.01, color="#333333", ls="--", lw=1.3, label=r"Tolerance $\varepsilon=0.01$")
    ax.scatter([20, 21], [.8**20, .8**21], color=colors[2], s=35, zorder=5)
    ax.annotate("n = 20: 0.0115292\nn = 21: 0.00922337", (21, .8**21),
                xytext=(3, .0042), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": colors[2]})
    ax.text(11, .35, "Supremum 1 is never attained:\nerror at x = 1 is zero.", fontsize=10)
    ax.set(xlim=(1, 35), ylim=(.0003, 1.5), xlabel="Approximation index n", ylabel=r"Supremum error $E_n$ (log scale)")
    ax.set_title("Uniform convergence: the error bound tends to zero", fontsize=11)
    ax.legend(loc="lower left", bbox_to_anchor=(0, -.015), fontsize=9, frameon=False)
    ax.grid(alpha=.15, which="both")
    fig.suptitle("Pointwise versus uniform convergence", fontsize=15)
    fig.subplots_adjust(left=.06, right=.98, bottom=.13, top=.84, wspace=.28)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"a=0.8: threshold={threshold}, error20={.8**20:.12g}, error21={.8**21:.12g}")


if __name__ == "__main__":
    main()
