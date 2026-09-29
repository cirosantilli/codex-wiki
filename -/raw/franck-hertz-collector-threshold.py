"""Original collector model schematic; Python 3.14, matplotlib 3.10.7.

Run from _media; writes franck-hertz-collector-threshold.png to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (ax, energy) = plt.subplots(2, 1, figsize=(10, 6.7),
                                   gridspec_kw={"height_ratios": [1.25, 1]})
    fig.subplots_adjust(left=.09, right=.97, top=.92, bottom=.11, hspace=.53)
    fig.suptitle("Franck–Hertz: an energy loss becomes a collection loss", fontsize=16)
    ax.set(xlim=(0, 10), ylim=(-.6, 4.6))
    ax.axis("off")
    tube = FancyBboxPatch((.3, 1), 9.2, 2.3, boxstyle="round,pad=0.14",
                         edgecolor="#657781", facecolor="#f4f8fa", linewidth=1.5)
    ax.add_patch(tube)
    ax.plot([1, 1], [1.45, 2.9], color="#d17c18", lw=7)
    ax.text(1, .55, "Heated cathode", ha="center")
    ax.text(1, .15, "electron source", ha="center", fontsize=10)
    ax.plot([6.6, 6.6], [1.2, 3.1], color="#326f9a", lw=2, ls="--")
    ax.text(6.6, .55, "Grid", ha="center")
    ax.plot([8.7, 8.7], [1.4, 2.95], color="#326f9a", lw=5)
    ax.text(8.7, .55, "Collector", ha="center")
    ax.text(8.7, .15, r"current $I(V,V_r)$", ha="center", fontsize=10)
    ax.annotate("", (4.2, 2.2), (1.4, 2.2),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": "#326f9a"})
    ax.text(3.2, 2.6, r"gain $e(V-V_c)$", ha="center")
    ax.scatter([4.7], [2.2], s=260, color="#b45283", edgecolor="white", zorder=4)
    ax.text(4.7, 1.55, r"one atom takes $\Delta$", ha="center", color="#943e6b")
    ax.annotate("", (6.25, 2.2), (5.05, 2.2),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": "#326f9a"})
    ax.annotate("", (8.35, 2.2), (7, 2.2),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": "#326f9a"})
    ax.text(7.7, 2.65, r"barrier $eV_r$", ha="center")
    ax.text(4.8, 3.65, "Vapor density sets collision opportunities; retarder selects survivors",
            ha="center", fontsize=11)
    ax.text(.35, -.45, "Functional model schematic • not historical geometry or a scale drawing",
            fontsize=10, color="#555555")

    energy.set_title("Chosen one-collision example: 5.6 eV input, 4.9 eV loss, probability 0.75",
                     fontsize=12, pad=14)
    energy.set(xlim=(0, 6.2), ylim=(0, 1.05), xlabel="Outgoing kinetic energy E (eV)")
    energy.axvspan(0, 1, color="#f9dfd9")
    energy.axvspan(1, 6.2, color="#e3f0e9")
    energy.vlines([.7, 5.6], [0, 0], [.75, .25], colors=["#a54732", "#217349"], lw=4)
    energy.scatter([.7, 5.6], [.75, .25], color=["#a54732", "#217349"], zorder=3)
    energy.axvline(1, color="#555555", ls="--", lw=1.4)
    energy.text(.7, .82, "75% at 0.7 eV", ha="center")
    energy.text(5.6, .32, "25% at 5.6 eV", ha="center")
    energy.text(1.13, .91, "1.0 V retarder: only 25% collected", color="#217349")
    energy.text(2, .68, "0.5 V retarder: both branches collected", color="#444444")
    energy.set_ylabel("Probability mass")
    energy.set_yticks([0, .25, .5, .75, 1])
    energy.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
