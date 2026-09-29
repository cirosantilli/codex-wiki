"""Toy Bernoulli losses and premium loading; no measured data.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Writes the matching PNG basename into the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, (loss, price) = plt.subplots(1, 2, figsize=(9.6, 4.5))
    blue, orange = "#2166ac", "#c96c18"
    loss.bar([0, 1], [0.9, 0.1], color=blue, width=0.55)
    loss.set_xticks([0, 1], ["£0", "£1,000"])
    loss.set_ylim(0, 1.04)
    loss.set_ylabel("Probability")
    loss.set_xlabel("Actual covered loss")
    loss.yaxis.set_major_formatter(PercentFormatter(1))
    loss.set_title("What can actually happen", pad=14)
    for x, p in enumerate([0.9, 0.1]):
        loss.text(x, p + 0.025, f"{p:.0%}", ha="center", weight="bold")
    price.barh([0], [100], color=blue, height=0.38)
    price.barh([0], [20], left=[100], color=orange, height=0.38)
    price.text(50, 0, "£100\nexpected cost", color="white", ha="center", va="center")
    price.annotate("£20 loading", xy=(110, 0.20), xytext=(95, 0.60),
                   ha="center", arrowprops={"arrowstyle": "->", "color": orange},
                   color=orange, weight="bold")
    price.axvline(120, color="#333333", ymax=0.66, linestyle="--")
    price.text(120, -0.34, "£120 premium", ha="center", weight="bold")
    price.set_yticks([])
    price.set_xlim(0, 150)
    price.set_ylim(-0.60, 0.85)
    price.set_xticks([0, 50, 100, 150], ["£0", "£50", "£100", "£150"])
    price.set_xlabel("Expected cost × 1.20")
    price.set_title("How the price is built", pad=14)
    price.spines["left"].set_visible(False)
    fig.suptitle("Toy policy: a 10% chance of a £1,000 claim", fontsize=16, weight="bold")
    fig.text(0.5, 0.025, "Invented assumptions, exact calculation • Expected cost is not a realized claim", ha="center", fontsize=11)
    fig.tight_layout(rect=(0, 0.07, 1, 0.92), w_pad=2.5)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
