"""Original measurement/inference diagram; Python 3.14, matplotlib 3.10.7.

Run from _media; writes its basename PNG to the working directory.
Historical basis: Fermi, Nature 133, 757 (1934), and Fermi et al.,
Ricerca Scientifica 5(2), 282–283 (1934). Logical controls are labeled separately.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(11.6, 6.6), dpi=100, facecolor="white")
    ax.set(xlim=(0, 11.6), ylim=(0, 6.6))
    ax.axis("off")
    ink, blue, green = "#20344a", "#e8f2fc", "#eaf5ee"

    def box(x, y, w, h, text, color=blue, size=11):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.09",
                                   facecolor=color, edgecolor=ink, linewidth=1.2))
        ax.text(x+w/2, y+h/2, text, ha="center", va="center", fontsize=size, color=ink)

    def arrow(a, b):
        ax.annotate("", xy=b, xytext=a,
                    arrowprops={"arrowstyle": "->", "color": ink, "lw": 1.5})

    ax.text(0.15, 6.2, "Silver activation: irradiation first, counting later", fontsize=17,
            weight="bold", color=ink)
    ax.text(0.15, 5.78, "Original schematic of the measurement logic • no dimensions or source construction", fontsize=11)
    box(0.25, 3.9, 2.0, 1.1, "Historical\nneutron source")
    box(3.0, 3.6, 3.05, 1.7, "Irradiation environment\n\nCompare paraffin / water\nwith their absence")
    box(6.8, 3.9, 1.75, 1.1, "Silver\nspecimen")
    arrow((2.35, 4.45), (2.9, 4.45))
    arrow((6.15, 4.45), (6.7, 4.45))
    arrow((8.65, 4.45), (10.05, 4.45))
    ax.text(9.35, 4.85, "move after\nirradiation", ha="center", fontsize=10)
    box(9.1, 2.5, 2.15, 1.15, "Thin-wall counter\n+ silver specimen", green)
    arrow((10.15, 4.4), (10.15, 3.75))
    box(0.25, 1.85, 7.8, 0.95,
        "Historical control: without beryllium, no corresponding effect\nInterpretation: neutron-related activation, rather than gamma rays alone",
        "#fff4df", 11)
    box(0.25, 0.3, 7.8, 1.05,
        "Measurement model: subtract background; compare equal delays / count windows\nPersistence + decay supports an unstable product; counts alone do not identify it",
        green, 11)
    arrow((10.15, 2.4), (10.15, 1.6))
    ax.text(10.15, 1.08, "Pulses versus time\n\nProxy for activity,\nnot a neutron count", ha="center", va="center", fontsize=11, color=ink)
    fig.subplots_adjust(0, 0, 1, 1)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
