"""Original horizontal interaction diagram; Python 3.14 / matplotlib 3.10.7.

Run from _media; output is this script's basename with a .png extension.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10, 6.2), dpi=110, facecolor="white")
    ax = fig.add_axes([0.02, 0.03, 0.96, 0.89])
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis("off")
    blue, orange, ink = "#1765a3", "#be4b13", "#243342"
    fig.suptitle("One interaction, two bodies, one combined momentum balance", y=0.985, fontsize=16)

    def box(x, y, w, h, text, color=ink, dashed=False):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                                   facecolor="white", edgecolor=color, linewidth=1.8,
                                   linestyle="--" if dashed else "-"))
        if text:
            ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", color=color)

    def arrow(start, end, color):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=22,
                                    linewidth=3, color=color))

    box(0.3, 2.9, 9.35, 2.55, "", dashed=True)
    ax.text(0.52, 5.1, "Collection A + B: only horizontal forces shown", color=ink)
    box(2.1, 3.35, 1.65, 1.05, "$A$\n$m_A = 1$ kg", blue)
    box(6.25, 3.35, 1.65, 1.05, "$B$\n$m_B = 2$ kg", orange)
    arrow((2.92, 4.58), (1.15, 4.58), blue)
    arrow((7.08, 4.58), (8.85, 4.58), orange)
    ax.text(2.03, 4.82, r"$F_{B\mathrm{\ on\ }A}=-4$ N", ha="center", color=blue)
    ax.text(7.97, 4.82, r"$F_{A\mathrm{\ on\ }B}=+4$ N", ha="center", color=orange)
    ax.plot([3.8, 6.2], [3.9, 3.9], color="#78838b", ls=":", lw=2)
    ax.text(5, 4.12, "mutual repulsion", ha="center", fontsize=11)
    ax.text(2.92, 3.05, r"$a_A=-4$ m/s$^2$", ha="center", color=blue)
    ax.text(7.08, 3.05, r"$a_B=+2$ m/s$^2$", ha="center", color=orange)
    arrow((8.45, 5.7), (9.45, 5.7), ink)
    ax.text(8.35, 5.7, "$+x$", ha="right", va="center", color=ink)

    box(0.35, 0.65, 4.2, 1.65, "", blue)
    ax.text(2.45, 2.03, "A alone: keep the force on A", ha="center", color=blue)
    ax.text(2.45, 1.42, r"$\dfrac{dp_A}{dt} = -4$ N", ha="center", va="center", fontsize=17)
    ax.text(2.45, 0.83, "The +4 N force acts on B.", ha="center", fontsize=11)
    box(5.05, 0.65, 4.55, 1.65, "", ink)
    ax.text(7.33, 2.03, "A + B: add both equations", ha="center", color=ink)
    ax.text(7.33, 1.42, r"$\dfrac{d(p_A+p_B)}{dt}=-4+4=0$", ha="center", va="center", fontsize=16)
    ax.text(7.33, 0.83, "No other horizontal forces in this model.", ha="center", fontsize=10.5)
    ax.text(5, 0.18, "Equal force magnitudes; unequal accelerations; constant total momentum.",
            ha="center", color=ink, fontsize=12)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
