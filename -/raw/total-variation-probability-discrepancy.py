"""Plot one finite probability example and the event attaining its discrepancy."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    labels = ["A", "B", "C", "D"]
    p = np.array([0.4, 0.1, 0.2, 0.3])
    q = np.array([0.1, 0.3, 0.3, 0.3])
    x = np.arange(4)
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.5), layout="constrained")
    fig.set_facecolor("white")
    left, right = axes
    left.bar(x - 0.18, p, width=0.36, label="P", color="#176b9c")
    left.bar(x + 0.18, q, width=0.36, label="Q", color="#bd671b")
    for positions, values in [(x - 0.18, p), (x + 0.18, q)]:
        for pos, value in zip(positions, values):
            left.text(pos, value + 0.011, f"{value:.1f}", ha="center", fontsize=11)
    left.set(xticks=x, xticklabels=labels, ylim=(0, 0.5), ylabel="Probability mass")
    left.set_title("Two laws on the same four outcomes")
    left.legend(frameon=False)
    delta = p - q
    right.bar(x, delta, color=["#176b9c", "#bd671b", "#bd671b", "#777777"])
    right.axhline(0, color="black", linewidth=0.8)
    for pos, value in zip(x, delta):
        right.text(pos, value + (0.014 if value >= 0 else -0.014),
                   f"{value:+.1f}", ha="center", va="bottom" if value >= 0 else "top", fontsize=11)
    right.set(xticks=x, xticklabels=labels, ylim=(-0.33, 0.43), ylabel="P(x) − Q(x)")
    right.set_title("Positive excess: event {A}")
    right.text(0.5, 0.98, "P({A}) − Q({A}) = 0.3", transform=right.transAxes,
               ha="center", va="top", fontsize=11)
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", alpha=0.15)
        ax.set_axisbelow(True)
    fig.suptitle("Total variation distance: 0.3, not the sum 0.6", fontsize=14)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
