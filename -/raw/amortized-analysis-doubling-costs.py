"""Plot exact append costs; run from _media with Python 3.14 and matplotlib 3.10."""

from pathlib import Path

import matplotlib.pyplot as plt


def main():
    capacity = 1
    costs = []
    totals = []
    for size in range(64):
        copied = 0
        if size == capacity:
            copied = size
            capacity *= 2
        costs.append(1 + copied)
        totals.append(sum(costs))

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (single, total) = plt.subplots(1, 2, figsize=(11.2, 4.8), dpi=110)
    fig.set_facecolor("white")
    positions = list(range(1, 65))
    single.vlines(positions, 0, costs, color="#236b8e", linewidth=1.3)
    single.scatter(positions, costs, color="#236b8e", s=15, zorder=3)
    single.axhline(3, color="#a94c19", linestyle="--", linewidth=1.4,
                   label="Uniform amortized upper bound: 3")
    single.annotate("Append 33: copy 32 + write 1", xy=(33, 33),
                    xytext=(5, 36), fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": "#333333"})
    single.set(title="One costly append at each resize", xlabel="Append number i",
               ylabel="Actual cost cᵢ", xlim=(0, 65), ylim=(0, 41))
    single.legend(loc="upper right", bbox_to_anchor=(1.02, 0.79), fontsize=9,
                  frameon=False)

    total.plot(positions, totals, color="#236b8e", linewidth=2.1,
               label="Actual cumulative work T(n)")
    total.plot(positions, [3 * n for n in positions], color="#a94c19",
               linestyle="--", linewidth=1.5, label="3n upper bound")
    total.scatter([64], [127], color="#236b8e", s=32, zorder=4)
    total.annotate("64 appends: 127 units", xy=(64, 127), xytext=(24, 105),
                   fontsize=10, arrowprops={"arrowstyle": "->", "color": "#333333"})
    total.set(title="Every prefix has linear total cost", xlabel="Number of appends n",
              ylabel="Cumulative cost", xlim=(0, 68), ylim=(0, 205))
    total.legend(loc="upper left", fontsize=9, frameon=False)
    for ax in (single, total):
        ax.set_facecolor("white")
        ax.grid(axis="y", color="#e5e5e5", linewidth=0.7)
        ax.set_axisbelow(True)
        ax.set_xticks([1, 16, 32, 48, 64])
    fig.suptitle("Doubling an initially empty array: capacity 1, no reserve", fontsize=15)
    fig.text(0.5, 0.025, "Cost = 1 new write + number of existing entries copied; allocation is excluded.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.065, right=0.98, top=0.83, bottom=0.16, wspace=0.27)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
