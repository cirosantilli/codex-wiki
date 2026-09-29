"""Same probability constraint, different divergence/distance minimizers."""

from math import sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, 0.25, 701)
    q = np.column_stack((x, 0.5 - 2 * x, 0.5 + x))
    with np.errstate(divide="ignore", invalid="ignore"):
        divergence = np.sum(np.where(q > 0, q * np.log(3 * q), 0), axis=1)
    squared_distance = np.sum((q - 1 / 3) ** 2, axis=1)
    t = (1 + sqrt(13)) / 2
    entropy_min_x = 1 / (1 + t + t * t)
    least_squares_x = 1 / 12
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.7), dpi=120, facecolor="white")
    for ax, values, minimum, color, title, ylabel in (
        (axes[0], divergence, entropy_min_x, "#285f8a", "Relative entropy", "D(q ∥ p), nats"),
        (axes[1], squared_distance, least_squares_x, "#bd7624", "Least squares", "Squared Euclidean distance in probability coordinates"),
    ):
        ax.plot(x, values, color=color, linewidth=2.2)
        ax.axvline(minimum, linestyle="--", color=color, linewidth=1.2)
        if ax is axes[0]:
            star = np.array([minimum, 0.5 - 2 * minimum, 0.5 + minimum])
            value = np.sum(star * np.log(3 * star))
        else:
            star = np.array([minimum, 0.5 - 2 * minimum, 0.5 + minimum])
            value = np.sum((star - 1 / 3) ** 2)
            assert abs(value - 1 / 8) < 1e-12
        ax.plot(minimum, value, "o", color=color, markersize=7)
        ax.annotate(f"Minimum at x ≈ {minimum:.6f}", xy=(minimum, value),
            xytext=(0.02, max(values) * 0.84), fontsize=10,
            arrowprops={"arrowstyle": "->", "color": color})
        ax.set(xlim=(-0.006, 0.256), xlabel="x = q(−1)", ylabel=ylabel, title=title)
        ax.grid(alpha=0.2)
    fig.suptitle("The objective matters even with the same mean constraint", fontsize=15)
    fig.text(0.5, 0.027, "q = (x, 1/2 − 2x, 1/2 + x); reference p = (1/3, 1/3, 1/3). Original calculated example.",
        ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.075, 1, 0.94))
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
