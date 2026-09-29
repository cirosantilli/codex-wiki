"""Exact finite conditioning illustration; write matching PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.7), layout="constrained")
    colors = ["#315f86", "#315f86", "#b5702b", "#b5702b"]
    axes[0].bar([0, 4, 6, 10], [1/8, 1/8, 3/8, 3/8], width=.8, color=colors)
    axes[1].bar([2, 8], [1/4, 3/4], width=1, color=["#315f86", "#b5702b"])
    for ax in axes:
        ax.axvline(6.5, color="#a12a40", lw=2, label="Overall mean = 6.5")
        ax.set(xlim=(-1, 11), ylim=(0, .88), xlabel="Value", ylabel="Probability mass")
        ax.grid(axis="y", alpha=.2)
    for x, p in zip([0, 4, 6, 10], [1/8, 1/8, 3/8, 3/8]):
        axes[0].text(x, p+.025, "1/8" if p==1/8 else "3/8", ha="center", fontsize=11)
    for x, p, label in [(2, .25, "Group A\nprobability 1/4"), (8, .75, "Group B\nprobability 3/4")]:
        axes[1].text(x, p+.025, label, ha="center", fontsize=10)
    axes[0].set(title="Original values with their actual weights", xticks=[0, 4, 6, 10])
    axes[1].axvline(5, color=".3", ls="--", lw=1.5, label="Unweighted group average = 5")
    axes[1].set(title="Replace values by their group means", xticks=[2, 5, 6.5, 8])
    axes[1].legend(loc="upper left", fontsize=9)
    fig.suptitle("Total expectation: (1/4)·2 + (3/4)·8 = 13/2", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
