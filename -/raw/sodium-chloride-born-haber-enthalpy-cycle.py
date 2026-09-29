"""Original synthetic Hess-law inventory diagram; Python 3.14, matplotlib 3.10.7.

Run from _media; the matching PNG is written to the current directory.
All numerical enthalpies are invented, internally consistent teaching inputs.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    steps = np.array([100, 120, 500, -350, -770], dtype=int)
    levels = np.concatenate(([0], np.cumsum(steps)))
    inventories = [
        r"Na(s) + $\frac{1}{2}$Cl$_2$(g)",
        r"Na(g) + $\frac{1}{2}$Cl$_2$(g)",
        r"Na(g) + Cl(g)",
        r"Na$^+$(g) + Cl(g) + e$^-$(g)",
        r"Na$^+$(g) + Cl$^-$(g)",
        r"NaCl(s)",
    ]
    names = ["Na\nsublimation", "Cl\natomization", "Na\nionization", "Electron\nattachment", "Lattice\nformation"]
    fig, ax = plt.subplots(figsize=(11, 7.6), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.09, right=0.97, bottom=0.15, top=0.80)
    ax.set(xlim=(-0.9, 11.9), ylim=(-470, 820))
    ax.set_ylabel(r"Relative molar enthalpy / kJ mol$^{-1}$", fontsize=12)
    ax.set_xticks([])
    ax.spines[["top", "right", "bottom"]].set_visible(False)
    ax.tick_params(labelsize=11)
    for value, inventory in zip(levels, inventories):
        ax.plot([0.65, 11.55], [value, value], color="#d3dae0", lw=1, zorder=0)
        ax.plot([0.65, 4.95], [value, value], color="#304352", lw=2)
        ax.text(0.75, value + 18, inventory, fontsize=12, va="bottom")
    for i, (delta, name) in enumerate(zip(steps, names)):
        x = 5.55 + i * 1.3
        color = "#b65c16" if delta > 0 else "#176b8c"
        ax.annotate("", (x, levels[i + 1]), (x, levels[i]),
                    arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2, "mutation_scale": 15})
        ax.text(x + 0.09, (levels[i] + levels[i + 1]) / 2, f"{delta:+d}",
                color=color, fontsize=12, va="center", rotation=90 if i == 4 else 0)
        ax.text(x, 840, name, ha="center", va="bottom", fontsize=10, color=color)
    ax.annotate("", (-0.3, -400), (-0.3, 0),
                arrowprops={"arrowstyle": "-|>", "color": "#6b4090", "lw": 2, "mutation_scale": 15})
    ax.text(-0.48, -200, "Overall formation: −400", rotation=90,
            ha="center", va="center", color="#6b4090", fontsize=10)
    fig.suptitle("NaCl: a closed Born–Haber enthalpy balance", fontsize=17, y=0.965)
    fig.text(0.5, 0.913, "Synthetic inputs, not measured NaCl data • one mole of formula units", ha="center", fontsize=12)
    fig.text(0.5, 0.085, "100 + 120 + 500 − 350 − 770 = −400 kJ mol⁻¹", ha="center", fontsize=13)
    fig.text(0.5, 0.038, "Return to elements: +400  •  closed sum: 0  •  reversing lattice formation gives +770", ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
