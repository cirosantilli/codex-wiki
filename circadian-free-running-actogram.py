"""Draw a stipulated circadian actogram, not a record from an animal.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch, Rectangle


TAU = 23.5
ENVIRONMENT_PERIOD = 24.0
LD_DAYS = 7
TOTAL_DAYS = 24
ACTIVITY_DURATION = 8.0
RELEASE = LD_DAYS * ENVIRONMENT_PERIOD


def activity_intervals():
    """Absolute-time intervals; the first DD onset preserves the LD phase."""
    intervals = [(24.0 * day + 12.0, 24.0 * day + 20.0)
                 for day in range(LD_DAYS)]
    onset = RELEASE + 12.0
    while onset < TOTAL_DAYS * ENVIRONMENT_PERIOD:
        intervals.append((onset, onset + ACTIVITY_DURATION))
        onset += TAU
    return intervals


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(9, 6.6), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.16, right=0.97, bottom=0.19, top=0.83)
    for day in range(TOTAL_DAYS):
        ax.add_patch(Rectangle((0, day + 0.5), 24, 1,
                               facecolor="#edf0f3", edgecolor="white", lw=0.8))
        if day < LD_DAYS:
            ax.add_patch(Rectangle((0, day + 0.5), 12, 1,
                                   facecolor="#fff2c9", edgecolor="white", lw=0.8))
    for start, end in activity_intervals():
        for day in range(TOTAL_DAYS):
            left = max(start, day * 24.0)
            right = min(end, (day + 1) * 24.0)
            if right > left:
                ax.add_patch(Rectangle((left - day * 24.0, day + 0.68),
                                       right - left, 0.64,
                                       facecolor="#087e8b", edgecolor="none"))
        day = int(start // 24.0)
        if day < TOTAL_DAYS:
            ax.plot(start % 24, day + 1, "|", color="#003e47", markersize=11)
    ax.axhline(LD_DAYS + 0.5, color="#b94b32", lw=1.5, ls="--")
    ax.text(-2.7, 4, "12:12 LD", rotation=90, ha="center", va="center",
            color="#66521e", clip_on=False)
    ax.text(-2.7, 16, "Constant darkness (DD)", rotation=90,
            ha="center", va="center", color="#49535e", clip_on=False)
    ax.annotate("First DD onset:\n12 h", xy=(12, 8), xytext=(20.5, 10),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#003e47"})
    ax.annotate("17th DD onset: 4 h", xy=(4, 24), xytext=(17, 22),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#003e47"})
    ax.set(xlim=(0, 24), ylim=(24.65, 0.4), xlabel="Hour within a fixed 24-hour plotting row",
           ylabel="Successive calendar day")
    ax.set_xticks(np.arange(0, 25, 4))
    ax.set_yticks([1, 7, 8, 12, 16, 20, 24])
    fig.suptitle("A clock that keeps running when the light cycle stops", y=0.97, fontsize=15)
    fig.text(0.5, 0.915, "Original idealized model: τ = 23.5 h; every activity bout lasts 8 h",
             ha="center", fontsize=11)
    fig.legend(handles=[Patch(facecolor="#fff2c9", label="Light"),
                        Patch(facecolor="#edf0f3", label="Dark"),
                        Patch(facecolor="#087e8b", label="Constructed activity")],
               loc="upper center", bbox_to_anchor=(0.5, 0.9), ncol=3, frameon=False)
    fig.text(0.5, 0.065, "DD onsets are 23.5 h apart: 0.5 h earlier per cycle on this 24 h grid.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.027, "Stipulated phase and activity windows; no mouse or human observations.",
             ha="center", fontsize=10, color="#555555")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
