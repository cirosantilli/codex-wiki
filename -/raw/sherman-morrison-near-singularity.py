"""Inverse amplification near a singular rank-one update; PNG to CWD."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def amplification(delta):
    """Use positive delta = 1 + t explicitly to avoid subtractive cancellation."""
    u = np.array([1., 2.])
    v = np.array([3., -1.])
    correction = np.outer(u, v)
    t = delta - 1
    matrix = np.eye(2) + t * correction
    inverse = np.eye(2) - (t / delta) * correction
    norm = np.linalg.norm(inverse, 2)
    condition = np.linalg.norm(matrix, 2) * norm
    return norm, condition


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    delta = np.logspace(-4, 0, 501)
    data = np.array([amplification(value) for value in delta])
    fig, (left, right) = plt.subplots(1, 2, figsize=(12, 5.3), dpi=100)
    left.loglog(delta, data[:, 0], color="#246bce", linewidth=2.5,
                label=r"$\|B^{-1}\|_2$")
    left.loglog(delta, 1 / delta, color="#69747d", linestyle="--", linewidth=1.8,
                label=r"Direction $u$ gives lower bound $1/\delta$")
    right.loglog(delta, data[:, 1], color="#bf5520", linewidth=2.5,
                 label=r"$\kappa_2(B)=\|B\|_2\|B^{-1}\|_2$")
    marked_norm, marked_condition = amplification(0.01)
    for ax, value, text, color in [
        (left, marked_norm, "δ = 0.01, t = −0.99\nInverse norm ≈ 700.179", "#246bce"),
        (right, marked_condition, "δ = 0.01, t = −0.99\nCondition number ≈ 4902.500", "#bf5520"),
    ]:
        ax.scatter([0.01], [value], color=color, zorder=5)
        ax.annotate(text, (0.01, value), xytext=(0.025, value * 6),
                    textcoords="data", fontsize=10,
                    arrowprops={"arrowstyle": "-", "color": color},
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
        ax.set(xlabel=r"Nonzero denominator $\delta=1+t$", xlim=(1e-4, 1))
        ax.grid(which="both", alpha=0.16)
        ax.legend(loc="lower left", frameon=False, fontsize=10)
    left.set_ylabel("Maximum inverse amplification")
    right.set_ylabel("Spectral condition number")
    left.set_title("The inverse amplifies inputs", weight="bold", fontsize=13)
    right.set_title("The updated system becomes sensitive", weight="bold", fontsize=13)
    fig.suptitle("Approaching δ = 0 makes the rank-one update singular",
                 fontsize=16, weight="bold", y=0.975)
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.15, top=0.80, wspace=0.28)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
