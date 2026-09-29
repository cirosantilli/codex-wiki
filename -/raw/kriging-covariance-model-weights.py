"""How covariance assumptions change ordinary kriging weights.

Run from _media. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    sites = np.array([0.0, 1.0, 3.0])
    values = np.array([1.0, 3.0, 2.0])
    models = [(1, "Exponential", "#176b9b"), (2, "Gaussian", "#c65422")]
    solutions = []
    for power, name, color in models:
        covariance = 2.0 ** -(np.abs(sites[:, None] - sites) ** power)
        cross = 2.0 ** -(np.abs(sites - 2) ** power)
        system = np.block(
            [[covariance, np.ones((3, 1))], [np.ones((1, 3)), np.zeros((1, 1))]]
        )
        solution = np.linalg.solve(system, np.r_[cross, 1])
        weights, multiplier = solution[:3], solution[3]
        assert np.all(np.linalg.eigvalsh(covariance) > 0)
        assert np.isclose(weights.sum(), 1)
        assert np.allclose(system @ solution, np.r_[cross, 1])
        variance = 1 - 2 * weights @ cross + weights @ covariance @ weights
        assert np.isclose(variance, 1 - weights @ cross - multiplier)
        solutions.append((weights, weights @ values, variance))
    assert np.allclose(solutions[0][0], np.array([2, 13, 14]) / 29)
    assert np.allclose(solutions[1][0], np.array([-736, 2663, 2272]) / 4199)
    assert np.isclose(solutions[1][1], 11797 / 4199)
    assert np.isclose(solutions[1][2], 2115 / 4199)

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.6, 4.7), layout="constrained")
    positions = np.arange(3)
    for index, ((power, name, color), (weights, prediction, variance)) in enumerate(zip(models, solutions)):
        offset = (index - 0.5) * 0.34
        bars = ax.bar(positions + offset, weights, width=0.32, color=color,
                      label=name, zorder=3)
        for bar, weight in zip(bars, weights):
            ax.annotate(f"{weight:.3f}", (bar.get_x() + bar.get_width() / 2, weight),
                        xytext=(0, 6 if weight >= 0 else -6), textcoords="offset points",
                        ha="center", va="bottom" if weight >= 0 else "top", fontsize=11)
    ax.axhline(0, color="black", linewidth=1)
    ax.set(xticks=positions, xticklabels=["s = 0, z = 1", "s = 1, z = 3", "s = 3, z = 2"],
           ylabel="Ordinary kriging weight", ylim=(-0.33, 0.85),
           title="Same data and target s = 2; different covariance assumptions")
    ax.legend(frameon=False, loc="upper left")
    ax.grid(axis="y", alpha=0.18, zorder=0)
    fig.supxlabel(
        r"Exponential $C(h)=2^{-|h|}$: prediction 2.379, error variance 0.621"
        "\n" + r"Gaussian $C(h)=2^{-h^2}$: prediction 2.809, error variance 0.504"
        "\nWeights sum to one in both models; the Gaussian model uses a negative weight.",
        fontsize=10,
    )
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
