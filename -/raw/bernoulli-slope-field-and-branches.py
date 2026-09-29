"""Bernoulli slope and inverse branches; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes bernoulli-slope-field-and-branches.png to the CWD.
All curves and field slopes belong to the original analytic model.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (af, ab) = plt.subplots(1, 2, figsize=(10.4, 4.5), dpi=120,
                                layout="constrained", facecolor="white")
    orange, blue, purple = "#b85116", "#196f9b", "#8153a0"
    xx, yy = np.meshgrid(np.linspace(0, 2.8, 23),
                         np.linspace(-1.15, 2.15, 24))
    slopes = yy*(np.exp(xx)*yy-1)
    dx = 0.043/np.hypot(1, slopes)
    dy = slopes*dx
    starts = np.stack((xx-dx, yy-dy), axis=-1)
    ends = np.stack((xx+dx, yy+dy), axis=-1)
    segments = np.stack((starts, ends), axis=-2).reshape(-1, 2, 2)
    af.add_collection(LineCollection(segments, colors="#99a3aa", linewidths=0.8))
    x = np.linspace(0, 2.8, 800)
    xp = np.linspace(0, 1.999, 1100)
    af.plot(x, np.exp(-x), color="#478641", lw=2, ls="--",
            label=r"moving nullcline $y=e^{-x}$")
    af.axhline(0, color="#444444", lw=1.5, label=r"nullcline / solution $y=0$")
    af.plot(xp, np.exp(-xp)/(2-xp), color=orange, lw=2.6, label=r"$a=1/2$")
    af.plot(x, -np.exp(-x)/(1+x), color=blue, lw=2.6, label=r"$a=-1$")
    af.scatter([1], [np.exp(-1)], color=orange, zorder=4)
    af.axvline(2, color="#777777", ls=":", lw=1.5)
    af.annotate("turning point", (1, np.exp(-1)), xytext=(0.08, 1.55),
                arrowprops={"arrowstyle": "->"})
    af.set(title=r"Slope field: $y'=y(e^x y-1)$", xlabel="x", ylabel="y",
           xlim=(0, 2.8), ylim=(-1.2, 2.2))
    af.legend(loc="upper right", bbox_to_anchor=(1, 0.45), fontsize=8.5,
              framealpha=1)

    xl = np.linspace(0, 1.999, 1200)
    xr = np.linspace(2.001, 4, 1200)
    ab.plot(xl, np.exp(-xl)/(2-xl), color=orange, lw=2.6,
            label=r"positive branch: $x<2$")
    ab.plot(xr, np.exp(-xr)/(2-xr), color=purple, lw=2.6,
            label=r"separate negative branch: $x>2$")
    ab.axvline(2, color="#777777", ls=":", lw=1.7)
    ab.axhline(0, color="#444444", lw=1.5,
               label="zero solution (no reciprocal)")
    ab.scatter([0], [0.5], color=orange, zorder=4)
    ab.text(1.4, 2.3, "blow-up\nno joining value", ha="center", color=orange)
    ab.text(2.2, -2.25, "same formula,\ndifferent interval", color=purple)
    ab.set(title=r"Inverse branches: $y=e^{-x}/(2-x)$", xlabel="x", ylabel="y",
           xlim=(0, 4), ylim=(-3, 3))
    ab.legend(loc="lower left", fontsize=8.5, framealpha=1)
    for ax in (af, ab):
        ax.set_facecolor("white")
        ax.grid(alpha=0.12)
    fig.savefig(Path.cwd()/"bernoulli-slope-field-and-branches.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
