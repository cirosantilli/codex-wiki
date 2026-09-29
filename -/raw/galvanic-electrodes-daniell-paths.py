"""Original Daniell-cell charge-path schematic, not experimental data.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
The PNG basename is written to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(10.2, 7.2), dpi=110, facecolor="white")
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.98)
    ax.set(xlim=(0, 10), ylim=(0, 8.8))
    ax.axis("off")
    ink, electron, ionic = "#243649", "#1565a8", "#276a43"

    def label(x, y, text, **kwargs):
        ax.text(x, y, text, color=kwargs.pop("color", ink),
                ha="center", va="center", **kwargs)

    def arrow(start, end, color, width=2):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=17, linewidth=width,
                                    color=color, zorder=4))

    label(5, 8.4, "Daniell cell delivering current to a passive load",
          fontsize=17, weight="bold")
    ax.plot([1.6, 1.6, 4.3], [6.1, 7.3, 7.3], color=ink, lw=2)
    ax.plot([5.7, 8.4, 8.4], [7.3, 7.3, 6.1], color=ink, lw=2)
    ax.add_patch(Rectangle((4.3, 7.08), 1.4, 0.44,
                           facecolor="#f2f3f6", edgecolor=ink, lw=2))
    label(5, 7.3, "load R", fontsize=11)
    arrow((2.9, 7.8), (7.1, 7.8), electron)
    label(5, 8.04, r"electrons: Zn $\rightarrow$ Cu", fontsize=12)
    arrow((7.1, 6.86), (2.9, 6.86), ink)
    label(5, 6.59, "conventional current through load", fontsize=11)

    for x0, fill in [(0.45, "#f2f5f7"), (5.8, "#e9f3fa")]:
        ax.add_patch(Rectangle((x0, 2.3), 3.75, 2.8,
                               facecolor=fill, edgecolor="none"))
        ax.plot([x0, x0, x0+3.75, x0+3.75],
                [5.65, 2.3, 2.3, 5.65], color=ink, lw=2)
        ax.plot([x0, x0+3.75], [5.1, 5.1], color="#a9bdca", lw=1)
    ax.add_patch(Rectangle((1.43, 3.2), 0.34, 2.9,
                           facecolor="#a8b4bf", edgecolor=ink))
    ax.add_patch(Rectangle((8.23, 3.2), 0.34, 2.9,
                           facecolor="#cc8356", edgecolor=ink))
    label(1.6, 6.37, "Zn anode (−)", weight="bold")
    label(8.4, 6.37, "Cu cathode (+)", weight="bold")
    label(1.6, 4.6, "Zn(s)", rotation=90, fontsize=10)
    label(8.4, 4.6, "Cu(s)", rotation=90, fontsize=10)

    bridge_x, bridge_y = [3.7, 3.7, 6.3, 6.3], [4.3, 5.75, 5.75, 4.3]
    ax.plot(bridge_x, bridge_y, color="#9dbfa8", lw=21,
            solid_joinstyle="round", solid_capstyle="round")
    ax.plot(bridge_x, bridge_y, color="#eaf4eb", lw=14,
            solid_joinstyle="round", solid_capstyle="round")
    label(5, 6.07, r"chosen KNO$_3$ salt bridge", fontsize=11)
    arrow((3.7, 4.9), (3.7, 3.78), ionic)
    arrow((6.3, 4.9), (6.3, 3.78), ionic)
    label(3.02, 3.87, r"NO$_3^-$", fontsize=15, color=ionic)
    label(6.96, 3.87, r"K$^+$", fontsize=15, color=ionic)
    arrow((4.35, 5.75), (5.65, 5.75), ionic)
    label(5, 5.32, "ionic current →", fontsize=10)
    arrow((1.8, 3.5), (2.65, 3.0), ink)
    arrow((7.35, 3.0), (8.18, 3.5), ink)
    label(2.8, 2.67, r"Zn$^{2+}$ produced", fontsize=12)
    label(7.2, 2.67, r"Cu$^{2+}$ consumed", fontsize=12)
    label(2.25, 1.88, "OXIDATION: electrons released", fontsize=12,
          weight="bold")
    label(7.75, 1.88, "REDUCTION: electrons accepted", fontsize=12,
          weight="bold")
    label(2.25, 1.48, r"Zn(s) $\rightarrow$ Zn$^{2+}$(aq) + 2e$^-$",
          fontsize=13)
    label(7.75, 1.48, r"Cu$^{2+}$(aq) + 2e$^-$ $\rightarrow$ Cu(s)",
          fontsize=13)
    label(5, 0.93, "Ideal inventory per 1 mol of net reaction:",
          fontsize=11, weight="bold")
    label(2.4, 0.57, r"Zn side: +2F from Zn$^{2+}$ − 2F from NO$_3^-$ = 0",
          fontsize=10)
    label(7.6, 0.57, r"Cu side: −2F from Cu$^{2+}$ + 2F from K$^+$ = 0",
          fontsize=10)
    label(5, 0.17, "Schematic: no measured fluxes. Other ions can share transport.",
          fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
