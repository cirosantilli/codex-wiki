"""Seed-bank fixed points; Python 3.14, root NumPy/Matplotlib dependencies.

The caller supplies MPLCONFIGDIR. Write only a basename PNG in cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    gain = 2.4
    population = np.linspace(0, 1.15, 400)
    recruitment = 1 - np.exp(-gain * population)
    low, high = 0.01, 1.0
    for _ in range(60):
        middle = (low + high) / 2
        if 1 - np.exp(-gain * middle) > middle:
            low = middle
        else:
            high = middle
    equilibrium = (low + high) / 2
    fig, ax = plt.subplots(figsize=(8, 4.8), dpi=100, facecolor="white")
    ax.plot(population, recruitment, color="#176a9a", linewidth=2.5,
            label=r"$N(AM)$: bounded, concave recruitment")
    ax.plot(population, population, color="#444444", linewidth=1.8,
            label=r"Identity $M$")
    ax.plot([0, equilibrium], [0, equilibrium], "o", color="#a44211", markersize=7)
    ax.annotate(r"Positive steady state $M_*$", xy=(equilibrium, equilibrium),
                xytext=(0.33, 1.05), arrowprops={"arrowstyle": "->"}, fontsize=12)
    ax.text(0.03, 0.045, "Extinction", fontsize=11)
    ax.set_xlim(0, 1.15)
    ax.set_ylim(0, 1.16)
    ax.set_xlabel(r"Population $M$ (normalized)")
    ax.set_ylabel(r"Recruitment $N(AM)$ (normalized)")
    ax.set_title("Seed survival above replacement gives a positive fixed point")
    ax.legend(loc="lower right", fontsize=10)
    ax.grid(alpha=0.2)
    fig.text(0.5, 0.02, r"Illustrative $N(S)=1-e^{-S}$, $A=2.4>1$; initial slope $A$, limiting recruitment 1.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.055, 1, 1))
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
