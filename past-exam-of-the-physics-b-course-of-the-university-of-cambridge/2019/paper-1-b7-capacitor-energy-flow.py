#!/usr/bin/env python3
"""Original capacitor field/energy diagram; writes its PNG basename to cwd.

Tested: Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7 (+dfsg1).
Dependencies are listed in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def arrow(ax, start, end, color, width=1.8):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "-|>", "lw": width, "color": color})


def main():
    fig, ax = plt.subplots(figsize=(7.3, 4.2), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.plot([-1, 1], [.55, .55], lw=6, color=".25", solid_capstyle="butt")
    ax.plot([-1, 1], [-.55, -.55], lw=6, color=".25", solid_capstyle="butt")
    ax.text(-1.15, .55, "+", fontsize=18, va="center")
    ax.text(-1.15, -.55, "−", fontsize=18, va="center")
    ax.text(0, .72, "Positive plate", ha="center", fontsize=11)
    ax.text(0, -.78, "Negative plate", ha="center", fontsize=11)
    ax.add_patch(Rectangle((-.045, -.55), .09, 1.1, facecolor="#e8cccc",
                           edgecolor="#9e3333", lw=1.5))
    arrow(ax, (0, .30), (0, -.29), "#9e3333", 2.5)
    ax.text(.09, .02, r"$I=V/R$", fontsize=11, color="#9e3333")
    for x in [-.82, .82]:
        arrow(ax, (x, .38), (x, -.36), "#0072b2")
    ax.text(.87, .29, r"$\mathbf{E}$", color="#0072b2", fontsize=13)
    for z in [-.26, .26]:
        arrow(ax, (-.65, z), (-.14, z), "#d55e00")
        arrow(ax, (.65, z), (.14, z), "#d55e00")
    ax.text(-.45, .34, r"$\mathbf{S}$", color="#d55e00", fontsize=13)
    ax.scatter([-.58], [0], s=230, marker=r"$\otimes$", color="#009e73")
    ax.scatter([.58], [0], s=230, marker=r"$\odot$", color="#009e73")
    ax.text(-.58, -.13, r"$\mathbf{H}$ in", ha="center", color="#007c5a", fontsize=10)
    ax.text(.58, -.13, r"$\mathbf{H}$ out", ha="center", color="#007c5a", fontsize=10)
    ax.text(0, -1.08, "Meridional section, viewed from −y; not to scale.\n"
            "The magnetic field circulates around the axial resistor.", ha="center", fontsize=10)
    ax.set(xlim=(-1.35, 1.35), ylim=(-1.23, .95),
           title="Discharge: electromagnetic energy flows into the resistor")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path(__file__).stem+".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
