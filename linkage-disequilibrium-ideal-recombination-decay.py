"""Draw deterministic recombination decay, not measured population data.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the matching opaque PNG is written to the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    generations = np.arange(61)
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.6), facecolor="white")
    fig.subplots_adjust(left=0.085, right=0.98, top=0.77, bottom=0.22, wspace=0.27)
    colors = ["#555555", "#0072b2", "#d55e00", "#009e73"]
    for recombination, color in zip([0.0, 0.01, 0.1, 0.5], colors):
        normalized_d = (1-recombination)**generations
        # Recursively update all four frequencies as a separate check of the curves.
        f = np.array([0.36, 0.24, 0.04, 0.36])  # p = 0.60, q = 0.40, D0 = 0.12
        for t in generations:
            d = f[0]*f[3] - f[1]*f[2]
            np.testing.assert_allclose(d, 0.12*normalized_d[t], atol=2e-15)
            np.testing.assert_allclose([f[0]+f[1], f[0]+f[2]], [0.60, 0.40])
            assert np.min(f) >= 0
            f += recombination*d*np.array([-1, 1, 1, -1])
        for ax, power in zip(axes, [1, 2]):
            ax.plot(generations, normalized_d**power, color=color, linewidth=2,
                    marker="o", markersize=3, markevery=5, label=f"r = {recombination:g}")
    for ax in axes:
        ax.set_xlim(0, 60)
        ax.set_ylim(-0.025, 1.04)
        ax.set_xlabel("Generation t", fontsize=12)
        ax.set_yticks(np.linspace(0, 1, 6))
        ax.tick_params(labelsize=10)
        ax.grid(color="#dddddd", linewidth=0.65)
        ax.spines[["top", "right"]].set_visible(False)
        ax.axhline(0.5, color="#999999", linestyle=":", linewidth=1)
    axes[0].set_title(r"Signed association: $D_t/D_0=(1-r)^t$", fontsize=12)
    axes[0].set_ylabel("Fraction of initial D", fontsize=12)
    axes[1].set_title(r"Squared correlation: $r_{\rm LD,t}^2/r_{\rm LD,0}^2=(1-r)^{2t}$", fontsize=12)
    axes[1].set_ylabel("Fraction of initial squared correlation", fontsize=11)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.52, 0.9),
               ncol=4, frameon=False, fontsize=11)
    fig.suptitle("Ideal recombination decay at fixed allele frequencies", fontsize=16, y=0.98)
    fig.text(0.5, 0.065, "Random mating; constant r; no selection, mutation, migration or drift\n"
             "D₀ ≠ 0; normalization applies to either sign. Points are model generations.",
             ha="center", fontsize=10.5, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
