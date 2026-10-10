"""Illustrate y' + 2y = 3; tested with Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from the desired output directory; writes integrating-factor-balance.png.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0.0, 3.0, 601)
    transient = -1.5 * np.exp(-2.0 * t)
    y = 1.5 + transient
    rate = 3.0 * np.exp(-2.0 * t)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.3), dpi=120,
                             constrained_layout=True, facecolor="white")
    axes[0].plot(t, y, color="#2176a5", lw=2.8, label=r"total $y=\frac{3}{2}(1-e^{-2t})$")
    axes[0].axhline(1.5, color="#258568", ls="--", lw=2,
                   label=r"particular solution $y_p=3/2$")
    axes[0].plot(t, transient, color="#bb4b20", ls=":", lw=2.5,
                 label=r"transient $y_h=-\frac{3}{2} e^{-2t}$")
    axes[0].scatter([0], [0], color="#2176a5", zorder=5)
    axes[0].set(title="Add the particular and homogeneous solutions",
                ylabel="state y", ylim=(-1.65, 1.9))
    axes[0].legend(loc="lower right", fontsize=9, framealpha=1)
    axes[1].fill_between(t, 0, 2*y, color="#258568", alpha=0.18)
    axes[1].fill_between(t, 2*y, 3, color="#2176a5", alpha=0.16)
    axes[1].axhline(3, color="#444444", ls="--", lw=2, label="input = 3")
    axes[1].plot(t, 2*y, color="#258568", lw=2.5, label="removal = 2y")
    axes[1].plot(t, rate, color="#2176a5", lw=2.5, label="net increase = y'")
    axes[1].set(title=r"The rate balance: $3=y'+2y$", ylabel="rate",
                ylim=(-0.05, 3.4))
    axes[1].legend(loc="center right", fontsize=9, framealpha=1)
    for ax in axes:
        ax.set(xlabel="time t", xlim=(0, 3))
        ax.set_facecolor("white")
        ax.grid(alpha=0.15)
    fig.savefig(Path.cwd() / "integrating-factor-balance.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
