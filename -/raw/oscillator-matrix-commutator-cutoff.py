"""Draw the exact boundary defect of compressed oscillator matrices.

Emit the matching PNG into CWD. Tested with Python 3.14,
matplotlib 3.10.7 and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
import numpy as np


def main():
    count = 8
    a = np.diag(np.sqrt(np.arange(1, count)), 1)
    x = (a + a.T) / np.sqrt(2)
    p_over_i = (a.T - a) / np.sqrt(2)
    commutator_over_i = x @ p_over_i - p_over_i @ x
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.9),
                             gridspec_kw={"width_ratios": [1, 1, 1.45]})
    fig.set_facecolor("white")
    norm = TwoSlopeNorm(vmin=-2, vcenter=0, vmax=2)
    for ax, matrix, title in zip(axes[:2], [x, p_over_i],
                                [r"$x_8=X_8/\ell$", r"$p_8/i=P_8/(i\hbar/\ell)$"]):
        im = ax.imshow(matrix, cmap="RdBu_r", norm=norm)
        ax.set(title=title, xticks=[0, 3, 7], yticks=[0, 3, 7],
               xlabel="Column n", ylabel="Row m")
        ax.set_xticks(np.arange(-.5, count), minor=True)
        ax.set_yticks(np.arange(-.5, count), minor=True)
        ax.grid(which="minor", color="#dddddd", lw=.5)
        ax.tick_params(which="minor", bottom=False, left=False)
    color_axis = fig.add_axes([.14, .14, .40, .025])
    fig.colorbar(im, cax=color_axis, orientation="horizontal")
    color_axis.tick_params(labelsize=9)
    fig.text(.34, .065, "Real matrix entries", ha="center", fontsize=10)
    ax = axes[2]
    diagonal = np.diag(commutator_over_i)
    ax.bar(np.arange(count), diagonal,
           color=["#2166ac"] * (count - 1) + ["#b35806"], width=.7)
    ax.axhline(0, color="#555555", lw=.8)
    ax.axhline(1, color="#555555", ls="--", lw=1)
    ax.set(title=r"Diagonal of $[X_8,P_8]/(i\hbar)$",
           xlabel="Retained number state n", ylabel="Commutator diagonal",
           xticks=np.arange(count), yticks=[-7, 0, 1], ylim=(-8.4, 2.6))
    ax.text(3, 1.55, "Exact on states 0 through 6", ha="center", fontsize=10)
    ax.text(7, -7.35, "−7", ha="center", va="top", color="#b35806", fontsize=12)
    ax.text(.06, .26, "Last state loses the path through |8⟩.\nTrace: 7 × 1 − 7 = 0.",
            transform=ax.transAxes, fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("A finite oscillator cutoff preserves low-state commutators, but leaves a boundary defect", y=.98)
    fig.text(.5, .015, r"$\ell=\sqrt{\hbar/(m\omega)}$. Retain $|0\rangle,\ldots,|7\rangle$; compress X and P before multiplying. Original exact model.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.055, right=.985, top=.80, bottom=.28, wspace=.57)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
