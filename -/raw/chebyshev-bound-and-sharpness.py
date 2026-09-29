"""Show a general variance bound, a normal tail, and an attaining distribution."""

from math import erfc, sqrt
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    values = np.array([-2.0, 0.0, 2.0])
    masses = np.array([1 / 8, 3 / 4, 1 / 8])
    assert np.isclose(values @ masses, 0)
    assert np.isclose(values**2 @ masses, 1)
    assert np.isclose(masses[np.abs(values) >= 2].sum(), 1 / 4)
    assert np.isclose(masses[np.abs(values) > 2].sum(), 0)
    assert np.isclose(erfc(2 / sqrt(2)), 0.04550026389635843)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.4), dpi=120, facecolor="white")
    k = np.linspace(0.15, 4, 801)
    actual = np.array([erfc(float(v) / sqrt(2)) for v in k])
    bound = np.minimum(1, 1 / k**2)
    ax = axes[0]
    ax.plot(k, bound, color="#be7521", lw=2.5, label=r"General bound: $\min(1,1/k^2)$")
    ax.plot(k, actual, color="#206a9d", lw=2.5, label=r"Normal: $P(|Z|\geq k)$")
    ax.vlines(2, erfc(2 / sqrt(2)), 0.25, color="#2f8a68", lw=2.5)
    ax.scatter([2, 2], [erfc(2 / sqrt(2)), 0.25],
               color=["#206a9d", "#be7521"], s=55, zorder=5)
    ax.annotate("At k = 2:\nnormal tail ≈ 0.0455\nbound = 0.25", xy=(2, 0.15),
                xytext=(2.25, 0.39), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#2f8a68"})
    ax.set(xlim=(0.15, 4), ylim=(0, 1.08), xlabel="Deviation k in standard deviations",
           ylabel="Two-sided tail probability / bound", title="Normal tails lie well below the bound")
    ax.legend(loc="upper right", fontsize=10, frameon=False)
    ax.grid(color="#e7eaed")
    ax = axes[1]
    ax.axvspan(-2.1, -1.9, color="#be7521", alpha=0.1)
    ax.axvspan(1.9, 2.1, color="#be7521", alpha=0.1)
    ax.bar(values, masses, width=0.45, color=["#be7521", "#206a9d", "#be7521"])
    for v, p, label in zip(values, masses, ["1/8", "3/4", "1/8"]):
        ax.text(v, p + 0.026, label, ha="center", fontsize=12)
    ax.text(0, 0.91, r"Mean = 0; variance = 1", ha="center", fontsize=12)
    ax.text(0, 0.84, r"$P(|X|\geq2)=1/8+1/8=1/4$", ha="center", fontsize=12)
    ax.set(xlim=(-2.75, 2.75), ylim=(0, 1.04), xticks=values,
           xlabel="Value of X", ylabel="Probability mass",
           title="A three-point distribution attains equality")
    ax.grid(axis="y", color="#e7eaed")
    ax.set_axisbelow(True)
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Chebyshev's inequality: a distribution-free guarantee can be sharp", fontsize=15)
    fig.subplots_adjust(left=0.065, right=0.985, top=0.79, bottom=0.14, wspace=0.29)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
