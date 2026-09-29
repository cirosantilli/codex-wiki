"""Plot original polynomial cancellation examples; Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Run from _media to write the matching PNG there.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 3, figsize=(10, 6), layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("Polynomial cancellation is signed overlap", fontsize=17)
    examples = [
        ("Haar h: one vanishing moment", [0, .5, 1], [1, -1],
         ["0", "−1/4", "−1/4"]),
        ("Second difference η: two vanishing moments", [0, 1, 2, 3],
         np.array([1, -2, 1]) / np.sqrt(6), ["0", "0", "2/√6"]),
    ]
    for row, (name, edges, heights, labels) in enumerate(examples):
        for power in range(3):
            ax = axes[row, power]
            ax.set_facecolor("white")
            for left, right, height in zip(edges[:-1], edges[1:], heights):
                x = np.linspace(left, right, 150)
                y = height * x**power
                ax.fill_between(x, 0, y, color="#237aaf" if height > 0
                                else "#d36a31", alpha=.30)
                ax.plot(x, y, color="#237aaf" if height > 0 else "#d36a31",
                        linewidth=2)
                ax.plot([left, left], [0, y[0]], color=".55", linewidth=.6)
                ax.plot([right, right], [0, y[-1]], color=".55", linewidth=.6)
            ax.axhline(0, color=".3", linewidth=.8)
            ax.set_xlim(-.07, edges[-1] + .07)
            ax.set_xticks(edges)
            ax.set_xlabel("u")
            ax.set_title(["Test polynomial 1", "Test polynomial u",
                          "Test polynomial u²"][power])
            ax.text(.04, .94, "Signed integral = " + labels[power],
                    transform=ax.transAxes, va="top", fontsize=11,
                    bbox={"facecolor": "white", "alpha": .95, "edgecolor": "none"})
            low, high = ax.get_ylim()
            ax.set_ylim(low, high + .25 * (high - low))
            if power == 0:
                ax.set_ylabel("h(u) × test" if row == 0 else "η(u) × test")
        axes[row, 1].text(.5, -.28, name, transform=axes[row, 1].transAxes,
                          ha="center", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
