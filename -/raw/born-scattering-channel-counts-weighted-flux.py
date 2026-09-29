"""Velocity weights and accepted counts for the article's chosen scattering model.

Python 3.14, NumPy 2.3, Matplotlib 3.10. Run from _media; output is the
script's basename with a .png suffix in CWD. Counts are expectations, not data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (flux, counts) = plt.subplots(1, 2, figsize=(10, 4.4), layout="constrained")
    positions = np.arange(2)
    width = 0.34
    raw = np.array([9 / 25, 32 / 25])
    weights = np.array([1, 1 / 2])
    probability = raw * weights
    bars_raw = flux.bar(positions - width / 2, raw, width, color="#adb8c9", label=r"Raw $|c_i|^2$")
    bars_flux = flux.bar(positions + width / 2, probability, width, color="#264d8b", label=r"Flux $(v_i/v_1)|c_i|^2$")
    flux.bar_label(bars_raw, labels=["9/25", "32/25"], padding=3)
    flux.bar_label(bars_flux, labels=["9/25", "16/25"], padding=3)
    flux.set(xticks=positions, xticklabels=["Channel 1\nvelocity v", "Channel 2\nvelocity v/2"],
             ylim=(0, 1.8), ylabel="Dimensionless weight", title="A slower wave needs a velocity weight")
    flux.axhline(1, color="0.7", ls=":", lw=1)
    flux.legend(loc="upper left", fontsize=9)
    flux.text(0.5, 0.83, r"$9/25+16/25=1$", transform=flux.transAxes, ha="center")

    all_counts = 1600 * probability
    accepted = all_counts * np.array([19 / 64, 1 / 4])
    bars_all = counts.bar(positions - width / 2, all_counts, width, color="#adb8c9", label="All directions")
    bars_accepted = counts.bar(positions + width / 2, accepted, width, color="#ad6a12", label="Inside 60° cone")
    counts.bar_label(bars_all, labels=[f"{x:.0f}" for x in all_counts], padding=3)
    counts.bar_label(bars_accepted, labels=[f"{x:.0f}" for x in accepted], padding=3)
    counts.set(xticks=positions, xticklabels=["Channel 1", "Channel 2"], ylim=(0, 1420),
               ylabel="Expected detections / 1600 incident events", title="Angular acceptance selects the counts")
    counts.legend(loc="upper left", fontsize=9)
    counts.text(0.5, 0.81, "427 accepted; 1173 outside cone", transform=counts.transAxes, ha="center", fontsize=10)
    for ax in (flux, counts):
        ax.set_axisbelow(True)
        ax.grid(axis="y", alpha=0.2)
    fig.suptitle("Chosen scattering model: conserve flux, then apply detector acceptance", fontsize=14)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
