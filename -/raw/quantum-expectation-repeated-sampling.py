"""Plot simulated fresh-copy spin measurements and exact sample-mean masses.

Tested with Python 3.14 and root pyproject.toml dependencies; run from _media.
No experimental observations are represented.
"""

from math import comb
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def binomial_masses(n, p):
    k = np.arange(n + 1)
    masses = np.array([comb(n, int(j)) * p**int(j) * (1-p)**(n-int(j))
                       for j in k])
    return k / n - 0.5, masses


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    p, seed, count = 0.75, 73129, 1600
    rng = np.random.default_rng(seed)
    n = np.arange(1, count + 1)
    mean, single_sd = p - 0.5, np.sqrt(p * (1-p))
    fig, (left, right) = plt.subplots(1, 2, figsize=(11, 4.7))
    colors = ["#365d9d", "#16837b", "#9570a4", "#6f7540"]
    for color in colors:
        outcomes = np.where(rng.random(count) < p, 0.5, -0.5)
        left.plot(n, np.cumsum(outcomes) / n, color=color, lw=1.1, alpha=0.85)
    left.plot(n, mean + single_sd / np.sqrt(n), "--", color="#555555", lw=1,
              label="Mean ± one theoretical SE")
    left.plot(n, mean - single_sd / np.sqrt(n), "--", color="#555555", lw=1)
    left.axhline(mean, color="#c46a12", lw=2, label=r"True mean $1/4$")
    left.set(xscale="log", xlim=(1, count), ylim=(-0.53, 0.75),
             xlabel="Fresh preparations N (log scale)",
             ylabel=r"Running sample mean / $\hbar$",
             title="Four independent simulated records")
    left.legend(loc="lower right", fontsize=9)
    left.grid(alpha=0.18)
    for size, color, marker in [(16, "#365d9d", "o"), (128, "#16837b", ".")]:
        values, masses = binomial_masses(size, p)
        right.vlines(values, 0, masses, color=color, alpha=0.75, lw=1.2)
        right.plot(values, masses, marker, color=color, ms=5,
                   label=f"N = {size}")
    right.axvline(mean, color="#c46a12", lw=2, linestyle="--")
    right.set(xlim=(-0.12, 0.53), ylim=(0, 0.24),
              xlabel=r"Possible sample mean / $\hbar$",
              ylabel="Probability at each discrete mean",
              title="Exact binomial sampling distributions")
    right.legend(fontsize=10)
    right.grid(axis="y", alpha=0.18)
    fig.suptitle(r"Estimating $\langle S_z\rangle=\hbar/4$ from outcomes $\pm\hbar/2$",
                 fontsize=15)
    fig.text(0.5, 0.025, "Model only: p(+) = 3/4; fresh independent copies; seed 73129",
             ha="center", color="#555555")
    fig.tight_layout(rect=(0, 0.055, 1, 0.91))
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
