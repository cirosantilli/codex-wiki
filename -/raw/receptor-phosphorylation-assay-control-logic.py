"""Draw assay inference and controls; write the matching PNG to the CWD.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
This is a reasoning diagram, not a blot image or a measured time course.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def box(ax, x, y, width, height, text, color="#216a94", size=11):
    ax.add_patch(FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.10",
                               edgecolor=color, facecolor="white", lw=1.8))
    ax.text(x + width / 2, y + height / 2, text, ha="center", va="center", fontsize=size, color="#23313c")


def arrow(ax, start, end):
    ax.annotate("", end, start, arrowprops={"arrowstyle": "->", "lw": 1.7, "color": "#52616b"})


def main():
    fig, ax = plt.subplots(figsize=(10.4, 7.2))
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.03, right=0.97, top=0.91, bottom=0.06)
    ax.set(xlim=(0, 12), ylim=(0, 10))
    ax.axis("off")
    fig.suptitle("A phosphorylation readout needs several independent controls", y=0.975, fontsize=15)
    box(ax, 0.2, 8.0, 3.2, 1.25, "Matched samples\nligand omitted / added")
    box(ax, 4.4, 8.0, 3.2, 1.25, "Stop reactions at sampling\npreserve phosphorylation")
    box(ax, 8.6, 8.0, 3.2, 1.25, "Separate / detect\nphospho + total receptor")
    arrow(ax, (3.5, 8.6), (4.25, 8.6))
    arrow(ax, (7.7, 8.6), (8.45, 8.6))
    controls = [
        (0.2, "Receptor identity", "Receptor loss + independent antibody\nIs this the intended protein?", "#216a94"),
        (4.4, "Phosphate-dependent epitope", "Phosphatase-treated sample\nwith retained total receptor", "#b34f18"),
        (8.6, "Detection / abundance", "Loading, transfer, background\nand usable response range", "#287c61"),
    ]
    for x, title, text, color in controls:
        ax.text(x + 1.6, 7.0, title, ha="center", fontsize=11, weight="bold", color=color)
        box(ax, x, 5.35, 3.2, 1.2, text, color, 10)
        arrow(ax, (x + 1.6, 5.15), (x + 1.6, 4.55))
    box(ax, 0.2, 3.25, 11.6, 1.1,
        "After appropriate controls: a ligand-associated change in detected receptor phosphorylation\nA phospho / total-receptor ratio can track relative modification within a linear response range.", size=11)
    arrow(ax, (6.0, 3.05), (6.0, 2.55))
    box(ax, 0.2, 0.6, 5.45, 1.65, "Mechanistic follow-up\nKinase perturbation, phosphate removal,\nand direct activity / recruitment tests", "#216a94", 11)
    box(ax, 6.35, 0.6, 5.45, 1.65, "Remaining ambiguity\nSignal depends on addition AND removal.\nPhosphorylation alone is not catalytic flux.", "#b34f18", 11)
    fig.text(0.5, 0.025, "Original control logic; no bands, measurements, experimental outcomes or timing are drawn.", ha="center", fontsize=10)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(output.name)


if __name__ == "__main__":
    main()
