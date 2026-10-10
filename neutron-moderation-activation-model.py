"""Original stipulated models, not measured historical data.

Python 3.14, numpy 2.3.5, matplotlib 3.10.7. Run from _media.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def decrement(mass_ratio):
    if mass_ratio == 1:
        return 1.0
    alpha = ((mass_ratio - 1) / (mass_ratio + 1)) ** 2
    return 1 + alpha * np.log(alpha) / (1 - alpha)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.3), dpi=100, facecolor="white")
    fig.suptitle("Moderation and activation: two distinct models", fontsize=17, weight="bold", y=0.98)
    fig.text(0.5, 0.905, "Chosen examples • no measured historical data • no isotope-specific parameters",
             ha="center", fontsize=11)
    ax = axes[0]
    n = np.linspace(0, 125, 501)
    for ratio, label, color in [(1, "Mass ratio 1 (hydrogen model)", "#1764a0"),
                                (12, "Mass ratio 12 (carbon model)", "#bd651b")]:
        ax.semilogy(n, 1e6 * np.exp(-decrement(ratio) * n), label=label, color=color, lw=2)
    ax.axhline(0.025, color="#555555", ls=":", label="Chosen 0.025 eV stopping scale")
    ax.set(xlabel="Number of elastic collisions, n", ylabel="Geometric-mean energy (eV)",
           ylim=(0.01, 2e6), xlim=(0, 125), title="Mean log-energy loss; stationary free targets")
    ax.legend(loc="upper right", fontsize=9, framealpha=1)
    ax.grid(alpha=0.2)
    ax.text(0.04, 0.06, "Curves stop at the chosen scale:\nthermal motion then matters.",
            transform=ax.transAxes, fontsize=9, bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    # Mask below the chosen scale: free stationary targets cease to be adequate.
    for line in ax.lines[:2]:
        line.set_ydata(np.where(line.get_ydata() >= 0.025, line.get_ydata(), np.nan))
    ax = axes[1]
    time = np.linspace(0, 12, 601)
    lam, end = np.log(2) / 2, 4.0
    for rate, color in [(120, "#1764a0"), (40, "#bd651b")]:
        activity = rate * (-np.expm1(-lam * np.minimum(time, end))) * np.exp(-lam * np.maximum(time-end, 0))
        ax.plot(time, activity, lw=2, color=color, label=f"Production R = {rate}/min")
    ax.axhline(120, ls=":", color="#555555", label="Saturation activity for R = 120/min")
    ax.axvline(end, color="#555555", ls="--")
    ax.text(4.18, 108, "Irradiation\nends", fontsize=9)
    ax.scatter([4, 6], [90, 45], s=25, color="#1764a0", zorder=4)
    ax.set(xlabel="Time from irradiation start (min)", ylabel="Expected activity (decays/min)",
           xlim=(0, 12), ylim=(0, 130), title="Production plus decay; chosen half-life 2 min")
    ax.legend(loc="upper right", bbox_to_anchor=(1, 0.78), fontsize=9, framealpha=1)
    ax.grid(alpha=0.2)
    ax.text(0.53, 0.08, "Activity is not the\nrecorded count rate.", transform=ax.transAxes, fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.12, top=0.8, wspace=0.29)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
