"""Exact relaxation of a stipulated reversible catalytic mass-action model.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media: MPLBACKEND=Agg python ../catalysis-reversible-equilibrium-relaxation.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


def rates(catalyst_concentration):
    """Concentration in mol/L; output effective first-order constants in 1/s."""
    return 0.030 + 270 * catalyst_concentration, 0.010 + 90 * catalyst_concentration


def fraction(t, x0, catalyst_concentration):
    kf, kr = rates(catalyst_concentration)
    equilibrium = kf / (kf + kr)
    return equilibrium + (x0 - equilibrium) * np.exp(-(kf + kr) * t)


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.8), dpi=120, sharey=True)
    fig.subplots_adjust(left=0.085, right=0.96, bottom=0.28, top=0.80, wspace=0.12)
    for ax, end, title in zip(axes, [120, 15], ["Longer observation", "Early approach"]):
        t = np.linspace(0, end, 1201)
        for x0, color in [(0, "#176b9b"), (1, "#b64b27")]:
            for c, style in [(0, "--"), (0.001, "-")]:
                kf, kr = rates(c)
                assert np.isclose(kf / kr, 3)
                ax.plot(t, fraction(t, x0, c), color=color, linestyle=style, lw=2.3)
        ax.axhline(0.75, color="#333333", ls=":", lw=1.8)
        ax.set(xlim=(0, end), ylim=(-0.025, 1.025), xlabel="Time / s", title=title)
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel(r"B fraction: $[B]/([A]+[B])$")
    axes[0].text(118, 0.77, "Common equilibrium: ¾", ha="right", fontsize=10)
    handles = [Line2D([], [], color="#176b9b", lw=2.3, label="Initially all A"),
               Line2D([], [], color="#b64b27", lw=2.3, label="Initially all B"),
               Line2D([], [], color="#444444", lw=2.3, ls="--", label="No C: τ = 25 s"),
               Line2D([], [], color="#444444", lw=2.3, label="With C: τ = 2.5 s")]
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.075),
               ncol=2, frameon=False, fontsize=11)
    fig.suptitle("Catalysis changes relaxation time, not this model's equilibrium", fontsize=15)
    fig.text(0.5, 0.88, "Illustrative exact model: both forward/reverse rate ratios equal 3",
             ha="center", fontsize=11)
    fig.text(0.5, 0.03, "With C: [C] = 0.001 mol/L. All parameters are stipulated, not fitted measurements.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
