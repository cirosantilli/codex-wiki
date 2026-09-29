"""Show ion drift and conventional current; write basename.png to CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Uniform-field bulk toy model in a driven electrolytic cell. No diffusion,
convection, or electrode boundary layers. Arrow lengths are schematic.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def arrow(ax, start, end, y, color, width=2.5):
    ax.annotate("", xy=(end, y), xytext=(start, y),
                arrowprops={"arrowstyle": "-|>", "color": color,
                            "lw": width, "mutation_scale": 17})


def main():
    elementary_charge = 1.602176634e-19
    n = np.array([1e25, 1e25])
    q = elementary_charge * np.array([1.0, -1.0])
    vx = np.array([2e-4, -3e-4])
    jx = n * q * vx
    blue, orange = "#236d99", "#b6531f"
    fig, ax = plt.subplots(figsize=(10, 6.6))
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.14, top=0.86)
    for x in (0.6, 9.0):
        ax.add_patch(Rectangle((x, 3.1), 0.4, 3.0, facecolor="#dddddd",
                               edgecolor="#555555", linewidth=1.4))
    ax.text(0.8, 6.35, "+ anode\nOxidation", ha="center", fontsize=12)
    ax.text(9.2, 6.35, "− cathode\nReduction", ha="center", fontsize=12)
    arrow(ax, 3.6, 6.4, 5.9, "#333333")
    ax.text(5.0, 6.12, "Uniform electric field E →", ha="center", fontsize=12)
    ax.scatter([3.2, 6.8], [4.9, 3.8], s=650, c=[blue, orange],
               edgecolors="white", linewidths=1)
    ax.text(3.2, 4.9, "+", color="white", ha="center", va="center", fontsize=19)
    ax.text(6.8, 3.8, "−", color="white", ha="center", va="center", fontsize=19)
    arrow(ax, 3.65, 7.5, 4.9, blue)
    arrow(ax, 6.35, 2.5, 3.8, orange)
    ax.text(4.7, 5.22, "Cation drift: v₊,ₓ > 0", color=blue, fontsize=12,
            ha="center")
    ax.text(5.3, 4.12, "Anion drift: v₋,ₓ < 0", color=orange, fontsize=12,
            ha="center")
    ax.plot([1.4, 8.6], [2.9, 2.9], color="#cccccc", lw=1)
    ax.text(5.0, 2.56, "Conventional current contributions: n q vₓ", ha="center",
            fontsize=13, weight="bold")
    for k, (y, color, sign) in enumerate([(1.85, blue, "+"), (0.8, orange, "−")]):
        ax.text(1.5, y + 0.23, f"q = {sign}e", color=color, fontsize=12)
        arrow(ax, 3.5, 7.7, y, color)
        ax.text(5.6, y + 0.23, f"J{'₊' if k == 0 else '₋'},ₓ = {jx[k]:.6f} A/m² > 0",
                color=color, fontsize=12, ha="center")
    ax.text(5.0, 0.08, f"Both point right: total Jₓ = {jx.sum():.6f} A/m²",
            ha="center", fontsize=12, weight="bold")
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.2, 7.0)
    ax.axis("off")
    fig.suptitle("Opposite ion motion, same conventional current", fontsize=17, y=0.97)
    fig.text(0.5, 0.905, "Driven electrolytic cell: external source fixes the electrode signs",
             ha="center", fontsize=12)
    fig.text(0.5, 0.065, "Toy inputs: n₊ = n₋ = 10²⁵ m⁻³; v₊,ₓ = +2 × 10⁻⁴ m/s; v₋,ₓ = −3 × 10⁻⁴ m/s.",
             ha="center", fontsize=10.5)
    fig.text(0.5, 0.03, "Uniform bulk field; no diffusion or convection; schematic arrow lengths.",
             ha="center", fontsize=10.5, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
