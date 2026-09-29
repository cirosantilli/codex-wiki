"""Exact analytic spectra; not measured data.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Writes the matching PNG basename to the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 3, figsize=(11.8, 5.5))
    blue, green, orange = "#245b92", "#17775b", "#ac4c10"
    ax = axes[0]
    levels = np.arange(4) + 0.5
    for n, energy in enumerate(levels):
        ax.hlines(energy, 0.13, 0.82, lw=3, color=green if n == 0 else blue)
        ax.plot(0.28, energy, "o", color=green if n == 0 else blue, ms=8)
        ax.text(0.88, energy, f"n = {n}", va="center", fontsize=11)
    ax.annotate("Ground state\nattained", xy=(0.49, 0.5), xytext=(0.63, 1.02),
                ha="center", fontsize=11, color=green,
                arrowprops={"arrowstyle": "->", "color": green})
    ax.set(title="Harmonic oscillator", ylabel=r"Energy / $\hbar\omega$",
           ylim=(-0.35, 4.0), xlim=(0, 1.36), yticks=levels, xticks=[])
    ax.text(0.5, -0.18, r"$E_n/\hbar\omega=n+1/2$", transform=ax.transAxes,
            ha="center", fontsize=12)

    ax = axes[1]
    diagonal = np.array([0.0, 0.0, 2.0, 5.0])
    eigenvalues = np.linalg.eigvalsh(np.diag(diagonal))
    assert np.array_equal(eigenvalues, diagonal)
    assert np.count_nonzero(eigenvalues == 0) == 2
    for energy in [0, 2, 5]:
        ax.hlines(energy, 0.10, 0.87, lw=3, color=green if energy == 0 else blue)
    for x, y, label in [(0.27, 0, r"$e_1$"), (0.70, 0, r"$e_2$"),
                        (0.48, 2, r"$e_3$"), (0.48, 5, r"$e_4$")]:
        ax.plot(x, y, "o", color=green if y == 0 else blue, ms=8)
        ax.text(x, y + 0.25, label, ha="center")
    ax.text(0.48, 1.00, "Two basis states\none ground energy", ha="center",
            fontsize=11, color=green)
    ax.set(title="Finite degenerate model", ylabel=r"Energy / $\varepsilon$",
           ylim=(-0.55, 5.9), xlim=(0, 1), yticks=[0, 2, 5], xticks=[])
    ax.text(0.5, -0.18, r"$H/\varepsilon=\mathrm{diag}(0,0,2,5)$",
            transform=ax.transAxes, ha="center", fontsize=11)

    ax = axes[2]
    ax.fill_betweenx([0, 3.85], 0.15, 0.87, color="#e4edf6")
    ax.annotate("", xy=(0.53, 3.85), xytext=(0.53, 0.12),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": blue})
    ax.text(0.53, 2.9, "Continuous\nspectral values\n(all E > 0)",
            ha="center", va="center", fontsize=11, color=blue,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 4})
    ax.hlines(0, 0.15, 0.87, color=orange, lw=2, ls="--")
    ax.text(0.53, 0.9, "Bottom E = 0\nno normalized\neigenstate", ha="center",
            va="center", fontsize=11, color=orange)
    ax.set(title="Free particle on the line", ylabel=r"Energy / chosen unit $E_u$",
           ylim=(-0.35, 3.85), xlim=(0, 1), yticks=[0, 1, 2, 3], xticks=[])
    ax.text(0.5, -0.18, r"$\sigma(H)=[0,\infty)$", transform=ax.transAxes,
            ha="center", fontsize=12)
    fig.suptitle("A spectral bottom need not be a unique, attained ground energy", y=0.97,
                 fontsize=15)
    fig.text(0.5, 0.035, "Analytic models, not measured data • dots denote independent basis states • panel energy units differ",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.065, right=0.98, top=0.81, bottom=0.22, wspace=0.48)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
