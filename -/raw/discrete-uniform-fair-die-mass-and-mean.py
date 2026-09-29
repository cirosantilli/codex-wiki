"""Draw the exact stipulated fair-die law; run from _media to save the PNG."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.8, 4.5), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.12, right=0.97, bottom=0.23, top=0.79)
    fig.suptitle("Ideal fair die: equal masses, mean between faces", fontsize=16, y=0.96)
    fig.text(0.5, 0.865, "Model assumption: each face has probability 1/6", ha="center")
    for value in range(1, 7):
        color = "#007d80" if value % 2 == 0 else "#3269a8"
        ax.vlines(value, 0, 1 / 6, color=color, linewidth=4)
        ax.plot(value, 1 / 6, "o", color=color, markersize=10)
        ax.text(value, 1 / 6 + 0.012, "1/6", ha="center", color=color)
    ax.axvline(3.5, color="#a94c00", linestyle="--", linewidth=2)
    ax.text(3.5, 0.235, "Mean = 7/2", ha="center", color="#a94c00",
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.set(xlim=(0.5, 6.5), ylim=(0, 0.26), xlabel="Face value x",
           ylabel="Probability P(X = x)", xticks=range(1, 7))
    ax.yaxis.set_major_locator(FixedLocator([0, 1 / 12, 1 / 6]))
    ax.yaxis.set_major_formatter(FixedFormatter(["0", "1/12", "1/6"]))
    ax.grid(axis="y", alpha=0.18)
    fig.text(0.5, 0.085, "Teal faces: P(even) = 3/6 = 1/2     |     Variance = 35/12",
             ha="center", fontsize=12)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
