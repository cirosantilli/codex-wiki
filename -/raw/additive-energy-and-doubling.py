"""Compare exact counts and energy bounds; tested with Python 3.14.

Write additive-energy-and-doubling.png to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    examples = [np.array([0, 1, 2, 3]), np.array([0, 1, 4, 10]), np.array([0, 2, 4])]
    sizes, energies, lower_bounds, upper_bounds = [], [], [], []
    for index, values in enumerate(examples):
        sums = values[:, None] + values[None, :]
        differences = values[:, None] - values[None, :]
        if index == 2:
            sums %= 6
            differences %= 6
        sums, counts = np.unique(sums, return_counts=True)
        differences, difference_counts = np.unique(differences, return_counts=True)
        energy = int(counts @ counts)
        assert energy == int(difference_counts @ difference_counts)
        sizes.append([len(values), len(sums), len(differences)])
        energies.append(energy)
        lower_bounds.append(len(values) ** 4 / len(sums))
        upper_bounds.append(len(values) ** 3)
        assert lower_bounds[-1] <= energy <= upper_bounds[-1]
    assert sizes == [[4, 7, 7], [4, 10, 13], [3, 3, 3]]
    assert energies == [44, 28, 27]
    assert np.allclose(lower_bounds, [256 / 7, 256 / 10, 27])
    assert np.allclose(np.array(sizes)[:, 1] / np.array(sizes)[:, 0], [7 / 4, 5 / 2, 1])

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.8), dpi=120, facecolor="white")
    fig.suptitle("Small doubling forces large additive energy", fontsize=16, y=0.975)
    row_positions = np.arange(3)
    bar_height = 0.21
    offsets = [-0.23, 0, 0.23]
    colors = ["#bdcbd5", "#266e9e", "#cc7822"]
    ax = axes[0]
    sizes = np.array(sizes)
    for offset, color, values, label in zip(
            offsets, colors, sizes.T, [r"$|S|$", r"$|S+S|$", r"$|S-S|$"]):
        bars = ax.barh(row_positions + offset, values, height=bar_height,
                       color=color, label=label)
        ax.bar_label(bars, labels=list(map(str, values)), padding=4, fontsize=11)
    ax.set_title("Set sizes and doubling")
    ax.set_xlabel("Number of distinct elements")
    ax.set_xlim(0, 14.7)
    ax.set_xticks([0, 3, 6, 9, 12])
    ax.set_yticks(row_positions, labels=["A\nK = 7/4", "B\nK = 5/2", "H\nK = 1"])
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=3,
              frameon=False, handlelength=1.2, columnspacing=1.0)

    ax = axes[1]
    energy_colors = ["#77a89c", "#266e9e", "#bdcbd5"]
    for offset, color, values, labels, label in zip(
            offsets, energy_colors, [lower_bounds, energies, upper_bounds],
            [["256/7 ≈ 36.57", "256/10 = 25.6", "27"], ["44", "28", "27"],
             ["64", "64", "27"]],
            [r"Lower: $|S|^4/|S+S|$", r"Actual: $E(S)$", r"Upper: $|S|^3$"]):
        bars = ax.barh(row_positions + offset, values, height=bar_height,
                       color=color, label=label)
        ax.bar_label(bars, labels=labels, padding=4, fontsize=10)
    ax.set_title("Energy and its bounds")
    ax.set_xlabel("Quadruple count (bounds may be fractional)")
    ax.set_xlim(0, 86)
    ax.set_xticks([0, 16, 32, 48, 64])
    ax.set_yticks(row_positions, labels=["A", "B", "H"])
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15),
              frameon=False, fontsize=10)
    for ax in axes:
        ax.set_ylim(2.55, -0.55)
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.tick_params(axis="y", length=0, pad=9)
        ax.set_axisbelow(True)
        ax.grid(axis="x", color="#e3e8eb")
    fig.text(0.5, 0.075, "A = {0, 1, 2, 3} and B = {0, 1, 4, 10}: ordinary integer addition",
             ha="center", fontsize=11)
    fig.text(0.5, 0.035, "H = {0, 2, 4} in Z/6Z: addition modulo 6; H + H = H − H = H",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.085, right=0.97, top=0.84, bottom=0.31, wspace=0.30)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
