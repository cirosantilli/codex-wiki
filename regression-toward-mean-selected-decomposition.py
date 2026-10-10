"""Synthetic repeated signal plus fresh errors, with analytic selected means.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; writes this script's basename with a .png suffix to the CWD.
"""
from math import erfc, exp, pi, sqrt
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def main():
    rng = np.random.default_rng(271828)
    latent = sqrt(0.6) * rng.standard_normal(60000)
    first_error, second_error = sqrt(0.4) * rng.standard_normal((2, 60000))
    x, y = latent + first_error, latent + second_error
    selected = np.flatnonzero(x > 1)
    shown = rng.choice(selected, size=40, replace=False)
    tail = 0.5 * erfc(1 / sqrt(2))
    first_mean = exp(-0.5) / sqrt(2 * pi) / tail
    signal_mean, error_mean = 0.6 * first_mean, 0.4 * first_mean
    fig, (ax, parts) = plt.subplots(1, 2, figsize=(9.2, 4.8), layout="constrained")
    fig.set_facecolor("white")
    fig.suptitle("Synthetic repeated-measurement model: X = T + ε₁, Y = T + ε₂\n"
                 "Generated values and model expectations; no actual measurements", fontsize=13)
    for i in shown:
        farther = abs(y[i]) > abs(x[i])
        ax.plot([0, 1], [x[i], y[i]], "o-", markersize=3, linewidth=1,
                color="#c87920" if farther else "#54818b", alpha=0.7)
    ax.axhline(1, color="#999999", linestyle=":", linewidth=1)
    ax.axhline(0, color="#bbbbbb", linewidth=0.7)
    ax.set(xticks=[0, 1], xticklabels=["First X", "Second Y"], xlim=(-0.25, 1.25),
           ylabel="Standardized measurement", title="40 generated units selected by X > 1")
    ax.legend(handles=[Line2D([0], [0], color="#54818b", label="Closer to zero"),
                       Line2D([0], [0], color="#c87920", label="Farther from zero")],
              loc="upper right", fontsize=9)
    positions = np.arange(2)
    parts.bar(positions, [signal_mean, signal_mean], width=0.55,
              color="#377ba8", label="Expected persistent signal T")
    parts.bar(positions, [error_mean, 0], bottom=[signal_mean, signal_mean],
              width=0.55, color="#e8ab58", label="Expected error after selection")
    sample_means = [float(x[selected].mean()), float(y[selected].mean())]
    parts.scatter(positions, sample_means, color="#222222", s=35, zorder=4,
                  label=f"Generated group means (n = {len(selected):,})")
    parts.text(0, first_mean + 0.045, f"Model total {first_mean:.3f}", ha="center", fontsize=10)
    parts.text(1, signal_mean + 0.045, f"Model total {signal_mean:.3f}", ha="center", fontsize=10)
    parts.text(0, signal_mean + error_mean / 2, f"ε₁: {error_mean:.3f}", ha="center", fontsize=11)
    for j in positions:
        parts.text(j, signal_mean / 2, f"T: {signal_mean:.3f}", color="white", ha="center", fontsize=11)
    parts.text(1, 1.3, "Fresh error:\nE[ε₂ | X > 1] = 0", ha="center", fontsize=10)
    parts.axhline(0, color="#bbbbbb", linewidth=0.7)
    parts.set(xticks=positions, xticklabels=["First X", "Second Y"], ylim=(0, 2.05),
              ylabel="Selected-group mean", title="Same selected population, unchanged T")
    parts.legend(loc="upper center", fontsize=8, framealpha=0.95)
    for panel in (ax, parts):
        panel.set_facecolor("white")
        panel.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
