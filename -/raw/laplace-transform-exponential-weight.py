"""Plot Laplace weighting and real convergence boundaries; write PNG to cwd.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, (left, right) = plt.subplots(
        1, 2, figsize=(10.4, 4.6), dpi=120, facecolor="white"
    )
    time = np.linspace(0, 4, 801)
    profiles = [
        (-2.25, "#b24741", "-", r"$\sigma=-2.25$: grows"),
        (-2.0, "#747474", "--", r"$\sigma=-2$: constant"),
        (-1.5, "#207699", "-", r"$\sigma=-1.5$: decays"),
        (0.0, "#24845f", "-", r"$\sigma=0$: decays faster"),
    ]
    for sigma, color, style, label in profiles:
        left.plot(time, np.exp(-(sigma + 2) * time), color=color,
                  linestyle=style, linewidth=2.4, label=label)
    left.set(title=r"Weighting the input $f(t)=e^{-2t}$",
             xlabel="Time t", ylabel=r"Weighted input $e^{-(\sigma+2)t}$",
             xlim=(0, 4), ylim=(0, 2.9))
    left.legend(loc="upper left", frameon=False, fontsize=10)
    s_exp = np.linspace(-1.89, 4.5, 1500)
    s_one = np.linspace(0.11, 4.5, 1000)
    right.plot(s_exp, 1 / (s_exp + 2), color="#24845f", linewidth=2.6,
               label=r"$e^{-2t}\ \longmapsto\ 1/(s+2)$, $s>-2$")
    right.plot(s_one, 1 / s_one, color="#207699", linewidth=2.6,
               label=r"$1\ \longmapsto\ 1/s$, $s>0$")
    right.axvspan(-2.5, -2, color="#ececec", zorder=0)
    for boundary, color in [(-2, "#24845f"), (0, "#207699")]:
        right.axvline(boundary, color=color, linestyle="--", linewidth=1.3)
        right.annotate("", xy=(boundary + 0.13, 9.7),
                       xytext=(boundary + 0.28, 7.3),
                       arrowprops={"arrowstyle": "->", "color": color,
                                   "linewidth": 1.8})
    right.set(title="Approaching a convergence boundary",
              xlabel="Real transform parameter s", ylabel="Value of the integral",
              xlim=(-2.5, 4.5), ylim=(0, 10), xticks=[-2, -1, 0, 1, 2, 3, 4])
    right.legend(loc="upper right", frameon=False, fontsize=10)
    right.text(0.98, 0.55, "Each curve diverges at its\nboundary from the right.",
               transform=right.transAxes, ha="right", fontsize=10)
    for ax in (left, right):
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", color="#e5e9eb", linewidth=0.7)
        ax.set_axisbelow(True)
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.15, top=0.89, wspace=0.29)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
