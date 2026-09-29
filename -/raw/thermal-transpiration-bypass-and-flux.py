"""Simplified capillary apparatus and separate thin-hole molecular toy model.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../thermal-transpiration-bypass-and-flux.py
Output: matching PNG basename in the current working directory.
Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Apparatus inspired by Rojas Cardenas et al., doi:10.1299/jtst.7.437.
No measured curves or hardware photographs are reproduced. Thin-hole arrows
use relative rates p/sqrt(T), not an empirical capillary calibration.
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


COLD, HOT, INK = "#1472aa", "#bb542d", "#293e54"


def arrow(ax, start, end, color, width=2):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=13, lw=width, color=color))


def reservoir(ax, x, color, title):
    ax.add_patch(Rectangle((x, 1.0), 1.85, 1.45, facecolor="white", edgecolor=color, lw=2.4))
    ax.text(x + 0.925, 1.75, title, ha="center", va="center", color=color, fontsize=11)


def main():
    plt.rcParams.update({"font.size": 11})
    fig = plt.figure(figsize=(9.4, 7.2), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=[1.25, 1.0])
    ax = fig.add_subplot(grid[0, :])
    ax.set(xlim=(0, 10), ylim=(0, 4.5))
    ax.axis("off")
    ax.set_title("Simplified glass-microtube experiment: close the bypass at t = 0", fontsize=13)
    reservoir(ax, 0.4, COLD, "Cold reservoir\nrecord $p_c(t)$")
    reservoir(ax, 7.75, HOT, "Heated reservoir\nrecord $p_h(t)$")
    ax.plot([2.25, 7.75], [1.8, 1.8], color=INK, lw=2)
    ax.plot([2.25, 7.75], [1.5, 1.5], color=INK, lw=2)
    ax.text(5, 1.13, "glass microtube: diameter 490 µm; length 3.05 cm", ha="center", fontsize=10)
    arrow(ax, (3.4, 2.15), (6.6, 2.15), HOT)
    ax.text(5, 2.4, "initial net gas transfer: cold → hot", ha="center", fontsize=10)
    ax.plot([1.3, 1.3, 4.65], [2.45, 3.4, 3.4], color="#687782", lw=3)
    ax.plot([5.35, 8.7, 8.7], [3.4, 3.4, 2.45], color="#687782", lw=3)
    ax.plot([4.65, 5.35], [3.65, 3.15], color=INK, lw=2.5)
    ax.text(5, 3.94, "wide bypass: open to equalize pressures; then shut", ha="center", fontsize=10)
    ax.text(5, 0.57, "Isolate supply and pump. Measure tube-end temperatures as well as reservoir conditions.", ha="center", fontsize=10)
    ax.text(5, 0.13, "At final zero net transfer: $p_h>p_c$. The pressure ratio depends on rarefaction and walls.", ha="center", fontsize=10)

    tc, th = 300.0, 351.0
    ratio = math.sqrt(th / tc)
    hot_initial = 1 / ratio
    for i, final in enumerate([False, True]):
        ax = fig.add_subplot(grid[1, i])
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis("off")
        ax.text(0.5, 0.96, "Ideal thin-hole model: " + ("zero net transfer" if final else "equal pressures"), ha="center", fontsize=11, weight="bold")
        ax.text(0.21, 0.78, "$T_c=300$ K\n$p_c=1$", color=COLD, ha="center")
        ax.text(0.80, 0.78, "$T_h=351$ K\n" + (f"$p_h={ratio:.4f}$" if final else "$p_h=1$"), color=HOT, ha="center")
        # A thin partition with a small aperture; not the actual glass tube.
        ax.plot([0.5, 0.5], [0.40, 0.48], color=INK, lw=3)
        ax.plot([0.5, 0.5], [0.65, 0.84], color=INK, lw=3)
        hot_rate = 1.0 if final else hot_initial
        arrow(ax, (0.14, 0.61), (0.86, 0.61), COLD, width=2.5)
        arrow(ax, (0.86, 0.51), (0.86 - 0.72 * hot_rate, 0.51), HOT, width=2.5)
        ax.text(0.5, 0.33, f"one-way rates: 1.0000 →    ← {hot_rate:.4f}", ha="center", fontsize=10)
        ax.text(0.5, 0.18, "net cold → hot" if not final else r"$p_h/p_c=\sqrt{351/300}$", ha="center", color=INK)
        ax.text(0.5, 0.04, "Each panel normalizes cold pressure and outgoing rate to 1.", ha="center", fontsize=9)
    fig.suptitle("Thermal transpiration: unequal pressures can balance unequal temperatures", fontsize=14)
    fig.supxlabel("Schematic and ideal limits only. No measured capillary curves are shown.", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
