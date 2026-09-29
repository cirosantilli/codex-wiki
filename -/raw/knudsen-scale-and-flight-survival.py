"""Draw scale comparisons and an explicitly fixed-hazard free-flight toy model.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../knudsen-scale-and-flight-survival.py
Output: matching PNG basename in the current working directory.
Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
No experimental data; lambda is a prescribed toy mean free path.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig = plt.figure(figsize=(9.4, 6.9), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 3, height_ratios=[1.05, 1.15])
    ratios = [0.03, 0.5, 3.0]
    colors = ["#1670a7", "#90539c", "#bb5a20"]
    labels = ["Much shorter than the gap", "Comparable scales", "Longer than the gap"]
    for i, (kn, color, label) in enumerate(zip(ratios, colors, labels)):
        ax = fig.add_subplot(grid[0, i])
        ax.set(xlim=(0, 1), ylim=(0, 2.9))
        ax.axis("off")
        # All three wall separations represent L=0.7 drawing units.
        low, high = 0.35, 1.05
        ax.plot([0.08, 0.92], [low, low], lw=5, color="#79848e", solid_capstyle="butt")
        ax.plot([0.08, 0.92], [high, high], lw=5, color="#79848e", solid_capstyle="butt")
        ax.annotate("", (0.18, high), (0.18, low), arrowprops={"arrowstyle": "<->", "color": "#333333"})
        ax.text(0.11, (low + high) / 2, "$L$", ha="right", va="center")
        ax.plot([0.56, 0.56], [low, low + kn * (high - low)], lw=4, color=color, solid_capstyle="butt")
        ax.plot([0.51, 0.61], [low + kn * (high - low)] * 2, lw=2, color=color)
        if i == 0:
            ax.annotate(r"$\ell_{\rm mfp}$", (0.56, low + kn * (high - low)), (0.72, 0.63),
                        color=color, va="center", arrowprops={"arrowstyle": "-", "color": color})
        else:
            ax.text(0.66, low + kn * (high - low), r"$\ell_{\rm mfp}$", color=color, va="center")
        ax.text(0.5, 2.75, rf"$\mathrm{{Kn}}={kn:g}$", ha="center", weight="bold", fontsize=14)
        ax.text(0.5, 0.08, label, ha="center", fontsize=10)
    ax = fig.add_subplot(grid[1, :])
    kns = np.geomspace(0.01, 100, 700)
    survival = np.exp(-1 / kns)
    ax.semilogx(kns, survival, color="#293e54", lw=2.6)
    for kn, color in zip(ratios, colors):
        p = float(np.exp(-1 / kn))
        ax.plot(kn, p, "o", color=color, ms=7, zorder=3)
    ax.set(xlabel=r"Prescribed ratio $\mathrm{Kn}=\ell_{\rm mfp}/L$", ylabel="Probability of no gas–gas collision",
           ylim=(-0.025, 1.06), xlim=(0.01, 100))
    ax.set_title(r"Single flight of length $L$: $P_0=e^{-L/\ell_{\rm mfp}}$", fontsize=12)
    ax.grid(alpha=0.18, which="both")
    fig.suptitle("Mean free path is a molecular scale; the gap is an apparatus scale", fontsize=14)
    fig.supxlabel("Toy constant hazard per distance. Chosen points are not regime boundaries or measured data.", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
