"""Generate markov-periodicity.png in cwd; Python 3.14, NumPy, Matplotlib."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    c = np.array([[0, 1], [1, 0]])
    pi = np.array([0.5, 0.5])
    n = np.arange(13)
    probability = (n % 2 == 0).astype(float)
    visits = np.cumsum(probability) / (n + 1)
    np.testing.assert_allclose(pi @ c, pi)
    np.testing.assert_array_equal(c @ c, np.eye(2, dtype=int))
    for k in n:
        np.testing.assert_allclose(np.linalg.matrix_power(c, int(k))[0, 0], probability[k])

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.3), facecolor="white")
    fig.subplots_adjust(left=0.075, right=0.98, top=0.75, bottom=0.21, wspace=0.28)
    fig.suptitle("A stationary law does not guarantee convergence", fontsize=16, y=0.98)
    fig.text(0.5, 0.865, "Deterministic cycle: A → B → A → B → …    •    Initial state: A", ha="center", fontsize=11)
    axes[0].plot(n, probability, "o-", color="#1765a8", lw=1.8, ms=5, label="Start in A")
    axes[0].axhline(0.5, color="#576b39", ls="--", lw=1.8, label="Start with π = (1/2, 1/2)")
    axes[0].set_title("One-time probabilities oscillate")
    axes[0].set_ylabel("Probability of state A at step n")
    axes[0].legend(loc="lower center", bbox_to_anchor=(0.5, -0.43), frameon=False, fontsize=9.5)
    axes[1].plot(n, visits, "o-", color="#9a5b00", lw=1.8, ms=5)
    axes[1].axhline(0.5, color="#576b39", ls="--", lw=1.8)
    axes[1].set_title("Time-averaged visits approach 1/2")
    axes[1].set_ylabel("Fraction in A, counting steps 0 to n")
    axes[1].text(0.5, -0.36, "Visits to A: ⌊n/2⌋ + 1 out of n + 1", transform=axes[1].transAxes, ha="center", fontsize=10)
    for ax in axes:
        ax.set_xlim(-0.2, 12.2)
        ax.set_ylim(-0.04, 1.06)
        ax.set_xticks(np.arange(0, 13, 2))
        ax.set_yticks([0, 0.5, 1])
        ax.set_xlabel("Number of steps n")
        ax.grid(color="#e3e7eb", lw=0.7)
    fig.savefig(Path.cwd() / "markov-periodicity.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
