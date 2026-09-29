"""Original functional point-contact experiment diagram; Python 3.14 / matplotlib 3.10.7.

Run from _media; emits the matching PNG in the current directory.
Connections follow Bardeen and Brattain, Physical Review 74 (1948), Fig. 1,
and Bardeen's memoir of Brattain (1994), pp. 78–80. Current bookkeeping and
the resistor readout formula are original explanatory annotations.
Geometry and annotation are explanatory, not a reconstruction or measured data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(12, 7.2), dpi=120, facecolor="white")
    ax.set(xlim=(0, 12), ylim=(0, 7.2))
    ax.axis("off")
    ink, blue, gold = "#263445", "#126a9a", "#9a6510"

    def wire(points, color=ink, lw=2):
        ax.plot(*zip(*points), color=color, lw=lw, solid_capstyle="round")

    def arrow(a, b, color=blue):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=14,
                                    color=color, lw=2))

    def label(x, y, text, **kw):
        ax.text(x, y, text, ha="center", va="center", color=kw.pop("color", ink), **kw)

    label(6, 6.95, "Two contacts control a powered output", fontsize=18, weight="bold")
    label(6, 6.52, "Functional connections, not a scale drawing or measured response", fontsize=11)

    ax.add_patch(Rectangle((4.0, 2.55), 4.0, 1.95, facecolor="#e9f1f7", edgecolor=ink, lw=2))
    label(6, 3.45, "n-type germanium", fontsize=15)
    label(6, 3.05, "holes introduced near emitter", fontsize=11)
    ax.add_patch(Rectangle((4.2, 2.46), 3.6, 0.12, facecolor=ink))
    ax.text(5.65, 2.15, "B: broad base contact", ha="right", va="center", color=ink, fontsize=11)

    for x, name in [(5.0, "E"), (6.9, "C")]:
        wire([(x, 4.5), (x, 5.18)])
        ax.plot(x, 4.5, "o", color=gold, ms=6)
        label(x, 5.43, name, fontsize=14, weight="bold")
    arrow((5.3, 4.02), (6.6, 4.02), gold)
    label(6, 3.75, "hole transport", fontsize=10)

    wire([(5, 5.18), (5, 5.98), (1.2, 5.98), (1.2, 3.7)])
    ax.add_patch(Rectangle((0.36, 2.2), 1.68, 1.5, facecolor="white", edgecolor=blue, lw=2))
    label(1.2, 2.95, "emitter bias\n+ input signal", fontsize=11)
    label(1.2, 3.92, "+", fontsize=16)
    label(1.2, 1.99, "−", fontsize=16)
    wire([(1.2, 2.2), (1.2, 1.22), (10.7, 1.22)])
    arrow((4.68, 5.75), (4.68, 5.05))
    label(4.3, 5.45, r"$I_E$")

    wire([(6.9, 5.18), (6.9, 5.98), (10.7, 5.98), (10.7, 5.3)])
    ax.add_patch(Rectangle((10.46, 4.45), 0.48, 0.85, facecolor="#edf7ef", edgecolor=ink, lw=2))
    label(10.03, 4.88, r"$R_L$")
    wire([(10.7, 4.45), (10.7, 3.7)])
    ax.add_patch(Rectangle((9.84, 2.2), 1.72, 1.5, facecolor="white", edgecolor=blue, lw=2))
    label(10.7, 2.95, "collector\nDC supply", fontsize=11)
    label(10.7, 3.92, "−", fontsize=16)
    label(10.7, 1.99, "+", fontsize=16)
    wire([(10.7, 2.2), (10.7, 1.22)])
    arrow((10.34, 5.88), (10.34, 5.38))
    label(9.96, 5.65, r"$I_C$")
    wire([(11.18, 5.3), (11.55, 5.3), (11.55, 4.45), (11.18, 4.45)], blue, 1.5)
    ax.text(9.0, 4.12, r"readout: $\Delta v_L=R_L\Delta I_C$", fontsize=10, color=blue)

    wire([(6, 2.46), (6, 1.22)])
    ax.plot(6, 1.22, "o", color=ink, ms=5)
    arrow((6.32, 1.48), (6.32, 2.13))
    label(6.76, 1.82, r"$I_B$")
    label(3.1, 0.85, "Base is the voltage reference", fontsize=11)
    label(8.8, 0.85, r"Signed currents: $I_E+I_B=I_C$", fontsize=11)
    label(6, 0.28, "Signal changes the current; DC supplies provide the energy", fontsize=13, color=blue)
    fig.subplots_adjust(left=0.015, right=0.985, top=0.985, bottom=0.025)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
