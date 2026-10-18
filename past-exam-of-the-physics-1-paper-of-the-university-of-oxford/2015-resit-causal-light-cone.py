"""Original causal spacetime diagram. Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7; writes the same-basename PNG in the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    blue, green, red, gray = "#126782", "#287d53", "#b3443c", "#596672"
    fig, ax = plt.subplots(figsize=(8.3, 6.3))
    ct = np.linspace(0, 6, 300)
    ax.fill_betweenx(ct, 8 - (6 - ct), 8 + (6 - ct), color=blue, alpha=0.10)
    for sign in (-1, 1):
        ax.plot(8 + sign * (6 - ct), ct, color=blue, lw=1.8)
        ax.plot([8, 8 + sign * 3.3], [6, 9.3], color=blue, lw=1, ls=":")
    ax.scatter([8], [6], color="#233746", s=55, zorder=5)
    ax.scatter([2], [3], color=red, s=55, zorder=5)
    ax.scatter([10], [1.5], color=green, s=55, zorder=5)
    ax.annotate("", (8, 6), (2, 3), arrowprops={"arrowstyle": "->", "color": red, "lw": 1.7, "ls": "--"})
    ax.annotate("", (8, 6), (10, 1.5), arrowprops={"arrowstyle": "->", "color": green, "lw": 1.8})
    ax.text(8.3, 6.18, r"$A=(8,6)$", fontsize=13)
    ax.text(0.5, 3.55, r"$B=(2,3)$", fontsize=13, color=red)
    ax.text(10.1, 0.60, r"$C=(10,1.5)$", fontsize=13, color=green)
    ax.text(4.4, 1.0, "Past light cone of A", color=blue, fontsize=12)
    ax.text(2.3, 5.45, r"B to A would require $2c$", color=red, fontsize=11)
    ax.text(10.45, 4.2, "C can send\na subluminal signal", color=green, fontsize=11)
    ax.set(xlim=(0, 15), ylim=(0, 9.4), xlabel=r"Position $x$ (m)",
           ylabel=r"Time coordinate $ct$ (m)", aspect="equal", xticks=np.arange(0, 16, 2))
    ax.grid(alpha=0.16)
    secondary = ax.secondary_yaxis("right", functions=(lambda value: value / 3, lambda value: 3 * value))
    secondary.set_ylabel(r"Time $t$ ($10^{-8}$ s)")
    secondary.set_yticks([0, 0.5, 1, 2, 3])
    fig.suptitle("Which earlier event could have caused A?", fontsize=17, y=0.97)
    fig.text(0.5, 0.09, r"A causal signal requires $|\Delta x|\leq c\Delta t$ and $\Delta t>0$.",
             ha="center", fontsize=13)
    fig.text(0.5, 0.035, r"B is spacelike separated; C is timelike separated. Here $c\simeq3.00\times10^8$ m/s.",
             ha="center", fontsize=11, color=gray)
    fig.subplots_adjust(left=0.09, right=0.88, bottom=0.19, top=0.88)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white", transparent=False,
                metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
