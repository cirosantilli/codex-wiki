"""Plot three aggregate Boltzmann populations for degeneracies 1, 2, 1.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes the matching PNG basename into the current working directory.
Fixed gap Delta > 0, four microstates, positive temperatures only.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0.015, 8.0, 1600)  # k_B T / Delta, strictly positive
    q = np.exp(-1.0 / x)
    populations = np.array([np.ones_like(q), 2 * q, q ** 2]) / (1 + q) ** 2
    assert np.allclose(populations.sum(axis=0), 1.0)
    crossing = 1.0 / np.log(2.0)
    crossing_populations = np.array([4.0, 4.0, 1.0]) / 9.0

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.6, 5.4), dpi=120)
    fig.subplots_adjust(left=0.1, right=0.83, bottom=0.24, top=0.80)
    fig.suptitle("Boltzmann populations of three energy macrostates", fontsize=15, y=0.97)
    fig.text(0.5, 0.89, r"Four microstates; fixed gap $\Delta>0$; degeneracies 1, 2, 1",
             ha="center", fontsize=12)
    colors = ["#236b9b", "#bd6429", "#33836b"]
    labels = [r"$E=0$, $g=1$", r"$E=\Delta$, $g=2$", r"$E=2\Delta$, $g=1$"]
    for population, color, label in zip(populations, colors, labels):
        ax.plot(x, population, lw=2.7, color=color, label=label)
    for limit, color in zip([0.25, 0.5, 0.25], colors):
        ax.axhline(limit, color=color, lw=1.0, ls=":", alpha=0.55)
    ax.axvline(crossing, color="#777777", ls="--", lw=1.1)
    ax.scatter([crossing, crossing], crossing_populations[[0, 2]],
               c=[colors[1], colors[2]], s=35, zorder=5)
    ax.annotate(r"$P(0)=P(\Delta)=4/9$", xy=(crossing, 4 / 9), xytext=(2.2, 0.71),
                arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=11)
    ax.text(crossing + 0.12, 0.91, r"$x=1/\ln 2$", fontsize=10, color="#555555")
    ax.set(xlim=(0, 8), ylim=(0, 1.02), xlabel=r"Positive temperature scale $x=k_B T/\Delta$",
           ylabel=r"Aggregate probability $P(E)$")
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1], ["0", "1/4", "1/2", "3/4", "1"])
    ax.grid(alpha=0.16)
    ax.legend(loc="upper right", frameon=False, fontsize=11)
    ax.text(8.15, 0.5, "1/2\n(middle)", va="center", fontsize=10, color=colors[1])
    ax.text(8.15, 0.25, "1/4\n(each outer)", va="center", fontsize=10, color="#444444")
    fig.text(0.5, 0.115, "High-temperature limits (dotted): aggregate 1/4, 1/2, 1/4; each microstate 1/4",
             ha="center", fontsize=10)
    fig.text(0.5, 0.045, "Uniform microstate limit applies to this fixed finite model", ha="center", fontsize=10, color="#444444")
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
