"""Original comparison of four two-particle ground states.

Python 3.14, matplotlib 3.10.7. Run from _media; output basename.png in CWD.
Energies are invented: three spatial levels 0, Delta, 3 Delta; no interactions.
"""

from pathlib import Path

import matplotlib.pyplot as plt


def main():
    fig, axes = plt.subplots(1, 4, figsize=(11.2, 4.9), facecolor="white", sharey=True)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.24, top=0.72, wspace=0.14)
    fig.suptitle("Ground energy depends on the available spin states", fontsize=15, y=0.96)
    cases = [
        ("Distinguishable\nboth spins available", [(0, "↑₁", -0.19), (0, "↑₂", 0.19)], "0", 4, "One of four ground states"),
        ("Identical electrons\nboth spins available", [(0, "↑", -0.19), (0, "↓", 0.19)], "0", 1, "Spin singlet; symmetric space"),
        ("Distinguishable\nparallel spins only", [(0, "↑₁", -0.19), (0, "↑₂", 0.19)], "0", 1, "Both may occupy A↑"),
        ("Identical electrons\nparallel spins only", [(0, "↑", 0), (1, "↑", 0)], r"\Delta", 1, "Triplet ↑↑; antisymmetric space"),
    ]
    for ax, (title, occupants, energy, degeneracy, note) in zip(axes, cases):
        for level, label in [(0, "A"), (1, "B"), (3, "C")]:
            ax.hlines(level, -0.45, 0.45, color="#9aa9b4", linewidth=2)
            ax.text(0.51, level, label, va="center", fontsize=11)
        for level, spin, x in occupants:
            ax.text(x, level + 0.11, spin, ha="center", va="bottom", color="#215d98", fontsize=22, weight="bold")
        ax.set_title(title, fontsize=11, pad=15)
        ax.set(xlim=(-0.65, 0.8), ylim=(-0.4, 3.8), xticks=[], yticks=[0, 1, 3], yticklabels=["0", "Δ", "3Δ"])
        ax.spines[["top", "right", "bottom"]].set_visible(False)
        ax.tick_params(axis="y", length=0)
        ax.text(0.5, -0.13, rf"$E_0={energy}$,  $g_0={degeneracy}$", transform=ax.transAxes, ha="center", fontsize=12)
        ax.text(0.5, -0.27, note, transform=ax.transAxes, ha="center", fontsize=9)
    axes[0].set_ylabel("One-particle energy", fontsize=11)
    fig.text(0.5, 0.855, r"Original noninteracting model: $\epsilon_A=0$, $\epsilon_B=\Delta$, $\epsilon_C=3\Delta$, with $\Delta>0$.", ha="center", fontsize=12)
    fig.text(0.5, 0.055, "Arrows show occupied spin orbitals, not particle positions. Subscripts label distinguishable particles only.", ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
