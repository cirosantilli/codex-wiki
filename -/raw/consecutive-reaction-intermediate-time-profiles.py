"""Exact illustrative consecutive kinetics; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.

Run from _media; writes consecutive-reaction-intermediate-time-profiles.png there.
All parameters are chosen, not measured. No numerical ODE solver is needed.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    k = 0.20  # s^-1; both steps
    a0 = 1.00  # mmol L^-1
    t = np.linspace(0.0, 30.0, 601)
    a = a0 * np.exp(-k * t)
    intermediate = a0 * k * t * np.exp(-k * t)
    product = a0 - a - intermediate
    direct = a0 - a
    assert np.allclose(a + intermediate + product, a0)
    assert np.all(product >= 0.0)

    fig = plt.figure(figsize=(9.4, 5.4), layout="constrained")
    gs = fig.add_gridspec(2, 1, height_ratios=[0.8, 3.6])
    network = fig.add_subplot(gs[0])
    network.set_axis_off()
    network.set_xlim(0, 1)
    network.set_ylim(0, 1)
    for x, label, colour in [(0.13, "A", "#2864a5"),
                             (0.49, "I", "#b66015"),
                             (0.85, "P", "#24764d")]:
        network.text(x, 0.42, label, fontsize=20, color=colour,
                     ha="center", va="center",
                     bbox={"boxstyle": "round,pad=0.35", "fc": "white", "ec": colour})
    for left, right in [(0.20, 0.42), (0.56, 0.78)]:
        network.annotate("", (right, 0.42), (left, 0.42),
                         arrowprops={"arrowstyle": "->", "lw": 2, "color": "#444444"})
        network.text((left + right) / 2, 0.85, r"$k=0.20\ \mathrm{s^{-1}}$",
                     ha="center", va="center", fontsize=11)

    ax = fig.add_subplot(gs[1])
    ax.plot(t, a, color="#2864a5", lw=2.4, label="A: same in both models")
    ax.plot(t, intermediate, color="#b66015", lw=2.6, label="I: consecutive model")
    ax.plot(t, product, color="#24764d", lw=2.6, label="P: consecutive model")
    ax.plot(t, direct, color="#777777", lw=1.9, linestyle="--", label="P: direct A → P model")
    peak_t = 1.0 / k
    peak_i = a0 / np.e
    ax.plot(peak_t, peak_i, "o", color="#b66015", ms=6)
    ax.annotate("I peaks at 5.00 s\n[A] = [I] = 0.367879",
                xy=(peak_t, peak_i), xytext=(10.0, 0.40),
                arrowprops={"arrowstyle": "->", "color": "#b66015"},
                color="#84460e", fontsize=10)
    ax.set(xlim=(0, 30), ylim=(0, 1.05), xlabel="Time (s)",
           ylabel=r"Concentration ($\mathrm{mmol\,L^{-1}}$)")
    ax.grid(alpha=0.18)
    ax.legend(loc="center right", bbox_to_anchor=(1, 0.29), frameon=True,
              facecolor="white", framealpha=0.96, fontsize=10)
    fig.suptitle("An intermediate creates a delay in product formation", fontsize=15)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
