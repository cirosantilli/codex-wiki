"""Original functional diagram; Python 3.14, matplotlib 3.10.7.

Run from _media; emits the matching opaque PNG in the working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10.8, 5.5), dpi=110, facecolor="white")
    ax.set(xlim=(0, 12), ylim=(0, 6))
    ax.axis("off")
    red, blue, purple = "#c54336", "#2266a4", "#7055a0"

    def box(x, y, w, h, text, color="#f2f4f7"):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04",
                                   facecolor=color, edgecolor="#344351", lw=1.2))
        ax.text(x+w/2, y+h/2, text, ha="center", va="center")

    def arrow(a, b, color, width=2):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=14,
                                     lw=width, color=color))

    ax.text(6, 5.75, "Saturated absorption: one scanned frequency, two directions",
            ha="center", fontsize=15, weight="bold")
    box(.25, 4.25, 1.7, .85, "Tunable laser\nscan frequency")
    arrow((1.99, 4.67), (2.8, 4.67), "#344351")
    ax.plot([2.75, 3.05], [4.42, 4.92], color="#344351", lw=3)
    ax.text(2.9, 5.15, "Beam splitter", ha="center")
    arrow((3, 4.67), (10.1, 4.67), red, 3)
    ax.text(6.1, 4.95, "Strong pump: periodically blocked", color=red, ha="center")
    ax.add_patch(Rectangle((6.35, 4.4), .14, .56, facecolor="#344351"))
    ax.text(6.42, 4.1, "Chopper", ha="center")
    ax.plot([10.1, 10.1], [4.67, 2.95], color=red, lw=3)
    ax.plot([9.95, 10.25], [4.52, 4.82], color="#344351", lw=3)
    ax.plot([9.95, 10.25], [2.8, 3.1], color="#344351", lw=3)
    arrow((10.1, 2.95), (3.65, 2.95), red, 3)
    box(3.1, 2.7, .45, .5, "", "#dddddd")
    ax.text(3.3, 3.4, "Pump stop", ha="center", fontsize=10)
    ax.plot([2.9, 2.9], [4.55, 2.55], color=blue, lw=1.8)
    arrow((2.9, 2.55), (10.15, 2.55), blue, 1.8)
    ax.text(3.3, 2.08, "Weak probe", color=blue, ha="center")
    ax.add_patch(FancyBboxPatch((4.55, 2.12), 3.15, 1.3,
                               boxstyle="round,pad=0.05", facecolor="#fff9e8",
                               edgecolor="#8b794d", lw=1.4, zorder=0))
    ax.text(6.12, 3.17, "Vapour cell", ha="center")
    ax.text(6.12, 2.25, "Same illuminated atoms", ha="center", fontsize=10)
    box(10.25, 2.15, 1.35, .8, "Probe\ndetector")
    box(8.6, .55, 2, .8, "Lock-in amplifier\npump on − off")
    ax.annotate("", xy=(9.8, 1.39), xytext=(10.9, 2.1),
                arrowprops={"arrowstyle": "->", "color": "#344351", "lw": 1.4})
    ax.plot([6.42, 7.95, 7.95, 8.55], [4.37, 3.75, .95, .95],
            ls="--", color=purple, lw=1.4)
    ax.text(7.72, 1.65, "Chopper\nreference", ha="right", color=purple, fontsize=10)
    ax.text(.4, 1.25, "At resonance: pump reduces absorption;\nmore probe light reaches the detector.",
            fontsize=11, va="center")
    ax.text(6, .08, "Functional layout; nearly opposed beams overlap in the cell. Separation is exaggerated.",
            ha="center", fontsize=10, color="#45515b")
    fig.subplots_adjust(left=.02, right=.99, top=.98, bottom=.03)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
