"""Plot an original finite optimization example; run from _media.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    states = np.arange(5)
    energy = np.array([2, 1, 4, 2, 0])
    assert energy[1] < min(energy[0], energy[2])
    assert np.argmin(energy) == 4
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.09, right=0.97, bottom=0.24, top=0.86)
    ax.plot(states, energy, color="#9ca3af", linewidth=2, zorder=1)
    ax.scatter(states, energy, s=95,
               c=["#687584", "#d97706", "#b83245", "#687584", "#087e8b"],
               edgecolor="white", linewidth=1, zorder=3)
    for state, value in zip(states, energy):
        ax.text(state, value - 0.28, f"E = {value}", ha="center", va="top")
    for start, end in [(1, 2), (2, 3), (3, 4)]:
        ax.annotate("", xy=(end - 0.08, energy[end] + 0.18),
                    xytext=(start + 0.08, energy[start] + 0.18),
                    arrowprops={"arrowstyle": "->", "color": "#087e8b", "lw": 2})
    ax.annotate("Start: local minimum\ngreedy search stays here",
                xy=(1, 1), xytext=(-0.1, 3.55), ha="left", fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#d97706"})
    ax.text(1.43, 2.8, "Uphill\nΔE = +3", color="#b83245", ha="right", fontsize=11)
    ax.text(3.1, 3.35, "One possible escape:\n1 → 2 → 3 → 4",
            ha="center", color="#087e8b")
    ax.annotate("Global minimum", xy=(4, 0), xytext=(3.22, 1.05),
                ha="center", color="#087e8b", fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#087e8b"})
    ax.set(xticks=states, xlabel="State (only the five dots are feasible)",
           ylabel="Objective E to minimize", ylim=(-0.65, 4.65), xlim=(-0.42, 4.42))
    ax.grid(axis="y", alpha=0.2)
    fig.suptitle("Accepting an uphill step can unlock a lower minimum", fontsize=15, y=0.97)
    fig.text(0.5, 0.075,
             "Symmetric proposals: left/right each ½; endpoints hold with probability ½.\n"
             "At T = 1/ln 2: accept 1 → 2 with probability ⅛ given that proposal.",
             ha="center", va="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
