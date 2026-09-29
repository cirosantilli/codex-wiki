"""Exact original quadratic energies; Python 3.14, numpy 2.3.5, matplotlib 3.10.7."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.facecolor": "white"})
    k = np.arange(21)
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 5.0), dpi=120)
    fig.patch.set_facecolor("white")
    histories = [
        (0.1, 2 * 0.81 ** k + 4.5 * 0.01 ** k, "#33865d"),
        (0.2, 6.5 * 0.64 ** k, "#176c9c"),
        (0.25, 2 * (9 / 16) ** k + 4.5 * (25 / 16) ** k, "#bd4729"),
    ]
    for eta, energy, color in histories:
        axes[0].plot(k[:4], energy[:4], "o-", color=color, lw=2,
                     ms=5, label=f"η = {eta:g}")
        axes[1].semilogy(k, energy, "o-", color=color, lw=2,
                         ms=3.5, label=f"η = {eta:g}")
    axes[0].set(title="First three updates", xlim=(-0.12, 3.12), ylim=(0, 19),
                xlabel="Iteration k", ylabel=r"Energy $E_k=f(x_k)-f(0)$")
    axes[0].set_xticks(range(4))
    axes[0].legend(loc="upper left", frameon=True, facecolor="white")
    axes[0].annotate("η = 0.1 wins the first step", xy=(1, 1.665),
                     xytext=(1.1, 5.9), color="#33865d", fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": "#33865d"})
    axes[1].set(title="Longer history (log energy)", xlim=(0, 20),
                xlabel="Iteration k", ylabel=r"Energy $E_k$ (log scale)")
    axes[1].set_xticks([0, 5, 10, 15, 20])
    axes[1].text(6.5, 2e4, "unstable mode: factor 25/16", color="#bd4729", fontsize=10)
    axes[1].text(7, 0.007, "η = 0.2: exact factor 0.64", color="#176c9c", fontsize=10)
    axes[1].text(7, 0.3, "η = 0.1: slow factor 0.81", color="#33865d", fontsize=10)
    for ax in axes:
        ax.grid(True, alpha=0.23)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"Exact energies for $f(x)=\frac{1}{2}(x_1^2+9x_2^2)$, starting at $(2,1)$",
                 fontsize=14, y=0.98)
    fig.text(0.5, 0.025, "Constructed mathematical example; points evaluated from the exact energy formulas.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.08, right=0.97, top=0.81, bottom=0.14, wspace=0.30)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
