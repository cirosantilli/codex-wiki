"""Compare original one-mode number distributions; Python 3.14, matplotlib 3.10.7, numpy 2.3.5."""

from pathlib import Path
from math import factorial

import matplotlib.pyplot as plt
import numpy as np


def main():
    n = np.arange(15)
    mu = 2
    coherent = np.array([np.exp(-mu) * mu**int(k) / factorial(int(k)) for k in n])
    thermal = (1 / 3) * (2 / 3) ** n
    fock = (n == 2).astype(float)
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.4), dpi=100, facecolor="white", sharey=True)
    fig.subplots_adjust(left=0.075, right=0.985, bottom=0.28, top=0.80, wspace=0.18)
    for ax, p, title, color, pair, variance in zip(
        axes,
        [coherent, thermal, fock],
        ["Coherent state", "Single-mode thermal state", "Two-photon Fock state"],
        ["#2469a3", "#c16b22", "#277b60"],
        ["1", "2", "1/2"],
        ["2", "6", "0"],
    ):
        ax.set_facecolor("white")
        ax.bar(n, p, color=color, width=0.75)
        ax.set(xlim=(-0.6, 14.6), ylim=(0, 1.08), xticks=[0, 2, 4, 6, 8, 10, 12, 14])
        ax.set_title(title, fontsize=11, pad=13)
        ax.set_xlabel("Photon number n", fontsize=11)
        ax.tick_params(labelsize=9)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", alpha=0.18)
        ax.set_axisbelow(True)
        ax.text(0.48, 0.77, rf"$g^{{(2)}}(0)={pair}$" + "\n" + rf"$\mathrm{{Var}}\,N={variance}$",
                transform=ax.transAxes, fontsize=14, va="top")
    axes[0].set_ylabel(r"Probability $p_n$", fontsize=11)
    fig.suptitle("Same mean photon number, different pair counts", fontsize=17, y=0.97)
    fig.text(0.5, 0.135, r"All three: $\langle N\rangle=2$     •     $g^{(2)}(0)=\langle N(N-1)\rangle/\langle N\rangle^2$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.045, "Calculated models, not data. Thermal tail above n = 14 omitted; bars are not renormalized.",
             ha="center", fontsize=10, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
