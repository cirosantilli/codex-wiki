"""Original schematic; write an opaque white basename PNG in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Arrows encode N-to-C sequence direction. Dashed links are generic symbols,
not atomic positions, measured bond angles, or an exact residue registry.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.8), facecolor="white")
    colors = ("#217a9e", "#b35d23", "#217a9e")
    panels = (("Parallel", (1, 1, 1)), ("Antiparallel", (1, -1, 1)))
    for ax, (title, directions) in zip(axes, panels):
        ax.set_facecolor("white")
        ax.set_title(title, fontsize=16, pad=10)
        for y in (0.8, 1.8):
            for x in (1.2, 2.0, 2.8, 3.6):
                ax.plot((x, x), (y + 0.19, y + 0.81),
                        color="#777777", lw=1.6, linestyle=(0, (3, 3)), zorder=1)
        for y, direction, color in zip((2.8, 1.8, 0.8), directions, colors):
            start = 0.85 if direction == 1 else 3.95
            ax.add_patch(FancyArrow(start, y, direction * 3.1, 0,
                                    width=0.27, head_width=0.56, head_length=0.45,
                                    length_includes_head=True, color=color, zorder=2))
            left, right = ("N-side", "C-side") if direction == 1 else ("C-side", "N-side")
            ax.text(0.62, y, left, ha="right", va="center", fontsize=10)
            ax.text(4.18, y, right, ha="left", va="center", fontsize=10)
        ax.text(2.4, 0.14, "Each arrow follows N → C sequence order", ha="center", fontsize=10)
        ax.set_xlim(-0.18, 4.98)
        ax.set_ylim(-0.08, 3.35)
        ax.axis("off")
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.22, top=0.82, wspace=0.17)
    fig.suptitle("Beta-sheet strand directions", fontsize=18, y=0.97)
    fig.text(0.5, 0.10, "Dashed links: schematic interstrand backbone hydrogen bonds",
             ha="center", fontsize=11, color="#555555")
    fig.text(0.5, 0.045, "No atoms, exact bond angles or chain connections are represented.",
             ha="center", fontsize=10, color="#555555")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
