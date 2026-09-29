"""A one-space-dimensional slice of a light cone and three event types.

Coordinates x and ct are in light-seconds. Output is written to CWD.
Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12})
    fig, ax = plt.subplots(figsize=(9.2, 8.0), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.11, right=0.96, top=0.88, bottom=0.20)
    x = np.linspace(-5, 5, 501)
    ax.fill_between(x, np.abs(x), 5.2, color="#eef4fc", zorder=0)
    ax.fill_between(x, -np.abs(x), -5.2, color="#f1f4f8", zorder=0)
    ax.plot(x, x, color="#29795c", linewidth=2, label="Light-cone boundaries")
    ax.plot(x, -x, color="#29795c", linewidth=2)
    ax.axhline(0, color="#7c8692", linewidth=0.8)
    ax.axvline(0, color="#7c8692", linewidth=0.8)
    ax.plot([0, 3], [0, 4], color="#275aa0", linewidth=2.3,
            label="Straight massive-observer world line")
    ax.scatter([0], [0], color="#273643", s=40, zorder=5)
    ax.text(-0.55, -0.48, "O", weight="bold")
    events = [
        (3, 4, "#275aa0", "A: (x, ct) = (3, 4)\nTimelike: s² = −7",
         (1.4, 4.48)),
        (3, 3, "#29795c", "N: (3, 3)\nNull: s² = 0", (3.22, 3.12)),
        (3, 2, "#bb6430", "B: (3, 2)\nSpacelike: s² = 5", (3.22, 1.66)),
    ]
    for ex, et, color, label, position in events:
        ax.scatter([ex], [et], s=65, color=color, edgecolor="white", zorder=5)
        ax.annotate(label, xy=(ex, et), xytext=position, color=color, fontsize=11,
                    arrowprops={"arrowstyle": "-", "color": color}, zorder=6)
    ax.text(-1.8, 3.7, "Future timelike interior\ns² < 0", color="#275aa0",
            ha="center", fontsize=12)
    ax.text(-1.8, -3.8, "Past timelike interior\ns² < 0", color="#526a87",
            ha="center", fontsize=12)
    ax.text(-3.6, 0.7, "Spacelike\nexterior\ns² > 0", ha="center",
            color="#9d5a2b", fontsize=12)
    ax.set(xlim=(-5.1, 5.1), ylim=(-5.2, 5.2), aspect="equal",
           xlabel="Spatial coordinate x  [light-seconds]",
           ylabel="Time coordinate ct  [light-seconds]")
    ax.grid(alpha=0.15)
    ax.legend(loc="lower left", frameon=True, facecolor="white", fontsize=10)
    fig.suptitle("The sign of the interval determines the causal relation",
                 fontsize=16, y=0.96)
    fig.text(0.5, 0.055,
             "s² = x² − (ct)².  The cone is its null boundary, not the shaded interior.\n"
             "From O to A: speed 0.75c and clock time √7 seconds.",
             ha="center", fontsize=11, linespacing=1.5)
    fig.savefig(Path.cwd() / "minkowski-light-cone-events.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
