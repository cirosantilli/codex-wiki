"""Write operator-spectrum-examples.png to cwd; Python 3.14, NumPy, Matplotlib."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    blue, orange, gray = "#1765a8", "#bc570e", "#596572"
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), facecolor="white")
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.22, top=0.76, wspace=0.32)
    fig.suptitle("Spectral values need not have eigenvectors", fontsize=16, y=0.97)
    fig.legend(
        handles=[
            Line2D([], [], color=blue, lw=5, label="Spectrum without eigenvectors"),
            Line2D([], [], color=orange, marker="o", ls="", label="Eigenvalues"),
        ],
        loc="upper center", bbox_to_anchor=(0.5, 0.92), ncol=2, frameon=False,
    )

    ax = axes[0]
    ax.set_title(r"Multiplication: $(Mf)(x)=xf(x)$ on $L^2[0,1]$")
    ax.plot([0, 1], [0, 0], color=blue, lw=7, solid_capstyle="round", zorder=3)
    ax.text(0.5, -0.063, r"$\sigma(M)=[0,1],\quad\sigma_p(M)=\varnothing$", ha="center", color=blue)
    ax.scatter([0.5], [0.1], color=gray, s=35, zorder=4)
    ax.plot([0.5, 0.5], [0, 0.1], color=gray, ls="--", lw=1.5)
    ax.annotate(r"$\lambda=\frac{1}{2}+\frac{i}{10}$", (0.5, 0.1), (0.68, 0.107), fontsize=12)
    ax.text(0.15, 0.043, r"$\mathrm{dist}=0.1$", fontsize=11, color=gray)
    ax.text(0.5, 0.163, r"$\|(M-\lambda I)^{-1}\|=10$", ha="center", fontsize=12)
    ax.set_ylim(-0.097, 0.2)
    ax.set_yticks([0, 0.1])
    ax.set_ylabel(r"$\operatorname{Im}\lambda$")
    ax.set_xlabel(r"$\operatorname{Re}\lambda$")

    ax = axes[1]
    ax.set_title(r"Diagonal: $(Dx)_n=x_n/n$ on $\ell^2$")
    values = 1 / np.arange(1, 81)
    ax.scatter(values, np.zeros_like(values), color=orange, s=28, zorder=3)
    ax.scatter([0], [0], facecolor="white", edgecolor=blue, linewidth=2.5, s=90, zorder=5)
    ax.annotate("0: spectral, not an eigenvalue", (0, 0), (0.1, 0.33),
                arrowprops={"arrowstyle": "->", "color": blue}, color=blue, fontsize=11)
    for val, label in [(1, "1"), (0.5, "1/2"), (1/3, "1/3"), (0.25, "1/4")]:
        ax.annotate(label, (val, 0), (val, -0.13 if val != 0.25 else -0.24), ha="center", color=orange)
    ax.text(0.72, 0.14, r"$De_n=\frac{1}{n} e_n$", ha="center", fontsize=13)
    ax.set_ylim(-0.36, 0.48)
    ax.set_yticks([])
    ax.set_xlabel(r"Real spectral parameter $\lambda$")

    for ax in axes:
        ax.set_xlim(-0.12, 1.22)
        ax.set_xticks([0, 0.5, 1])
        ax.axhline(0, color="#b5bdc5", lw=1, zorder=0)
        ax.grid(axis="x", color="#e7ebef", lw=0.8)
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.065, "An entire interval can lack eigenvectors; a limit of eigenvalues can lack one too.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / "operator-spectrum-examples.png", dpi=145, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
