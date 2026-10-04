"""Draw an original schematic, not a numerical stellar-evolution model.

Run in the intended output directory; uses the project's Matplotlib dependency.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(9.5, 6.8), dpi=100, facecolor="white")
    ax.set_facecolor("white")
    # Ordered landmarks chosen only to explain the sequence and axis convention.
    stages = [
        (4.20, 2.75),  # zero-age main sequence
        (4.13, 3.05),  # hydrogen exhaustion
        (3.61, 3.25),  # first giant excursion / helium ignition
        (3.77, 3.00),  # beginning of a possible blue loop
        (3.98, 3.13),  # hotter part of helium-burning loop
        (3.77, 3.26),  # returning to the giant region
        (3.58, 3.47),  # central helium exhausted, early AGB
        (3.52, 4.03),  # first thermal pulse
    ]
    colours = ["#245ca5", "#e08b25", "#3c8c58", "#3c8c58", "#3c8c58", "#9a4aa1", "#9a4aa1"]
    for a, b, colour in zip(stages, stages[1:], colours):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=17,
                                    linewidth=2.7, color=colour, zorder=3))
    for x, y in stages:
        ax.plot(x, y, "o", markersize=5.5, color="#253341", zorder=4)
    labels = [
        (0, "Zero-age main sequence\nCore H burning (~100 Myr)", (12, -42)),
        (1, "Central H exhausted", (-9, 22)),
        (2, "Giant: H-burning shell\nNondegenerate He ignition", (-165, 92)),
        (4, "Possible blue loop\nCore He burning (~20 Myr)", (-72, -66)),
        (6, "Early AGB: shell burning\nCentral He exhausted", (-155, -32)),
        (7, "First AGB thermal pulse", (-150, 12)),
    ]
    for index, text, offset in labels:
        ax.annotate(text, stages[index], xytext=offset, textcoords="offset points",
                    fontsize=11, color="#253341", ha="left",
                    arrowprops={"arrowstyle": "-", "color": "#7b858d", "lw": 0.8},
                    bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9, "pad": 1.5})
    ax.text(4.21, 3.67, "Hertzsprung-gap crossing\nEnvelope expands and cools",
            fontsize=11, color="#ad6417", ha="left")
    ax.set_xlim(4.31, 3.42)
    ax.set_ylim(2.45, 4.26)
    ax.set_xlabel(r"$\log_{10}(T_{\rm eff}/{\rm K})$   (hotter to the left)")
    ax.set_ylabel(r"$\log_{10}(L/L_\odot)$")
    ax.set_title(r"Schematic $5\,M_\odot$ stellar evolution", pad=14, fontsize=17)
    ax.grid(alpha=0.17)
    fig.text(0.5, 0.024, "Arrows show time direction. Coordinates and loop extent are illustrative; no computed track is implied.",
             ha="center", fontsize=10, color="#4b5663")
    fig.subplots_adjust(left=0.10, right=0.97, bottom=0.13, top=0.89)
    fig.savefig(Path.cwd() / "paper-63-stellar-track.png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
