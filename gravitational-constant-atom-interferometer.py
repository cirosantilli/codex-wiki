"""Original conceptual diagram of a published cold-atom G experiment.

Facts inspected in Rosi et al. (Nature 2014), author manuscript:
https://arxiv.org/pdf/1412.7954, pp. 3–6, Methods pp. 13–18 and Fig. 1 caption.
The selected cylinder blocks represent arrays; geometry is schematic and
neither data nor an engineering drawing. Python 3.14, matplotlib 3.10.7.
Run from _media to emit the matching opaque PNG to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10.8, 6.5))
    fig.suptitle("Cold-atom measurement of G: change the source, compare the phases", fontsize=15, y=0.96)
    apparatus_ax = fig.add_axes((0.025, 0.15, 0.49, 0.71))
    apparatus_ax.set(xlim=(0, 10), ylim=(0, 8))
    apparatus_ax.axis("off")
    for xcenter, label, levels in [(2.6, "C", (3.3, 5.0)), (7.3, "F", (2.35, 6.0))]:
        apparatus_ax.text(xcenter, 7.7, "Configuration " + label, ha="center", weight="bold")
        apparatus_ax.add_patch(Rectangle((xcenter - 0.62, 1.4), 1.24, 5.6,
                                         facecolor="#f7fafc", edgecolor="#95a5b3", lw=1.2))
        apparatus_ax.plot([xcenter - 0.62, xcenter + 0.62], [7.0, 7.0], color="0.25", lw=4)
        apparatus_ax.annotate("", (xcenter - 0.17, 6.9), (xcenter - 0.17, 1.55),
                               arrowprops={"arrowstyle": "->", "color": "#368356", "lw": 2})
        apparatus_ax.annotate("", (xcenter + 0.17, 1.55), (xcenter + 0.17, 6.9),
                               arrowprops={"arrowstyle": "->", "color": "#368356", "lw": 2})
        for cloud_y, cloud_label in [(5.4, "U"), (3.0, "L")]:
            apparatus_ax.add_patch(Circle((xcenter, cloud_y), 0.22, facecolor="#3174ad", edgecolor="white", lw=1.5, zorder=5))
            apparatus_ax.text(xcenter + 0.7, cloud_y, cloud_label, va="center", color="#175a91", weight="bold")
        for source_y in levels:
            for source_x in (xcenter - 1.18, xcenter + 1.18):
                apparatus_ax.add_patch(Rectangle((source_x - 0.29, source_y - 0.31), 0.58, 0.62,
                                                 facecolor="#d99546", edgecolor="#9e611f", lw=1.2))
        apparatus_ax.add_patch(FancyBboxPatch((xcenter - 0.83, 0.52), 1.66, 0.6, boxstyle="round,pad=0.08",
                                              facecolor="#e3eff8", edgecolor="#175a91"))
        apparatus_ax.text(xcenter, 0.82, "Launch", ha="center", va="center", fontsize=10)
    apparatus_ax.annotate("", (5.65, 4.05), (4.28, 4.05), arrowprops={"arrowstyle": "<->", "lw": 1.6, "color": "#9e611f"})
    apparatus_ax.text(4.95, 4.48, "Move\nsource", ha="center", va="center", fontsize=10)
    apparatus_ax.text(4.95, 6.9, "Mirror", ha="center", fontsize=10)
    apparatus_ax.text(4.95, 1.45, "Shared\nlaser pulses", ha="center", fontsize=10, color="#368356")
    apparatus_ax.text(4.95, -0.15, "Selected cylinders shown; clouds in vacuum", ha="center", fontsize=10, color="0.35")

    readout_ax = fig.add_axes((0.56, 0.15, 0.415, 0.71))
    readout_ax.set(xlim=(0, 10), ylim=(0, 8))
    readout_ax.axis("off")
    readout_ax.text(5, 7.7, "Readout and inference", ha="center", weight="bold")
    readout_ax.plot([1.0, 9.0], [6.5, 6.5], color="0.5", lw=1.2)
    for pos, label, time in [(1.0, r"$\pi/2$", "0"), (5, r"$\pi$", "T"), (9, r"$\pi/2$", "2T")]:
        readout_ax.plot([pos, pos], [6.18, 6.85], color="#368356", lw=4)
        readout_ax.text(pos, 7.03, label, ha="center", color="#368356", fontsize=14)
        readout_ax.text(pos, 5.82, time, ha="center")
    readout_ax.text(5, 5.26, "Fluorescence → paired fringes", ha="center", fontsize=11)
    for ypos, text in [(4.02, r"$D_C=(\phi_U-\phi_L)_C$"),
                       (2.83, r"$D_F=(\phi_U-\phi_L)_F$"),
                       (1.63, r"$S=D_C-D_F$"),
                       (0.4, r"Model response $\mathcal{K}$ → $G=S/\mathcal{K}$")]:
        readout_ax.add_patch(FancyBboxPatch((0.48, ypos - 0.32), 9.04, 0.72, boxstyle="round,pad=0.05",
                                           facecolor="#f1f5f9", edgecolor="#95a5b3"))
        readout_ax.text(5, ypos + 0.04, text, ha="center", va="center", fontsize=12)
    fig.text(0.5, 0.055, "Original conceptual scheme of Rosi et al. (2014) • geometry schematic • no measurement data", ha="center", color="0.35", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
