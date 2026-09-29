"""Original illustrative lanes and logarithmic calibration; run from _media.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5. No measured data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


def distance(length):
    return 55 - 12*np.log10(np.asarray(length)/100)


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    lengths = np.array([100, 250, 500, 1000])
    distances = distance(lengths)
    unknown, unknown_d = 375, float(distance(375))
    fig, (lanes, curve) = plt.subplots(1, 2, figsize=(10.8, 6.4), dpi=100,
                                     gridspec_kw={"width_ratios": [1.05, 1]})
    fig.patch.set_facecolor("white")
    fig.suptitle("Reading DNA bands with a ladder: a constructed example", fontsize=16, y=.97)
    lanes.set_title("A. Schematic lanes", fontsize=13, pad=13)
    lanes.set_xlim(-.65, 4.9)
    lanes.set_ylim(60, -5)
    lanes.set_ylabel("Distance from wells (mm)  →", fontsize=11)
    lanes.set_yticks([0, 20, 40, 60])
    lanes.set_xticks([])
    for spine in ("top", "right", "bottom"):
        lanes.spines[spine].set_visible(False)
    labels = ["Ladder", "U", "Mixture", "Blank"]
    for x, label in zip([.75, 1.95, 3.15, 4.35], labels):
        lanes.add_patch(Rectangle((x-.37, 0), .74, 58, facecolor="#f0f4f8", edgecolor="#cbd5e1"))
        lanes.add_patch(Rectangle((x-.31, -.6), .62, 1.2, facecolor="white", edgecolor="#475569"))
        lanes.text(x, -2.8, label, ha="center", fontsize=11)
    for length, d in zip(lengths, distances):
        lanes.plot([.45, 1.05], [d, d], color="#265e8b", lw=4, solid_capstyle="butt")
        lanes.text(.28, d, str(length), va="center", ha="right", fontsize=10)
    lanes.plot([1.65, 2.25], [unknown_d, unknown_d], color="#c45127", lw=4, solid_capstyle="butt")
    for length in [250, 1000]:
        lanes.plot([2.85, 3.45], [distance(length)]*2, color="#265e8b", lw=4, solid_capstyle="butt")
    lanes.text(2.6, 22, "Each lane starts\nat its own well", ha="center", color="#475569", fontsize=11)
    lanes.annotate(f"U: {unknown_d:.2f} mm", xy=(1.95, unknown_d), xytext=(1.5, 34),
                   arrowprops={"arrowstyle": "->", "color": "#c45127"}, color="#c45127", fontsize=11)
    lanes.text(4.35, 53, "No\nband", ha="center", fontsize=10, color="#475569")
    lanes.text(-.4, 58.4, "bp", ha="center", fontsize=10)

    curve.set_title("B. Calibration on a logarithmic length axis", fontsize=12, pad=13)
    xs = np.geomspace(100, 1000, 150)
    curve.semilogx(xs, distance(xs), color="#265e8b", lw=2)
    curve.scatter(lengths, distances, color="#265e8b", s=45, zorder=3, label="Chosen ladder")
    curve.scatter([unknown], [unknown_d], s=65, color="#c45127", zorder=4, label="Chosen unknown")
    curve.plot([100, unknown, unknown], [unknown_d, unknown_d, 41.6], color="#c45127", ls="--", lw=1.2)
    curve.annotate(f"375 bp\n{unknown_d:.2f} mm", xy=(unknown, unknown_d), xytext=(570, 50.1),
                   arrowprops={"arrowstyle": "->", "color": "#c45127"}, color="#c45127", fontsize=11)
    curve.set_xlim(90, 1120)
    curve.set_ylim(41.6, 56.5)
    curve.set_xticks([100, 250, 500, 1000], ["100", "250", "500", "1000"])
    curve.minorticks_off()
    curve.set_xlabel("Linear double-stranded DNA length L (bp)", fontsize=11)
    curve.set_ylabel("Migration distance d (mm)", fontsize=11)
    curve.grid(alpha=.2)
    curve.text(.5, .10, r"$d=55-12\log_{10}(L/100)$", transform=curve.transAxes, ha="center", fontsize=13)
    curve.legend(loc="upper right", fontsize=10, frameon=False)
    fig.text(.5, .035, "Illustrative model, not a real gel or universal calibration. Band darkness does not encode DNA amount.",
             ha="center", fontsize=10, color="#455a64")
    fig.subplots_adjust(left=.075, right=.98, top=.85, bottom=.16, wspace=.32)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
