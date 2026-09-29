"""Original disc-axis geometry and predicted inertia decomposition.

Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib
python3 ../rotational-inertia-energy-parallel-axis-shift.py
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


NAVY = "#17324d"
TEAL = "#167d9a"
ORANGE = "#bd591c"


def main():
    plt.rcParams.update({"font.size": 11, "text.color": NAVY, "mathtext.fontset": "dejavusans"})
    fig, (geometry, bars) = plt.subplots(1, 2, figsize=(9, 4.9), facecolor="white",
                                        gridspec_kw={"width_ratios": [1.15, 1]})
    fig.subplots_adjust(left=0.055, right=0.96, bottom=0.28, top=0.77, wspace=0.28)
    fig.suptitle("Shift the axis, keep the same disc", fontsize=18, y=0.97)
    fig.text(0.5, 0.90, r"Original model diagram · uniform disc of mass $M$ and radius $R$", ha="center", fontsize=11)

    geometry.set_aspect("equal")
    geometry.set_xlim(-1.28, 1.52)
    geometry.set_ylim(-1.13, 1.62)
    geometry.axis("off")
    geometry.add_patch(Circle((0, 0), 1, facecolor="#edf6f8", edgecolor=TEAL, lw=2))
    for x, label, color in [(0, r"$G$ (centre)", TEAL), (1, r"$O$ (rim)", ORANGE)]:
        geometry.add_patch(Circle((x, 0), 0.075, facecolor="white", edgecolor=color, lw=2, zorder=5))
        geometry.plot(x, 0, ".", color=color, markersize=6, zorder=6)
        geometry.text(x, -0.24, label, fontsize=10, ha="center", color=color)
        geometry.plot([x, x], [0.12, 1.31], color="#7c8c9b", linestyle="--", lw=1)
    geometry.annotate("", xy=(1, 1.27), xytext=(0, 1.27),
                      arrowprops={"arrowstyle": "<->", "color": NAVY, "lw": 1.4})
    geometry.text(0.5, 1.42, r"$d=R$", ha="center", fontsize=13)
    geometry.annotate("", xy=(-0.7071, -0.7071), xytext=(-0.05, -0.05),
                      arrowprops={"arrowstyle": "->", "color": TEAL, "lw": 1.4})
    geometry.text(-0.80, -0.32, r"$R$", color=TEAL, fontsize=12)
    geometry.text(0.5, -0.16, "Both axes point out of the page", transform=geometry.transAxes,
                  ha="center", fontsize=10)

    bars.bar([0, 1], [0.5, 0.5], width=0.5, color=TEAL, label=r"$I_G/(MR^2)=1/2$")
    bars.bar(1, 1, bottom=0.5, width=0.5, color=ORANGE, label=r"$Md^2/(MR^2)=1$")
    bars.text(0, 0.25, "0.5", color="white", ha="center", va="center", fontsize=13)
    bars.text(1, 0.25, "0.5", color="white", ha="center", va="center", fontsize=13)
    bars.text(1, 1.0, "+ 1.0", color="white", ha="center", va="center", fontsize=13)
    bars.text(0, 0.59, r"$I_G=MR^2/2$", ha="center", fontsize=11)
    bars.text(1, 1.60, r"$I_O=3MR^2/2$", ha="center", fontsize=11)
    bars.set_ylim(0, 1.85)
    bars.set_xlim(-0.55, 1.55)
    bars.set_xticks([0, 1], ["Central axis G", "Rim axis O"])
    bars.set_yticks([0, 0.5, 1, 1.5])
    bars.set_ylabel(r"Moment of inertia / $MR^2$")
    bars.grid(axis="y", alpha=0.18)
    bars.set_axisbelow(True)
    bars.spines[["top", "right"]].set_visible(False)
    bars.legend(loc="upper center", bbox_to_anchor=(0.5, -0.19), frameon=False, fontsize=10)

    fig.text(0.5, 0.05, r"$I_O=I_G+Md^2$: shifting to the rim triples inertia; the orange part is the axis-shift term.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.015, "Geometry and normalized bars are model predictions, not measurements.", ha="center", fontsize=9)
    output = Path(__file__).with_suffix(".png").name
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
