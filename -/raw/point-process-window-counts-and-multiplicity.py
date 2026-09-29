"""Draw a point measure and its cumulative count; Python 3.14 / Matplotlib 3.10.7.

Run from _media; the opaque PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    locations = np.array([0.4, 1.1, 1.8, 2.4, 3.0])
    multiplicities = np.array([1, 2, 1, 1, 1])
    fig, (pattern, count) = plt.subplots(
        2, 1, figsize=(9, 5.8), sharex=True,
        gridspec_kw={"height_ratios": [1, 1.4]}, layout="constrained",
    )
    fig.suptitle("A point measure counts repeated locations", fontsize=17)
    for ax in (pattern, count):
        ax.axvspan(0, 1.5, color="#dcecf8", zorder=0)
        ax.axvspan(1.5, 3, color="#fff0d5", zorder=0)
        ax.axvline(1.5, color="#666666", linestyle="--", linewidth=1)
        ax.axvline(3, color="#666666", linestyle="--", linewidth=1)
        ax.set_xlim(-0.15, 3.35)
        ax.spines[["top", "right"]].set_visible(False)
    pattern.axhline(0, color="#555555", linewidth=1)
    for x, m in zip(locations, multiplicities):
        pattern.scatter([x] * int(m), 0.12 * np.arange(m), s=75,
                        color="#234e70", zorder=4)
        pattern.text(x, -0.14, f"{x:g}", ha="center")
    pattern.text(0.75, 0.49, r"$A=[0,1.5)$: count 3", ha="center", color="#234e70")
    pattern.text(2.25, 0.49, r"$B=[1.5,3)$: count 2", ha="center", color="#8b5700")
    pattern.annotate("multiplicity 2", xy=(1.1, 0.13), xytext=(1.5, 0.31),
                     ha="center", fontsize=11,
                     arrowprops={"arrowstyle": "->", "color": "#555555"})
    pattern.text(3.0, 0.38, "outside\n$A\\cup B$", ha="center", fontsize=11)
    pattern.set_ylim(-0.3, 0.7)
    pattern.set_yticks([])
    pattern.spines[["left", "bottom"]].set_visible(False)
    pattern.tick_params(axis="x", bottom=False, labelbottom=False)

    steps_x = np.r_[0, locations, 3.35]
    steps_y = np.r_[0, np.cumsum(multiplicities), multiplicities.sum()]
    count.step(steps_x, steps_y, where="post", linewidth=2.5, color="#234e70")
    previous = np.r_[0, np.cumsum(multiplicities)[:-1]]
    cumulative = np.cumsum(multiplicities)
    count.scatter(locations, previous, facecolors="white", edgecolors="#234e70", zorder=4)
    count.scatter(locations, cumulative, color="#234e70", zorder=5)
    count.set_ylim(-0.25, 6.7)
    count.set_yticks(range(7))
    count.set_xticks([0, 0.4, 1.1, 1.5, 1.8, 2.4, 3, 3.3])
    count.set_xlabel("Location / time t")
    count.set_ylabel(r"$N(t)=\Pi((0,t])$")
    count.grid(axis="y", alpha=0.22)
    count.text(0.05, 6.28, "The double atom makes a jump of 2; the atom at t = 3 is included.",
               fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
