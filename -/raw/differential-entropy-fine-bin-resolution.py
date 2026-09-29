"""Compute exact bin masses for U(0,1) and its square; output PNG to cwd."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    counts = 2 ** np.arange(0, 13)
    uniform_entropy = np.log(counts)
    squared_entropy = []
    for n in counts:
        edges = np.arange(n + 1, dtype=float) / n
        masses = np.diff(np.sqrt(edges))
        assert np.all(masses > 0) and np.isclose(masses.sum(), 1)
        squared_entropy.append(-np.dot(masses, np.log(masses)))
    squared_entropy = np.asarray(squared_entropy)
    corrected = squared_entropy - np.log(counts)
    exact_squared = np.log(2) - 1
    assert corrected[-1] > exact_squared
    assert abs(corrected[-1] - exact_squared) < 0.01
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.9), dpi=120)
    fig.patch.set_facecolor("white")
    axes[0].plot(counts, uniform_entropy, "o-", color="#226d9d", label="Uniform X")
    axes[0].plot(counts, squared_entropy, "s-", color="#aa5127", label="Y = X²")
    axes[0].set_title("Discrete bin entropy grows")
    axes[0].set_ylabel("H(Qₙ), nats")
    axes[0].legend(loc="upper left")
    axes[1].plot(counts, np.zeros_like(counts), "o-", color="#226d9d", label="Uniform: h = 0")
    axes[1].plot(counts, corrected, "s-", color="#aa5127", label="Squared: finite-bin value")
    axes[1].axhline(exact_squared, linestyle="--", color="#aa5127", lw=1.4)
    axes[1].text(2.0, exact_squared - 0.018, "h(Y) = ln 2 − 1 ≈ −0.306853", color="#aa5127", fontsize=11)
    axes[1].set_ylim(-0.37, 0.035)
    axes[1].set_title("Subtracting ln n removes resolution")
    axes[1].set_ylabel("H(Qₙ) − ln n, nats")
    axes[1].legend(loc="upper right", fontsize=10)
    for ax in axes:
        ax.set_xscale("log", base=2)
        ax.set_xticks([1, 4, 16, 64, 256, 1024, 4096], labels=["1", "4", "16", "64", "256", "1024", "4096"])
        ax.set_xlabel("Number n of equal-width bins in (0,1)")
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Fine-bin probabilities connect discrete and differential entropy", fontsize=17)
    fig.text(0.5, 0.025, "Exact model probabilities: pⱼ = 1/n or √((j+1)/n) − √(j/n).", ha="center")
    fig.subplots_adjust(left=0.075, right=0.98, top=0.8, bottom=0.18, wspace=0.26)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
