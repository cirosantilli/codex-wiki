"""Display independent strata and the dependence created by hiding them.

The tables are stipulated probabilities, not sampled or measured data.
Run in the output directory; versions are documented in pyproject.toml.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def model():
    strata = []
    for p in (Fraction(1, 10), Fraction(9, 10)):
        v = (1 - p, p)
        strata.append([[a * b for b in v] for a in v])
    mixed = [[(strata[0][i][j] + strata[1][i][j]) / 2 for j in range(2)] for i in range(2)]
    assert mixed == [[Fraction(41, 100), Fraction(9, 100)],
                     [Fraction(9, 100), Fraction(41, 100)]]
    assert mixed[1][1] - Fraction(1, 4) == Fraction(4, 25)
    assert mixed[1][1] / Fraction(1, 2) == Fraction(41, 50)
    return strata + [mixed, [[Fraction(1, 4)] * 2 for _ in range(2)]]


def main():
    titles = (r"Given $T=0$" + "\n" + r"$p_0=0.1$: independent",
              r"Given $T=1$" + "\n" + r"$p_1=0.9$: independent",
              "Environment hidden\nActual joint law",
              "Environment hidden\nProduct of marginals")
    fig, axes = plt.subplots(1, 4, figsize=(10.5, 3.4), dpi=120, layout="constrained")
    fig.set_facecolor("white")
    for ax, table, title in zip(axes, model(), titles):
        data = np.array(table, dtype=float)
        ax.imshow(data, vmin=0, vmax=1, cmap="Blues")
        for i in range(2):
            for j in range(2):
                ax.text(j, i, f"{data[i, j]:.2f}", ha="center", va="center", fontsize=16,
                        color="white" if data[i, j] > 0.5 else "#111111")
        ax.set_xticks((0, 1), labels=("0", "1"))
        ax.set_yticks((0, 1), labels=("0", "1"))
        ax.set(xlabel=r"$Y$", ylabel=r"$X$", title=title)
        ax.tick_params(length=0)
    fig.suptitle("Conditional independence does not imply unconditional independence", fontsize=13)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
