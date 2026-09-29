"""Plot a finite distribution and its exact inclusive tail against Markov's bound."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    values = np.array([0.0, 1.0, 2.0, 5.0])
    probabilities = np.array([0.5, 0.2, 0.2, 0.1])
    mean = float(values @ probabilities)
    assert np.isclose(mean, 1.1)
    assert np.isclose(probabilities[values >= 2].sum(), 0.3)
    assert np.isclose(probabilities[values >= 5].sum(), 0.1)
    assert np.isclose(0.22 * 5, mean)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.2), dpi=120, facecolor="white")
    ax = axes[0]
    ax.bar(values, probabilities, width=0.48, color="#206a9d")
    for v, p in zip(values, probabilities):
        ax.text(v, p + 0.022, f"p = {p:g}", ha="center", fontsize=11)
    ax.set(xlim=(-0.6, 5.6), ylim=(0, 0.62), xticks=values,
           xlabel="Value of Y", ylabel="Probability mass",
           title="Mean = 0.5·0 + 0.2·1 + 0.2·2 + 0.1·5 = 1.1")
    ax.grid(axis="y", color="#e7eaed")
    ax.set_axisbelow(True)
    ax = axes[1]
    thresholds = np.linspace(0.15, 6, 801)
    bound = np.minimum(1, mean / thresholds)
    ax.plot(thresholds, bound, color="#be7521", lw=2.5,
            label=r"Bound: $\min(1,1.1/a)$")
    segments = [(0.15, 1, 0.5), (1, 2, 0.3), (2, 5, 0.1), (5, 6, 0)]
    for i, (left, right, height) in enumerate(segments):
        ax.plot([left, right], [height, height], color="#206a9d", lw=2.5,
                label=r"Exact $P(Y\geq a)$" if i == 0 else None)
        if i > 0:
            ax.scatter(left, height, facecolor="white", edgecolor="#206a9d",
                       linewidth=1.7, s=55, zorder=5)
        if i < len(segments) - 1:
            ax.scatter(right, height, color="#206a9d", s=55, zorder=5)
    ax.vlines(2, 0.3, 0.55, color="#2f8a68", lw=3)
    ax.scatter(2, 0.55, color="#be7521", s=55, zorder=5)
    ax.annotate("At a = 2:\nactual 0.30, bound 0.55", xy=(2, 0.425),
                xytext=(2.7, 0.67), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#2f8a68"})
    ax.set(xlim=(0.15, 6), ylim=(-0.045, 1.08),
           xlabel="Threshold a > 0", ylabel="Tail probability / upper bound",
           title="Bound from mean and nonnegativity")
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    ax.grid(color="#e7eaed")
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Markov's inequality: the same mean limits every positive-threshold tail", fontsize=15)
    fig.subplots_adjust(left=0.06, right=0.985, top=0.79, bottom=0.14, wspace=0.3)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
