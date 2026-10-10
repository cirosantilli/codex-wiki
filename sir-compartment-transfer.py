"""Draw closed SIR transfers; write basename PNG to the current directory.

Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Run from _media: python3 ../sir-compartment-transfer.py
All parameters are stipulated teaching values, not disease estimates.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 4.6), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 4.6))
    ax.axis("off")
    ax.text(5, 4.28, "Closed SIR model: transfers preserve the total", ha="center",
            fontsize=17, weight="bold")
    labels = [(0.25, "Susceptible", "$s$", "Can acquire infection", "#e5f0fb"),
              (3.85, "Infectious", "$i$", "Can transmit infection", "#fde8dc"),
              (7.45, "Removed", "$r$", "No further transmission", "#e4f3e9")]
    for x, title, symbol, explanation, color in labels:
        ax.add_patch(FancyBboxPatch((x, 2.05), 2.3, 1.3,
                                   boxstyle="round,pad=0.06", facecolor=color,
                                   edgecolor="#344054", linewidth=1.5))
        ax.text(x + 1.15, 3.03, title, ha="center", fontsize=14, weight="bold")
        ax.text(x + 1.15, 2.59, symbol, ha="center", fontsize=23)
        ax.text(x + 1.15, 1.75, explanation, ha="center", fontsize=10.5)
    for left, right, formula, label in [
        (2.62, 3.75, r"$\beta si$", "New infections"),
        (6.22, 7.35, r"$\gamma i$", "Removal")
    ]:
        center = (left + right) / 2
        ax.annotate("", xy=(right, 2.7), xytext=(left, 2.7),
                    arrowprops={"arrowstyle": "-|>", "lw": 2, "color": "#344054"})
        ax.text(center, 3.08, formula, ha="center", fontsize=17)
        ax.text(center, 3.62, label, ha="center", fontsize=10.5)
    ax.text(5, 1.19, r"Fractions: $s+i+r=1$     |     Rates: $\beta,\gamma$ in day$^{-1}$",
            ha="center", fontsize=13)
    ax.text(5, 0.75, "At the start: 0.00297/day enters i; 0.00100/day leaves i",
            ha="center", fontsize=12)
    ax.text(5, 0.32, r"Example: $\beta=0.3$/day, $\gamma=0.1$/day, $(s_0,i_0,r_0)=(0.99,0.01,0)$",
            ha="center", fontsize=11, color="#475467")
    fig.subplots_adjust(left=0.015, right=0.985, top=0.98, bottom=0.02)
    target = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(target, facecolor="white", transparent=False)
    plt.close(fig)
    print(target)


if __name__ == "__main__":
    main()
