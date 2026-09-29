"""Draw a hand-chosen arrival path; this is a schematic, not empirical data.

Run from _media. Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    arrivals = np.array([0.35, 0.70, 1.25, 1.80, 2.15, 2.55, 2.85, 3.05, 3.70])
    horizon, rate = 4.0, 2.0
    blue = "#245a91"
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, (events, count) = plt.subplots(
        2, 1, figsize=(10, 5.5), sharex=True,
        gridspec_kw={"height_ratios": [1, 3]}, layout="constrained")
    fig.suptitle("Arrivals and the counting path", fontsize=18)
    events.set_title("Synthetic times chosen for illustration — not measured data", fontsize=12)
    events.hlines(0, 0, horizon, color="#888888", linewidth=1)
    events.vlines(arrivals, -0.10, 0.10, color=blue, linewidth=2)
    events.scatter(arrivals, np.zeros_like(arrivals), color=blue, s=35, zorder=3)
    for i, t in enumerate(arrivals):
        events.text(t, 0.17, f"$T_{{{i+1}}}$", ha="center", fontsize=11)
    events.annotate("", (arrivals[1], -0.26), (arrivals[0], -0.26),
                    arrowprops={"arrowstyle": "<->", "color": blue})
    events.text((arrivals[0]+arrivals[1])/2, -0.42, "$W_2$", ha="center", color=blue)
    events.set_ylim(-0.60, 0.46)
    events.set_yticks([])
    events.spines["left"].set_visible(False)
    events.spines["bottom"].set_visible(False)
    events.tick_params(axis="x", bottom=False)
    x = np.r_[0.0, arrivals, horizon]
    y = np.r_[0, np.arange(1, len(arrivals)+1), len(arrivals)]
    count.step(x, y, where="post", color=blue, linewidth=2.1, label="Synthetic count $N_t$")
    count.scatter(arrivals, np.arange(1, len(arrivals)+1), color=blue, s=25, zorder=4)
    count.scatter(arrivals, np.arange(len(arrivals)), facecolor="white", edgecolor=blue,
                  s=25, zorder=4)
    count.plot([0, horizon], [0, rate*horizon], "--", color="#ad6429", linewidth=2,
               label=r"Exact mean $\mathbb{E}[N_t]=2t$")
    count.axvline(2, color="#aaaaaa", linestyle=":", linewidth=1)
    count.annotate("$N_2=4$", (2, 4), (1.10, 5.2),
                   arrowprops={"arrowstyle": "->", "color": blue}, color=blue)
    count.text(3.76, 9.27, "$N_4=9$", ha="right", color=blue)
    count.set(xlim=(0, horizon), ylim=(-0.2, 10.5), xlabel="Time (minutes)",
              ylabel="Cumulative arrivals", xticks=np.arange(5), yticks=np.arange(0, 11, 2))
    count.grid(axis="y", alpha=0.18)
    count.legend(loc="upper left", frameon=False)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
