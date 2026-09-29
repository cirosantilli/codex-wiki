"""Uniformly small functions with nonconvergent derivatives on [0, pi].

Python 3.14, matplotlib/numpy. Run from _media to save the basename PNG to cwd.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, np.pi, 1801)
    indices = [2, 5, 12, 13]
    colors = ["#1976a3", "#d17624", "#38834d", "#8856a7"]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), dpi=120)
    for n, color in zip(indices, colors):
        values = np.sin(n*x)/n
        assert np.max(np.abs(values)) <= 1/n + 1e-14
        assert np.isclose(np.cos(n*np.pi), (-1)**n)
        assert np.isclose(np.sin(n*(np.pi/(2*n)))/n, 1/n)
        axes[0].plot(x, values, color=color, lw=1.7, label=f"n = {n}, error = {1/n:.3g}")
        axes[1].plot(x, np.cos(n*x), color=color, lw=1.5, label=f"n = {n}")
    axes[0].axhline(0, color="#202c35", ls="--", lw=2, label="Uniform limit: zero")
    axes[0].set(ylim=(-.57, .57), ylabel="Function value")
    axes[0].set_title(r"$f_n(x)=\sin(nx)/n$: amplitudes shrink", fontsize=12)
    axes[0].legend(loc="lower left", fontsize=9, frameon=False)
    axes[0].text(1.6, .41, r"$\sup_{[0,\pi]}|f_n|=1/n\ \longrightarrow\ 0$", fontsize=12,
                 bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
    axes[1].set(ylim=(-1.2, 1.25), ylabel="Derivative value")
    axes[1].set_title(r"$f_n'(x)=\cos(nx)$: amplitudes stay at one", fontsize=12)
    axes[1].legend(loc="upper left", ncol=2, fontsize=9, frameon=False)
    axes[1].scatter([np.pi, np.pi], [1, -1], color=[colors[2], colors[3]], s=55, zorder=5)
    axes[1].text(1.4, .89, "At x = π: even n gives +1", fontsize=10,
                 bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
    axes[1].text(1.6, -1.13, "At x = π: odd n gives −1", fontsize=10)
    for ax in axes:
        ax.set(xlim=(0, np.pi+.06), xlabel="Input x")
        ax.set_xticks([0, np.pi/2, np.pi], ["0", "π/2", "π"])
        ax.grid(alpha=.15)
    fig.suptitle("Uniform convergence controls values; differentiation needs extra hypotheses", fontsize=14)
    fig.subplots_adjust(left=.06, right=.98, bottom=.15, top=.82, wspace=.25)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)
    print("Exact supremum error=1/n; derivative at pi alternates +1 (even), -1 (odd).")


if __name__ == "__main__":
    main()
