"""Original explanatory schematic; emit the matching opaque PNG into the CWD.

Historical components: Chadwick, Proc. Roy. Soc. A 136 (1932), pp. 694–697.
This is a new logical layout, not a reproduction of the paper's figure.
Tested with Python 3.14, matplotlib 3.10.7; no measured trace is drawn.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


def box(ax, x, y, width, height, label, color="#edf4fa", size=11):
    ax.add_patch(FancyBboxPatch((x, y), width, height,
                              boxstyle="round,pad=0.025,rounding_size=0.09",
                              facecolor=color, edgecolor="#456075", linewidth=1.3))
    ax.text(x + width / 2, y + height / 2, label, ha="center", va="center",
            fontsize=size, linespacing=1.4, color="#172d40")


def arrow(ax, start, end, color="#286e9b"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=14,
                                linewidth=1.6, color=color))


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(11.2, 6.8), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.04, top=0.91)
    ax.set(xlim=(0, 11), ylim=(0, 6))
    ax.axis("off")
    fig.suptitle("Chadwick's experiment: detecting a recoil, inferring a neutron",
                 fontsize=16, fontweight="bold", y=0.97, color="#172d40")

    ax.text(0.1, 5.65, "Apparatus logic • schematic, not to scale", fontsize=12,
            fontweight="bold", color="#172d40")
    box(ax, 0.1, 4.1, 2.25, 1.05, "Polonium → α → Be\nEvacuable source vessel")
    box(ax, 3.05, 4.1, 1.15, 1.05, "Paraffin\nwax", color="#fff0d4")
    ax.add_patch(Rectangle((4.85, 4.1), 0.16, 1.05, facecolor="#b5bdc5",
                           edgecolor="#456075"))
    ax.text(4.93, 5.27, "Al screens", ha="center", fontsize=10)
    box(ax, 5.8, 4.1, 2.2, 1.05, "Thin window\nIonization chamber\nAir / substituted gas")
    box(ax, 8.65, 4.1, 2.2, 1.05, "Amplifier\nOscillograph\nPhotographic record")
    arrow(ax, (2.38, 4.62), (3.01, 4.62))
    ax.text(2.7, 3.82, "incident\nradiation", ha="center", fontsize=10)
    arrow(ax, (4.23, 4.62), (4.82, 4.62), "#b76016")
    arrow(ax, (5.04, 4.62), (5.76, 4.62), "#b76016")
    arrow(ax, (8.03, 4.62), (8.61, 4.62))
    ax.text(4.83, 3.45, "Recoil proton enters gas\nAl screens test its range",
            ha="center", fontsize=10, color="#995018")
    ax.text(7.18, 3.45, "Or: incident radiation creates\na recoil nucleus inside gas",
            ha="center", fontsize=10, color="#286e9b")

    ax.plot([0.1, 10.85], [2.91, 2.91], color="#d8e1e8", linewidth=1)
    ax.text(0.1, 2.54, "Inference chain • charged secondaries reveal the incident projectile",
            fontsize=12, fontweight="bold", color="#172d40")
    cards = [
        (0.1, "Range + ionization\nIdentify charged recoil"),
        (3.0, "H and N recoil endpoints\nCompare two target masses"),
        (5.9, "Conserve energy\nand momentum"),
        (8.8, "Neutral massive projectile\nMass near proton mass"),
    ]
    for x, label in cards:
        box(ax, x, 1.18, 2.05, 0.95, label, color="#eaf5ee", size=10)
    for x in (2.18, 5.08, 7.98):
        arrow(ax, (x, 1.65), (x + 0.77, 1.65))
    ax.text(5.5, 0.55, "A signal is not a direct neutron track. The collision model supplies the mass inference.",
            ha="center", fontsize=11, color="#172d40")
    ax.text(5.5, 0.12, "Original diagram • historical apparatus components, no reconstructed measured waveform",
            ha="center", fontsize=9, color="#566776")
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
