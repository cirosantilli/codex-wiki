"""Functional secondary-X-ray diagram; Python 3.14, matplotlib 3.10.7.

Run from _media; write an opaque PNG to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10, 6.2), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.2))
    ax.axis("off")
    fig.subplots_adjust(left=.025, right=.975, bottom=.03, top=.94)
    ax.set_title("Secondary X-rays: separate excitation, filtering and readout", pad=12)

    def box(x, y, w, h, label, color="#edf2f7"):
        ax.add_patch(Rectangle((x, y), w, h, facecolor=color,
                               edgecolor="#334155", linewidth=1.5))
        ax.text(x+w/2, y+h/2, label, ha="center", va="center")

    def arrow(start, end, color="#2563eb", style="-|"):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=16, color=color, lw=2))

    box(.25, 4.5, 1.6, .8, "X-ray tube")
    arrow((1.85, 4.9), (4.15, 4.9))
    ax.text(2.95, 5.15, "primary beam", ha="center", color="#1d4ed8")
    box(4.2, 4.5, 1.45, .8, "irradiated\ntarget", "#ffedd5")
    arrow((5.65, 4.9), (8.9, 4.9))
    box(9, 4.45, .4, .9, "", "#cbd5e1")
    ax.text(8.25, 5.35, "transmitted primary → stop", ha="center")
    arrow((4.92, 4.45), (4.92, 3.15), "#b45309")
    ax.text(5.2, 3.92, "side-view secondary path\ncharacteristic + scattered", va="center")
    box(4.35, 2.8, 1.15, .35, "", "#94a3b8")
    ax.text(3.95, 2.98, "removable absorbers", ha="right", va="center")
    arrow((4.92, 2.75), (4.92, 2.15), "#b45309")
    box(3.65, 1.25, 2.55, .85, "gas ionization\nelectroscope discharge", "#dcfce7")
    ax.text(4.92, .94, "historical integrating readout", ha="center", fontsize=10)
    box(.25, 1.25, 2.5, 1.5, "Comparison logic\ninsert successive sheets\nuse carbon radiator\nestimate scattered signal", "#f8fafc")
    box(7.15, 1.1, 2.5, 1.9, "Related chamber principle\n\ngas → charge collection\n→ electrometer\n(current or charge)", "#f0fdf4")
    ax.text(5, .35, "Functional schematic only • no historical dimensions or measured intensities",
            ha="center", color="#475569", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
