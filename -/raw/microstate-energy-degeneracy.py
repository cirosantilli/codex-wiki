"""Show the four microstates of two distinguishable, independent thermal units.

Build with: make _media/microstate-energy-degeneracy.png
Writes the same-basename, opaque white PNG to the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np


def main():
    states = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    energies = states.sum(axis=1)
    weights = np.exp(-np.log(3.0) * energies)
    probabilities = weights / weights.sum()
    degeneracies = np.bincount(energies, minlength=3)
    grouped = np.bincount(energies, weights=probabilities, minlength=3)
    assert np.array_equal(degeneracies, [1, 2, 1])
    assert np.allclose(probabilities, np.array([9, 3, 3, 1]) / 16.0)
    assert np.allclose(grouped, np.array([9, 6, 1]) / 16.0)
    assert np.isclose(grouped.sum(), 1.0)
    assert np.isclose(np.dot(np.arange(3), grouped), 0.5)

    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.0, 5.4), dpi=120)
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.06, top=0.79)
    fig.suptitle("Four microstates, three energy macrostates", fontsize=16, y=0.97)
    fig.text(0.5, 0.88, r"Two labeled units A, B  |  Energies add  |  $\beta\Delta=\ln 3$, $p=1/4$",
             ha="center")
    ax.set(xlim=(0, 10), ylim=(0, 5.9))
    ax.axis("off")
    ax.text(2.0, 5.62, "Microstate (A, B) and probability", ha="center", weight="bold")
    ax.text(8.03, 5.62, "Total energy, count and probability", ha="center", weight="bold")
    colors = ["#236a9e", "#277953", "#bd582b"]
    ys = [4.75, 3.55, 2.35, 1.15]
    group_ys = [4.75, 2.95, 1.15]
    fractions = ["9/16", "3/16", "3/16", "1/16"]
    for state, energy, y, fraction in zip(states, energies, ys, fractions):
        color = colors[energy]
        ax.add_patch(FancyBboxPatch((0.20, y - 0.40), 3.85, 0.80,
                                    boxstyle="round,pad=0.08", facecolor="white",
                                    edgecolor=color, linewidth=1.5))
        ax.text(0.45, y, f"({state[0]}, {state[1]})", va="center")
        for x, level in zip([1.80, 2.55], state):
            ax.add_patch(Circle((x, y), 0.23, facecolor=color if level else "white",
                                edgecolor=color, linewidth=1.5))
            ax.text(x, y, str(level), ha="center", va="center",
                    color="white" if level else color, fontsize=10)
        ax.text(3.25, y, fraction, ha="center", va="center")
        ax.annotate("", xy=(6.28, group_ys[energy]), xytext=(4.17, y),
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 1.8})
    for energy, y, count, fraction, label in zip(range(3), group_ys, degeneracies,
                                               ["9/16", "6/16", "1/16"],
                                               ["0", r"\Delta", r"2\Delta"]):
        ax.add_patch(FancyBboxPatch((6.42, y - 0.51), 3.10, 1.02,
                                    boxstyle="round,pad=0.08", facecolor="white",
                                    edgecolor=colors[energy], linewidth=1.8))
        ax.text(7.97, y + 0.21, rf"$E={label}$,  $g={count}$", ha="center", va="center")
        ax.text(7.97, y - 0.22, f"Probability = {fraction}", ha="center", va="center")
    ax.text(5.0, 0.18, r"The middle macrostate merges (0,1) and (1,0):  3/16 + 3/16 = 6/16",
            ha="center", fontsize=11)
    fig.savefig(Path.cwd() / "microstate-energy-degeneracy.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
