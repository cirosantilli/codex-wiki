"""Show individual Boltzmann probabilities and their energy grouping.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes the matching PNG basename into the current working directory.
Two distinguishable noninteracting two-level units; stipulated toy model.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    energies = np.array([0.0, 1.0, 1.0, 2.0])  # units of Delta
    weights = np.exp(-np.log(2.0) * energies)
    probabilities = weights / weights.sum()
    aggregates = np.array([probabilities[energies == e].sum() for e in range(3)])
    assert np.allclose(probabilities, np.array([4, 2, 2, 1]) / 9)
    assert np.allclose(aggregates, np.array([4, 4, 1]) / 9)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    colors = ["#236b9b", "#bd6429", "#bd6429", "#33836b"]
    fig = plt.figure(figsize=(9.0, 5.2), dpi=120)
    grid = fig.add_gridspec(1, 3, width_ratios=[1.0, 1.1, 1.05],
                           left=0.075, right=0.975, bottom=0.28, top=0.78, wspace=0.5)
    energy_ax, micro_ax, macro_ax = [fig.add_subplot(grid[0, i]) for i in range(3)]
    fig.suptitle("Boltzmann probabilities: count microstates before grouping", fontsize=15, y=0.97)
    fig.text(0.5, 0.885, r"$\Delta = k_B T\ln 2$,  $q=1/2$,  $Z=9/4$", ha="center", fontsize=13)
    positions = np.arange(4)
    state_labels = ["00", "01", "10", "11"]
    energy_ax.bar(positions, energies, color=colors, width=0.62, alpha=0.8)
    energy_ax.scatter(positions, energies, color=colors, marker="_", s=300, linewidths=3, zorder=4)
    energy_ax.set(ylim=(-0.1, 2.45), ylabel=r"Energy $E_i/\Delta$", title="Four microstates")
    energy_ax.set_xticks(positions, state_labels)
    energy_ax.set_yticks([0, 1, 2])
    for x, y, label in zip(positions, energies, ["0", r"$\Delta$", r"$\Delta$", r"$2\Delta$"]):
        energy_ax.text(x, y + 0.14, label, ha="center", fontsize=11)

    micro_ax.bar(positions, probabilities, color=colors, width=0.62)
    micro_ax.set(ylim=(0, 0.56), ylabel=r"Individual probability $p_i$", title="One bar per microstate")
    micro_ax.set_xticks(positions, state_labels)
    for x, y, label in zip(positions, probabilities, ["4/9", "2/9", "2/9", "1/9"]):
        micro_ax.text(x, y + 0.02, label, ha="center", fontsize=11)

    macro_ax.bar(np.arange(3), aggregates, color=[colors[0], colors[1], colors[3]], width=0.62)
    macro_ax.set(ylim=(0, 0.56), ylabel=r"Aggregate probability $P(E)$", title="Group by energy")
    macro_ax.set_xticks([0, 1, 2], ["0\ng = 1", r"$\Delta$" + "\ng = 2", r"$2\Delta$" + "\ng = 1"])
    for x, y, label in zip(range(3), aggregates, ["4/9", "4/9", "1/9"]):
        macro_ax.text(x, y + 0.02, label, ha="center", fontsize=11)
    for ax in [micro_ax, macro_ax]:
        ax.set_yticks([0, 0.25, 0.5], ["0", "1/4", "1/2"])
    for ax in [energy_ax, micro_ax, macro_ax]:
        ax.grid(axis="y", alpha=0.18)
        ax.set_axisbelow(True)
    fig.text(0.5, 0.14, "Middle energy: two distinct microstates, 2/9 + 2/9 = 4/9", ha="center", fontsize=12)
    fig.text(0.5, 0.06, "Two labeled, noninteracting units; fixed positive temperature; finite toy model",
             ha="center", fontsize=10, color="#444444")
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
