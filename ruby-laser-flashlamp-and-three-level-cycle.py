"""Original ruby-laser functional diagram and simplified pump cycle.

Python 3.14 / matplotlib 3.10 / numpy 2.3. Write matching PNG to the CWD.
This is not a historical drawing, a dimensioned plan or a chromium spectrum.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size":11, "axes.spines.top":False,
                         "axes.spines.right":False})
    fig, (ax, levels) = plt.subplots(1, 2, figsize=(12.4, 6.3), facecolor="white",
                                     gridspec_kw={"width_ratios":[1.25, 1]})
    fig.subplots_adjust(left=.045, right=.96, bottom=.14, top=.79, wspace=.27)
    ax.set(xlim=(-.9, 8.8), ylim=(-1.8, 3.8)); ax.axis("off")
    ax.add_patch(FancyBboxPatch((1.1, .6), 4.8, .7, boxstyle="round,pad=0.04",
                               facecolor="#ec9b9b", edgecolor="#8e3535", lw=1.8))
    # A two-dimensional functional projection of a surrounding helical lamp.
    t = np.linspace(0, 12*np.pi, 800)
    xx = 1.0+5.0*t/t[-1]
    ax.plot(xx, .95+1.0*np.sin(t), color="#d99b27", lw=3, alpha=.9)
    for x in [1.1, 5.9]:
        ax.add_patch(Rectangle((x-.055, .50), .11, .90, facecolor="#497fab", zorder=4))
    ax.annotate("", (5.5, .95), (1.5, .95), arrowprops={"arrowstyle":"<->", "lw":2.1, "color":"#a02e34"}, zorder=5)
    ax.annotate("", (8.3, .95), (6.1, .95), arrowprops={"arrowstyle":"->", "lw":3, "color":"#c42e35"})
    ax.text(7.0, 1.45, "Emitted\nred light", ha="center", color="#98252c")
    ax.text(3.5, 2.55, "Flashlamp surrounds the ruby", ha="center", fontsize=12)
    ax.annotate("", (3.5, 1.65), (3.5, 2.35), arrowprops={"arrowstyle":"->", "color":"#a6711c"})
    ax.text(3.5, -.75, "Crystal with coated parallel end faces", ha="center", fontsize=11)
    ax.text(3.5, -1.45, "Feedback returns light through the excited medium.\nGeometry and coupling fractions are schematic.",
            ha="center", fontsize=10, color=".3")
    ax.set_title("Store excitation in a pumped crystal", fontsize=13, pad=15)

    pump_e, laser_e = 1239.841984/550, 1239.841984/694.3
    for y, label in [(0, "Ground state / lower laser state"),
                     (laser_e, "Upper laser state"), (pump_e, "Pump state")]:
        levels.plot([.28, .91], [y, y], color="#394b5b", lw=2.1)
        levels.text(.94, y, label, va="center", fontsize=10)
    levels.annotate("", (.36, pump_e-.03), (.36, .03),
                    arrowprops={"arrowstyle":"->", "color":"#478651", "lw":2})
    levels.text(.06, .95, "Pump\n550 nm", color="#377543", ha="center", fontsize=10)
    levels.annotate("", (.60, laser_e+.03), (.60, pump_e-.03),
                    arrowprops={"arrowstyle":"->", "color":"#8a7049", "lw":1.8})
    levels.text(.64, (pump_e+laser_e)/2, "Fast nonradiative\nrelaxation", va="center", fontsize=9)
    levels.annotate("", (.80, .03), (.80, laser_e-.03),
                    arrowprops={"arrowstyle":"->", "color":"#ba393d", "lw":2.5})
    levels.text(1.06, .90, "Laser emission\n694.3 nm", color="#a52b35", fontsize=10)
    levels.set(xlim=(-.08, 2.05), ylim=(-.20, 2.65), ylabel="Energy above ground (eV)")
    levels.set_xticks([])
    levels.set_yticks([0, 1, 2])
    levels.spines["bottom"].set_visible(False)
    levels.set_title("Simplified three-level cycle", fontsize=13, pad=15)
    fig.suptitle("Ruby laser: pump, store, stimulate and feed back", y=.965, fontsize=18)
    fig.text(.5, .895, "Original functional model; no historical dimensions, reflectivities or crystal fine structure are assigned",
             ha="center", color=".3", fontsize=10)
    fig.text(.5, .045, "The energy sketch uses two chosen photon wavelengths. A real flashlamp has a broad spectrum and the crystal has sublevels.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd()/(Path(__file__).stem+".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
