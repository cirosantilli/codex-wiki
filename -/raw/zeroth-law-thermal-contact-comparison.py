"""Draw equilibrium comparisons; Python 3.14, matplotlib 3.10.7.

Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10.4, 6.1), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 10.4), ylim=(0, 6.1))
    ax.axis("off")
    blue, red, ink = "#2274a5", "#b55236", "#223344"

    def box(x, y, name, temperature, color=blue):
        ax.add_patch(FancyBboxPatch((x, y), 1.3, 1.05,
                                   boxstyle="round,pad=0.06", facecolor="#f2f7fa",
                                   edgecolor=color, linewidth=1.8))
        ax.text(x + .65, y + .7, name, ha="center", color=ink,
                weight="bold", fontsize=15)
        ax.text(x + .65, y + .28, temperature, ha="center", color=color)

    def contact(x1, x2, y):
        ax.plot([x1, x2], [y, y], color=blue, linewidth=3)
        ax.text((x1 + x2) / 2, y + .23, "Thermal\ncontact", ha="center",
                color=blue, fontsize=11)

    ax.text(5.2, 5.82, "Use the same equilibrium reference state", ha="center",
            va="center", fontsize=17, weight="bold", color=ink)
    ax.text(2.5, 5.17, "1. Compare A with C", ha="center", weight="bold")
    ax.text(7.85, 5.17, "2. Compare B with C", ha="center", weight="bold")
    box(.55, 3.85, "A", "25 °C")
    box(3.4, 3.85, "C", "25 °C")
    contact(1.91, 3.34, 4.25)
    box(5.9, 3.85, "B", "25 °C")
    box(8.75, 3.85, "C", "25 °C")
    contact(7.26, 8.69, 4.25)
    ax.text(2.6, 3.51, r"$A\sim C$", ha="center", color=blue, fontsize=16)
    ax.text(7.9, 3.51, r"$B\sim C$", ha="center", color=blue, fontsize=16)
    ax.axhline(3.13, xmin=.03, xmax=.97, color="#cdd5dd", linewidth=1)
    ax.text(2.6, 2.73, r"Zeroth law predicts $A\sim B$", ha="center",
            color=blue, weight="bold", fontsize=14)
    ax.text(7.8, 2.73, "Insulation alone supplies no test", ha="center",
            color=red, weight="bold", fontsize=14)
    box(.55, 1.16, "A", "25 °C")
    box(3.4, 1.16, "B", "25 °C")
    contact(1.91, 3.34, 1.58)
    box(5.9, 1.16, "D", "300 K", color=red)
    box(8.75, 1.16, "E", "350 K", color=red)
    ax.plot([7.26, 7.63], [1.58, 1.58], color=red, linewidth=2)
    ax.plot([8.23, 8.69], [1.58, 1.58], color=red, linewidth=2)
    ax.add_patch(Rectangle((7.7, 1.13), .46, 1.12, facecolor="#fcf2ee",
                           edgecolor=red, hatch="////", linewidth=1.8))
    ax.text(7.94, 2.39, "Rigid adiabatic wall", color=red, ha="center", fontsize=11)
    ax.text(2.6, .72, "No net heat transfer\nthrough an allowed thermal path",
            ha="center", color=blue, linespacing=1.5)
    ax.text(7.9, .72, "No heat transfer: path blocked\nTemperatures may differ",
            ha="center", color=red, linespacing=1.5)
    ax.text(5.2, .13, "Illustrative equilibrium states • rigid boundaries • no matter transfer or boundary work",
            ha="center", fontsize=10, color="#566575")
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
