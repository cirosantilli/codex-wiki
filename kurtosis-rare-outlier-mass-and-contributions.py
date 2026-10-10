"""Exact three-point laws, not sampled data. Python 3.14, matplotlib 3.10.7, numpy 2.3.5."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 6.3), layout="constrained", facecolor="white")
    x = np.array([-1.0, 0.0, 1.0])
    for row, q in enumerate((0.25, 0.01)):
        p = np.array([q / 2, 1 - q, q / 2])
        z = x / np.sqrt(q)
        contributions = p * z**4
        left, right = axes[row]
        left.bar(x, p, width=0.3, color=["#bc4d2f", "#2b6f9c", "#bc4d2f"])
        left.set(xlim=(-1.6, 1.6), ylim=(0, 1.13), xticks=x, xlabel="Original outcome x", ylabel="Probability mass p(x)")
        left.set_title(f"q = {q:g}: variance = {q:g}")
        for point, mass in zip(x, p):
            left.text(point, mass + 0.03, f"{mass:g}", ha="center")
        right.bar(z, contributions, width=0.55 if q == 0.25 else 1.1, color="#bc4d2f")
        right.set(xlim=(-1.35 / np.sqrt(q), 1.35 / np.sqrt(q)), ylim=(0, contributions.max() * 1.35), xticks=z, xlabel=r"Standard score $z=x/\sqrt{q}$", ylabel=r"Contribution $p(x)z^4$")
        right.set_title(f"Kurtosis = sum of contributions = {1 / q:g}")
        for point, contribution in zip(z, contributions):
            right.text(point, contribution + contributions.max() * 0.06, f"{contribution:g}", ha="center")
    fig.suptitle("Rare outcomes: little probability, large fourth-moment contribution", fontsize=14)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
