"""Count Na, Na+, Cl, and Cl- particles; write basename.png to CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Dots are inventories, not orbital positions; neutron counts are omitted.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    cases = [(r"$\mathrm{Na}$: neutral atom", 11, 11),
             (r"$\mathrm{Na}^{+}$: cation", 11, 10),
             (r"$\mathrm{Cl}$: neutral atom", 17, 17),
             (r"$\mathrm{Cl}^{-}$: anion", 17, 18)]
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 6.6))
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.05, right=0.97, bottom=0.13, top=0.82,
                        wspace=0.20, hspace=0.50)
    for ax, (title, protons, electrons) in zip(axes.flat, cases):
        for count, y, color, name in [(protons, 2.8, "#b74632", "Protons (+e)"),
                                      (electrons, 1.0, "#236d99", "Electrons (−e)")]:
            k = np.arange(count)
            ax.scatter(k % 9, y - (k // 9) * 0.45, s=115, c=color,
                       edgecolors="white", linewidths=0.6)
            ax.text(-1.05, y - 0.2, f"{name}\n{count}", ha="right", va="center",
                    fontsize=11, color=color)
        charge = protons - electrons
        result = "0" if charge == 0 else ("+e" if charge > 0 else "−e")
        ax.text(3.8, -0.65, f"Net charge: ({protons} − {electrons})e = {result}",
                fontsize=12, ha="center", weight="bold")
        ax.set_title(title, fontsize=14, pad=12)
        ax.set_xlim(-4.4, 8.7)
        ax.set_ylim(-0.95, 3.25)
        ax.axis("off")
    fig.suptitle("Ion charge is a particle-count imbalance", fontsize=17, y=0.96)
    fig.text(0.5, 0.895, "The proton count stays fixed; one electron is removed or added.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.045, "Each dot counts one particle. Counting rows are not atomic structure.",
             ha="center", fontsize=11, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
