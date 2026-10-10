"""Four toy cycles folded onto phase, with flux and magnitude views.

All data are synthetic; no physical source is fitted or measured.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
From _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../light-curve-phase-folding-magnitudes.py
Writes only light-curve-phase-folding-magnitudes.png to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

PERIOD = 3.0  # days
EPOCH = 1.0  # days
DEPTH = 0.01
HALF_DURATION = 2 / 24  # days
HALF_FLAT = 1.4 / 24  # days
SIGMA = 0.0006
COLORS = ["#156c97", "#ba4c40", "#338653", "#8b5aac"]


def folded_phase(t, period=PERIOD):
    """Return phase in [0, 1), using a floor also for negative times."""
    cycles = (np.asarray(t) - EPOCH) / period
    return cycles - np.floor(cycles)


def centred_phase(t, period=PERIOD):
    """Wrap phase at mid-transit for an unclipped dip."""
    return (folded_phase(t, period) + 0.5) % 1 - 0.5


def model(t):
    distance = np.abs(centred_phase(t) * PERIOD)
    fraction = np.clip((HALF_DURATION - distance) / (HALF_DURATION - HALF_FLAT), 0, 1)
    return 1 - DEPTH * fraction


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(29107)
    fig = plt.figure(figsize=(9.0, 8.0), facecolor="white")
    grid = fig.add_gridspec(3, 2, left=0.10, right=0.97, top=0.86, bottom=0.09, hspace=0.64, wspace=0.31)
    time_ax = fig.add_subplot(grid[0, :])
    good_ax = fig.add_subplot(grid[1, 0])
    wrong_ax = fig.add_subplot(grid[1, 1], sharey=good_ax)
    flux_ax = fig.add_subplot(grid[2, 0])
    mag_ax = fig.add_subplot(grid[2, 1])
    fig.suptitle("One repeating dip, several ways to see it", fontsize=16, y=0.97)
    fig.text(0.5, 0.92, "Synthetic toy data • period 3 days • epoch 1 day • depth 1%", ha="center", color="#555555")
    dense_t = np.linspace(0, 12, 6001)
    time_ax.plot(dense_t, model(dense_t), color="#555555", lw=1.3)
    for cycle, color in enumerate(COLORS):
        # More samples near each dip keep the instructional figure legible.
        local = np.unique(np.r_[np.linspace(-0.90, 1.90, 47), np.linspace(-0.13, 0.13, 31)])
        t = EPOCH + cycle * PERIOD + local
        f = model(t) + rng.normal(0, SIGMA, t.size)
        time_ax.scatter(t, f, color=color, s=8, alpha=0.65, label=f"cycle {cycle + 1}")
        good_ax.scatter(centred_phase(t), f, color=color, s=10, alpha=0.65)
        wrong_ax.scatter(centred_phase(t, 3.03), f, color=color, s=10, alpha=0.65)
    time_ax.set_title("A. Four dips in chronological order", loc="left", fontsize=11)
    time_ax.set_xlabel("Time (days)")
    time_ax.set_ylabel("Relative brightness")
    time_ax.set_xlim(0, 12)
    time_ax.legend(ncol=4, fontsize=8, loc="lower right", framealpha=1)
    good_ax.set_title("B. Correct fold: P = 3.00 days", loc="left", fontsize=11)
    wrong_ax.set_title("C. Wrong fold: P = 3.03 days", loc="left", fontsize=11)
    phase = np.linspace(-0.06, 0.06, 601)
    f_model = model(EPOCH + PERIOD * phase)
    good_ax.plot(phase, f_model, color="#222222", lw=1.5)
    for ax in (good_ax, wrong_ax, flux_ax, mag_ax):
        ax.set_xlim(-0.06, 0.06)
        ax.set_xlabel("Phase (cycles from mid-transit)")
    good_ax.set_ylabel("Relative brightness")
    good_ax.set_ylim(0.9875, 1.0025)
    time_ax.set_ylim(0.9875, 1.0025)
    flux_ax.set_title("D. Model in brightness units", loc="left", fontsize=11)
    flux_ax.plot(phase, f_model, color="#156c97", lw=2)
    flux_ax.set_ylabel("F / F₀")
    flux_ax.set_ylim(0.988, 1.002)
    flux_ax.text(0.5, 0.48, "minimum = 0.990", transform=flux_ax.transAxes, ha="center", fontsize=9)
    delta_m = -2.5 * np.log10(f_model)
    mag_ax.set_title("E. Same model in magnitude units", loc="left", fontsize=11)
    mag_ax.plot(phase, delta_m, color="#ba4c40", lw=2)
    mag_ax.set_ylabel("Δm (magnitudes)")
    mag_ax.set_ylim(0.013, -0.002)  # larger magnitudes lower: fainter below
    mag_ax.text(0.5, 0.48, "maximum Δm = +0.010912", transform=mag_ax.transAxes, ha="center", fontsize=9)
    mag_ax.text(0.96, 0.08, "Fainter ↓", transform=mag_ax.transAxes, ha="right", fontsize=9)
    for ax in (time_ax, good_ax, wrong_ax, flux_ax, mag_ax):
        ax.set_facecolor("white")
        ax.grid(alpha=0.16)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=135, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
