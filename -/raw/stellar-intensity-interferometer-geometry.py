"""Original functional stellar intensity interferometer; Python 3.14, matplotlib 3.10.7.

Run from _media: writes this script's basename.png in the current directory.
Schematic geometry and signal flow, not a reconstruction or measured data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11, 8), facecolor="white")
    ax = fig.add_axes((0.035, 0.04, 0.93, 0.87))
    ax.set(xlim=(0, 12), ylim=(0, 10))
    ax.axis("off")
    blue, orange, ink = "#176b94", "#bd6020", "#25333b"

    def arrow(start, end, color=ink, style="-|>", **kw):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                    mutation_scale=13, color=color, lw=1.6, **kw))

    def box(x, y, w, h, label, color=blue):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                                   facecolor="white", edgecolor=color, lw=1.6))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", color=ink)

    ax.add_patch(Circle((6, 8.95), 0.52, facecolor="#ffe2a4", edgecolor=orange, lw=1.5))
    ax.text(6, 9.77, "Distant thermal star: angular diameter θ", ha="center", color=ink)
    ax.text(6, 8.94, "disk", ha="center", va="center")
    # Almost parallel rays: the plotted angular spread is enlarged for readability.
    for x in (2.0, 10.0):
        arrow((x - 0.24, 8.20), (x - 0.24, 6.55), color=orange)
        arrow((x + 0.24, 8.20), (x + 0.24, 6.55), color=orange)
        ax.plot([x - 0.65, x, x + 0.65], [6.55, 6.25, 6.55], color=blue, lw=3)
    ax.text(6, 7.62, "Wavefront samples at two collectors\nReference direction normal to baseline", ha="center", color=ink)
    arrow((2, 5.95), (10, 5.95), style="<->")
    ax.text(6, 6.14, r"Projected baseline $B=|\mathbf{b}_\perp|$", ha="center")
    ax.text(2, 5.59, "Collector 1", ha="center", color=blue)
    ax.text(10, 5.59, "Collector 2", ha="center", color=blue)
    for x in (2, 10):
        arrow((x, 5.30), (x, 4.94), color=orange)
        box(x - 1.5, 4.20, 3, 0.65, "Matched optical band\n+ selected polarization", orange)
        arrow((x, 4.13), (x, 3.74), color=orange)
        box(x - 1.5, 3.01, 3, 0.65, "Photodetector → photocurrent")
        arrow((x, 2.94), (x, 2.55))
        box(x - 1.5, 1.81, 3, 0.65,
            "Response + mean removal" if x == 2 else "Response + mean removal\n+ delay compensation")
    box(4.35, 1.81, 3.3, 0.65, r"Multiply $\delta i_1(t)\,\delta i_2(t+\tau)$")
    arrow((3.57, 2.135), (4.26, 2.135))
    arrow((8.43, 2.135), (7.74, 2.135))
    arrow((6, 1.74), (6, 1.33))
    box(3.35, 0.59, 5.3, 0.65, "Average → calibrated correlation versus B")
    ax.text(6, 0.12, "Orange: light     Blue / dark: detection and electronics     Schematic; no optical beam recombination",
            ha="center", va="center", fontsize=10)
    fig.suptitle("Stellar intensity interferometry: correlate after detection", fontsize=16, y=0.965)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
