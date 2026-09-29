"""Draw repeated-prisoners-dilemma-discount-threshold.png in the current directory.

Original diagram; tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../repeated-prisoners-dilemma-discount-threshold.py
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def main():
    delta = np.linspace(0, .95, 381)
    fig, ax = plt.subplots(figsize=(8.4, 5.3), facecolor="white")
    ax.set_facecolor("white")
    ax.axvspan(.5, .95, color="#e9f4ee", zorder=0)
    ax.plot(delta, np.full_like(delta, 3), color="#2166a5", lw=2.6,
            label="Cooperate forever: 3")
    ax.plot(delta, 5 - 4 * delta, color="#b34e14", lw=2.6,
            label=r"First defection, then D forever: $5-4\delta$")
    ax.axvline(.5, color="#56616e", linestyle=":", lw=1.5)
    ax.scatter([.5], [3], s=65, color="#202933", zorder=5)
    ax.annotate("Threshold: δ = 1/2\nPayoffs tie at 3", (.5, 3), xytext=(.54, 4.25),
                fontsize=12, arrowprops={"arrowstyle": "->", "color": "#202933"})
    ax.text(.22, 1.62, "Defection gains", ha="center", fontsize=12, color="#b34e14")
    ax.text(.73, 1.25, "Cooperation is a best response", ha="center", fontsize=11,
            color="#226044")
    ax.set(xlim=(0, .95), ylim=(1, 5.25), xlabel=r"Common discount factor $\delta$",
           ylabel="Normalized payoff to one player")
    ax.set_xticks([0, .25, .5, .75, .95], ["0", "0.25", "0.50", "0.75", "0.95"])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#e0e4e9", lw=.7)
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.18), frameon=False, fontsize=11)
    fig.suptitle("When does future cooperation outweigh today's temptation?", fontsize=16, y=.97)
    fig.text(.5, .045, "Infinite repetition · perfect public monitoring · both use grim trigger · δ < 1",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.10, right=.97, bottom=.29, top=.86)
    fig.savefig("repeated-prisoners-dilemma-discount-threshold.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
