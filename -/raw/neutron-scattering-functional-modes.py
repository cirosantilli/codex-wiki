"""Draw functional neutron scattering routes; no historical geometry.

Tested with Python 3.14, matplotlib 3.10.7. Run from _media.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def box(ax, xy, label, color, width=1.6):
    x, y = xy
    ax.add_patch(FancyBboxPatch((x-width/2, y-.34), width, .68,
                               boxstyle="round,pad=0.05", facecolor=color,
                               edgecolor="#294056", linewidth=1.2))
    ax.text(x, y, label, ha="center", va="center", fontsize=11)


def arrow(ax, start, end, label="", offset=.23):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", lw=2, color="#294056"))
    if label:
        ax.text((start[0]+end[0])/2, (start[1]+end[1])/2+offset,
                label, ha="center", va="bottom", fontsize=11)


def main():
    fig, ax = plt.subplots(figsize=(10.4, 5.5), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(-.15, 11.3), ylim=(-.6, 6.25))
    ax.axis("off")
    ax.text(0, 5.95, "One beam, two measurement questions", fontsize=18, weight="bold")
    ax.text(0, 5.5, "Functional routes • bends are illustrative • no historical geometry", fontsize=11)

    ax.text(0, 4.95, "A   Elastic diffraction: angular peaks", fontsize=13, weight="bold")
    box(ax, (.8, 4.05), "Neutron\nbeam", "#e9eef3", 1.4)
    box(ax, (3.1, 4.05), "Crystal\nmonochromator", "#dcecf9", 1.85)
    box(ax, (5.8, 4.05), "Sample", "#e1f0df", 1.4)
    box(ax, (9.9, 4.05), "Detector", "#f9e8d6", 1.55)
    arrow(ax, (1.55, 4.05), (2.1, 4.05))
    arrow(ax, (4.1, 4.05), (5.05, 4.05), r"$\mathbf{k}_i$")
    arrow(ax, (6.55, 4.05), (9.05, 4.05), r"$\mathbf{k}_f$   (no analyzer)")
    ax.text(5.75, 3.38, r"Elastic interpretation: $E_f=E_i$; $Q$ from angle and $\lambda_i$",
            ha="center", fontsize=11)

    ax.text(0, 2.65, "B   Triple-axis analysis: energy and momentum transfer", fontsize=13, weight="bold")
    box(ax, (.8, 1.75), "Neutron\nbeam", "#e9eef3", 1.4)
    box(ax, (3.1, 1.75), "Crystal\nmonochromator", "#dcecf9", 1.85)
    box(ax, (5.8, 1.75), "Sample", "#e1f0df", 1.4)
    box(ax, (8.05, .8), "Crystal\nanalyzer", "#dcecf9", 1.5)
    box(ax, (10.45, 1.75), "Detector", "#f9e8d6", 1.55)
    arrow(ax, (1.55, 1.75), (2.1, 1.75))
    arrow(ax, (4.1, 1.75), (5.05, 1.75), r"$E_i,\mathbf{k}_i$")
    arrow(ax, (6.55, 1.5), (7.24, 1.04), r"$E_f,\mathbf{k}_f$", .3)
    arrow(ax, (8.85, .95), (9.9, 1.4), "selected", -.55)
    ax.text(3.1, 1.03, r"selects $\lambda_i$", ha="center", fontsize=10)
    ax.text(8.05, .2, r"selects $\lambda_f$", ha="center", fontsize=10)
    ax.text(5.6, -.35, r"$\Delta E=E_i-E_f$       $\mathbf{Q}=\mathbf{k}_i-\mathbf{k}_f$       counter reads accepted counts",
            ha="center", fontsize=12)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
