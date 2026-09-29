"""Compare the exact zero-T constant-shell BCS gap with its weak limit.

Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7 (repository pyproject.toml).
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
No measured points or fitted curves. Lambda stays strictly positive.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    lam = np.linspace(0.12, 1.2, 700)
    gap = 1 / np.sinh(1 / lam)
    weak = 2 * np.exp(-1 / lam)
    error = 100 * np.exp(-2 / lam)
    assert np.allclose((gap - weak) / gap, error / 100, rtol=1e-8)
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(8.2, 5.8), sharex=True,
                                      gridspec_kw={"height_ratios": [1.25, 1]})
    for ax in (top, bottom):
        ax.axvspan(0.12, 0.3, color="#edf4f9")
        ax.axvline(0.25, color="#7b8894", lw=0.9, ls=":")
        ax.grid(alpha=0.18, which="major")
        ax.set_xlim(0.12, 1.2)
    top.semilogy(lam, gap, color="#14639b", lw=2.3,
                 label=r"Exact cutoff model: $1/\sinh(1/\lambda)$")
    top.semilogy(lam, weak, "--", color="#bd5918", lw=2,
                 label=r"Weak coupling: $2e^{-1/\lambda}$")
    top.plot(0.25, 1 / np.sinh(4), "o", color="#14639b", ms=5)
    top.set(ylabel=r"$\Delta(0)/(\hbar\omega_D)$", ylim=(0.0003, 1.4),
            title="A small attraction produces an exponentially small gap")
    top.legend(loc="lower right", fontsize=10, framealpha=1)
    bottom.semilogy(lam, error, color="#14639b", lw=2.3)
    bottom.set(xlabel=r"Dimensionless coupling $\lambda=N_0V$",
               ylabel="Underestimate (%)", ylim=(0.000003, 30))
    bottom.scatter([0.25, 1], [100 * np.exp(-8), 100 * np.exp(-2)],
                   s=23, color="#14639b", zorder=4)
    bottom.annotate(r"$\lambda=0.25$: 0.03355%", (0.25, 100 * np.exp(-8)),
                    (0.39, 0.0003), fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": "#69737e"})
    bottom.annotate(r"$\lambda=1$: 13.53%", (1, 100 * np.exp(-2)),
                    (0.76, 0.35), fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": "#69737e"})
    bottom.text(0.62, 0.000007, r"Exact relative error: $e^{-2/\lambda}$", fontsize=10)
    fig.subplots_adjust(left=0.14, right=0.97, top=0.90, bottom=0.22, hspace=0.17)
    fig.text(0.5, 0.035, "Same sharp-cutoff model throughout; larger coupling tests the approximation,\n"
             "not the validity of this model for strongly coupled materials.",
             ha="center", fontsize=10, color="#414b54")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
