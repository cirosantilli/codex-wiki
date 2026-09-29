"""Original functional diagram, not an apparatus drawing or measured data.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; emits bose-condensation-apparatus-stages.png in CWD.
Historical basis: Anderson et al., Science 269, 198 (1995), Fig. 1;
Davis et al., PRL 75, 3969 (1995), pp. 3969–3972.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 6.2), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.2))
    ax.axis("off")
    blue, orange, ink = "#2166ac", "#b35806", "#183042"

    def box(x, y, w, h, title, detail, color=blue):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.10",
                                   facecolor="#f6f9fc", edgecolor=color, linewidth=1.5))
        ax.text(x + w/2, y + h - .29, title, ha="center", va="center",
                fontsize=12, weight="bold", color=color)
        ax.text(x + w/2, y + .38, detail, ha="center", va="center",
                fontsize=10.5, color=ink, linespacing=1.45)

    def arrow(start, end):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=16,
                                    linewidth=1.4, color=ink))

    ax.text(5, 5.94, "Making a dilute-gas Bose condensate visible", ha="center",
            fontsize=17, weight="bold", color=ink)
    ax.text(5, 5.56, "Functional stages • 1995 experiments • schematic, not to scale",
            ha="center", fontsize=11, color=ink)
    box(.3, 4.1, 2.45, 1.06, "1  Prepare", "Laser cooling\nMagneto-optical trap")
    box(3.1, 4.1, 3.0, 1.06, "2  Confine", "Magnetic trapping\nProtect atoms near field zero")
    box(6.5, 4.1, 3.15, 1.06, "3  Evaporate", "RF removes energetic atoms\nCollisions rethermalize")
    arrow((2.87, 4.63), (2.99, 4.63))
    arrow((6.22, 4.63), (6.39, 4.63))
    box(2.9, 2.44, 3.1, 1.02, "Rubidium route", "Quadrupole field\n+ rotating bias", blue)
    box(6.5, 2.44, 3.15, 1.02, "Sodium route", "Quadrupole field\n+ repulsive optical plug", orange)
    arrow((4.6, 3.99), (4.45, 3.58))
    arrow((5.8, 3.99), (7.85, 3.58))
    ax.text(.35, 3.08, "Two solutions\nto trap loss", ha="left", va="center",
            fontsize=12, color=ink, weight="bold")
    box(.3, .6, 2.7, 1.1, "4  Release", "Expand cloud\nResolve velocity structure")
    box(3.55, .6, 2.7, 1.1, "5  Image", "Probe light → cloud → camera\nAbsorption gives column density")
    box(6.8, .6, 2.85, 1.1, "6  Compare", "Broad wings + narrow core\nVary final RF cut")
    arrow((8.08, 3.99), (8.08, 3.73))
    ax.plot([8.08, 9.91, 9.91, 1.65, 1.65], [3.73, 3.73, 2.04, 2.04, 1.84],
            color=ink, linewidth=1.2)
    arrow((1.65, 1.84), (1.65, 1.80))
    arrow((3.11, 1.15), (3.43, 1.15))
    arrow((6.36, 1.15), (6.68, 1.15))
    ax.text(5, .12, "Rubidium release included decompression and a gravity-supporting gradient.",
            ha="center", fontsize=10, color=ink)
    fig.subplots_adjust(left=.015, right=.985, top=.985, bottom=.02)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
