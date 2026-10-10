"""Draw a functional InGaN LED, not a historical device reconstruction.

Run from _media; Python 3.14, matplotlib 3.10.7. Opaque white output.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(11, 7), dpi=120, facecolor="white")
    ax.set(xlim=(0, 11), ylim=(0, 7))
    ax.axis("off")
    fig.subplots_adjust(left=0.015, right=0.985, bottom=0.025, top=0.98)
    ax.text(0.3, 6.65, "Blue LED: electrical injection → light → readout", size=18, weight="bold")
    ax.text(0.3, 6.25, "Representative quantum-well structure; layer thicknesses not to scale", color="#53616d")

    def arrow(start, end, color="#253749", lw=2, style="-|>"):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=15,
                                    color=color, linewidth=lw))

    layers = [
        (1.55, 0.65, "Sapphire substrate", "#e6e1ef"),
        (2.20, 0.35, "Buffer: prepares growth", "#d6c3a7"),
        (2.55, 0.80, "n-GaN: electron supply", "#d5e7fa"),
        (3.35, 0.45, "InGaN active quantum well(s)", "#c4d3ff"),
        (3.80, 0.45, "p-AlGaN: carrier confinement", "#f8dfbb"),
        (4.25, 0.70, "p-GaN: hole supply", "#f8e8cf"),
    ]
    for y, height, label, color in layers:
        ax.add_patch(Rectangle((1.1, y), 5.0, height, facecolor=color, edgecolor="#65717b"))
        ax.text(3.6, y + height / 2, label, ha="center", va="center")
    ax.add_patch(Rectangle((1.1, 4.95), 1.2, 0.16, facecolor="#7b838b"))
    ax.add_patch(Rectangle((0.5, 2.65), 0.6, 0.16, facecolor="#7b838b"))
    ax.text(0.4, 5.32, "p contact (+)", size=10)
    ax.text(0.08, 2.95, "n contact (−)", size=10)
    ax.plot([1.7, 1.7, 0.25, 0.25, 1.4],
            [5.11, 5.72, 5.72, 0.69, 0.69], color="#394651", lw=1.6)
    ax.plot([0.8, 0.8, 6.6, 6.6, 6.1],
            [2.65, 1.20, 1.20, 0.69, 0.69], color="#394651", lw=1.6)
    ax.add_patch(FancyBboxPatch((1.4, 0.38), 4.7, 0.62, boxstyle="round,pad=0.12",
                               facecolor="white", edgecolor="#394651"))
    ax.text(3.75, 0.69, "Drive current I; measure terminal voltage V", ha="center", va="center", size=10)
    # Carrier arrows are schematic supply routes, not conventional current arrows.
    arrow((5.6, 2.77), (5.6, 3.47), "#285caa")
    arrow((5.6, 4.78), (5.6, 3.67), "#ab5a16")
    ax.text(6.20, 3.35, "electrons + holes\nrecombine", va="center", size=10)
    arrow((4.6, 3.59), (7.8, 5.48), "#426cd7", 2.8)
    ax.text(6.45, 4.80, "escaped photons", rotation=29, color="#285caa", size=10)
    ax.text(2.70, 5.45, "Some light is trapped or absorbed;\nsome recombination emits no photon", size=10, color="#7d3745")

    def box(x, y, width, height, text, fill):
        ax.add_patch(FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.13",
                                   facecolor=fill, edgecolor="#65717b"))
        ax.text(x + width / 2, y + height / 2, text, ha="center", va="center", size=10)

    box(7.6, 5.20, 2.7, 0.62, "Optical collection", "#edf2ff")
    arrow((8.2, 5.05), (8.2, 4.45), "#426cd7")
    box(7.6, 3.60, 2.7, 0.70, "Spectrometer\nread emission spectrum", "#edf2ff")
    ax.plot([10.1, 10.6, 10.6], [5.05, 5.05, 3.05], color="#426cd7", lw=2)
    arrow((10.6, 3.05), (9.6, 2.85), "#426cd7")
    box(7.6, 2.10, 2.7, 0.70, "Calibrated optical power\naccount for collection", "#edf2ff")
    ax.text(7.55, 1.15, "Spectrum → photon energy\nPower + current → photon yield\nPower + IV → energy efficiency", size=11, linespacing=1.7)
    ax.text(0.3, 0.05, "Functional illustration only • no measured spectrum or apparatus model implied", color="#59636e", size=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
