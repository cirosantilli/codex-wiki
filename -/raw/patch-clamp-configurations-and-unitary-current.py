"""Original patch-clamp schematic and synthetic channel traces.

Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Run from _media; the matching opaque PNG is written to the working directory.
No experimental data are used. Outward membrane current is positive.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle
import numpy as np


def channel_current(voltage_mv, conductance_ps=10.0, reversal_mv=0.0):
    """pS * mV / 1000 = pA."""
    return conductance_ps * (np.asarray(voltage_mv) - reversal_mv) / 1000


def configuration(ax, whole_cell):
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.axhspan(0, 0.35, color="#edf6fc")
    for a, b in [(0, 0.43), (0.57, 1)]:
        ax.plot([a, b], [0.35, 0.35], color="#24689a", lw=4)
    ax.add_patch(Polygon([(0.24, 0.98), (0.43, 0.35), (0.57, 0.35),
                          (0.76, 0.98)], closed=False, fill=False,
                         edgecolor="#666666", lw=3))
    ax.plot([0.5, 0.5], [0.99, 0.65], color="#555555", lw=3)
    ax.text(0.53, 0.78, "electrode\nto amplifier", fontsize=10)
    ax.text(0.03, 0.73, "bath", fontsize=11)
    ax.text(0.03, 0.19, "cytosol", fontsize=11)
    for x in (0.43, 0.57):
        ax.add_patch(Circle((x, 0.35), 0.022, color="#c5741b", zorder=5))
    ax.annotate("seal at glass rim", xy=(0.57, 0.35), xytext=(0.66, 0.52),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#c5741b"})
    if whole_cell:
        ax.annotate("", xy=(0.5, 0.20), xytext=(0.5, 0.55),
                    arrowprops={"arrowstyle": "<->", "color": "#ad3e45", "lw": 2})
        ax.text(0.64, 0.12, "open access;\nsolution exchange", fontsize=10)
        ax.set_title("Whole-cell: patch ruptured, seal retained", fontsize=12, loc="left")
    else:
        ax.plot([0.43, 0.57], [0.35, 0.35], color="#24689a", lw=4)
        ax.annotate("intact membrane patch", xy=(0.49, 0.35), xytext=(0.35, 0.08),
                    fontsize=10, arrowprops={"arrowstyle": "->"})
        ax.set_title("Cell-attached: membrane under tip intact", fontsize=12, loc="left")


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(2, 2, figsize=(10.8, 7.8),
                             gridspec_kw={"width_ratios": [1.08, 1]})
    configuration(axes[0, 0], False)
    configuration(axes[1, 0], True)
    t = np.arange(0, 100.01, 0.1)
    opened = ((t >= 15) & (t < 35)) | ((t >= 60) & (t < 80))
    for v, color in [(-80, "#24689a"), (-40, "#c5741b")]:
        axes[0, 1].plot(t, opened * channel_current(v), color=color,
                        label=f"V = {v} mV")
    axes[0, 1].set(title="Synthetic openings: prescribed times",
                   xlabel="Time (ms)", ylabel="Outward current (pA)", ylim=(-1, 0.15))
    axes[0, 1].legend(loc="lower right", fontsize=10)
    v = np.linspace(-100, 40, 141)
    axes[1, 1].plot(v, channel_current(v), color="#24689a")
    axes[1, 1].axhline(0, color="#aaaaaa", lw=0.8)
    axes[1, 1].axvline(0, color="#aaaaaa", lw=0.8)
    axes[1, 1].scatter([-80, -40, 0], channel_current([-80, -40, 0]), color="#c5741b", zorder=3)
    axes[1, 1].set(title="Synthetic open-channel current–voltage relation",
                   xlabel="Membrane potential (mV)", ylabel="Outward current (pA)")
    axes[1, 1].text(-96, 0.22, "g = 10 pS; reversal = 0 mV", fontsize=10)
    fig.suptitle("Patch configuration and unitary current", fontsize=16)
    fig.text(0.5, 0.025, "Original schematic; no experimental data. Voltage is across the membrane,\n"
             "not the pipette command in an intact cell-attached recording. No noise or filtering modeled.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.065, right=0.975, top=0.90, bottom=0.15, hspace=0.45, wspace=0.35)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
