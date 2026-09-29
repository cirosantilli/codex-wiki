"""Original carbon bookkeeping and ideal conversion toy, not measured yields.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../saccharomyces-fermentation-carbon-balance.py
Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
Basis: C6H12O6 -> 2 C2H5OH + 2 CO2, with no biomass or other products.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch


def carbon_group(ax, x, y, count, color):
    for i in range(count):
        ax.add_patch(Circle((x + i * 0.29, y), 0.115, facecolor=color, edgecolor="#172c42"))
        ax.text(x + i * 0.29, y, "C", color="white", ha="center", va="center", fontsize=9, weight="bold")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig = plt.figure(figsize=(9.5, 6.8), dpi=120, facecolor="white")
    fig.suptitle("S. cerevisiae: where does glucose carbon go?", fontsize=17, weight="bold", y=0.97)
    ax = fig.add_axes([0.04, 0.59, 0.92, 0.29])
    ax.set(xlim=(0, 10), ylim=(0, 3))
    ax.axis("off")
    ax.text(5, 2.85, "Ideal alcoholic fermentation — carbon atoms counted, intermediates omitted", ha="center", fontsize=11)
    ax.add_patch(FancyBboxPatch((0.15, 0.45), 2.25, 1.65, boxstyle="round,pad=0.02", facecolor="#eef4fa", edgecolor="#39516b"))
    ax.text(1.275, 1.78, "1 glucose", ha="center", weight="bold")
    carbon_group(ax, 0.55, 1.20, 6, "#386b9e")
    ax.text(1.275, 0.68, "6 carbon atoms", ha="center", fontsize=10)
    ax.annotate("", xy=(3.42, 1.29), xytext=(2.53, 1.29), arrowprops={"arrowstyle": "->", "lw": 1.7})
    ax.text(2.98, 1.72, "enzymes", ha="center", fontsize=10)
    for x, label, count, color in [(3.55, "2 ethanol", 2, "#207567"), (6.93, "2 carbon dioxide", 1, "#bb651d")]:
        ax.add_patch(FancyBboxPatch((x, 0.45), 2.87, 1.65, boxstyle="round,pad=0.02", facecolor="white", edgecolor=color))
        ax.text(x + 1.435, 1.78, label, ha="center", weight="bold")
        carbon_group(ax, x + 0.65, 1.20, count, color)
        carbon_group(ax, x + 1.87, 1.20, count, color)
        ax.text(x + 1.435, 0.68, f"{2 * count} carbon atoms", ha="center", fontsize=10)
    ax.text(6.56, 1.26, "+", fontsize=18, ha="center")
    plot = fig.add_axes([0.13, 0.16, 0.71, 0.38])
    extent = np.linspace(0, 10, 101)
    plot.plot(extent, 10 - extent, color="#386b9e", lw=2.4, label="Glucose remaining")
    plot.plot(extent, 2 * extent, color="#207567", lw=3.5, label="Ethanol formed")
    plot.plot(extent, 2 * extent, color="#bb651d", lw=2.1, ls="--", label="CO₂ formed (same amount)")
    plot.scatter([10], [20], color="#bb651d", zorder=4, s=40)
    plot.set(xlim=(0, 10), ylim=(0, 22), xlabel="Glucose converted (mmol); initial amount = 10 mmol",
             ylabel="Amount (mmol)", title="Toy calculation: full conversion gives 20 mmol of each product")
    plot.set_xticks([0, 2, 4, 6, 8, 10])
    plot.set_yticks([0, 5, 10, 15, 20])
    plot.grid(alpha=0.2)
    plot.spines[["top", "right"]].set_visible(False)
    plot.legend(loc="upper left", fontsize=9.5)
    fig.text(0.5, 0.035, "No time axis, growth, respiration, side products or gas losses: theoretical bookkeeping, not a culture measurement.",
             ha="center", fontsize=9.5, color="#526477")
    fig.savefig(Path.cwd() / "saccharomyces-fermentation-carbon-balance.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
