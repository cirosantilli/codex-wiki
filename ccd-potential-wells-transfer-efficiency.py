"""Original qualitative electron-energy wells and on-time packet model.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run in the desired output directory; writes the matching PNG there.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(11, 6.3), dpi=120, facecolor="white")
    gs = fig.add_gridspec(3, 2, width_ratios=[1.25, 1], hspace=.65, wspace=.38)
    fig.suptitle("CCD: move the well, preserve the packet", fontsize=17)
    x = np.linspace(0, 3, 700)
    profiles = [
        -.95 * np.exp(-((x - .65) / .29)**6) - .15 * np.exp(-((x - 1.55) / .29)**6),
        -.94 * np.exp(-((x - 1.1) / .78)**6),
        -.15 * np.exp(-((x - .65) / .29)**6) - 1.02 * np.exp(-((x - 1.55) / .29)**6),
    ]
    centers = [.65, 1.1, 1.55]
    labels = ["1. Store under A", "2. Open adjacent region", "3. Raise old well; arrive under B"]
    for i in range(3):
        ax = fig.add_subplot(gs[i, 0])
        ax.plot(x, profiles[i], color="#254f7d", lw=2)
        for j, center in enumerate([.65, 1.55, 2.45]):
            ax.add_patch(Rectangle((center - .34, .27), .68, .19,
                                   facecolor="#d8e3ef", edgecolor="#254f7d"))
            ax.text(center, .36, "ABC"[j], ha="center", va="center", fontsize=10)
        cx = centers[i]
        dots = np.array([cx - .16, cx, cx + .16])
        ax.scatter(dots, np.interp(dots, x, profiles[i]) + .11,
                   color="#b45309", s=28, zorder=4)
        if i < 2:
            ax.annotate("", xy=(1.62, -.55), xytext=(.8, -.55),
                        arrowprops={"arrowstyle": "->", "color": "#b45309", "lw": 1.5})
        ax.set(xlim=(0, 3), ylim=(-1.2, .55), yticks=[], xticks=[])
        ax.set_ylabel("Electron\nenergy U", fontsize=10)
        ax.set_title(labels[i], fontsize=11, loc="left")
        if i == 2:
            ax.set_xlabel("Position along channel; lower U attracts electrons", fontsize=10)

    ax = fig.add_subplot(gs[:2, 1])
    n = np.arange(0, 3001)
    for eta, color in [(.9999, "#b45309"), (.99999, "#2563a4")]:
        ax.plot(n, eta**n, label=f"η = {eta}", color=color, lw=2.2)
        ax.scatter([2000], [eta**2000], color=color, s=28, zorder=4)
    ax.axvline(2000, ls=":", color=".6")
    ax.set(xlim=(0, 3000), ylim=(.7, 1.02), xlabel="Number of transfers n",
           ylabel="On-time fraction ηⁿ", title="Repeated tiny errors accumulate")
    ax.legend(loc="lower left", fontsize=10)
    ax.grid(alpha=.2)
    textax = fig.add_subplot(gs[2, 1])
    textax.axis("off")
    textax.text(0, 1, "Chosen input: 10 000 electrons; n = 2000\nη = 0.9999  →  mean 8187.23 on time\nη = 0.99999 →  mean 9801.99 on time\n\nDeficit may be delayed charge or true loss.\nThis model alone does not give a trail shape.",
                va="top", fontsize=10, linespacing=1.4)
    fig.text(.5, .015, "Original qualitative effective wells and stipulated model; no measured voltages, historical data or prototype wiring.",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=.075, right=.975, top=.87, bottom=.1)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
