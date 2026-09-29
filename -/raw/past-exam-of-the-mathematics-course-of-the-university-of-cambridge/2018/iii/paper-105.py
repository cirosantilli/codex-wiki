"""Plot the two characteristic families in Cambridge Part III 2018 Paper 105.

Run this script to create paper-105.png in the current directory. The Makefile
runs it from the matching _media directory. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7 (Debian build 3.10.7+dfsg1), matching the
repository's Python 3.14 environment. Original mathematical plot; white,
opaque background and fixed 700 by 540 pixel output.
"""

from pathlib import Path
import os

# Keep the font cache within the permitted scratch directory.
os.environ.setdefault("MPLCONFIGDIR", "/tmp/2018-paper-105-matplotlib")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    blue, orange = "#2166ac", "#cf5c17"
    times = np.linspace(-2.6, 1.35, 1200)
    fig, ax = plt.subplots(figsize=(7, 5.4), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    fig.subplots_adjust(left=.10, right=.97, bottom=.12, top=.84)

    # The green strip for t>=0 is the actual forward vanishing region.
    ax.fill_betweenx([0, 1.35], -1, 1, color="#e9f3e7", zorder=0)
    for constant in [-2.0, -.5, .4, 1.6, 3.0]:
        ax.plot(-1 + constant * np.exp(times), times,
                color=blue, alpha=.34, lw=1.1)
        ax.plot(1 - constant * np.exp(times), times,
                color=orange, alpha=.34, lw=1.1)

    ax.axvline(-1, color="#444444", ls="--", lw=1.5)
    ax.axvline(1, color="#444444", ls="--", lw=1.5)
    ax.axhline(0, color="#aaaaaa", lw=.8)
    ax.plot([-1, 1], [0, 0], color="#202020", lw=2.2, zorder=4)

    ax.plot(np.exp(times)-1, times, color=blue, lw=2.4,
            label=r"$\rho=-1+Ce^t$")
    ax.plot(1-np.exp(times), times, color=orange, lw=2.4,
            label=r"$\rho=1+Ce^t$")
    for sign, color in [(1, blue), (-1, orange)]:
        for time in [-1.0, .42]:
            start = sign * (np.exp(time)-1)
            end = sign * (np.exp(time+.16)-1)
            ax.annotate("", (end, time+.16), (start, time),
                        arrowprops={"arrowstyle": "->", "color": color,
                                    "lw": 1.8}, zorder=5)
    ax.scatter([0], [0], s=23, color="#202020", zorder=6)
    ax.annotate("(0, 0)", (0, 0), xytext=(9, -17),
                textcoords="offset points", fontsize=9,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    ax.text(0, .98, "Forward vanishing region", ha="center", fontsize=10,
            color="#355c37", bbox={"facecolor": "#e9f3e7", "edgecolor": "none"})
    ax.text(0, -.14, "Zero initial data", ha="center", va="top", fontsize=9,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})

    ax.set(xlim=(-3.1, 3.1), ylim=(-2.6, 1.35),
           xlabel=r"Position $\rho$", ylabel=r"Time $t$")
    ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
    ax.set_yticks([-2.5, -2, -1.5, -1, -.5, 0, .5, 1])
    ax.grid(color="#eeeeee", linewidth=.65)
    ax.set_axisbelow(True)
    ax.legend(loc="lower center", bbox_to_anchor=(.5, 1.015), ncol=2,
              frameon=False, fontsize=11)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    fig.savefig(Path("paper-105.png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
