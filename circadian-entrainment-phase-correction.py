"""Illustrate a local, stipulated daily phase-correction map.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


TAU = 23.5
ENVIRONMENT_PERIOD = 24.0
GAIN = 0.4


def delay(offset):
    """Positive delay, in hours; this is not a measured phase-response curve."""
    return ENVIRONMENT_PERIOD - TAU - GAIN * offset


def phase_trace(initial=-3.0, cycles=10):
    phase = [initial]
    for _ in range(cycles):
        phase.append(phase[-1] + TAU - ENVIRONMENT_PERIOD + delay(phase[-1]))
    return np.array(phase)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 1, figsize=(9, 6.4), dpi=100,
                             sharex=True, facecolor="white",
                             gridspec_kw={"height_ratios": [1.6, 1]})
    fig.subplots_adjust(left=0.15, right=0.96, bottom=0.16, top=0.81, hspace=0.2)
    n = np.arange(11)
    phase = phase_trace()
    uncoupled = -3.0 + (TAU - ENVIRONMENT_PERIOD) * n
    axes[0].plot(n, phase, "o-", color="#087e8b", lw=2.2,
                 label="Daily phase correction")
    axes[0].plot(n, uncoupled, "s--", color="#b94b32", lw=1.6,
                 label="No correction (free running)")
    axes[0].axhline(0, color="#666666", ls=":", lw=1.4)
    axes[0].set(ylabel="Onset offset xₙ (h)\nrelative to lights-off", ylim=(-8.6, 1.0))
    axes[0].text(4.8, 0.45, "Stable phase relationship: x* = 0", fontsize=10)
    axes[0].text(4.4, -4.0, "Negative offset = earlier onset", fontsize=10)
    axes[0].legend(loc="lower left", frameon=False, fontsize=10)
    axes[1].plot(n, delay(phase), "o-", color="#087e8b", lw=2.2)
    axes[1].axhline(0.5, color="#666666", ls=":", lw=1.4)
    axes[1].text(4.0, 1.45, "0.5 h delay balances τ − T = −0.5 h", fontsize=10)
    axes[1].set(ylabel="Imposed daily\ndelay D(xₙ) (h)", xlabel="Environmental cycle n",
                ylim=(0.3, 1.85), xlim=(-0.2, 10.3))
    axes[1].set_xticks(np.arange(0, 11))
    for ax in axes:
        ax.grid(axis="y", color="#eeeeee")
        ax.set_axisbelow(True)
    fig.suptitle("Entrainment balances drift and restores phase", y=0.97, fontsize=15)
    fig.text(0.5, 0.91, "Stipulated local map: τ = 23.5 h, T = 24 h, D(x) = 0.5 h − 0.4x",
             ha="center", fontsize=11)
    fig.text(0.5, 0.86, "xₙ₊₁ = xₙ + (τ − T) + D(xₙ) = 0.6xₙ; start at x₀ = −3 h",
             ha="center", fontsize=11)
    fig.text(0.5, 0.04, "Original conceptual model; no fitted biological gain or recorded activity.",
             ha="center", fontsize=10, color="#555555")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
