"""Plot logistic growth; tested with Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from the desired output directory; writes logistic-growth-trajectories.png.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    capacity, rate = 1000.0, 0.4
    t = np.linspace(0.0, 20.0, 1001)

    def population(time, initial):
        return capacity / (1.0 + (capacity / initial - 1.0) * np.exp(-rate * time))

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.0, 4.8), dpi=120,
                           constrained_layout=True, facecolor="white")
    colors = {100: "#2176a5", 500: "#258568", 1200: "#b74a25"}
    for initial, color in colors.items():
        ax.plot(t, population(t, initial), color=color, lw=2.7,
                label=rf"$N_0={initial}$")
        ax.scatter([0], [initial], color=color, s=32, zorder=5, clip_on=False)
    ax.axhline(capacity, color="#665078", ls="--", lw=1.6)
    ax.text(19.6, 1027, r"carrying capacity $K=1000$", ha="right",
            color="#665078", fontsize=10)
    ax.axhline(0, color="#555555", ls="--", lw=1.4)
    ax.text(0.5, 28, r"equilibrium $N=0$", color="#555555", fontsize=10)
    ax.axhline(capacity / 2, color="#bbbbbb", ls=":", lw=1.2)
    ax.text(19.6, 519, r"$K/2=500$", ha="right", color="#777777", fontsize=10)

    inflection_time = np.log(9.0) / rate
    ax.plot([inflection_time, inflection_time], [0, 500], color=colors[100],
            ls=":", lw=1.2)
    ax.scatter([inflection_time], [500], color=colors[100], marker="D",
               s=44, zorder=6)
    ax.annotate("future inflection\n5.49306 days; N = 500",
                xy=(inflection_time, 500), xytext=(7.5, 295),
                arrowprops={"arrowstyle": "->", "color": colors[100]},
                color=colors[100], fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    for time, label_position in [(5, (1.0, 705)), (10, (11.6, 725))]:
        value = float(population(time, 100))
        ax.scatter([time], [value], color=colors[100], s=30, zorder=6)
        ax.annotate(f"N({time}) = {value:.2f}", xy=(time, value),
                    xytext=label_position, fontsize=10, color=colors[100],
                    arrowprops={"arrowstyle": "->", "color": colors[100]},
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.set(title="One growth law, three initial populations\n"
                 r"$N'=0.4N(1-N/1000)$",
           xlabel="time t (days)", ylabel="population N (individuals)",
           xlim=(0, 20), ylim=(-40, 1280), xticks=np.arange(0, 21, 5))
    ax.set_facecolor("white")
    ax.grid(alpha=0.14)
    ax.legend(loc="lower right", framealpha=1, fontsize=10)
    fig.savefig(Path.cwd() / "logistic-growth-trajectories.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
