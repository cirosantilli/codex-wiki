"""Original population-genotype diagram; writes basename.png to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    p = np.linspace(0, 1, 501)
    curves = np.array([p**2, 2 * p * (1 - p), (1 - p)**2])
    example_p = 0.7
    expected = np.array([example_p**2, 2 * example_p * (1 - example_p),
                         (1 - example_p)**2])
    observed = np.array([0.7, 0, 0.3])
    colors = ["#237ca3", "#78afc3", "#e6aa47"]
    labels = ["AA: p²", "Aa: 2pq", "aa: q²"]
    fig, (curves_ax, bars_ax) = plt.subplots(1, 2, figsize=(8.8, 4.6))
    fig.set_facecolor("white")
    for values, value, color, label in zip(curves, expected, colors, labels):
        curves_ax.plot(p, values, color=color, label=label, lw=2.4)
        curves_ax.plot(example_p, value, "o", color=color, ms=6)
    curves_ax.axvline(example_p, color="#555555", ls="--", lw=1)
    curves_ax.set(xlim=(0, 1), ylim=(0, 1.04), xlabel="Allele frequency p of A (q = 1 − p)",
                  ylabel="Predicted genotype proportion")
    curves_ax.set_title("Random union of gametes", fontsize=12)
    curves_ax.text(0.73, 0.97, "p = 0.70", fontsize=10)
    curves_ax.legend(loc="upper center", fontsize=9, framealpha=0.96)
    x = np.arange(3)
    bars_ax.bar(x - 0.18, expected, width=0.34, color=colors,
                label="HW expectation")
    bars_ax.bar(x + 0.18, observed, width=0.34, color="white",
                edgecolor="#555555", hatch="///", label="Example population")
    for i, (predicted, actual) in enumerate(zip(expected, observed)):
        bars_ax.text(i - 0.18, predicted + 0.02, f"{predicted:.2f}",
                     ha="center", fontsize=10)
        bars_ax.text(i + 0.18, actual + 0.02, f"{actual:.2f}",
                     ha="center", fontsize=10)
    bars_ax.set(xticks=x, xticklabels=["AA", "Aa", "aa"],
                ylim=(0, 0.95), ylabel="Genotype proportion")
    bars_ax.set_title("Same p = 0.70; different genotypes", fontsize=12)
    bars_ax.legend(loc="upper right", fontsize=9, framealpha=0.96)
    for ax in (curves_ax, bars_ax):
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_axisbelow(True)
        ax.grid(axis="y", alpha=0.18)
    fig.suptitle("Hardy–Weinberg proportions: p², 2pq, q²", fontsize=15)
    fig.text(0.5, 0.085,
             "Equilibrium model: large randomly mating population; equal parental allele pools;",
             ha="center", fontsize=9)
    fig.text(0.5, 0.04,
             "fair segregation; no selection, mutation, migration or drift. Observed counts can differ.",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.25, top=0.81, wspace=0.37)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
