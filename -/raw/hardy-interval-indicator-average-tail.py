"""Plot an original Hardy-average example; output matching PNG in the CWD.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True,
                             layout="constrained", facecolor="white")
    inner = np.linspace(0, 1, 250)
    tail = np.linspace(1, 5, 700)
    axes[0].plot([0, 1, 1, 5], [1, 1, 0, 0], color="#2463a4",
                 lw=3, linestyle="--", label=r"Input $f=\mathbf{1}_{(0,1)}$")
    axes[0].plot(inner, np.ones_like(inner), color="#b64c0b", lw=2.5,
                 label=r"Running average $Hf$")
    axes[0].plot(tail, 1 / tail, color="#b64c0b", lw=2.5)
    axes[0].annotate(r"$Hf=1/x$ after the input stops", xy=(2.5, .4),
                     xytext=(2.05, .88), arrowprops={"arrowstyle": "->"})
    axes[0].set(title="An average can outlive its input", ylabel="Value",
                 ylim=(-.07, 1.25))
    axes[0].legend(loc="upper right", fontsize=11)
    axes[1].fill_between(inner, 1, color="#2a8084", alpha=.3)
    axes[1].fill_between(tail, tail ** -2, color="#e4a33c", alpha=.5)
    axes[1].plot(inner, np.ones_like(inner), color="#2a8084", lw=2)
    axes[1].plot(tail, tail ** -2, color="#bc7510", lw=2)
    axes[1].text(.5, .48, "Inner area\n1", ha="center")
    axes[1].annotate("Full tail area = 1\nShown: 4/5; beyond 5: 1/5",
                     xy=(1.8, 1 / 1.8 ** 2), xytext=(2.05, .7),
                     arrowprops={"arrowstyle": "->"})
    axes[1].set(xlabel=r"$x$ (Lebesgue measure $dx$)", ylabel=r"$|Hf(x)|^2$",
                 title=r"$\|f\|_2^2=1$, but $\|Hf\|_2^2=1+1=2\leq4$",
                 ylim=(0, 1.12), xlim=(0, 5))
    for ax in axes:
        ax.axvline(1, color="#777777", lw=1, linestyle=":")
        ax.grid(axis="y", alpha=.16)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
