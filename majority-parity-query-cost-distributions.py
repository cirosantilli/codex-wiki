"""Enumerate uniform three-bit query costs. Python 3.14, matplotlib 3.10.7.

Run from _media; the opaque PNG is written to the current directory.
"""

from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    inputs = list(product((0, 1), repeat=3))
    majority_reads = [(0, 1) if x[0] == x[1] else (0, 1, 2) for x in inputs]
    parity_reads = [(0, 1, 2) for _ in inputs]
    costs = [[len(reads) for reads in algorithm] for algorithm in (majority_reads, parity_reads)]
    revealments = [[sum(i in reads for reads in algorithm) / len(inputs) for i in range(3)]
                   for algorithm in (majority_reads, parity_reads)]
    assert costs[0] == [2, 2, 3, 3, 3, 3, 2, 2]
    assert revealments == [[1.0, 1.0, 0.5], [1.0, 1.0, 1.0]]

    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.9), facecolor="white")
    colors = ["#2563eb", "#c2410c"]
    names = ["Majority: stop on agreement", "Parity: read all three"]
    width = 0.32
    for j, (values, label, color) in enumerate(zip(costs, names, colors)):
        probabilities = [values.count(q) / len(inputs) for q in (2, 3)]
        bars = axes[0].bar(np.array([2, 3]) + (j - 0.5) * width, probabilities, width,
                           color=color, label=label)
        axes[0].bar_label(bars, labels=[f"{p:g}" for p in probabilities], padding=4)
        bars = axes[1].bar(np.arange(1, 4) + (j - 0.5) * width, revealments[j], width,
                           color=color)
        axes[1].bar_label(bars, labels=[f"{p:g}" for p in revealments[j]], padding=4)
    axes[0].set(title="Query-count distribution", xlabel="Number of queries q",
                ylabel="Probability", xticks=[2, 3])
    axes[1].set(title="Coordinate revealment", xlabel="Coordinate inspected",
                xticks=[1, 2, 3], xticklabels=[r"$x_1$", r"$x_2$", r"$x_3$"])
    for ax in axes:
        ax.set_ylim(0, 1.17)
        ax.set_yticks([0, 0.5, 1])
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_axisbelow(True)
        ax.grid(axis="y", alpha=0.2)
    fig.suptitle("Uniform inputs: same worst-case depth, different query costs", fontsize=16)
    fig.legend(*axes[0].get_legend_handles_labels(), loc="lower center", ncol=2,
               frameon=False, bbox_to_anchor=(0.5, 0.115), fontsize=11)
    fig.text(0.5, 0.045, "Majority: E[q] = 2.5 = 1 + 1 + 0.5     |     Parity: E[q] = 3 = 1 + 1 + 1",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.29, top=0.79, wspace=0.30)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
