"""Stratified turbulence equilibrium curves.

Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7.
Write only the PNG basename to caller CWD; respect caller MPLCONFIGDIR.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=100, facecolor="white")
    ax.set_facecolor("white")
    parameters = (0, .04, .16, .25, .36)
    colors = ("#555555", "#2873b5", "#2a945d", "#d47c1d", "#b33f59")
    for parameter, color in zip(parameters, colors):
        if parameter == 0:
            x = np.linspace(0, 1.55, 600)
            ax.plot(x, x, color=color, lw=2, label="A = 0: unstratified")
            ax.plot([1], [1], "o", color=color, ms=6)
            continue
        minimum = np.sqrt(parameter)
        roots = []
        if parameter <= .25:
            discriminant = np.sqrt(1-4*parameter)
            roots = [(1-discriminant)/2, (1+discriminant)/2]
        x = np.unique(np.r_[np.linspace(.018, 1.55, 900), minimum, roots])
        ratio = x + parameter/x
        regime = "critical" if parameter == .25 else ("supercritical" if parameter > .25 else "subcritical")
        ax.plot(x, ratio, color=color, lw=2,
                label=f"A = {parameter:.2f}: {regime}")
        ax.plot([minimum], [2*minimum], "s", color=color, ms=6)
        if roots:
            ax.plot(roots, np.ones(len(roots)), "o", color=color, ms=6)
    ax.axhline(1, color="#333333", ls="--", lw=1.2)
    ax.text(1.49, 1.055, "R = 1", ha="right", fontsize=11)
    ax.set_xlim(0, 1.55)
    ax.set_ylim(0, 2.35)
    ax.set_xlabel(r"Normalized turbulent speed $\widetilde q=q/(L_u C_u S)$", fontsize=12)
    ax.set_ylabel("Total sinks / production, R", fontsize=12)
    ax.set_title(r"Stratified turbulence: $R=\widetilde{q}+\mathcal{A}/\widetilde{q}$", fontsize=14)
    ax.text(.035, 2.20, "Squares: minima     Circles: equilibria", fontsize=10)
    ax.legend(loc="upper right", framealpha=1, facecolor="white", fontsize=10)
    ax.grid(alpha=.18)
    fig.tight_layout()
    fig.savefig(Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
