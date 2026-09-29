"""Render the overlap interpretation of interval-indicator convolution to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def triangle(x):
    return np.maximum(0, np.minimum(1, x) - np.maximum(0, x - 1))


def main():
    shifts = [0.5, 1.0, 1.5]
    assert np.allclose(triangle(np.array(shifts)), [0.5, 1.0, 0.5])
    grid = np.linspace(-0.5, 2.5, 6001)
    assert np.isclose(np.trapezoid(triangle(grid), grid), 1.0)
    assert np.isclose(np.trapezoid(grid * triangle(grid), grid), 1.0)
    assert np.isclose(np.trapezoid((grid - 1) ** 2 * triangle(grid), grid), 1 / 6)
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig = plt.figure(figsize=(10.8, 6.3), dpi=120, facecolor="white")
    layout = fig.add_gridspec(2, 3, height_ratios=[1, 1.3])
    for i, x in enumerate(shifts):
        ax = fig.add_subplot(layout[0, i])
        ax.fill_between([0, 1], 0, 1, color="#2477aa", alpha=0.13)
        ax.fill_between([x - 1, x], 0, 1, color="#d77c21", alpha=0.13)
        left, right = max(0, x - 1), min(1, x)
        ax.fill_between([left, right], 0, 1, color="#22976d", alpha=0.45)
        ax.plot([-0.7, 0, 0, 1, 1, 2.1], [0, 0, 1, 1, 0, 0],
                color="#2477aa", lw=2, label=r"$q(y)$")
        ax.plot([-0.7, x - 1, x - 1, x, x, 2.1], [0, 0, 1, 1, 0, 0],
                color="#d77c21", lw=2, linestyle="--", label=r"$q(x-y)$")
        ax.text((left + right) / 2, 0.47, f"Overlap\nlength {right - left:g}",
                ha="center", va="center", color="#10593d", fontsize=11)
        ax.set_title(f"At x = {x:g}, integrate the overlap")
        ax.set_xlabel("Integration variable y")
        ax.set_xlim(-0.7, 2.1)
        ax.set_ylim(-0.08, 1.27)
        ax.set_yticks([0, 1])
        ax.set_xticks([-0.5, 0, 0.5, 1, 1.5, 2])
        ax.spines[["top", "right"]].set_visible(False)
        if i == 0:
            fig.legend(*ax.get_legend_handles_labels(), loc="upper center", ncol=2,
                       bbox_to_anchor=(0.5, 1.0), frameon=False, fontsize=10)
    ax = fig.add_subplot(layout[1, :])
    values = triangle(grid)
    ax.plot(grid, values, color="#1c8460", lw=3)
    ax.fill_between(grid, 0, values, color="#1c8460", alpha=0.12)
    for x in shifts:
        height = float(triangle(np.asarray(x)))
        ax.vlines(x, 0, height, color="#718a80", linestyle=":")
        ax.scatter(x, height, s=65, color="#1c8460", edgecolor="white", zorder=4)
    ax.set_title("All overlap lengths form a triangular function with total integral 1")
    ax.set_xlabel("Output argument x")
    ax.set_ylabel(r"$(q*q)(x)$")
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.04, 1.16)
    ax.set_yticks([0, 0.5, 1])
    ax.grid(axis="y", color="#e5e9eb")
    ax.spines[["top", "right"]].set_visible(False)
    fig.subplots_adjust(left=0.075, right=0.975, top=0.89, bottom=0.085, hspace=0.58, wspace=0.28)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
