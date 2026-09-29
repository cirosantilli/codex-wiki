"""Generate radical-charge-and-orbital-occupancy.png in the current directory.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Left: hydrogen ground-state occupancies. Right: invented two-orbital models.
Run from _media with MPLBACKEND=Agg and MPLCONFIGDIR in /tmp.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def orbital(ax, x, y, occupancy):
    ax.add_patch(Rectangle((x - 0.24, y - 0.20), 0.48, 0.40,
                           facecolor="white", edgecolor="#45586c", lw=1.4))
    for j in range(occupancy):
        xx = x if occupancy == 1 else x - 0.09 + 0.18 * j
        dy = 0.26 if j == 0 else -0.26
        ax.annotate("", (xx, y + dy / 2), (xx, y - dy / 2),
                    arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#216c91"})


def inventories():
    # label, proton count, spatial-orbital occupations, expected charge, unpaired
    return [(r"$\mathrm{H}^{+}$", 1, (0,), 1, 0),
            (r"$\mathrm{H}^{\bullet}$", 1, (1,), 0, 1),
            (r"$\mathrm{H}^{-}$", 1, (2,), -1, 0),
            ("Neutral model", 2, (1, 1), 0, 2),
            ("Cation model", 2, (1, 0), 1, 1),
            ("Anion model", 2, (2, 1), -1, 1)]


def main():
    records = inventories()
    for _, protons, occ, charge, unpaired in records:
        assert all(n in (0, 1, 2) for n in occ)
        assert protons - sum(occ) == charge
        assert sum(n == 1 for n in occ) == unpaired
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.7), dpi=120, facecolor="white")
    fig.suptitle("Charge counts particles; radical character counts unpaired electrons",
                 fontsize=14, weight="bold", y=0.98)
    for panel, ax in enumerate(axes):
        ax.set(xlim=(0, 5), ylim=(-0.8, 4.2))
        ax.axis("off")
        ax.text(2.5, 3.9, ["Hydrogen ground states: one proton",
                          "Invented models: two protons"][panel], ha="center",
                fontsize=12, weight="bold")
        ax.text(1.85, 3.32, [r"$1s$ orbital", "Orbitals A, B"][panel],
                ha="center", fontsize=11)
        ax.text(3.0, 3.32, r"$q/e$", ha="center", fontsize=12)
        ax.text(4.1, 3.32, "Unpaired", ha="center", fontsize=11)
        for row, (label, _, occ, charge, unpaired) in enumerate(records[3 * panel:3 * panel + 3]):
            y = 2.65 - row * 1.0
            if unpaired:
                ax.add_patch(Rectangle((0.02, y - 0.35), 4.93, 0.70,
                                       facecolor="#eef6fa", edgecolor="none"))
            ax.text(0.1, y, label, fontsize=11.2, va="center")
            for j, n in enumerate(occ):
                orbital(ax, 1.6 + j * 0.65 if panel else 1.85, y, n)
            ax.text(3.0, y, f"{charge:+d}" if charge else "0",
                    fontsize=13, ha="center", va="center")
            ax.text(4.1, y, str(unpaired), fontsize=13, ha="center", va="center")
        ax.text(2.5, -0.28, ["Only neutral H is a radical here.",
                            "All three models have unpaired electrons."][panel],
                ha="center", fontsize=11, color="#216c91")
    fig.text(0.5, 0.035, "Boxes are spatial orbitals; arrows label opposite spins. Right-hand models are not named substances.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=0.015, right=0.995, top=0.88, bottom=0.13, wspace=0.04)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
