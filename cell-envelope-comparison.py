"""Generate cell-envelope-comparison.png in CWD; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle


MEMBRANE = "#c5e1f2"
WALL = "#f8d59c"
OUTER = "#ddd0ed"
INK = "#233747"
# Layer order is exterior to cytoplasm; the sizes below are schematic only.
ENVELOPES = [
    ("Typical Gram-positive bacterium", [("Peptidoglycan wall", WALL, 0.29),
     ("Cell membrane", MEMBRANE, 0.13)], "Thick supporting mesh"),
    ("Typical Gram-negative bacterium", [("Outer membrane", OUTER, 0.13),
     ("Peptidoglycan wall", WALL, 0.12), ("Cell membrane", MEMBRANE, 0.13)],
     "Wall between two membranes"),
    ("Representative plant cell", [("Wall: cellulose composite", WALL, 0.29),
     ("Cell membrane", MEMBRANE, 0.13)], "Composition varies with cell type"),
    ("Representative fungal cell", [("Wall: chitin + glucans", WALL, 0.29),
     ("Cell membrane", MEMBRANE, 0.13)], "A composite, not pure chitin"),
    ("One archaeal example", [("Protein-based wall", WALL, 0.29),
     ("Cell membrane", MEMBRANE, 0.13)], "Other wall types exist; no peptidoglycan"),
    ("Representative animal cell", [("Cell membrane", MEMBRANE, 0.13)],
     "No cell wall"),
]


def main():
    plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(2, 3, figsize=(11.2, 7.2), dpi=100)
    fig.patch.set_facecolor("white")
    fig.suptitle("Cell envelopes: shared boundaries, different walls", fontsize=18,
                 color=INK, y=0.965)
    for ax, (title, layers, note) in zip(axes.flat, ENVELOPES):
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis("off")
        ax.set_title(title, fontsize=11, fontweight="bold", color=INK, pad=10)
        bottom = 0.20
        ax.add_patch(Rectangle((0.06, 0.07), 0.88, 0.13, color="#f0f4f6"))
        ax.text(0.5, 0.13, "Cytoplasm", ha="center", va="center", color=INK)
        for label, color, height in reversed(layers):
            ax.add_patch(Rectangle((0.06, bottom), 0.88, height,
                                  facecolor=color, edgecolor=INK, linewidth=1.1))
            ax.text(0.5, bottom + height / 2, label, ha="center", va="center", color=INK)
            bottom += height
            # Visible separation in the two-membrane bacterial example.
            if title == "Typical Gram-negative bacterium":
                bottom += 0.035
        ax.text(0.5, 0.84, "Exterior", ha="center", color=INK)
        ax.annotate("", (0.03, 0.22), (0.03, 0.77),
                    arrowprops={"arrowstyle": "->", "color": INK, "lw": 1.3})
        ax.text(0.5, -0.06, note, ha="center", color=INK, fontsize=9)
    fig.legend(handles=[Patch(facecolor=MEMBRANE, edgecolor=INK, label="Cell membrane"),
                        Patch(facecolor=WALL, edgecolor=INK, label="Supporting wall"),
                        Patch(facecolor=OUTER, edgecolor=INK, label="Additional outer membrane")],
               loc="lower center", bbox_to_anchor=(0.5, 0.045), ncol=3, frameon=False)
    fig.text(0.5, 0.025, "Layer order only: thicknesses are unscaled; these examples do not exhaust variation.",
             ha="center", fontsize=10, color=INK)
    fig.subplots_adjust(left=0.03, right=0.98, top=0.86, bottom=0.17, hspace=0.48, wspace=0.13)
    fig.savefig(Path.cwd() / "cell-envelope-comparison.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
