"""Draw equal masses on unequal gaps and the equal-width sampling construction."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import FixedLocator, FixedFormatter


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (mass, sampling) = plt.subplots(2, 1, figsize=(9.2, 6.6), dpi=100,
                                       gridspec_kw={"height_ratios": [1.5, 1]},
                                       facecolor="white")
    fig.subplots_adjust(left=0.11, right=0.965, bottom=0.15, top=0.79, hspace=0.64)
    fig.suptitle("Equal probabilities do not require equal value gaps", fontsize=16, y=0.97)
    fig.text(0.5, 0.9, "Stipulated model: choose one of {1, 2, 4, 8} with equal chances",
             ha="center")
    values = [1, 2, 4, 8]
    colors = ["#3269a8", "#007d80", "#7955a1", "#ba5c22"]
    for value, color in zip(values, colors):
        mass.vlines(value, 0, 0.25, color=color, linewidth=4)
        mass.plot(value, 0.25, "o", color=color, markersize=10)
        mass.text(value, 0.27, "1/4", color=color, ha="center")
    mass.axvline(15 / 4, color="#555555", linestyle="--", linewidth=1.8)
    mass.text(15 / 4, 0.345, "Mean = 15/4", color="#555555", ha="center",
              bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    mass.set(xlim=(0.4, 8.6), ylim=(0, 0.39), xticks=range(1, 9),
             xlabel="Output value x (gaps: 1, 2, 4)", ylabel="P(X = x)")
    mass.yaxis.set_major_locator(FixedLocator([0, 1 / 8, 1 / 4]))
    mass.yaxis.set_major_formatter(FixedFormatter(["0", "1/8", "1/4"]))
    mass.grid(axis="y", alpha=0.18)
    sampling.set_title("An ideal uniform U on [0, 1) selects an equal-width interval",
                       fontsize=13, pad=15)
    for j, (value, color) in enumerate(zip(values, colors)):
        sampling.add_patch(Rectangle((j / 4, 0.15), 1 / 4, 0.7,
                                     facecolor=color, alpha=0.16, edgecolor=color, linewidth=2))
        sampling.text((j + 0.5) / 4, 0.58, f"Output {value}", color=color, ha="center", weight="bold")
        sampling.text((j + 0.5) / 4, 0.3, "Probability 1/4", ha="center", fontsize=11)
    sampling.set(xlim=(0, 1), ylim=(0, 1), xlabel="Sampling probability coordinate u",
                 yticks=[], xticks=[0, 0.25, 0.5, 0.75, 1],
                 xticklabels=["0", "1/4", "1/2", "3/4", "1"])
    sampling.spines["left"].set_visible(False)
    fig.text(0.5, 0.045, "Mean = 15/4     |     Variance = 115/16     |     P(X ≥ 4) = 1/2",
             ha="center", fontsize=12)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
