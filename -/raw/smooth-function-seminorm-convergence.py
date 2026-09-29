"""Uniformly small functions whose derivative measurements stay large.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; the basename PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axes = plt.subplots(1, 3, figsize=(11.6, 4.5), dpi=110)
    t = np.linspace(0, 1, 2501)
    indices, colors = [4, 12, 32], ["#236d9b", "#b65e1c", "#714ba0"]
    for n, color in zip(indices, colors):
        axes[0].plot(t, np.sin(n*t)/n, color=color, lw=1.6, label=f"n = {n}")
        axes[1].plot(t, np.cos(n*t), color=color, lw=1.35, label=f"n = {n}")
        assert np.isclose(np.sin(n * (np.pi/(2*n)))/n, 1/n)
        assert np.cos(0) == 1
    axes[0].set(title=r"$f_n(t)=\sin(nt)/n$", ylim=(-.28, .28), ylabel="Function value")
    axes[1].set(title=r"$f_n'(t)=\cos(nt)$", ylim=(-1.18, 1.18), ylabel="Derivative value")
    for ax in axes[:2]:
        ax.axhline(0, color="#48535b", lw=.8, ls="--")
        ax.set(xlabel="t", xlim=(0, 1))
        ax.legend(loc="lower left", fontsize=9, framealpha=.95)
    axes[1].scatter([0], [1], color="#242e36", s=28, zorder=4)
    axes[1].annotate("Always 1 at t = 0", (0, 1), xytext=(.14, 1.05), fontsize=10)
    ns = np.arange(2, 65)
    axes[2].semilogy(ns, 1/ns, color="#236d9b", lw=2, label=r"$p_0(f_n)=1/n$")
    axes[2].semilogy(ns, np.ones_like(ns), color="#b65e1c", lw=2, label=r"$p_1(f_n)=1$")
    axes[2].semilogy(ns, ns, color="#714ba0", lw=2, label=r"$p_2(f_n)=n$")
    axes[2].set(title="Different orders see different errors", xlabel="Sequence index n", ylabel="Error measurement (log scale)", xlim=(2, 64), ylim=(.01, 90))
    axes[2].legend(loc="upper left", fontsize=10)
    axes[2].set_yticks([.01, .1, 1, 10, 100], ["0.01", "0.1", "1", "10", "100"])
    for ax in axes:
        ax.grid(alpha=.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Uniform convergence to zero does not imply smooth convergence", fontsize=15, y=.98)
    fig.text(.5, .025, r"On $[0,1]$: values shrink, slopes stay large, and second derivatives grow.", ha="center", fontsize=12)
    fig.subplots_adjust(left=.065, right=.985, bottom=.17, top=.81, wspace=.37)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
