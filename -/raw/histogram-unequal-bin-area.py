"""Draw count versus density heights for one explicitly invented dataset.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../histogram-unequal-bin-area.py
Outputs histogram-unequal-bin-area.png in the current directory.
Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    data = np.array([1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 20])
    edges = np.array([0, 2, 4, 8, 22])
    counts, _ = np.histogram(data, bins=edges)
    widths = np.diff(edges)
    density = counts / (len(data) * widths)
    assert counts.tolist() == [1, 3, 6, 2]
    assert np.isclose(np.dot(density, widths), 1)
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    colors = ["#8bbfce", "#f0bf70", "#e59850", "#9db8d7"]
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.4), facecolor="white")
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.24, top=0.75, wspace=0.25)
    fig.suptitle("Same toy values, same unequal bins", fontsize=15, y=0.96)
    fig.text(0.5, 0.86, "Invented values: 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 20",
             ha="center", fontsize=10)
    titles = ["Count heights: area is misleading", "Density heights: area is proportion"]
    for ax, heights, title in zip(axes, (counts, density), titles):
        ax.set_facecolor("white")
        ax.bar(edges[:-1], heights, width=widths, align="edge", color=colors,
               edgecolor="#354553", linewidth=1)
        ax.set_xlim(-0.5, 22.5)
        ax.set_xticks(edges)
        ax.set_xlabel("Toy value (unitless); bin edges shown")
        ax.set_title(title, fontsize=11, pad=12)
        ax.grid(axis="y", color="#e5e5e5", linewidth=0.6)
        ax.set_axisbelow(True)
    axes[0].set_ylabel("Count per bin")
    axes[0].set_ylim(0, 7.3)
    axes[0].set_yticks([0, 2, 4, 6])
    for left, width, count in zip(edges[:-1], widths, counts):
        axes[0].text(left + width / 2, count + 0.15, str(count), ha="center")
    axes[0].text(15, 1, "2 observations\nwidth 14\narea 28", ha="center", va="center", fontsize=9)
    axes[1].set_ylabel("Density per unit value")
    axes[1].set_ylim(0, 0.165)
    axes[1].set_yticks([0, 0.05, 0.10, 0.15])
    labels = ["1/24", "1/8", "1/8", "1/84"]
    for left, width, height, label in zip(edges[:-1], widths, density, labels):
        axes[1].text(left + width / 2, height + 0.005, label, ha="center", fontsize=10)
    axes[1].text(15, 0.048, "2 observations\nwidth 14\narea 1/6", ha="center", fontsize=9)
    axes[1].annotate("", xy=(18, density[-1]), xytext=(18, 0.043),
                     arrowprops={"arrowstyle": "-", "color": "#354553"})
    fig.text(0.5, 0.11, "Bin counts: 1, 3, 6, 2     |     Widths: 2, 2, 4, 14",
             ha="center", fontsize=10)
    fig.text(0.5, 0.055, "Density areas: 1/12 + 1/4 + 1/2 + 1/6 = 1",
             ha="center", fontsize=11, color="#234f71")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
