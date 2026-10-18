"""Original figure for Oxford Prelims Mathematics III (2015), Question 3.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from the mirrored _media directory; the only output is a PNG in CWD.
Dependencies are declared in the repository's root pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    s = np.sqrt(97)
    radius = np.sqrt(29)
    lo, hi = 1 - radius, 1 + radius
    rminus, rplus = (2 - s) / 3, (2 + s) / 3
    hminus, hplus = np.sqrt(163 - 2 * s) / 3, np.sqrt(163 + 2 * s) / 3

    def restricted(x):
        return -x**3 + 2*x**2 + 31*x + 28

    fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 4.7),
                                 gridspec_kw={"width_ratios": [1, 1.15]},
                                 layout="constrained")
    angle = np.linspace(0, 2*np.pi, 600)
    ax.plot(1 + radius*np.cos(angle), radius*np.sin(angle), color="0.6", lw=1.5)
    ax.scatter([lo, hi], [0, 0], color="#1766a3", s=45, zorder=4,
               label="Other constrained extrema")
    ax.scatter([rminus]*2, [-hminus, hminus], color="#ba2828", s=55, zorder=4,
               label="Global minima on circle")
    ax.scatter([rplus]*2, [-hplus, hplus], color="#7141a3", s=55, zorder=4,
               label="Global maxima on circle")
    ax.annotate("Local maximum", (lo, 0), xytext=(3, 12), textcoords="offset points")
    ax.annotate("Local minimum", (hi, 0), xytext=(-4, -20),
                textcoords="offset points", ha="right")
    for y in [-hminus, hminus]:
        ax.annotate(r"$r_-$", (rminus, y), xytext=(-19, 2), textcoords="offset points")
    for y in [-hplus, hplus]:
        ax.annotate(r"$r_+$", (rplus, y), xytext=(7, 2), textcoords="offset points")
    ax.axhline(0, color="0.88", lw=0.7, zorder=0)
    ax.axvline(0, color="0.88", lw=0.7, zorder=0)
    ax.set(xlim=(-5.7, 7.3), ylim=(-6.1, 6.2), xlabel="$x$", ylabel="$y$",
           title=r"Six extrema on $(x-1)^2+y^2=29$")
    ax.set_aspect("equal")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.27), fontsize=8.5,
              frameon=False)

    xx = np.linspace(lo, hi, 1200)
    yy = restricted(xx)
    bx.plot(xx, yy, color="#1766a3", lw=2)
    bx.scatter([lo, hi], restricted(np.array([lo, hi])), color="#1766a3", s=40)
    bx.scatter([rminus], [restricted(rminus)], color="#ba2828", s=55, zorder=4)
    bx.scatter([rplus], [restricted(rplus)], color="#7141a3", s=55, zorder=4)
    bx.axhline(-20, color="#ba2828", ls="--", lw=1)
    bx.fill_between(xx, yy, -20, where=yy < -20, color="#ba2828", alpha=0.22)
    bx.annotate("Printed bound: -20", (hi, -20), xytext=(-1, 8),
                textcoords="offset points", ha="right", color="#ba2828")
    bx.annotate(f"Minimum = {restricted(rminus):.6f}",
                (rminus, restricted(rminus)), xytext=(14, -24),
                textcoords="offset points", color="#ba2828")
    bx.annotate(f"Maximum = {restricted(rplus):.6f}",
                (rplus, restricted(rplus)), xytext=(-4, 13),
                textcoords="offset points", ha="right", color="#7141a3")
    bx.set(xlim=(lo-0.3, hi+0.3), ylim=(-44, 141), xlabel="$x$",
           ylabel="Value on the circle", title=r"$H(x)=-x^3+2x^2+31x+28$")
    bx.grid(alpha=0.15)
    fig.savefig(Path.cwd() / "mathematics-iii-constrained-extrema.png",
                dpi=110, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
