"""Draw laser-stimulated-emission-cycle.png in CWD on opaque white.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Illustrative nondegenerate transition and four-level cycle, not to scale.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, start, end, color, **kwargs):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "lw": 2.4,
                            "color": color, **kwargs})


def wave(ax, x0, x1, y):
    x = np.linspace(x0, x1, 160)
    ax.plot(x, y + .055 * np.sin(2 * np.pi * 4 * (x-x0)/(x1-x0)),
            color="#c44536", lw=1.8)
    arrow(ax, (x1-.035, y), (x1+.10, y), "#c44536")


def main():
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.4), dpi=110)
    fig.subplots_adjust(left=.035, right=.975, top=.80, bottom=.15, wspace=.24)
    for ax in axes:
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis("off")
    ax = axes[0]
    ax.set_title("One stimulated event", pad=18, fontsize=12)
    for y, label in [(.70, r"$E_2$"), (.26, r"$E_1$")]:
        ax.plot([.40, .59], [y, y], color="#273849", lw=2)
        ax.text(.61, y, label, va="center")
    ax.scatter([.49], [.70], color="#1768ac", s=65, zorder=4)
    arrow(ax, (.49, .68), (.49, .28), "#1768ac")
    wave(ax, .035, .29, .51)
    wave(ax, .69, .87, .55)
    wave(ax, .69, .87, .43)
    ax.text(.17, .64, "1 incoming\nphoton", ha="center")
    ax.text(.81, .72, "2 outgoing photons\nsame selected mode", ha="center")
    ax.text(.50, .10, r"Emitter supplies $\Delta E=h\nu$", ha="center")
    ax.text(.49, .82, "Initially excited", ha="center", color="#1768ac")
    ax = axes[1]
    ax.set_title("One four-level pumping route", pad=18, fontsize=12)
    levels = [(.12, "Ground"), (.32, r"Lower lasing $E_1$"),
              (.68, r"Upper lasing $E_2$"), (.90, "Pump level")]
    for y, label in levels:
        ax.plot([.23, .79], [y, y], color="#273849", lw=2)
        ax.text(.81, y, label, va="center", fontsize=9)
    arrow(ax, (.28, .14), (.28, .88), "#b27a15")
    ax.text(.16, .51, "Pump energy in", rotation=90, ha="center", va="center",
            color="#926310")
    arrow(ax, (.67, .88), (.67, .70), "#6b7c85")
    ax.text(.63, .79, "Rapid\nrelaxation", ha="right", va="center", fontsize=9)
    arrow(ax, (.53, .66), (.53, .34), "#c44536")
    ax.text(.58, .50, "Lasing\nlight out", va="center", color="#c44536")
    arrow(ax, (.67, .30), (.67, .14), "#6b7c85")
    ax.text(.63, .22, "Rapid\nrelaxation", ha="right", va="center", fontsize=9)
    fig.suptitle("Stored material energy becomes additional light", fontsize=15, y=.98)
    fig.text(.5, .04, "Schematic paths; energy spacing is not to scale. This cycle does not describe every laser.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / "laser-stimulated-emission-cycle.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
