"""Draw oxidation-state allocations; run from _media with Python 3.14.

Tested with matplotlib 3.10.7 and numpy 2.3.5. These are bookkeeping
diagrams, not electron-density maps or measured partial charges.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def atom(ax, x, y, symbol, state, assigned):
    ax.add_patch(Circle((x, y), 0.15, facecolor="white", edgecolor="#34495e", lw=1.7))
    ax.text(x, y, symbol, ha="center", va="center", fontsize=18)
    ax.text(x, y - 0.26, f"OS = {state}", ha="center", fontsize=13, color="#095c80")
    ax.text(x, y - 0.43, f"assigned: {assigned} e⁻", ha="center", fontsize=10.5)


def allocation(ax, a, b):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=16,
                               color="#095c80", linewidth=1.8))


def panel(ax, title, note):
    ax.set(xlim=(0, 2.5), ylim=(0, 1.7))
    ax.axis("off")
    ax.text(1.25, 1.50, title, ha="center", fontsize=16, weight="bold")
    ax.text(1.25, 0.11, note, ha="center", fontsize=11)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": "white"})
    fig, axs = plt.subplots(2, 2, figsize=(9.6, 6.7), dpi=120)
    fig.suptitle("Oxidation states count assigned electrons", fontsize=19, y=0.97)
    ax = axs[0, 0]
    panel(ax, "Water · H₂O", "O: 4 lone-pair e⁻ + 4 bonding e⁻ = 8")
    for x, symbol, state, count in [(0.42, "H", "+1", 0), (1.25, "O", "−2", 8),
                                     (2.08, "H", "+1", 0)]:
        atom(ax, x, 0.93, symbol, state, count)
    allocation(ax, (0.60, 0.93), (1.06, 0.93))
    allocation(ax, (1.90, 0.93), (1.44, 0.93))
    ax.text(1.25, 1.21, "O receives both O–H pairs", ha="center", fontsize=11)

    ax = axs[0, 1]
    panel(ax, "Hydrogen peroxide · H₂O₂", "Each O: 4 + 2 + 1 = 7 assigned e⁻")
    for x, symbol, state, count in [(0.28, "H", "+1", 0), (0.94, "O", "−1", 7),
                                     (1.56, "O", "−1", 7), (2.22, "H", "+1", 0)]:
        atom(ax, x, 0.93, symbol, state, count)
    allocation(ax, (0.45, 0.93), (0.76, 0.93))
    allocation(ax, (2.05, 0.93), (1.74, 0.93))
    ax.plot([1.12, 1.38], [0.93, 0.93], color="#34495e", lw=1.8)
    ax.text(1.25, 1.21, "O–O pair split equally", ha="center", fontsize=11)

    ax = axs[1, 0]
    panel(ax, "Molecular oxygen · O₂", "Equal allocation leaves 6 e⁻ on each O")
    atom(ax, 0.80, 0.93, "O", "0", 6)
    atom(ax, 1.70, 0.93, "O", "0", 6)
    ax.plot([0.98, 1.52], [0.93, 0.93], color="#34495e", lw=1.8)
    ax.text(1.25, 1.21, "Same element: equal splitting", ha="center", fontsize=11)

    ax = axs[1, 1]
    panel(ax, "Sodium hydride · NaH", "An ionic formula unit, not a molecule")
    atom(ax, 0.80, 0.93, "Na", "+1", 0)
    atom(ax, 1.70, 0.93, "H", "−1", 2)
    allocation(ax, (1.00, 0.93), (1.50, 0.93))
    ax.text(1.25, 1.21, "H receives the valence inventory", ha="center", fontsize=11)

    fig.text(0.5, 0.035, "OS = neutral valence count − assigned count   ·   Not measured partial charges",
             ha="center", fontsize=12, weight="bold")
    fig.subplots_adjust(left=0.015, right=0.985, top=0.90, bottom=0.095, hspace=0.12, wspace=0.02)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
