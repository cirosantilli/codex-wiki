"""Compare hidden flips and flagged erasures at equal probabilities; PNG to CWD."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def binary_entropy(probabilities):
    p = np.asarray(probabilities, dtype=float)
    result = np.zeros_like(p)
    mask = (p > 0) & (p < 1)
    result[mask] = -p[mask] * np.log2(p[mask]) - (1 - p[mask]) * np.log2(1 - p[mask])
    return result


def arrow(ax, start, end, label, label_position, failed=False):
    color = "#bf5520" if failed else "#246bce"
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=17, linewidth=2,
                                linestyle="--" if failed else "-",
                                color=color, shrinkA=19, shrinkB=21))
    ax.text(*label_position, label, color=color, ha="center", va="center",
            fontsize=11, bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})


def node(ax, position, label, erasure=False):
    ax.text(*position, label, ha="center", va="center", fontsize=13, zorder=4,
            bbox={"boxstyle": "round,pad=0.35", "facecolor": "white",
                  "edgecolor": "#69747d" if erasure else "#246bce", "linewidth": 1.5})


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(12, 7), dpi=100)
    left = fig.add_axes([0.05, 0.57, 0.43, 0.28])
    right = fig.add_axes([0.54, 0.57, 0.43, 0.28])
    lower = fig.add_axes([0.13, 0.12, 0.74, 0.32])
    for ax in [left, right]:
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis("off")
        ax.text(0.13, 0.98, "Input", ha="center", fontsize=11)
        ax.text(0.87, 0.98, "Output", ha="center", fontsize=11)
    left.set_title("Binary symmetric channel: hidden flips",
                   fontsize=13, weight="bold", pad=15)
    right.set_title("Binary erasure channel: announced losses",
                    fontsize=13, weight="bold", pad=15)
    for ax in [left, right]:
        for y, bit in [(0.8, "0"), (0.2, "1")]:
            arrow(ax, (0.13, y), (0.87, y), "0.9", (0.5, y))
            node(ax, (0.13, y), bit)
            node(ax, (0.87, y), bit)
    arrow(left, (0.13, 0.8), (0.87, 0.2), "0.1", (0.35, 0.62), failed=True)
    arrow(left, (0.13, 0.2), (0.87, 0.8), "0.1", (0.65, 0.62), failed=True)
    arrow(right, (0.13, 0.8), (0.87, 0.5), "0.1", (0.43, 0.67), failed=True)
    arrow(right, (0.13, 0.2), (0.87, 0.5), "0.1", (0.43, 0.33), failed=True)
    node(right, (0.87, 0.5), "erasure", erasure=True)
    p = np.linspace(0, 0.5, 501)
    lower.plot(p, 1 - p, color="#23855b", linewidth=2.5,
               label="Erasure: 1 − p")
    lower.plot(p, 1 - binary_entropy(p), color="#246bce", linewidth=2.5,
               label="Flip: 1 − h₂(p)")
    erasure_value = 0.9
    flip_value = float(1 - binary_entropy(0.1))
    lower.scatter([0.1, 0.1], [erasure_value, flip_value],
                  color=["#23855b", "#246bce"], zorder=5)
    lower.plot([0.1, 0.1], [flip_value, erasure_value],
               color="#69747d", linestyle=":", linewidth=1.5)
    lower.annotate("At p = 0.1:\n0.900000 vs 0.531004 bits/use",
                   (0.1, (erasure_value + flip_value) / 2),
                   xytext=(0.24, 0.91), textcoords="data",
                   arrowprops={"arrowstyle": "-", "color": "#69747d"}, fontsize=11,
                   bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    lower.set(xlabel="Flip or erasure probability p",
              ylabel="Capacity (bits per use)",
              xlim=(0, 0.5), ylim=(-0.025, 1.06))
    lower.grid(alpha=0.2)
    lower.legend(loc="lower left", frameon=False)
    fig.suptitle("Knowing where information was lost changes the channel capacity",
                 fontsize=16, weight="bold", y=0.975)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
