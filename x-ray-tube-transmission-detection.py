"""Draw an original modern X-ray source and narrow-beam detection schematic.

Tested with Python 3.14, matplotlib 3.10.7; run from _media.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(11, 5.1), dpi=120, facecolor="white")
    ax.set(xlim=(0, 12), ylim=(0, 5.1))
    ax.axis("off")
    blue, orange, grey = "#1768a2", "#b64a18", "#40464d"

    def arrow(start, end, color, **kwargs):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=15, color=color,
                                    linewidth=2, **kwargs))

    ax.text(6, 4.85, "X-ray tube → sample → detector", ha="center",
            fontsize=18, weight="bold")
    ax.text(6, 4.43, "Modern source and ideal narrow-beam measurement • schematic, not to scale",
            ha="center", color=grey, fontsize=10)
    ax.add_patch(FancyBboxPatch((0.35, 1.7), 4.55, 2.1,
                               boxstyle="round,pad=0.04,rounding_size=0.3",
                               facecolor="#f2f7fa", edgecolor=blue, linewidth=1.8))
    ax.text(2.5, 3.95, "evacuated envelope", ha="center", color=blue)
    ax.plot([1.0, 1.10, 1.20, 1.30, 1.40, 1.50, 1.60],
            [2.6, 2.95, 2.6, 2.95, 2.6, 2.95, 2.6], color=orange, lw=2.5)
    ax.text(1.3, 2.25, "heated\ncathode (−)", ha="center", color=orange)
    arrow((1.8, 2.82), (3.6, 2.82), orange)
    ax.text(2.7, 3.04, "electrons", ha="center", color=orange)
    ax.add_patch(Polygon([(3.6, 2.27), (4.2, 3.35), (4.42, 3.35), (4.42, 2.27)],
                         facecolor="#6e7379", edgecolor=grey))
    ax.text(4.03, 2.0, "target anode (+)", ha="center", fontsize=10)
    ax.text(2.55, 1.32, "Accelerating voltage V supplies energy eV per electron",
            ha="center", fontsize=10)
    arrow((3.91, 2.82), (10.95, 2.82), blue)
    ax.text(5.25, 3.06, "X-rays", ha="center", color=blue)
    for x in (5.8, 9.7):
        for y in (2.0, 2.99):
            ax.add_patch(Rectangle((x, y), 0.25, 0.65, facecolor=grey))
    ax.text(6.0, 3.85, "aperture", ha="center", fontsize=10)
    ax.add_patch(Rectangle((7.45, 2.05), 0.55, 1.55,
                           facecolor="#f5dda7", edgecolor="#87642a", linewidth=1.5))
    ax.text(7.72, 3.85, "sample", ha="center")
    ax.annotate("", (7.45, 1.87), (8.0, 1.87),
                arrowprops={"arrowstyle": "<->", "color": grey})
    ax.text(7.72, 1.58, "thickness x", ha="center", fontsize=10)
    arrow((7.78, 2.82), (9.76, 3.43), "#999999", linestyle="--")
    ax.text(9.7, 4.01, "scatter rejected", ha="center", fontsize=10, color=grey)
    ax.add_patch(Rectangle((11.0, 2.2), 0.45, 1.3,
                           facecolor="#c8e7dd", edgecolor="#25795f", linewidth=1.5))
    ax.text(11.2, 3.8, "detector", ha="center")
    ax.text(8.7, 0.83, r"Empty path: $R_0$     Sample: $R$     Background: $b$",
            ha="center", fontsize=11)
    ax.text(8.7, 0.32, r"Transmission: $T=(R-b)/(R_0-b)$", ha="center",
            fontsize=13, color=blue)
    fig.subplots_adjust(left=0.015, right=0.985, bottom=0.035, top=0.985)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
