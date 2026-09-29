"""Original simulated charge-state readings; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; emits oil-drop-charge-jump-series.png in the working directory.
No historical measurements or SI elementary-charge estimate are used.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    means = np.array([2.03, 2.96, 5.02, 3.99])
    offsets = np.array([-0.18, 0.10, -0.04, 0.22, -0.12, 0.02])
    assert np.isclose(offsets.sum(), 0)
    sigma = 0.08  # Stipulated uncertainty of each state mean, not an estimate.
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (ax, jumps) = plt.subplots(2, 1, figsize=(9, 6.4),
                                   gridspec_kw={"height_ratios": [2.4, 1.2]})
    colors = ["#1864ab", "#087f5b", "#9c36b5", "#d9480f"]
    for j, (mean, color) in enumerate(zip(means, colors)):
        x = np.arange(1, 7) + 7 * j
        readings = mean + np.roll(offsets, j)
        assert np.isclose(readings.mean(), mean)
        ax.plot(x, readings, "o-", color=color, ms=4, lw=0.7)
        ax.hlines(mean, x[0] - 0.3, x[-1] + 0.3, color=color, lw=1.8)
        ax.fill_between([x[0] - 0.3, x[-1] + 0.3], mean - sigma,
                        mean + sigma, color=color, alpha=0.12)
        ax.text(x.mean(), mean + 0.38, f"State {j + 1}: mean {mean:.2f}",
                ha="center", color=color, fontsize=10)
    ax.set(xlim=(0, 29), ylim=(1.5, 5.8), ylabel=r"Inferred $|q|/Q_*$",
           xlabel="Acquisition order (not elapsed time)")
    ax.grid(axis="y", alpha=0.18)
    ax.text(0.02, 0.96, "Chosen noisy readings; shaded mean ± 0.08",
            transform=ax.transAxes, va="top", fontsize=10)
    delta = np.diff(means)
    jumps.axhline(0, color="0.6", lw=0.8)
    jumps.errorbar([1, 2, 3], delta, yerr=np.sqrt(2) * sigma, fmt="o",
                   color="#343a40", capsize=5)
    for j, d in enumerate(delta):
        jumps.text(j + 1, d + 0.25, f"{d:+.2f}", ha="center")
    jumps.set(xticks=[1, 2, 3], xticklabels=["1 → 2", "2 → 3", "3 → 4"],
              xlim=(0.5, 3.5), ylim=(-1.5, 2.75),
              ylabel=r"Change in $|q|/Q_*$", xlabel="Transition between state means")
    jumps.grid(axis="y", alpha=0.18)
    fig.suptitle("Simulated charge states of one oil drop", fontsize=16)
    fig.text(0.5, 0.015, r"Arbitrary reference charge $Q_*$; no historical data or numerical estimate of $e$",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.04, 1, 0.95), h_pad=1.5)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
