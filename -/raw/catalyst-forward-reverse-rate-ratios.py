"""Generate catalyst-forward-reverse-rate-ratios.png in the current directory.

Original fixed-temperature toy model, with common Eyring prefactor factored out.
Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7. Run from _media.
"""

import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    rt = 8.314462618 * 300
    # Values are J/mol; normalized rates k/nu are dimensionless.
    barriers = np.array([[80000, 100000], [50000, 70000]], dtype=float)
    logs = -barriers / (rt * math.log(10))
    speedup = math.exp(30000 / rt)
    equilibrium = math.exp(20000 / rt)
    colors = ("#b64928", "#176d9c")
    fig, (ax, ratio_ax) = plt.subplots(1, 2, figsize=(8, 4.6), dpi=120,
                                     gridspec_kw={"width_ratios": [1.35, 1]})
    x = np.arange(2)
    for row, color, label, offset in zip(
        logs, colors, ("Without catalyst", "With catalyst"), (-0.18, 0.18)
    ):
        bars = ax.bar(x + offset, row, width=0.34, color=color, label=label)
        for bar, value in zip(bars, row):
            ax.text(bar.get_x() + bar.get_width() / 2, value - 0.5,
                    f"{value:.2f}", ha="center", va="top", fontsize=10)
    ax.set_xticks(x, ("Forward", "Reverse"))
    ax.set(ylim=(-20, 0), ylabel=r"$\log_{10}(k/\nu)$",
           title="Faster in both directions")
    ax.grid(axis="y", alpha=0.18)
    ax.set_axisbelow(True)
    ax.text(0.5, -0.30, f"Each direction × {speedup / 1e5:.3f} × 10⁵",
            transform=ax.transAxes, ha="center", fontsize=10)
    ratio_logs = logs[:, 0] - logs[:, 1]
    bars = ratio_ax.bar(x, ratio_logs, color=colors, width=0.55)
    for bar, value in zip(bars, ratio_logs):
        ratio_ax.text(bar.get_x() + bar.get_width() / 2, value + 0.09,
                      f"{value:.3f}", ha="center", fontsize=10)
    ratio_ax.set_xticks(x, ("Without\ncatalyst", "With\ncatalyst"))
    ratio_ax.set(ylim=(0, 4.5), ylabel=r"$\log_{10}(k_f/k_r)$",
                 title="Same equilibrium ratio")
    ratio_ax.grid(axis="y", alpha=0.18)
    ratio_ax.set_axisbelow(True)
    ratio_ax.text(0.5, -0.30, f"Both routes: K = {equilibrium:.2f}",
                  transform=ratio_ax.transAxes, ha="center", fontsize=10)
    for panel in (ax, ratio_ax):
        panel.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Rate comparisons at 300 K", weight="bold", y=0.96)
    fig.text(0.5, 0.88, "Chosen free-energy barriers; common ν = kBT/h",
             ha="center", fontsize=10)
    fig.legend(handles=ax.get_legend_handles_labels()[0],
               labels=ax.get_legend_handles_labels()[1], loc="lower center",
               ncol=2, frameon=False, bbox_to_anchor=(0.5, 0.015), fontsize=10)
    fig.subplots_adjust(left=0.09, right=0.98, wspace=0.43, top=0.74, bottom=0.29)
    fig.savefig("catalyst-forward-reverse-rate-ratios.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
