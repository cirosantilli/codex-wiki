"""Illustrative free-energy paths, not experimental data.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media: MPLBACKEND=Agg python ../catalysis-barriers-and-net-free-energy.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def profile(x, peak):
    """Two cosine ramps with flat endpoints and a prescribed maximum."""
    left = peak * (1 - np.cos(np.pi * np.clip((x - 0.10) / 0.40, 0, 1))) / 2
    right = peak + (-3 - peak) * (
        1 - np.cos(np.pi * np.clip((x - 0.50) / 0.40, 0, 1))
    ) / 2
    return np.where(x <= 0.50, left, right)


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.5, 5), dpi=120)
    fig.subplots_adjust(left=0.11, right=0.96, bottom=0.26, top=0.83)
    x = np.linspace(0, 1, 1001)
    for peak, color, label in [(12, "#b64b27", "Uncatalysed"), (7, "#176b9b", "Catalysed")]:
        y = profile(x, peak)
        assert y[0] == 0 and y[-1] == -3 and y.max() == peak
        ax.plot(x, y, lw=3, color=color, label=label)
        ax.plot([0.50], [peak], "o", color=color)
        ax.text(0.52, peak + 0.25, f"Chosen maximum: {peak}", color=color)
    ax.hlines([0, -3], 0, 1.05, color="#999999", linestyle=":", lw=1)
    ax.text(0.03, -1.2, "A + C", ha="left")
    ax.text(0.97, -4.25, "B + C", ha="right")
    ax.annotate("", xy=(1.045, -3), xytext=(1.045, 0),
                arrowprops={"arrowstyle": "<->", "color": "#333333", "lw": 1.5})
    ax.text(1.07, -1.5, r"$\Delta_r G^\circ=-3$", va="center", fontsize=11)
    ax.set(xlim=(-0.015, 1.27), ylim=(-5, 14),
           ylabel=r"Standard molar Gibbs free energy / kJ mol$^{-1}$",
           xlabel="Reaction coordinate (not time)")
    ax.set_xticks([])
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper left", frameon=False, fontsize=11)
    fig.suptitle("Illustrative barriers: different paths, identical endpoints", fontsize=15)
    fig.text(0.5, 0.90, "C is included at both endpoints and regenerated; chosen values, not measurements",
             ha="center", fontsize=10)
    fig.text(0.5, 0.12,
             "Forward barriers: 12 → 7       Reverse barriers: 15 → 10  (kJ/mol)",
             ha="center", fontsize=12)
    fig.text(0.5, 0.06, "Both climbs fall by 5; the net free-energy change stays −3 kJ/mol.",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
