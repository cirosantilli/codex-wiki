"""Draw qualitative mitochondrial routes; emit the matching PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


def main():
    fig, ax = plt.subplots(figsize=(12, 6.3), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 7.4))
    ax.axis("off")
    blue, orange, green = "#2466a1", "#c86612", "#24845c"

    def label(x, y, text, size=12, color="#24313d", **kw):
        return ax.text(x, y, text, ha="center", va="center", fontsize=size,
                       color=color, **kw)

    def arrow(a, b, color, style="-", curve=0):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=15,
                                    lw=2, color=color, linestyle=style,
                                    connectionstyle=f"arc3,rad={curve}"))

    def complex_box(x, y, name, color="#eaf0f6", w=0.85, h=1.5):
        ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
                                   boxstyle="round,pad=0.06", facecolor=color,
                                   edgecolor="#4d6173", lw=1.5))
        label(x, y, name, 14, weight="bold")

    label(6, 7.08, "Mitochondrial electron and proton routes", 18, weight="bold")
    ax.add_patch(Rectangle((0.3, 3.0), 11.4, 2.0, facecolor="#f6f0df",
                           edgecolor="#bcae88", lw=1.2))
    label(6, 5.9, "INTERMEMBRANE SPACE", 13, weight="bold")
    label(6, 2.6, "MITOCHONDRIAL MATRIX", 13, weight="bold")
    label(3.6, 5.3, "inner mitochondrial membrane", 11, color="#766a4c")

    complex_box(1.75, 4.0, "I")
    complex_box(3.35, 3.65, "II", w=0.7, h=0.65)
    complex_box(6.05, 4.0, "III")
    complex_box(8.65, 4.0, "IV")
    complex_box(10.65, 4.0, "ATP\nsynthase", color="#e8f3eb", w=1.2)

    label(0.7, 4.5, "NADH", 11, blue)
    arrow((0.35, 4.18), (1.25, 4.18), blue)
    label(4.6, 4.25, "Q", 15, blue, weight="bold")
    arrow((2.25, 4.25), (4.3, 4.25), blue)
    arrow((4.85, 4.25), (5.55, 4.25), blue)
    label(7.4, 5.35, "cytochrome c", 11, blue)
    arrow((6.48, 4.65), (7.2, 5.13), blue)
    arrow((7.7, 5.13), (8.25, 4.65), blue)
    label(3.35, 1.9, "succinate\noxidation", 11, blue)
    arrow((3.35, 2.3), (3.35, 3.27), blue)
    arrow((3.77, 3.65), (4.46, 4.04), blue)
    label(3.35, 1.2, "II does not pump H⁺", 11)
    arrow((8.65, 3.23), (8.65, 2.15), blue)
    label(8.65, 1.68, "O₂ + chemical H⁺\n→ H₂O", 12, blue)

    for x in (1.45, 5.75, 8.35):
        arrow((x, 3.0), (x, 5.6), orange)
        label(x-0.3, 5.55, "H⁺", 12, orange)
    arrow((11.2, 5.55), (11.2, 2.55), green)
    label(11.5, 5.52, "H⁺", 12, green)
    label(10.65, 1.7, "ADP + Pᵢ → ATP", 12, green)
    label(10.65, 1.14, "proton return", 11, green)

    for x, color, text in ((1.25, blue, "electron route"),
                           (5.1, orange, "outward H⁺ transfer"),
                           (9.4, green, "return through ATP synthase")):
        arrow((x-0.7, 0.5), (x-0.15, 0.5), color)
        ax.text(x, 0.5, text, va="center", fontsize=10.5, color=color)
    label(6, 0.05, "Qualitative schematic: no transport counts or rates are encoded.", 10)
    fig.subplots_adjust(left=0.015, right=0.985, top=0.97, bottom=0.035)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
