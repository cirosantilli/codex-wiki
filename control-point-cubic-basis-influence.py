"""Plot the influence of one cubic handle; save the matching PNG in CWD.

Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7.
Run from _media with MPLBACKEND=Agg.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    t = np.linspace(0, 1, 601)
    b = 3*t*(1-t)**2
    fig, ax = plt.subplots(figsize=(8.8, 5.3), layout="constrained")
    ax.plot(t, b, color="#bb4f12", lw=3)
    ax.fill_between(t, 0, b, color="#bb4f12", alpha=.08)
    ax.set(xlim=(-.035, 1.035), ylim=(-.035, .56),
           xlabel="Curve parameter $t$ (not arc length)",
           ylabel=r"Influence $b_{1,3}(t)$ = upward displacement $\Delta y$")
    ax.set_xticks((0, 1/3, .5, 1), ("0", "$1/3$", "$1/2$", "1"))
    ax.set_yticks((0, .125, .25, .375, 4/9),
                 ("0", "$1/8$", "$1/4$", "$3/8$", "$4/9$"))
    ax.grid(alpha=.2)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.axhline(0, color="#555555", lw=1)
    ax.plot((0, 1), (0, 0), "o", color="#333333", ms=6)
    ax.plot((1/3, .5), (4/9, 3/8), "o", color="#bb4f12", ms=6)
    ax.annotate("", (1/3, 4/9), (1/3, 0),
                arrowprops={"arrowstyle": "<->", "lw": 1.5, "color": "#333333"})
    ax.annotate("Largest same-parameter displacement: $4/9$", (1/3, 4/9),
                xytext=(.12, .515), fontsize=11,
                arrowprops={"arrowstyle": "-", "color": "#555555"})
    ax.annotate("At $t=1/2$: $3/8$", (.5, 3/8), xytext=(.62, .40),
                fontsize=11, arrowprops={"arrowstyle": "-", "color": "#555555"})
    ax.text(.025, .032, "Start unchanged", fontsize=10)
    ax.text(.975, .11, "End unchanged", ha="right", fontsize=10)
    ax.text(.79, .30, r"$\Delta C(t)=(0,b_{1,3}(t))$" + "\n" +
            r"$h=(0,1),\quad \|h\|=1$", fontsize=12, ha="center")
    ax.set_title(r"One handle's influence: $b_{1,3}(t)=3t(1-t)^2$", pad=15, fontsize=16)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
