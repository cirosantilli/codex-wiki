"""Original functional schematics; no historical dimensions or measured data.

Tested with Python 3.14, matplotlib 3.10.7. Run from _media.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def arrow(ax, start, end, color="#1976a5"):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", lw=2, color=color))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.3), facecolor="white")
    for ax in axes:
        ax.set(xlim=(0, 10), ylim=(0, 9))
        ax.axis("off")
    ax = axes[0]
    ax.set_title("Flow test: drive and readout", fontweight="bold", pad=12)
    # Open reservoirs joined by a narrow passage; deliberate schematic geometry.
    ax.add_patch(Rectangle((0.6, 1.1), 3.0, 5.0, facecolor="#dceff9", ec="none"))
    ax.add_patch(Rectangle((6.4, 1.1), 3.0, 2.6, facecolor="#dceff9", ec="none"))
    ax.add_patch(Rectangle((3.6, 1.45), 2.8, 0.35, facecolor="#dceff9", ec="none"))
    ax.plot([0.6, 0.6, 3.6, 3.6], [7.3, 1.1, 1.1, 1.45], color="#283947", lw=2)
    ax.plot([3.6, 3.6], [1.8, 7.3], color="#283947", lw=2)
    ax.plot([6.4, 6.4], [1.8, 7.3], color="#283947", lw=2)
    ax.plot([6.4, 6.4, 9.4, 9.4], [1.45, 1.1, 1.1, 7.3], color="#283947", lw=2)
    ax.plot([3.6, 6.4], [1.45, 1.45], color="#283947", lw=2)
    ax.plot([3.6, 6.4], [1.8, 1.8], color="#283947", lw=2)
    ax.plot([0.6, 3.6], [6.1, 6.1], color="#1976a5", lw=2)
    ax.plot([6.4, 9.4], [3.7, 3.7], color="#1976a5", lw=2)
    ax.annotate("", xy=(4.8, 6.1), xytext=(4.8, 3.7),
                arrowprops=dict(arrowstyle="<->", color="#333333"))
    ax.text(5.1, 4.9, r"$\Delta h$", va="center")
    ax.text(1.9, 6.5, "Track level", ha="center")
    ax.text(7.9, 4.2, "Reference level", ha="center")
    ax.text(5, 2.4, "Narrow slit", ha="center")
    arrow(ax, (4.0, 1.62), (6.0, 1.62))
    ax.text(5, 0.35, r"$\Delta P\simeq\rho g\Delta h$", ha="center")
    ax.text(5, 8.1, "Compare temperatures across the transition", ha="center", fontsize=10)
    ax = axes[1]
    ax.set_title("Thermomechanical balance: ideal model", fontweight="bold", pad=12)
    for x, label, tint in [(0.6, r"$T_c,\ P_c$", "#dceff9"),
                            (6.2, r"$T_h>T_c,\ P_h$", "#ffecd6")]:
        ax.add_patch(Rectangle((x, 1.8), 3.2, 4.5, facecolor=tint, ec="#283947", lw=2))
        ax.text(x + 1.6, 5.55, label, ha="center")
    ax.add_patch(Rectangle((3.8, 2.5), 2.4, 0.7, facecolor="#eef1f4", ec="#283947", lw=2, hatch="///"))
    ax.text(5, 3.65, "Superleak", ha="center")
    ax.text(5, 1.05, r"$v_n\simeq0$; superfluid can pass", ha="center")
    arrow(ax, (3.9, 2.85), (6.1, 2.85))
    ax.text(5, 0.35, "Initial inflow toward heated side", ha="center", fontsize=10)
    ax.plot([6.8, 7.2, 7.5, 7.8, 8.1, 8.5], [4, 4.35, 3.65, 4.35, 3.65, 4], color="#b45121", lw=2)
    arrow(ax, (8, 7.55), (8, 6.4), color="#b45121")
    ax.text(8, 8.0, r"Heat input $\dot Q$", ha="center", color="#b45121")
    ax.text(2.2, 4.1, "Cold reservoir", ha="center")
    ax.text(8, 4.9, "Closed chamber", ha="center", fontsize=10)
    ax.text(5, 7.0, r"Read $\Delta T$ and $P_h-P_c$", ha="center")
    fig.text(0.5, 0.025, "Functional schematics, not historical reconstructions; slit and superleak enlarged.",
             ha="center", fontsize=10, color="#444444")
    fig.subplots_adjust(left=0.025, right=0.98, bottom=0.105, top=0.87, wspace=0.19)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
