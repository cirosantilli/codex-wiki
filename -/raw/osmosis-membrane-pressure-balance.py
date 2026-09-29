"""Draw selective water passage and its pressure balance (Python 3.14)."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def arrow(ax, start, end, color, width=2.5):
    ax.annotate("", end, start, arrowprops={"arrowstyle": "->", "lw": width, "color": color})


def chamber(ax, balanced):
    ax.set(xlim=(0, 10), ylim=(0, 8))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Rectangle((0.6, 2.2), 8.8, 3.9, facecolor="#eaf5fa", edgecolor="#42505c", lw=2))
    ax.add_patch(Rectangle((4.86, 2.2), 0.28, 3.9, facecolor="#92a69d", hatch="...", edgecolor="#52665c"))
    ax.text(2.6, 5.65, "A: pure water", ha="center", fontsize=12)
    ax.text(7.35, 5.65, "B: retained solute", ha="center", fontsize=12)
    for x, y in [(6, 3), (7.1, 4.8), (8.55, 3.3), (6.2, 4.55), (8.25, 4.6)]:
        ax.add_patch(Circle((x, y), 0.13, facecolor="#c5742b", edgecolor="#854916"))
    if balanced:
        ax.add_patch(Rectangle((5.17, 5.03), 4.18, 0.22, facecolor="#66717c"))
        for x in (6, 7.3, 8.6):
            arrow(ax, (x, 7), (x, 5.3), "#735094", 2)
        ax.text(7.3, 7.4, r"Added pressure: $P_B-P_A=\Pi$", ha="center", fontsize=11)
        arrow(ax, (3.8, 4.35), (6.1, 4.35), "#147493")
        arrow(ax, (6.1, 3.85), (3.8, 3.85), "#147493")
        ax.text(5, 1.5, "Equal mean opposing water transfers", ha="center", fontsize=11)
        ax.text(5, 0.85, r"$\mu_{w,A}=\mu_{w,B}$  ·  zero net flux", ha="center", fontsize=12)
        ax.set_title("Pressure balances the osmotic drive", fontsize=14, pad=14)
    else:
        ax.text(5, 7.1, r"Equal pressure: $P_A=P_B$", ha="center", fontsize=12)
        arrow(ax, (3.4, 4.35), (6.6, 4.35), "#147493", 3.8)
        arrow(ax, (5.8, 3.85), (4.1, 3.85), "#147493", 1.5)
        ax.text(5, 1.5, "Water crosses both ways; net A → B", ha="center", fontsize=11)
        ax.text(5, 0.85, r"$\mu_{w,A}>\mu_{w,B}$", ha="center", fontsize=12)
        ax.set_title("Initial osmotic movement", fontsize=14, pad=14)
    arrow(ax, (7, 2.75), (5.3, 2.75), "#c5742b", 1.5)
    ax.plot([5.24, 5.4], [2.65, 2.85], color="#c5742b", lw=2)
    ax.plot([5.24, 5.4], [2.85, 2.65], color="#c5742b", lw=2)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.6), facecolor="white")
    for ax, balanced in zip(axes, (False, True)):
        chamber(ax, balanced)
    fig.suptitle("Osmosis: selective passage and pressure balance", fontsize=17, y=0.98)
    fig.text(0.5, 0.095, "Membrane passes water (blue arrows); excludes the illustrated solute (orange).", ha="center", fontsize=11)
    fig.text(0.5, 0.045, "Schematic, not measured particle counts or rates. Equilibrium still includes molecular exchange.", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.03, right=0.97, top=0.83, bottom=0.15, wspace=0.09)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
