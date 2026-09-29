"""Draw the functions of a lamp-based rubidium optical-pumping experiment.

Run from _media; output is the generator's basename with a .png suffix.
Python 3.14, matplotlib 3.10.7. The apparatus functions follow MIT's
Optical Pumping guide (17 February 2011), section V and figure 4.
The drawing is original, with schematic geometry and no measured trace.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 13, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(12, 5.7), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 6.8))
    ax.axis("off")
    blue, green, red = "#1768ac", "#16734a", "#b24636"

    def text(x, y, value, **kwargs):
        return ax.text(x, y, value, ha="center", va="center", **kwargs)

    def arrow(start, end, color=blue, **kwargs):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=15, color=color,
                                    linewidth=2, **kwargs))

    def box(x, width, label, color="#eef5fb"):
        ax.add_patch(FancyBboxPatch((x, 3.95), width, 1.08,
                                    boxstyle="round,pad=0.06",
                                    facecolor=color, edgecolor=blue,
                                    linewidth=1.5))
        text(x + width / 2, 4.49, label)

    text(6, 6.37, "Prepare populations; read out their redistribution",
         fontsize=19, weight="bold")
    box(0.12, 1.40, "Rb discharge\nlamp")
    box(1.99, 1.42, "D1\nfilter")
    box(3.88, 1.94, "Polarizer\n+ quarter-wave plate")
    box(6.45, 2.08, "Rb + neon\ncell", "#edf7ef")
    box(9.40, 2.30, "Photodiode\ntransmission")
    for a, b in [(1.56, 1.93), (3.45, 3.82), (5.87, 6.39), (8.58, 9.34)]:
        arrow((a, 4.49), (b, 4.49))
    text(6.15, 4.92, r"$\sigma^+$", fontsize=16, color=blue)
    arrow((6.72, 5.40), (8.27, 5.40), color=green)
    text(7.49, 5.66, r"$B_0$ along beam", fontsize=12, color=green)
    arrow((7.49, 3.15), (7.49, 3.87), color=red)
    text(7.49, 2.92, "Transverse RF", fontsize=12, color=red)

    # The preparation/readout statements express the physical signal sign;
    # they are not copies of a measured historical resonance curve.
    for y, color, heading, detail in [
        (1.83, green, "Pumping", "Absorption decreases."),
        (0.93, red, "RF resonance", "Absorption increases; transmission decreases."),
    ]:
        ax.plot([0.23, 0.23], [y - 0.26, y + 0.30], color=color, linewidth=5)
        ax.text(0.49, y + 0.15, heading, ha="left", va="center",
                fontsize=14, color=color, weight="bold")
        ax.text(0.49, y - 0.20, detail, ha="left", va="center", fontsize=12)
    text(6, 0.20, "Later rubidium-cell experiment; schematic geometry.",
         fontsize=11, color="#505050")
    fig.subplots_adjust(left=0.025, right=0.985, bottom=0.025, top=0.985)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
