"""Generate pauli-spin-orbital-occupancy.png in the current directory.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
All energies and occupation strings describe a finite model, not observations.
"""

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np


def main():
    states = sorted(
        (tuple(int(i in occupied) for i in range(4))
         for occupied in combinations(range(4), 2)),
        reverse=True,
    )
    energies = np.array([0, 0, 1, 1])
    assert len(states) == 6
    assert sorted(int(np.dot(s, energies)) for s in states) == [0, 1, 1, 1, 1, 2]
    fig, ax = plt.subplots(figsize=(9.0, 5.6), dpi=130, facecolor="white")
    ax.set(xlim=(-1.6, 5.5), ylim=(-0.95, 7.3))
    ax.axis("off")
    ax.text(1.85, 7.06, "One per complete state; two per spatial orbital",
            ha="center", fontsize=16, weight="bold")
    ax.text(1.85, 6.52, r"Model: $N=2$, $\epsilon_A=0$, $\epsilon_B=\Delta>0$; spin does not change energy",
            ha="center", fontsize=12)
    for x, label in [(0.5, r"Spatial orbital $A$"), (2.5, r"Spatial orbital $B$")]:
        ax.text(x, 5.94, label, ha="center", fontsize=12, weight="bold")
        ax.plot([x - 0.81, x + 0.81], [5.72, 5.72], color="#64748b", lw=1)
    labels = [r"$A\uparrow$", r"$A\downarrow$", r"$B\uparrow$", r"$B\downarrow$"]
    for x, label in enumerate(labels):
        ax.text(x, 5.32, label, ha="center", fontsize=15)
    ax.text(-1.45, 5.32, "Occupations", fontsize=11)
    ax.text(4.65, 5.32, "Total energy", ha="center", fontsize=11)
    for row, state in enumerate(states):
        y = 4.62 - row * 0.78
        double_orbital = state in [(1, 1, 0, 0), (0, 0, 1, 1)]
        color = "#137b67" if double_orbital else "#245b99"
        if double_orbital:
            ax.add_patch(Rectangle((-1.55, y - 0.32), 7.0, 0.64,
                                   facecolor="#edf7f1", edgecolor="none"))
        ax.text(-1.35, y, "".join(map(str, state)), va="center", fontsize=13,
                family="monospace", color=color)
        for x, occupied in enumerate(state):
            ax.add_patch(Rectangle((x - 0.3, y - 0.27), 0.6, 0.54,
                                   facecolor="white", edgecolor="#64748b", lw=1))
            if occupied:
                ax.add_patch(Circle((x, y), 0.13, facecolor=color, edgecolor="none"))
        e = int(np.dot(state, energies))
        ax.text(4.65, y, [r"$0$", r"$\Delta$", r"$2\Delta$"][e],
                va="center", ha="center", fontsize=15, color=color)
    ax.text(1.85, -0.38, "Green rows: opposite spins share one spatial orbital. Every box holds at most one.",
            ha="center", fontsize=10.7)
    ax.text(1.85, -0.81, r"Six states: $\binom{4}{2}=6$. Energy multiplicities: $1,4,1$. Boxes are states, not positions.",
            ha="center", fontsize=11.2)
    fig.subplots_adjust(left=0.03, right=0.99, bottom=0.04, top=0.98)
    fig.savefig(Path.cwd() / "pauli-spin-orbital-occupancy.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
