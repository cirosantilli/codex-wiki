"""Compare a prior-averaged likelihood and its peak; Python 3.14.4.

Run from _media; writes its matching PNG to the current directory.
All curves and bars are calculated from stipulated models, with no data fit
except the explicitly labeled likelihood maximum.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    p = np.linspace(0, 1, 2001)
    likelihood = p**8 * (1-p)**2
    average = float(Fraction(1, 495))
    null = float(Fraction(1, 1024))
    fixed = float(Fraction(7, 10)**8 * Fraction(3, 10)**2)
    peak = float(Fraction(4, 5)**8 * Fraction(1, 5)**2)
    fig, (left, right) = plt.subplots(
        1, 2, figsize=(10.4, 5.1), dpi=120, facecolor="white",
        gridspec_kw={"width_ratios": [1.25, 1]},
    )
    fig.suptitle("Eight heads + two tails: averaging is different from maximizing",
                 fontsize=15, y=0.98)
    left.fill_between(p, likelihood * 1000, color="#b9d6e8", alpha=0.65,
                      label="Area = uniform-prior average × 1000")
    left.plot(p, likelihood * 1000, color="#176eaa", lw=2.4,
              label="L(p) = p⁸(1 − p)²")
    left.axhline(average * 1000, color="#008573", lw=2.3,
                 label="Average mᵤ = 1/495 ≈ 0.00202020")
    left.scatter([0.5, 0.7, 0.8], np.array([null, fixed, peak])*1000,
                 c=["#69757c", "#9851a1", "#ce5900"], s=42, zorder=5)
    left.annotate("Null p = 0.5", xy=(0.5, null*1000), xytext=(0.14, 0.45),
                  fontsize=10, arrowprops={"arrowstyle": "->", "color": "#69757c"})
    left.annotate("Peak at p = 0.8", xy=(0.8, peak*1000), xytext=(0.38, 7.5),
                  fontsize=10, color="#a54600",
                  arrowprops={"arrowstyle": "->", "color": "#a54600"})
    left.set(xlim=(0, 1), ylim=(0, 8.3), xlabel="Heads probability p",
             ylabel="Ordered-sequence likelihood × 1000",
             title="Uniform prior density = 1 on [0, 1]")
    left.legend(loc="upper left", bbox_to_anchor=(-0.015, 0.84),
                fontsize=8.5, framealpha=1)
    values = np.array([average, fixed, peak]) / null
    bars = right.bar([0, 1, 2], values,
                      color=["#008573", "#9851a1", "#ce5900"], width=0.62)
    right.axhline(1, color="#69757c", linestyle="--", lw=1.2)
    right.bar_label(bars, labels=[f"{v:.5f}" for v in values], padding=5, fontsize=11)
    right.set(ylim=(0, 8.3), xticks=[0, 1, 2],
              xticklabels=["Uniform\naverage", "Fixed\np = 0.7", "Fitted peak\np̂ = 0.8"],
              ylabel="Ratio to null likelihood L(0.5) = 2⁻¹⁰",
              title="Same null, three different comparisons")
    right.text(0.5, 0.95, "Prespecified alternatives        Maximum",
               transform=right.transAxes, ha="center", fontsize=9, color="#53616b")
    for ax in (left, right):
        ax.grid(axis="y", color="#e4e9ec")
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.035,
             "One stipulated ordered sequence; all probabilities calculated. The fitted peak is not the uniform model's evidence.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.07, right=0.985, bottom=0.18,
                        top=0.83, wspace=0.29)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
