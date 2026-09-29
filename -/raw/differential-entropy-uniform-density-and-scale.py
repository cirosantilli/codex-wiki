"""Plot two exact uniform laws; write the matching PNG to the working directory."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.8), dpi=120)
    fig.patch.set_facecolor("white")
    for ax, length, color in zip(axes, [0.5, 2.0], ["#aa5127", "#226d9d"]):
        height = 1 / length
        entropy = np.log(length)
        ax.fill_between([0, length], height, color=color, alpha=0.2)
        ax.plot([0, 0, length, length], [0, height, height, 0], color=color, lw=3)
        ax.axhline(1, color="#707070", linestyle="--", lw=1.1)
        ax.text(1.05, 1.04, "Density = 1", color="#555555", fontsize=10)
        ax.text(length / 2, height / 2, "Area = 1", ha="center", va="center")
        ax.set_title(f"L = {length:g}: h = ln L = {entropy:.6f} nats")
        ax.set_xlim(-0.1, 2.25)
        ax.set_ylim(0, 2.4)
        ax.set_xlabel("Numerical coordinate x")
        ax.set_ylabel("Probability density f(x)")
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Probability density can exceed one; probability cannot", fontsize=17)
    fig.text(0.5, 0.025, "Same logarithm convention and coordinate scale; no sampled data.", ha="center")
    fig.subplots_adjust(left=0.075, right=0.98, top=0.8, bottom=0.18, wspace=0.29)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
