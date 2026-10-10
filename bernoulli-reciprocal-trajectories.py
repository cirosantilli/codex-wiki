"""Exact Bernoulli trajectories; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes bernoulli-reciprocal-trajectories.png to the CWD.
The curves are analytic model solutions, not measurements.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (ay, az) = plt.subplots(1, 2, figsize=(10.4, 4.5), dpi=120,
                                layout="constrained", facecolor="white")
    orange, blue = "#b85116", "#196f9b"
    xp = np.linspace(0, 1.999, 1200)
    xn = np.linspace(0, 3, 700)
    ay.plot(xp, np.exp(-xp)/(2-xp), color=orange, lw=2.6,
            label=r"$a=1/2:\ y=e^{-x}/(2-x)$")
    ay.plot(xn, -np.exp(-xn)/(1+xn), color=blue, lw=2.6,
            label=r"$a=-1:\ y=-e^{-x}/(1+x)$")
    ay.axhline(0, color="#555555", lw=1)
    ay.axvline(2, color="#777777", ls=":", lw=1.5)
    ay.scatter([0, 0, 1], [0.5, -1, np.exp(-1)],
               color=[orange, blue, orange], zorder=4)
    ay.annotate(r"minimum $(1,e^{-1})$", (1, np.exp(-1)),
                xytext=(0.2, 1.25), arrowprops={"arrowstyle": "->"})
    ay.annotate("blow-up at x = 2", (1.96, 3.4), xytext=(0.2, 3.2),
                arrowprops={"arrowstyle": "->"}, color=orange)
    ay.set(title=r"Nonlinear: $y'+y=e^x y^2$", xlabel="x", ylabel="y",
           xlim=(0, 3), ylim=(-1.15, 4))
    ay.legend(loc="upper right", bbox_to_anchor=(1, 0.55), fontsize=9,
              framealpha=1)

    xs = np.linspace(0, 2, 600)
    xe = np.linspace(2, 2.25, 120)
    xx = np.linspace(0, 2.25, 600)
    az.plot(xs, np.exp(xs)*(2-xs), color=orange, lw=2.6,
            label=r"$z=e^x(2-x)$")
    az.plot(xe, np.exp(xe)*(2-xe), color=orange, lw=2.6, ls="--",
            label="linear continuation only")
    az.plot(xx, -np.exp(xx)*(1+xx), color=blue, lw=2.6,
            label=r"$z=-e^x(1+x)$")
    az.axhline(0, color="#555555", lw=1)
    az.axvline(2, color="#777777", ls=":", lw=1.5)
    az.scatter([0, 0, 2], [2, -1, 0], color=[orange, blue, orange], zorder=4)
    az.annotate("z = 0: inverse undefined", (2, 0), xytext=(0.3, -10),
                arrowprops={"arrowstyle": "->"})
    az.set(title=r"Linearized exactly: $z'-z=-e^x$", xlabel="x",
           ylabel="z = 1/y", xlim=(0, 2.25), ylim=(-33, 5))
    az.legend(loc="lower left", fontsize=9, framealpha=1)
    for ax in (ay, az):
        ax.set_facecolor("white")
        ax.grid(alpha=0.15)
    fig.savefig(Path.cwd()/"bernoulli-reciprocal-trajectories.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
