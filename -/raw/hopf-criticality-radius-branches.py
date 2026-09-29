"""Compute cubic Hopf radius branches and drift; output PNG basename to CWD.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
Dimensionless cubic models only: no measured data or global prediction.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(2, 2, figsize=(9.0, 6.0))
    fig.subplots_adjust(left=0.085, right=0.975, bottom=0.17, top=0.79,
                        wspace=0.27, hspace=0.64)
    stable, unstable = "#187154", "#bb4937"
    fig.suptitle("The cubic sign selects the side and stability of the small cycle", y=0.975, fontsize=13)
    fig.text(0.5, 0.92, "Radius branches above; computed radial drift below. Dimensionless models, not measured data.",
             ha="center", fontsize=9)
    handles = [Line2D([0], [0], color=stable, lw=2.5, label="attracting branch"),
               Line2D([0], [0], color=unstable, lw=2.5, ls="--", label="repelling branch")]
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, 0.9), ncol=2,
               frameon=False, fontsize=9)
    side = np.linspace(0, 0.4, 500)
    r = np.linspace(0, 0.7, 500)
    for col, sign in enumerate((-1, 1)):
        ax = axes[0, col]
        ax.axvline(0, color="#bbc3c9", lw=1, zorder=0)
        ax.plot((-0.4, 0), (0, 0), color=stable, lw=3)
        ax.plot((0, 0.4), (0, 0), color=unstable, ls="--", lw=3)
        branch_mu = side if sign < 0 else -side
        ax.plot(branch_mu, np.sqrt(side), color=stable if sign < 0 else unstable,
                ls="-" if sign < 0 else "--", lw=2.5)
        for mu in (-0.2, 0.2):
            for rad in (0.13, 0.34, 0.57):
                drift = mu * rad + sign * rad**3
                direction = 1 if drift > 0 else -1
                ax.annotate("", xy=(mu, rad + direction * 0.045),
                            xytext=(mu, rad - direction * 0.045),
                            arrowprops={"arrowstyle": "->", "color": "#59616a", "lw": 1.1})
        ax.plot(0, 0, "o", ms=4.5, color="#333333", clip_on=False, zorder=5)
        ax.set(xlim=(-0.42, 0.42), ylim=(-0.04, 0.70), xlabel=r"parameter $\mu$", ylabel=r"radius $r$")
        ax.set_title(("Supercritical: " + r"$\dot r=\mu r-r^3$") if sign < 0
                     else ("Subcritical: " + r"$\dot r=\mu r+r^3$"), fontsize=11)
        ax.text(0.96 if sign < 0 else 0.04, 0.94,
                r"$r_*=\sqrt{\mu}$" if sign < 0 else r"$r_*=\sqrt{-\mu}$",
                transform=ax.transAxes, ha="right" if sign < 0 else "left", fontsize=11)
        ax = axes[1, col]
        ax.axhline(0, color="#bbc3c9", lw=1)
        for mu, color in ((-0.2, "#5365af"), (0.2, "#c37822")):
            ax.plot(r, mu * r + sign * r**3, color=color, lw=2, label=rf"$\mu={mu:g}$")
            if -mu / sign > 0:
                ax.plot(np.sqrt(-mu / sign), 0, "o", ms=6, mew=1.5,
                        mec=color, mfc=color if sign < 0 else "white", zorder=5)
        ax.set(xlim=(0, 0.70), ylim=(-0.51, 0.51), xlabel=r"radius $r$", ylabel=r"radial drift $\dot r$")
        ax.set_yticks((-0.4, 0, 0.4))
        ax.set_title("Positive drift grows the radius; negative drift shrinks it", fontsize=9, pad=8)
        ax.legend(frameon=False, fontsize=9, loc="lower left" if sign < 0 else "upper left")
    fig.text(0.5, 0.075, "Upper arrows show radial motion at fixed parameter. The zero-radius branch is an equilibrium.",
             ha="center", fontsize=9)
    fig.text(0.5, 0.035, "Outward subcritical drift leaves the local neighbourhood; the cubic model supplies no distant attractor.",
             ha="center", fontsize=9)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
