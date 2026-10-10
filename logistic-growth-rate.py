"""Plot the logistic rate; tested with Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from the desired output directory; writes logistic-growth-rate.png.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    capacity, rate = 1000.0, 0.4
    abundance = np.linspace(0.0, 1400.0, 1001)
    growth = rate * abundance * (1.0 - abundance / capacity)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (ax, phase) = plt.subplots(
        2, 1, figsize=(8.0, 4.8), dpi=120, sharex=True,
        gridspec_kw={"height_ratios": [3.6, 1]}, constrained_layout=True,
        facecolor="white")
    ax.plot(abundance, growth, lw=2.8, color="#2176a5")
    ax.fill_between(abundance, 0, growth, where=growth >= 0,
                    color="#258568", alpha=0.12)
    ax.fill_between(abundance, 0, growth, where=growth < 0,
                    color="#b74a25", alpha=0.12)
    ax.axhline(0, color="#555555", lw=1.2)
    ax.plot([500, 500], [0, 100], color="#777777", ls=":", lw=1.2)
    ax.scatter([500], [100], color="#2176a5", s=45, zorder=5)
    ax.annotate("maximum: 100 individuals/day\nat N = K/2 = 500",
                xy=(500, 100), xytext=(700, 140), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#2176a5"},
                color="#2176a5")
    ax.text(390, 23, "positive rate: population increases", ha="center",
            color="#21634e", fontsize=10)
    ax.annotate("negative rate:\npopulation decreases", xy=(1250, -125),
                xytext=(1200, 60), ha="center", color="#993c1c", fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#993c1c"})
    ax.scatter([0], [0], s=55, facecolors="white", edgecolors="#333333",
               linewidths=1.5, zorder=5, clip_on=False)
    ax.scatter([1000], [0], s=55, color="#333333", zorder=5)
    ax.set(title="The total rate peaks halfway to capacity\n"
                 r"$N'=0.4N(1-N/1000)$",
           ylabel="total rate N' (individuals/day)", ylim=(-240, 175),
           yticks=[-200, -100, 0, 100])
    ax.grid(alpha=0.14)
    ax.tick_params(axis="x", bottom=False)

    phase.axhline(0, color="#555555", lw=1.2)
    for left, right in [(110, 340), (530, 820), (1350, 1090)]:
        phase.annotate("", xy=(right, 0), xytext=(left, 0),
                       arrowprops={"arrowstyle": "-|>", "lw": 2.3,
                                   "color": "#258568" if right > left else "#b74a25"})
    phase.scatter([0], [0], s=62, facecolors="white", edgecolors="#333333",
                  linewidths=1.5, zorder=5, clip_on=False)
    phase.scatter([1000], [0], s=62, color="#333333", zorder=5)
    phase.text(20, 0.43, "0: unstable", fontsize=10, color="#333333")
    phase.text(1000, 0.43, "K: stable", ha="center", fontsize=10, color="#333333")
    phase.set(xlabel="population N (individuals)", ylabel="phase line",
              xlim=(0, 1400), ylim=(-0.6, 1.0), yticks=[],
              xticks=np.arange(0, 1401, 200))
    phase.spines["left"].set_visible(False)
    for panel in (ax, phase):
        panel.set_facecolor("white")
    fig.savefig(Path.cwd() / "logistic-growth-rate.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
