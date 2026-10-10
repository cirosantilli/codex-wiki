"""Generate an original functional schematic and hypothetical charge-loss readout.

Run from _media. Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
The geometry and traces are explanatory models, not historical measurements.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np


def charge_loss_model():
    """Return synthetic readout parameters in SI units and hours."""
    elementary_charge = 1.602176634e-19
    capacitance = 2e-12
    volume = 2e-3
    total_slope = 6.0  # V/hour; invented, not Hess's calibration
    leakage_slope = 0.6
    ion_current = capacitance * (total_slope - leakage_slope) / 3600
    pairs_per_volume_second = ion_current / (elementary_charge * volume)
    return ion_current, pairs_per_volume_second


def draw():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11.2, 6.0), dpi=120, facecolor="white")
    left = fig.add_axes([0.025, 0.22, 0.49, 0.64])
    right = fig.add_axes([0.63, 0.30, 0.34, 0.50])
    fig.suptitle("From air ionization to electrometer discharge", fontsize=18, y=0.96)
    fig.text(0.5, 0.885, "Functional schematic and invented readout — not Hess's measured traces",
             ha="center", fontsize=11, color="#545454")
    left.set(xlim=(0, 10), ylim=(0, 8))
    left.axis("off")

    left.add_patch(Rectangle((1.0, 1.5), 5.0, 4.6, linewidth=7,
                             edgecolor="#65717d", facecolor="#f6f9fc"))
    left.text(3.5, 0.9, r"Sealed gas volume $\mathcal{V}$" + "\nconducting vessel wall", ha="center", va="top")
    left.add_patch(Rectangle((3.3, 1.55), 0.4, 3.3, facecolor="#b83b37", edgecolor="none"))
    left.text(3.5, 3.8, "+", color="white", ha="center", va="center", fontsize=17)
    left.text(3.9, 4.65, "Charged\nelectrode", ha="left", fontsize=10)
    left.add_patch(Rectangle((3.15, 5.85), 0.7, 0.5, facecolor="#ede1b9", edgecolor="#75663c"))
    left.plot([3.5, 3.5, 7.5], [4.85, 6.6, 6.6], color="#b83b37", lw=2)
    left.text(4.0, 6.55, "Insulator", ha="left", va="bottom", fontsize=10)
    left.plot([7.5, 7.0], [6.6, 4.7], color="#b83b37", lw=2)
    left.plot([7.5, 8.0], [6.6, 4.7], color="#b83b37", lw=2)
    left.annotate("Fiber separation\nindicates voltage $U$", xy=(7.5, 4.95), xytext=(7.6, 3.5),
                  ha="center", arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    left.text(7.6, 7.1, "Electrometer", ha="center", fontsize=12)

    for x, y in [(2.2, 3.2), (4.8, 2.5), (2.3, 4.6)]:
        left.text(x, y, "−", color="#1867a6", ha="center", va="center", fontsize=18)
        left.text(x + 0.35, y + 0.4, "+", color="#27734d", ha="center", va="center", fontsize=15)
        target = 3.2 if x < 3.5 else 3.8
        left.add_patch(FancyArrowPatch((x, y - 0.1), (target, y - 0.1),
                                       arrowstyle="->", mutation_scale=10, color="#1867a6"))
    left.text(1.45, 2.0, "Ion pairs in air", fontsize=10)
    left.add_patch(FancyArrowPatch((0.1, 7.35), (2.0, 5.1), arrowstyle="->",
                                   mutation_scale=15, color="#714199", lw=2))
    left.text(0.1, 7.6, "Penetrating radiation", color="#714199", fontsize=11)
    left.text(7.8, 2.1, "Effective capacitance $C$\nStored charge $Q=CU$", ha="center", fontsize=10)

    time = np.linspace(0, 2, 101)
    right.plot(time, 180 - 0.6 * time, color="#66717d", ls="--", lw=2,
               label="Leakage alone: 0.60 V/h")
    right.plot(time, 180 - 6 * time, color="#b83b37", lw=2.5,
               label="Total loss: 6.00 V/h")
    right.set(xlabel="Elapsed time (hours)", ylabel="Electrometer voltage $U$ (V)",
              xlim=(0, 2), ylim=(166.5, 181.5), title="Hypothetical discharge")
    right.set_xticks([0, 0.5, 1, 1.5, 2])
    right.grid(alpha=0.2)
    right.legend(loc="lower left", fontsize=9, framealpha=1)
    right.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.14, r"$C=2.00$ pF,   $\mathcal{V}=2.00$ L,   full collection:   "
             r"$q=\dfrac{C(6.00-0.60)\,/\,3600}{e\mathcal{V}}=9.36\ \mathrm{cm^{-3}\,s^{-1}}$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.045, "The readout integrates ionization; it does not identify or count incoming primary particles.",
             ha="center", fontsize=11, color="#333333")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    draw()
