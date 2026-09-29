"""Compare independently stipulated atomic and bond-energy scale inputs.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
All numbers are invented model inputs, not a table of measured elements.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    conversion = 96.485
    positions = np.arange(3)
    labels = ["A", "B", "C"]
    ionization = np.array([8.0, 7.0, 6.0])
    affinity = np.array([0.5, 3.0, 3.0])
    mulliken = (ionization + affinity) / 2
    drr = 300.0
    dxx = np.array([200.0, 300.0, 450.0])
    drx = (drr + dxx) / 2 + conversion * np.array([0.5, 1.0, 1.5]) ** 2
    pauling_difference = np.sqrt((drx - (drr + dxx) / 2) / conversion)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 2, figsize=(10, 6.8), layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("Different scale inputs can give different orderings", fontsize=15)
    atoms, bonds = axes[0]
    mean, difference = axes[1]
    width = 0.33
    atoms.bar(positions - width / 2, ionization, width, label="Removal cost I",
              color="#276c9a")
    atoms.bar(positions + width / 2, affinity, width, label="Attachment release Aₑₐ",
              color="#b34827")
    atoms.set(ylim=(0, 10), ylabel="Isolated-species energy (eV)",
              title="Mulliken inputs: positive attachment release")
    atoms.legend(fontsize=10, loc="upper right")
    for x, i, a in zip(positions, ionization, affinity):
        atoms.text(x - width/2, i + 0.15, f"{i:g}", ha="center")
        atoms.text(x + width/2, a + 0.15, f"{a:g}", ha="center")
    bonds.bar(positions - width / 2, dxx, width, label="Like-atom Dₓₓ", color="#7899af")
    bonds.bar(positions + width / 2, drx, width, label="Reference bond Dᵣₓ", color="#276c9a")
    bonds.set(ylim=(0, 770), ylabel="Dissociation energy (kJ/mol)",
              title="Pauling inputs: common reference R, Dᵣᵣ = 300")
    bonds.legend(fontsize=10, loc="upper left")
    for x, d in zip(positions, drx):
        bonds.text(x + width/2, d + 10, f"{d:.3f}", ha="center", fontsize=10)
    mean.plot(positions, mulliken, "o-", color="#b34827", linewidth=2, markersize=7)
    mean.set(ylim=(3.8, 5.4), ylabel="Mulliken electronegativity (eV)",
             title=r"$(I+A_{\rm ea})/2$: A < C < B")
    difference.plot(positions, pauling_difference, "o-", color="#276c9a", linewidth=2,
                    markersize=7)
    difference.set(ylim=(0, 1.95), ylabel="Pauling difference (dimensionless)",
                   title=r"$|\chi_P(X)-\chi_P(R)|$: A < B < C")
    for ax, values in [(mean, mulliken), (difference, pauling_difference)]:
        for x, value in zip(positions, values):
            ax.text(x, value + 0.08, f"{value:g}", ha="center")
        ax.grid(axis="y", alpha=0.2)
    for ax in axes.flat:
        ax.set_xticks(positions, labels)
        ax.set_xlim(-0.55, 2.55)
        ax.set_facecolor("white")
    fig.supxlabel("Stipulated species and energies: arithmetic illustration, not experimental data", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
