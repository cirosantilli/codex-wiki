"""Original climate bookkeeping diagram; Python 3.14, matplotlib 3.10.7.

Run from _media; the PNG is written to the current working directory.
Fluxes are stipulated model values, not measurements.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def arrow(ax, start, end, color, text, xytext):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=17, linewidth=2.4, color=color))
    ax.text(*xytext, text, color=color, ha="center", va="center", fontsize=11,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})


def box(ax, xy, width, height, label, face, edge):
    ax.add_patch(FancyBboxPatch(xy, width, height,
                               boxstyle="round,pad=0.015,rounding_size=0.02",
                               facecolor=face, edgecolor=edge, linewidth=1.5))
    ax.text(xy[0] + width / 2, xy[1] + height / 2, label,
            ha="center", va="center", fontsize=11, color="#16334a")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, (left, right) = plt.subplots(1, 2, figsize=(12, 6.4), dpi=100,
                                    gridspec_kw={"width_ratios": [1.18, 1]})
    fig.patch.set_facecolor("white")
    for ax in (left, right):
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis("off")
    fig.suptitle("Energy accounting and a spectral observation", fontsize=19, y=0.97)
    left.set_title("A. Chosen one-layer model", fontsize=14, pad=14, loc="left")
    right.set_title("B. Functional measurement chain", fontsize=14, pad=14, loc="left")

    box(left, (0.05, 0.08), 0.90, 0.13,
        "Surface  •  289.81 K", "#e8f1df", "#527937")
    box(left, (0.05, 0.56), 0.90, 0.12,
        "Atmosphere  •  255.06 K", "#e8f2fa", "#337398")
    left.text(0.5, 0.92, "Space: outgoing thermal flux = 240", ha="center", fontsize=11)
    arrow(left, (0.14, 0.87), (0.14, 0.23), "#b87900", "Sunlight\n240", (0.14, 0.42))
    arrow(left, (0.39, 0.23), (0.39, 0.54), "#b84032", "Infrared\n400", (0.39, 0.39))
    arrow(left, (0.62, 0.54), (0.62, 0.23), "#b84032", "Infrared\n240", (0.62, 0.39))
    arrow(left, (0.84, 0.23), (0.84, 0.54), "#247464", "Heat\n80", (0.84, 0.39))
    arrow(left, (0.50, 0.70), (0.50, 0.88), "#b84032", "Infrared\n240", (0.65, 0.79))
    left.text(0.5, 0.015, "All fluxes: W m⁻²  •  infrared absorptivity = 1",
              ha="center", va="center", fontsize=10)

    labels = [
        (0.78, "Outgoing directional spectral radiance"),
        (0.57, "Spectrometer\nchannel response + calibration"),
        (0.34, "Match resolution and sampling\nselect comparable clear scenes"),
        (0.11, "Difference of matched spectra\ncompare with radiative transfer"),
    ]
    for y, label in labels:
        box(right, (0.04, y), 0.92, 0.13, label, "#f0f5f9", "#5d7c94")
    for top, bottom in zip(labels, labels[1:]):
        right.add_patch(FancyArrowPatch((0.50, top[0] - 0.015),
                                       (0.50, bottom[0] + 0.15),
                                       arrowstyle="-|>", mutation_scale=15,
                                       color="#35566e", linewidth=1.7))
    right.text(0.5, 0.015, "A spectral channel is not the total outgoing flux.",
               ha="center", va="center", fontsize=10)
    fig.text(0.5, 0.028,
             "Original schematic and illustrative energy budget; no historical data are plotted.",
             ha="center", fontsize=11, color="#405464")
    fig.subplots_adjust(left=0.035, right=0.975, bottom=0.11, top=0.84, wspace=0.20)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
