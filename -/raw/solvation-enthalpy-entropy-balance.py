"""Synthetic dissolution bookkeeping, not measured salt or solvent data.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the matching opaque PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


TEMPERATURE = 300.0  # K, stipulated model temperature
SEPARATION = 100.0  # kJ per mol of hypothetical 1:1 salt
REORGANIZATION = 20.0
INTERACTIONS = np.array([-150.0, -90.0])
ENTROPIES = np.array([-0.050, 0.150])  # kJ mol^-1 K^-1, total process


def main():
    enthalpies = SEPARATION + REORGANIZATION + INTERACTIONS
    entropy_terms = -TEMPERATURE * ENTROPIES
    free_energies = enthalpies + entropy_terms
    assert np.allclose(enthalpies, [-30, 30])
    assert np.allclose(free_energies, [-15, -15])
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 6.2), facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.25, top=0.77, wspace=0.36)
    ax = axes[0]
    x = np.arange(4)
    for interaction, name, color, offset in zip(INTERACTIONS, ["A", "B"], ["#246d9d", "#b15c22"], [-0.035, 0.035]):
        levels = np.array([0, SEPARATION, SEPARATION + REORGANIZATION, SEPARATION + REORGANIZATION + interaction])
        ax.plot(x + offset, levels, marker="o", color=color, lw=2.2, label=f"Solvent {name}")
        ax.text(3.10, levels[-1], f"{levels[-1]:+.0f}", va="center", color=color, fontsize=13)
    ax.axhline(0, color="#88919b", lw=1)
    ax.set_ylim(-50, 155)
    ax.set_xlim(-0.25, 3.6)
    ax.set_xticks(x, ["Initial", "Separate\nsolute", "Reorganize\nsolvent", "Establish\ninteractions"], fontsize=10)
    ax.set_ylabel(r"Cumulative enthalpy / kJ mol$^{-1}$")
    ax.set_title("Enthalpy accounting path", fontsize=14, pad=15)
    ax.text(0.50, 61, "+100", ha="center", color="#4d5968")
    ax.text(1.50, 130, "+20", ha="center", color="#4d5968")
    ax.text(2.48, 45, "A: −150\nB: −90", ha="center", color="#4d5968", fontsize=11)
    ax.legend(loc="upper left", frameon=False, fontsize=11)
    ax = axes[1]
    width = 0.33
    x = np.arange(3)
    for i, (name, color) in enumerate(zip(["A", "B"], ["#246d9d", "#b15c22"])):
        values = [enthalpies[i], entropy_terms[i], free_energies[i]]
        bars = ax.bar(x + (i - 0.5) * width, values, width=width, color=color, label=f"Solvent {name}")
        for bar, value in zip(bars, values):
            ax.text(bar.get_x() + width / 2, value + (3 if value >= 0 else -3), f"{value:+.0f}", ha="center", va="bottom" if value >= 0 else "top", fontsize=12)
    ax.axhline(0, color="#88919b", lw=1)
    ax.set_ylim(-65, 60)
    ax.set_xticks(x, [r"$\Delta H$", r"$-T\Delta S$", r"$\Delta G$"], fontsize=15)
    ax.set_ylabel(r"Molar contribution / kJ mol$^{-1}$")
    ax.set_title(r"$\Delta G=\Delta H-T\Delta S$ at 300 K", fontsize=14, pad=15)
    ax.legend(loc="upper right", frameon=False, fontsize=11)
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", color="#edf0f3", zorder=0)
        ax.set_axisbelow(True)
    fig.suptitle("Dissolution balances solvent interactions and total entropy", y=0.96, fontsize=17)
    fig.text(0.5, 0.86, "Synthetic example: one mole of a hypothetical 1:1 salt in either of two unspecified solvents", ha="center", fontsize=12)
    fig.text(0.5, 0.14, r"A: $\Delta S=-50$ J mol$^{-1}$ K$^{-1}$      B: $\Delta S=+150$ J mol$^{-1}$ K$^{-1}$", ha="center", fontsize=12)
    fig.text(0.5, 0.08, "Both stipulated processes have ΔG = −15 kJ/mol, despite opposite signs of ΔH.", ha="center", fontsize=12)
    fig.text(0.5, 0.035, "Invented, internally consistent values. The accounting path is not a time sequence or activation barrier.", ha="center", fontsize=10.5)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
