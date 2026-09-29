"""Compare exact partial sums and first-order Cesaro means of two series."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    n = np.arange(36)
    series = [("1 − 1 + 1 − 1 + …", (-1)**n),
              ("1 − 2 + 3 − 4 + …", (-1)**n*(n+1))]
    fig, axes = plt.subplots(2, 2, figsize=(12, 7.4), dpi=110)
    fig.patch.set_facecolor("white")
    fig.suptitle("Averaging partial sums: one success and one failure", fontsize=19, y=0.98)
    for row, (name, terms) in enumerate(series):
        sums = terms.cumsum()
        means = sums.cumsum()/(n+1)
        axes[row, 0].plot(n, sums, color="#6c7480", linewidth=1, marker="o", markersize=4)
        axes[row, 1].plot(n, means, color="#216da2", linewidth=1, marker="o", markersize=4)
        axes[row, 0].set_title(name+"\npartial sums", fontsize=14)
        axes[row, 1].set_title("first-order Cesàro means", fontsize=14)
        axes[row, 1].axhline(0.5, color="#d07e20", linestyle="--", linewidth=1.5,
                           label="limit ½" if row == 0 else "even-index limit ½")
        if row == 1:
            axes[row, 1].axhline(0, color="#369075", linestyle=":", linewidth=1.7,
                               label="odd-index value 0")
        axes[row, 1].legend(fontsize=10, loc="upper right")
        axes[row, 1].set_ylim(-0.08, 1.08)
        for ax in axes[row]:
            ax.set_xlabel("last included index N (first term has index 0)", fontsize=10)
            ax.grid(alpha=0.22)
            ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.025, "The second series has no first-order Cesàro sum: its means retain two distinct subsequential limits.", ha="center", fontsize=12)
    fig.subplots_adjust(left=0.055, right=0.98, top=0.87, bottom=0.11, hspace=0.60, wspace=0.20)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
