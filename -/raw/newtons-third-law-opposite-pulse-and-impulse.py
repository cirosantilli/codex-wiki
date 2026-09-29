"""Constructed triangular interaction pulse, not measured data.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    t = np.linspace(0, 1.15, 1151)
    f = np.where(t <= 0.5, 8 * t, np.where(t <= 1, 8 * (1 - t), 0))
    impulse = np.where(t <= 0.5, 4 * t**2,
                       np.where(t <= 1, 2 - 4 * (1 - t)**2, 2))
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.6), dpi=110, facecolor="white")
    blue, orange = "#1765a3", "#be4b13"
    series = [(-f, f), (-impulse, impulse), (-f, f / 2)]
    labels = [("Force (N)", "Opposite forces"),
              ("Cumulative impulse (N s)", "Opposite momentum changes"),
              (r"Acceleration (m/s$^2$)", "Unequal accelerations")]
    for ax, (a, b), (ylabel, title) in zip(axes, series, labels):
        ax.axhline(0, color="#89939c", lw=0.8)
        ax.axvline(1, color="#89939c", ls=":", lw=1)
        ax.plot(t, a, color=blue, lw=2.5, label="A: 1 kg")
        ax.plot(t, b, color=orange, lw=2.5, label="B: 2 kg")
        ax.set(xlim=(0, 1.15), xlabel="Time (s)", ylabel=ylabel, title=title)
        ax.set_xticks([0, 0.5, 1])
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].fill_between(t, 0, -f, color=blue, alpha=0.09)
    axes[0].fill_between(t, 0, f, color=orange, alpha=0.09)
    axes[0].set_ylim(-4.85, 4.85)
    axes[0].text(0.54, 4.1, "+4 N", color=orange)
    axes[0].text(0.54, -4.4, "−4 N", color=blue)
    axes[1].set_ylim(-2.6, 2.6)
    axes[1].text(0.71, 2.14, "+2 N s", color=orange)
    axes[1].text(0.71, -2.35, "−2 N s", color=blue)
    axes[2].set_ylim(-4.85, 4.85)
    axes[2].text(0.54, 2.2, r"+2 m/s$^2$", color=orange)
    axes[2].text(0.54, -4.4, r"−4 m/s$^2$", color=blue)
    axes[2].legend(loc="upper right", frameon=False, fontsize=10)
    fig.suptitle("Constructed interaction pulse: equal forces do not mean equal accelerations", fontsize=15)
    fig.text(0.5, 0.055, "No other horizontal forces: ΔpA + ΔpB = 0; final ΔvA = −2 m/s, ΔvB = +1 m/s.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.012, "Original prescribed model • not a measured trace • pulse ends at 1 s", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.985, bottom=0.23, top=0.81, wspace=0.42)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
