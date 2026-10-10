"""All eight XOR patterns and all three pair marginals; Python 3.14.4.

Uses the repository's matplotlib/numpy environment. Writes the PNG to CWD.
"""

from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    joint = np.zeros((2, 2, 2))
    for x, y in product((0, 1), repeat=2):
        joint[x, y, x ^ y] = 0.25
    patterns = list(product((0, 1), repeat=3))
    # Check every triple, including the four impossible patterns.
    for x, y, z in patterns:
        assert joint[x, y, z] == (0.25 if z == x ^ y else 0)
    assert joint.sum() == 1
    marginals = [joint.sum(axis=axis) for axis in range(3)]
    assert all(np.array_equal(m, [0.5, 0.5]) for m in
               [joint.sum(axis=(1, 2)), joint.sum(axis=(0, 2)), joint.sum(axis=(0, 1))])
    # Each of the four cells of every pair is 1/4.
    for marginal in marginals:
        for i, j in product((0, 1), repeat=2):
            assert marginal[i, j] == 0.25
    assert joint[0, 0, 0] == 0.25 != 0.5 ** 3
    plt.rcParams.update({"font.size": 12, "text.color": "#182332", "axes.labelcolor": "#182332"})
    fig = plt.figure(figsize=(9.4, 6.5), layout="constrained", facecolor="white")
    grid = fig.add_gridspec(2, 3, height_ratios=[1.25, 1])
    ax = fig.add_subplot(grid[0, :])
    positions = np.arange(8)
    masses = [joint[state] for state in patterns]
    ax.bar(positions, masses, width=0.64, color="#287eac", zorder=3,
           label="Actual joint law: Z = X XOR Y")
    ax.axhline(0.125, color="#bd5a37", linestyle="--", linewidth=2,
               label="Product of marginals: 1/8 in every cell", zorder=4)
    for position, mass in zip(positions, masses):
        ax.text(position, mass + 0.008, "1/4" if mass else "0", ha="center", fontsize=12)
    ax.set_xticks(positions, ["".join(map(str, pattern)) for pattern in patterns])
    ax.set_yticks([0, 0.125, 0.25], ["0", "1/8", "1/4"])
    ax.set_ylim(0, 0.37)
    ax.set_xlabel("All eight (X, Y, Z) patterns")
    ax.set_ylabel("Probability")
    ax.set_title("Four allowed triples, four impossible triples", fontsize=13)
    ax.grid(axis="y", color="#e1e7ed", zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper right", fontsize=10, frameon=False)
    pairs = [(joint.sum(axis=2), "X", "Y"),
             (joint.sum(axis=1), "X", "Z"),
             (joint.sum(axis=0), "Y", "Z")]
    for i, (matrix, first, second) in enumerate(pairs):
        panel = fig.add_subplot(grid[1, i])
        panel.imshow(matrix, vmin=0, vmax=0.5, cmap="Blues")
        for row, col in product((0, 1), repeat=2):
            panel.text(col, row, "1/4", ha="center", va="center", fontsize=17, color="#182332")
        panel.set_xticks([0, 1], [f"{second} = 0", f"{second} = 1"])
        panel.set_yticks([0, 1], [f"{first} = 0", f"{first} = 1"])
        panel.set_xticks([0.5], minor=True)
        panel.set_yticks([0.5], minor=True)
        panel.grid(which="minor", color="white", linewidth=2)
        panel.tick_params(which="both", length=0)
        panel.set_title(f"Pair ({first}, {second}) is independent", fontsize=11, pad=10)
        panel.set_xlabel("Each row and column sums to 1/2", fontsize=9)
    fig.suptitle("Pairwise independence does not imply joint independence", fontsize=16, weight="bold")
    fig.savefig(Path.cwd() / "pairwise-versus-joint-independence.png",
                dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
