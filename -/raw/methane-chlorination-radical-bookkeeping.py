"""Generate methane-chlorination-radical-bookkeeping.png in CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Electron and chain-carrier bookkeeping, not spectral or kinetic measurements.
Run from _media with MPLBACKEND=Agg and MPLCONFIGDIR in /tmp.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch


def electron(ax, x, y, color="#216c91"):
    ax.add_patch(Circle((x, y), 0.055, facecolor=color, edgecolor="none"))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 5.4), dpi=120, facecolor="white",
                             gridspec_kw={"width_ratios": [1.5, 1]})
    for ax in axes:
        ax.set(xlim=(0, 6), ylim=(0, 6))
        ax.axis("off")
    left, right = axes
    fig.suptitle("Methane chlorination transfers a neutral radical carrier",
                 fontsize=14, weight="bold", y=0.98)
    left.text(3, 5.65, "Initiation: split one bonding pair", ha="center",
              fontsize=12, weight="bold")
    for x, label in [(0.6, "Cl"), (1.9, "Cl"), (4.2, "Cl"), (5.4, "Cl")]:
        left.text(x, 4.93, label, ha="center", va="center", fontsize=15)
    electron(left, 1.13, 4.93)
    electron(left, 1.36, 4.93, "#b46c27")
    left.annotate("", (3.65, 4.93), (2.4, 4.93), arrowprops={"arrowstyle": "->", "lw": 1.6})
    left.text(3.03, 5.20, r"$h\nu$", ha="center", fontsize=13)
    electron(left, 4.58, 4.93)
    electron(left, 5.78, 4.93, "#b46c27")
    left.text(3, 4.40, "0 carriers → 2 carriers; total charge stays zero", ha="center", fontsize=11)
    left.text(3, 3.83, "Propagation: replace one carrier", ha="center",
              fontsize=12, weight="bold")
    equations = [r"$\mathrm{Cl}^{\bullet}+\mathrm{CH}_4\ \longrightarrow\ \mathrm{HCl}+\mathrm{CH}_3^{\bullet}$",
                 r"$\mathrm{CH}_3^{\bullet}+\mathrm{Cl}_2\ \longrightarrow\ \mathrm{CH}_3\mathrm{Cl}+\mathrm{Cl}^{\bullet}$"]
    for y, equation in zip([3.12, 2.12], equations):
        left.text(3, y, equation, ha="center", fontsize=14)
        left.text(3, y - 0.42, "1 carrier → 1 carrier", ha="center", fontsize=11, color="#216c91")
    left.text(3, 1.22, "Sum: cancel both intermediate radicals", ha="center", fontsize=11)
    left.text(3, 0.64, r"$\mathrm{CH}_4+\mathrm{Cl}_2\ \longrightarrow\ \mathrm{CH}_3\mathrm{Cl}+\mathrm{HCl}$",
              ha="center", fontsize=14)
    right.add_patch(FancyBboxPatch((0.12, 0.35), 5.75, 5.28, boxstyle="round,pad=0.04",
                                   facecolor="#faf5ed", edgecolor="#c6aa89"))
    right.text(3, 5.25, "Termination: form a bonding pair", ha="center",
               fontsize=12, weight="bold")
    right.text(3, 4.53, r"$2\mathrm{CH}_3^{\bullet}\longrightarrow\mathrm{C}_2\mathrm{H}_6$",
               ha="center", fontsize=16)
    right.text(3, 3.92, "2 carriers → 0 carriers", ha="center", fontsize=12, color="#9a5a20")
    for x, label in [(1.0, r"$R$"), (2.4, r"$R$"), (4.35, r"$R$"), (5.48, r"$R$")]:
        right.text(x, 3.10, label, fontsize=17, ha="center", va="center")
    electron(right, 1.4, 3.10)
    electron(right, 2.0, 3.10, "#b46c27")
    right.annotate("", (3.97, 3.10), (2.84, 3.10), arrowprops={"arrowstyle": "->", "lw": 1.6})
    electron(right, 4.78, 3.10)
    electron(right, 5.03, 3.10, "#b46c27")
    right.text(3, 2.40, r"$R=\mathrm{CH}_3$; only reacting electrons shown", ha="center", fontsize=11)
    right.text(3, 1.66, "Radical count need not be conserved.", ha="center", fontsize=11.2)
    right.text(3, 1.13, "Atoms, electrons and charge are conserved.", ha="center", fontsize=11.2)
    right.text(3, 0.65, "Schematic; not rates or an EPR spectrum.", ha="center", fontsize=10.7)
    fig.subplots_adjust(left=0.015, right=0.985, bottom=0.03, top=0.90, wspace=0.13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
