"""Draw explicitly interpolated quartiles and observation-based whiskers.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../boxplot-quartile-fences-toy.py
Outputs boxplot-quartile-fences-toy.png in the current directory.
Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    data = np.array([1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 20])
    q1, median, q3 = np.quantile(data, [0.25, 0.5, 0.75], method="linear")
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    inside = data[(data >= lower) & (data <= upper)]
    outside = data[(data < lower) | (data > upper)]
    assert (q1, median, q3, iqr, lower, upper) == (2.75, 4.5, 6.25, 3.5, -2.5, 11.5)
    assert (inside.min(), inside.max()) == (1, 8)
    assert outside.tolist() == [20]
    stats = {"q1": q1, "med": median, "q3": q3,
             "whislo": inside.min(), "whishi": inside.max(), "fliers": outside}
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(9.2, 4.3), facecolor="white")
    fig.subplots_adjust(left=0.045, right=0.985, bottom=0.25, top=0.73)
    fig.suptitle("Box, whiskers and fences have different jobs", fontsize=15, y=0.96)
    fig.text(0.5, 0.86, "Invented values; type-7 quartiles; whiskers use the inclusive 1.5-IQR rule",
             ha="center", fontsize=10)
    ax.set_facecolor("white")
    ax.bxp([stats], positions=[1.1], widths=0.38, orientation="horizontal",
           patch_artist=True, manage_ticks=False,
           boxprops={"facecolor": "#b4d6e4", "edgecolor": "#234f71", "linewidth": 1.5},
           medianprops={"color": "#ad581b", "linewidth": 2},
           whiskerprops={"color": "#234f71", "linewidth": 1.5},
           capprops={"color": "#234f71", "linewidth": 1.5},
           flierprops={"marker": "o", "markerfacecolor": "white",
                       "markeredgecolor": "#ad581b", "markersize": 7})
    for fence, label in [(lower, "Lower fence\n−2.5"), (upper, "Upper fence\n11.5")]:
        ax.axvline(fence, color="#777777", linestyle="--", linewidth=1)
        ax.text(fence, 1.62, label, ha="center", va="top", fontsize=10)
    for x, label, text_x, text_y in [(q1, "Q₁ = 2.75", 2.0, 1.58),
                                   (median, "Median = 4.5", 4.5, 1.92),
                                   (q3, "Q₃ = 6.25", 7.0, 1.58)]:
        ax.annotate(label, xy=(x, 1.3), xytext=(text_x, text_y), ha="center",
                    fontsize=10, arrowprops={"arrowstyle": "-", "color": "#234f71"})
    ax.annotate("Whisker at 1", xy=(1, 1.1), xytext=(0, 0.65), ha="center",
                fontsize=10, arrowprops={"arrowstyle": "-", "color": "#234f71"})
    ax.annotate("Whisker at 8", xy=(8, 1.1), xytext=(9, 0.65), ha="center",
                fontsize=10, arrowprops={"arrowstyle": "-", "color": "#234f71"})
    ax.text(20, 1.48, "20: beyond fence\nInvestigate before\ncalling it an error", ha="center", fontsize=9)
    seen = {}
    for value in data:
        stack = seen.get(value, 0)
        ax.scatter(value, 0.12 + 0.13 * stack, s=32, color="#234f71", zorder=3)
        seen[value] = stack + 1
    ax.text(-3.6, 0.12, "Raw\nvalues", ha="right", va="center", fontsize=9)
    ax.set_xlim(-4.8, 23.4)
    ax.set_ylim(-0.08, 2.03)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xticks([-2.5, 0, 4, 8, 11.5, 16, 20])
    ax.set_xlabel("Toy value (unitless)")
    fig.text(0.5, 0.105, "Box width: IQR = 6.25 − 2.75 = 3.5", ha="center", fontsize=11)
    fig.text(0.5, 0.045, "Fences: 2.75 − 1.5 × 3.5 = −2.5     and     6.25 + 1.5 × 3.5 = 11.5",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
