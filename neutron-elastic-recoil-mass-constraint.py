"""Original recoil-kinematics plots; emit matching opaque PNG into the CWD.

All plotted endpoints are ideal calculations, not historical measurements.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 5.5), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.075, right=0.975, top=0.79, bottom=0.20, wspace=0.35)
    fig.suptitle("Elastic recoils: energy transfer and projectile mass", fontsize=16,
                 fontweight="bold", y=0.965, color="#172d40")
    fig.text(0.5, 0.88, "Stationary, freely recoiling targets • nonrelativistic, single elastic collisions",
             ha="center", fontsize=11, color="#40576a")

    ratio = np.geomspace(0.08, 250, 600)
    ax.plot(ratio, 4 * ratio / (1 + ratio) ** 2, color="#286e9b", linewidth=2.4)
    ax.set_xscale("log")
    ax.set(xlim=(0.08, 250), ylim=(0, 1.1), xlabel=r"Target / projectile mass $M/m$",
           ylabel=r"Maximum fraction $T_{\max}/E$", title=r"$f_{\max}=4mM/(m+M)^2$")
    ax.set_xticks([0.1, 1, 4, 14, 100], labels=["0.1", "1", "4", "14", "100"])
    examples = [(1, "H: 1.000", (-40, 12)), (4, "He: 0.640", (12, 5)),
                (14, "N: 0.249", (15, 5))]
    for target, label, offset in examples:
        y = 4 * target / (1 + target) ** 2
        ax.scatter([target], [y], s=40, color="#b76016", zorder=3)
        ax.annotate(label, (target, y), textcoords="offset points", xytext=offset,
                    fontsize=10, color="#995018")
    ax.text(0.04, 0.08, "Equal masses allow full transfer.\nVery heavy targets take little energy.",
            transform=ax.transAxes, fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 1})

    mass = np.linspace(0, 8, 401)
    speed_ratio = (mass + 14) / (mass + 1)
    bx.plot(mass, speed_ratio, color="#286e9b", linewidth=2.4)
    bx.axhline(7.5, color="#b76016", linestyle="--", linewidth=1.5)
    bx.plot([1, 1], [1, 7.5], color="#b76016", linestyle=":", linewidth=1.5)
    bx.scatter([1], [7.5], color="#b76016", zorder=4, s=45)
    bx.set(xlim=(0, 8), ylim=(1, 14.5), xlabel=r"Projectile mass $m/m_p$",
           ylabel=r"Endpoint speed ratio $R=u_{\rm H}/u_{\rm N}$",
           title=r"$R=(m/m_p+14)/(m/m_p+1)$")
    bx.annotate(r"$R=7.5\ \Rightarrow\ m=m_p$", (1, 7.5), xytext=(2.5, 9.8),
                arrowprops={"arrowstyle": "->", "color": "#995018"}, color="#995018")
    bx.text(0.97, 0.78, "Same incident speed in both runs\nTarget masses: 1 and 14 proton masses",
            transform=bx.transAxes, ha="right", fontsize=10)
    for a in (ax, bx):
        a.grid(alpha=0.17)
        a.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.08, "Illustrative only: m = mₚ, E = 4 MeV → H endpoint 4 MeV; N endpoint 0.996 MeV.",
             ha="center", fontsize=11, color="#172d40")
    fig.text(0.5, 0.025, "Original calculations • integer target-mass approximation • not measured 1932 data",
             ha="center", fontsize=10, color="#566776")
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
