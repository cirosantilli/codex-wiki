"""Original cutback schematic and additive-offset calculation.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run in the desired output directory; writes the matching PNG there.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig, (ax, plot) = plt.subplots(1, 2, figsize=(11, 5.4), dpi=120,
                                  gridspec_kw={"width_ratios": [1.22, 1]})
    fig.patch.set_facecolor("white")
    fig.suptitle("Fiber cutback: cancel the launch, subtract the background", fontsize=16)
    ax.set(xlim=(0, 10), ylim=(0, 10))
    ax.axis("off")
    ax.set_title("A. Functional measurement; original chosen values", fontsize=11)

    def box(x, y, w, label, color="#edf2f7"):
        ax.add_patch(FancyBboxPatch((x, y), w, .95, boxstyle="round,pad=0.08",
                                    facecolor=color, edgecolor="#36465b"))
        ax.text(x + w / 2, y + .475, label, ha="center", va="center", fontsize=10)

    box(.1, 7.7, 1.55, "Stable\nsource")
    box(2.1, 7.7, 1.65, "Fixed\nlaunch")
    ax.annotate("", xy=(2.05, 8.175), xytext=(1.7, 8.175),
                arrowprops={"arrowstyle": "->", "color": "#2563a4", "lw": 2})
    ax.plot([3.85, 4.55, 5.2], [8.175, 8.175, 8.1], color="#2563a4", lw=3)
    t = np.linspace(0, 4 * np.pi, 300)
    ax.plot(5.2 + .6 * np.sin(t), 6.9 + 1.2 * np.cos(t), color="#2563a4", lw=2)
    ax.plot([5.2, 6.8, 6.8, 7.2], [8.1, 8.1, 7.2, 7.2], color="#2563a4", lw=2)
    box(7.3, 6.7, 2.4, "Detector\n79.4328 µW")
    ax.text(5.5, 5.2, "Long fiber: 2.1 km", ha="center", color="#2563a4")
    ax.annotate("Cut at 0.1 km;\nkeep input untouched", xy=(4.1, 8.15), xytext=(1.8, 4.2),
                ha="center", arrowprops={"arrowstyle": "->", "color": "#b45309"})
    ax.plot([2.7, 4.8], [2.6, 2.6], color="#2563a4", lw=3)
    box(.3, 2.1, 2.3, "Same input")
    box(5.1, 2.1, 2.6, "Detector\n100 µW")
    ax.annotate("", xy=(5, 2.6), xytext=(4.2, 2.6),
                arrowprops={"arrowstyle": "->", "color": "#2563a4", "lw": 2})
    ax.text(5, 1.35, "Short fiber: 0.1 km", ha="center", color="#2563a4")
    ax.text(5, .2, "Dark reading • linear detector • same collection\nNew end face and mode changes remain possible errors",
            ha="center", va="bottom", fontsize=9)

    b = np.linspace(0, 30, 250)
    short, long = 100, 100 * 10**(-.1)
    apparent = 5 * np.log10((short + b) / (long + b))
    plot.plot(b, apparent, color="#b45309", lw=2.5, label="Background left in readings")
    plot.axhline(.5, color="#2563a4", ls="--", lw=2, label="Background subtracted")
    y = 5 * np.log10(105 / (long + 5))
    plot.scatter([5], [y], color="#b45309", zorder=4)
    plot.annotate(f"5 µW offset\n{y:.5f} dB/km", xy=(5, y), xytext=(10, .46),
                  arrowprops={"arrowstyle": "->"}, fontsize=10)
    plot.set(xlim=(0, 30), ylim=(.35, .52), xlabel="Common additive background (µW)",
             ylabel="Inferred attenuation (dB/km)", title="B. A common offset does not cancel")
    plot.grid(alpha=.2)
    plot.legend(loc="lower left", fontsize=9)
    fig.text(.5, .015, "Calculated example: 2 km removed, true attenuation 0.5 dB/km. No historical measurements.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, .045, 1, .93), w_pad=2)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
