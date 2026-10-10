"""Functional reconstruction of selected parts of Millikan's 1916 apparatus.

Python 3.14, Matplotlib 3.10. Run from _media; emits matching PNG to CWD.
Based on Physical Review 7, 355–388, Figs. 1–2 and sections 2–3.
Successive operations are separated; geometry is deliberately rearranged.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle


def main():
    fig, ax = plt.subplots(figsize=(12, 6.8), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 6.8))
    ax.axis("off")
    ax.text(6, 6.5, "Millikan’s photoelectric apparatus: three successive operations",
            ha="center", fontsize=17, weight="bold")
    ax.text(6, 6.12, "Functional schematic from the 1916 paper • rearranged geometry • not to scale",
            ha="center", fontsize=11, color="0.35")

    def box(x, y, w, h, text, color="#edf4f8", size=12):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                   facecolor=color, edgecolor="#506773", linewidth=1.3))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size)

    def arrow(start, end, color="#506773", style="->"):
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": style, "color": color, "lw": 1.8})

    # Operation 1: external magnetic manipulation without opening the vessel.
    box(0.25, 3.35, 3.2, 2.25, "", size=12)
    ax.text(1.85, 5.32, "1  Prepare surface", ha="center", fontsize=14, weight="bold")
    ax.add_patch(Circle((1.17, 4.35), 0.57, color="#d9e1e5", ec="#506773"))
    ax.add_patch(Rectangle((1.45, 4.19), 0.45, 0.32, color="#c15c16"))
    ax.plot([2.12, 2.5], [4.10, 4.65], color="0.25", lw=5)
    ax.text(1.1, 3.57, "Wheel", fontsize=11, ha="center")
    ax.text(2.65, 4.78, "Knife", fontsize=11, ha="center")
    ax.text(1.85, 3.92, "Na or Li", fontsize=11, ha="center")
    arrow((3.55, 4.5), (4.08, 4.5))

    # Operation 2: collector contains gauze plus outer solid copper shell.
    box(4.18, 3.35, 3.45, 2.25, "")
    ax.text(5.9, 5.32, "2  Illuminate and collect", ha="center", fontsize=14, weight="bold")
    ax.add_patch(Rectangle((4.8, 3.85), 2.25, 1.02, fill=False, ec="#8b4b26", lw=3))
    ax.add_patch(Rectangle((4.98, 4.02), 1.88, 0.68, fill=False, ec="#8b4b26", lw=1.5, ls="--"))
    ax.add_patch(Rectangle((5.12, 4.2), 0.17, 0.3, color="#c15c16"))
    arrow((5.35, 4.35), (6.6, 4.35), "#116c99")
    ax.text(5.95, 4.45, "electrons", fontsize=10, ha="center", color="#116c99")
    ax.text(5.9, 3.58, "Gauze + outer copper collector", fontsize=10, ha="center")
    box(4.18, 1.95, 3.45, 0.95, "Electrometer: charge in 30 s\nRepeat at different voltages", size=11)
    arrow((6.85, 3.82), (6.85, 2.98))
    arrow((7.72, 4.5), (8.25, 4.5))

    # Operation 3 is an independent displacement-null measurement.
    box(8.35, 3.35, 3.4, 2.25, "")
    ax.text(10.05, 5.32, "3  Check contact offset", ha="center", fontsize=14, weight="bold")
    ax.add_patch(Rectangle((8.85, 4.03), 0.16, 0.7, color="#c15c16"))
    ax.add_patch(Rectangle((9.6, 4.03), 0.13, 0.7, color="#8b4b26"))
    arrow((9.62, 4.9), (10.2, 4.9), style="<->")
    ax.text(10.65, 4.38, "Move copper\ntest plate", ha="center", va="center", fontsize=11)
    ax.text(10.05, 3.58, "Adjust voltage to displacement null", ha="center", fontsize=10)
    box(8.35, 1.95, 3.4, 0.95, "Certified voltmeter\nIndependent voltage scale", size=12)
    arrow((10.05, 3.28), (10.05, 2.98))
    box(0.25, 1.95, 3.2, 0.95, "Mercury lamp\nMonochromator + filters", size=12)
    arrow((3.52, 2.45), (4.98, 4.18), "#c15c16")
    ax.text(3.84, 3.02, "light", rotation=48, fontsize=11, color="#a14812")
    ax.text(6, 1.32, "Vacuum vessel: surface operations proceed without opening it", ha="center", fontsize=12)
    ax.text(6, 0.81, "Readout chain: voltage scan → current endpoint → frequency slope h/e",
            ha="center", fontsize=13, color="#116c99")
    ax.text(6, 0.32, "Separate contact measurement is needed to interpret the threshold", ha="center", fontsize=12)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
