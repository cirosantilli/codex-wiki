"""Draw chosen species inventories; run from _media to write the PNG there.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Every marker denotes the same chosen amount, rather than a literal molecule.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 5.2), dpi=120)
    cases = [
        ("Strong: small inventory", 2, 2, 0, "2 units dissolved; all converted", "100% converted; 4 ionic units"),
        ("Weak: larger inventory", 5, 5, 15, "20 units dissolved; 5 converted", "25% converted; 10 ionic units"),
        ("Nonelectrolyte", 0, 0, 20, "20 units dissolved; none converted", "0% converted; 0 ionic units"),
    ]
    for ax, (title, positive, negative, neutral, inventory, tally) in zip(axes, cases):
        ax.set(xlim=(0, 5), ylim=(0, 6.5), aspect="equal")
        ax.axis("off")
        ax.set_title(title, fontsize=12, fontweight="bold", pad=12)
        ax.add_patch(Rectangle((0.1, 0.85), 4.8, 5.0, facecolor="#fbfcfe", edgecolor="#536174", linewidth=1.5))
        species = [("+", "#d95e39")] * positive + [("−", "#3278b5")] * negative + [("N", "#647684")] * neutral
        # A neutral parent unit yields one positive and one negative ion.
        assert neutral + positive == (2 if positive == 2 else 20)
        assert positive == negative
        for index, (label, color) in enumerate(species):
            col, row = index % 5, index // 5
            x, y = 0.58 + col * 0.96, 5.30 - row * 0.91
            ax.add_patch(Circle((x, y), 0.30, facecolor=color, edgecolor="white", linewidth=0.8))
            ax.text(x, y, label, ha="center", va="center", color="white", fontsize=13, fontweight="bold")
        ax.text(2.5, 0.45, inventory, ha="center", fontsize=10)
        ax.text(2.5, 0.05, tally, ha="center", fontsize=10, fontweight="bold")
    fig.suptitle("Converted fraction and ion amount are different", fontsize=16, y=0.97)
    fig.text(0.5, 0.115, "Equal solution volumes • one-to-one ion production • solvent omitted", ha="center", fontsize=11)
    fig.text(0.5, 0.037, "+ / − = ions; N = neutral unit. Each marker represents the same chosen amount.\nStipulated schematic inventories, not measured material data.", ha="center", fontsize=10, linespacing=1.4)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.86, bottom=0.17, wspace=0.14)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
