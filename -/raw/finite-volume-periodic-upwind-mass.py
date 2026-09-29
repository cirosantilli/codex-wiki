"""Plot original periodic upwind cell averages and the exact translated profile.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
"""

from fractions import Fraction
from math import comb
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def profiles():
    initial = [Fraction(x) for x in (0, 0, 2, 2, 1, 0, 0, 1)]
    courant = Fraction(1, 2)
    history = [initial]
    for _ in range(4):
        old = history[-1]
        history.append([(1 - courant) * old[j] + courant * old[(j - 1) % 8]
                        for j in range(8)])
    exact_four = [initial[(j - 2) % 8] for j in range(8)]
    # Independent closed form for four applications of the averaging operator.
    binomial_four = [sum(Fraction(comb(4, m), 16) * initial[(j - m) % 8]
                         for m in range(5)) for j in range(8)]
    assert history[4] == binomial_four
    for state in history + [exact_four]:
        assert sum(state) / 8 == Fraction(3, 4)
        assert all(0 <= value <= 2 for value in state)
    assert history[1] == [Fraction(x, 2) for x in (1, 0, 2, 4, 3, 1, 0, 1)]
    return history, exact_four


def main():
    history, exact_four = profiles()
    edges = np.linspace(0, 1, 9)
    fig, axes = plt.subplots(3, 1, figsize=(8.2, 6.1), dpi=130,
                             sharex=True, facecolor="white")
    colors = ["#52677a", "#2377b4", "#2377b4"]
    for ax, n, color in zip(axes, (0, 1, 4), colors):
        state = np.array(history[n], dtype=float)
        ax.stairs(state, edges, fill=True, alpha=0.15, color=color, baseline=0)
        ax.stairs(state, edges, color=color, linewidth=2.2,
                  label="Stored cell averages")
        if n == 4:
            ax.stairs(np.array(exact_four, dtype=float), edges,
                      color="#c56916", linewidth=1.8, linestyle="--",
                      label="Exact translation (two cells)")
        for face in edges:
            ax.axvline(face, color="#e1e5e8", linewidth=0.7, zorder=0)
        ax.set(ylim=(-0.05, 2.4), yticks=[0, 1, 2], ylabel="Cell average")
        ax.text(0.02, 0.85, rf"$n={n}$, $t={n}/16$", transform=ax.transAxes,
                fontsize=11)
        ax.text(0.98, 0.85, r"$M=h\sum_j U_j=3/4$", transform=ax.transAxes,
                fontsize=11, ha="right")
        ax.spines[["top", "right"]].set_visible(False)
    axes[-1].legend(loc="upper center", bbox_to_anchor=(0.5, -0.38),
                    ncol=2, frameon=False, fontsize=10)
    axes[-1].set(xlim=(0, 1), xticks=edges, xlabel="Position x (endpoints identified)")
    fig.suptitle("Periodic upwind advection: mass survives the spreading", fontsize=15,
                 y=0.98)
    fig.text(0.5, 0.925, r"Synthetic data; $a=1$, $h=1/8$, $k=1/16$, $\nu=1/2$",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.1, right=0.97, top=0.89, bottom=0.15, hspace=0.23)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(output)


if __name__ == "__main__":
    main()
