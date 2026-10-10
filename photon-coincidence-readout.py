"""Functional photon-pair readout, not an apparatus replica; tested with Python 3.14 and matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon


def main():
    fig, ax = plt.subplots(figsize=(10.5, 5.6), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.975, top=0.91, bottom=0.04)
    ax.set(xlim=(0, 10), ylim=(0, 5))
    ax.axis("off")
    optical, electronic = "#2476a5", "#7a4b90"

    def box(x, y, w, h, label, color="#f2f6f9", size=11):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.06",
                                   facecolor=color, edgecolor="#455460", linewidth=1.2))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=size)

    def arrow(start, stop, color=optical):
        ax.annotate("", xy=stop, xytext=start, arrowprops=dict(arrowstyle="->", lw=2, color=color))

    box(0.1, 3.0, 1.2, 0.7, "Light\nsource")
    box(1.75, 2.95, 1.5, 0.8, "Select mode\nand polarization")
    arrow((1.3, 3.35), (1.75, 3.35))
    arrow((3.25, 3.35), (4.2, 3.35))
    ax.add_patch(Polygon([[4.2, 3.35], [4.7, 3.85], [5.2, 3.35], [4.7, 2.85]],
                         facecolor="#e7f0f6", edgecolor=optical, linewidth=1.8))
    ax.plot([4.44, 4.96], [3.09, 3.61], color=optical, linewidth=2)
    ax.text(3.85, 4.10, "Beam splitter", ha="center", fontsize=11)
    arrow((4.7, 3.85), (4.7, 4.72))
    # The upper branch bends toward detector 2.
    ax.plot([4.7, 6.15], [4.72, 4.72], color=optical, linewidth=2)
    arrow((6.15, 4.72), (6.15, 4.50))
    box(5.55, 3.85, 1.25, 0.65, "Detector 2")
    arrow((5.2, 3.35), (5.55, 3.35))
    box(5.55, 3.0, 1.25, 0.65, "Detector 1")
    ax.text(4.7, 1.95, "Unused input:\nvacuum", ha="center", fontsize=10, color="#455460")
    arrow((4.7, 2.50), (4.7, 2.85), color="#758490")
    box(7.45, 3.2, 2.25, 1.0, "Record both\nevent-time streams", color="#f5eff8")
    arrow((6.8, 4.17), (7.45, 3.92), electronic)
    arrow((6.8, 3.32), (7.45, 3.48), electronic)
    arrow((8.58, 3.2), (8.58, 2.63), electronic)
    box(6.6, 1.68, 3.1, 0.9, "All cross-channel pairs\n" + r"Bin $\tau=t_2-t_1$ → counts $C_j$", color="#f5eff8")
    ax.plot([6.6, 5.4], [2.13, 2.13], color=electronic, linewidth=2)
    box(0.7, 0.55, 5.05, 1.05,
        "Normalize by independent-pair expectation\n" + r"$\widehat g^{(2)}_j=C_j/(r_1r_2T_j\,\Delta\tau)$", size=12)
    arrow((5.4, 2.13), (5.4, 1.6), electronic)
    ax.text(8.15, 1.12, r"$r_i$: single-count rates" + "\n" + r"$T_j$: live overlap time" + "\n" + r"$\Delta\tau$: full bin width",
            ha="center", va="center", fontsize=11)
    ax.text(5, 0.12, "One photon → at most one ideal detector event. Count pairs of distinct photons.",
            ha="center", fontsize=11, color="#344551")
    fig.suptitle("From split light to a normalized coincidence readout", fontsize=17, y=0.98)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
