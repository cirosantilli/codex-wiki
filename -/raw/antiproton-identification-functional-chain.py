"""Original functional schematic. Python 3.14; matplotlib 3.10.7.

Historical functions: Chamberlain et al., UCRL-3172, pp. 3–8;
Chamberlain, Nobel lecture (1959), pp. 496–501. Not a beamline drawing.
Run from _media; writes the matching PNG to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 5.5))
    ax.axis("off")
    ax.text(5, 5.16, "How a negative particle becomes an antiproton candidate",
            ha="center", fontsize=15, weight="bold", color="#172b40")
    ax.text(5, 4.82, "Functional identification chain • not a physical layout",
            ha="center", fontsize=11, color="#4c5968")

    def box(x, y, w, h, title, body, color):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                                   linewidth=1.4, edgecolor=color, facecolor="#f8fafc"))
        ax.text(x+w/2, y+h-0.23, title, ha="center", va="center", fontsize=12,
                weight="bold", color=color)
        ax.text(x+w/2, y+0.36, body, ha="center", va="center", fontsize=11,
                linespacing=1.45, color="#172b40")

    def arrow(a, b, color="#65758a"):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=16,
                                    linewidth=1.5, color=color))

    box(0.25, 3.14, 2.65, 1.12, "Prepare", "Bevatron protons\n→ copper target", "#245d88")
    box(3.66, 3.14, 2.65, 1.12, "Select", "Negative curvature\n+ momentum band", "#245d88")
    box(7.02, 3.14, 2.65, 1.12, "Time", "S1 → S2 delay\nScintillation pulses", "#245d88")
    arrow((2.98, 3.70), (3.57, 3.70))
    arrow((6.39, 3.70), (6.93, 3.70))
    box(7.02, 1.31, 2.65, 1.12, "Cross-check", "C2 velocity window\nC1 fast-particle guard", "#a75a16")
    arrow((8.34, 3.06), (8.34, 2.51))
    box(3.66, 1.31, 2.65, 1.12, "Infer", "Negative charge\n+ proton mass", "#267254")
    arrow((6.93, 1.87), (6.39, 1.87), "#267254")
    box(0.25, 1.31, 2.65, 1.12, "Control", "Reverse field: protons\nScan mass settings", "#784f8c")
    arrow((2.98, 1.87), (3.57, 1.87), "#784f8c")
    ax.text(5, 0.73, "Photographed pulse traces expose accidental coincidences.",
            ha="center", fontsize=11, color="#172b40")
    ax.text(5, 0.35, "Curvature + velocity identify mass; annihilation is a separate test.",
            ha="center", fontsize=11, color="#172b40")
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
