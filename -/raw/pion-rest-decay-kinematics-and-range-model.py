"""Original relativistic calculation and expressly synthetic range illustration.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5; run from _media, PNG to CWD.
Rounded masses are calculation inputs. No historical data or calibrated ranges.
The normal response width and two illustrative mean ranges are stipulated.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def decay_values(mpi=139.57, mmu=105.66):
    """Energies in MeV, with masses represented by rest energies."""
    pc = (mpi**2 - mmu**2) / (2 * mpi)
    emu = (mpi**2 + mmu**2) / (2 * mpi)
    return pc, emu - mmu, pc


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, (ax, hist) = plt.subplots(1, 2, figsize=(11, 5.8), facecolor="white")
    fig.subplots_adjust(left=.055, right=.975, top=.78, bottom=.22, wspace=.28)
    fig.suptitle("Stopped pion: one visible daughter, one inferred partner", fontsize=17, y=.97)
    fig.text(.5, .88, "Original calculation + synthetic range response; no historical plate data",
             ha="center", fontsize=11, color="#555555")
    pc, tmu, enu = decay_values()
    blue, orange = "#156a9a", "#b45b13"
    ax.set(xlim=(-1.6, 1.6), ylim=(-1.05, 1.4), aspect="equal")
    ax.axis("off")
    ax.set_title("Decay at rest: equal and opposite momenta", fontsize=12, pad=18)
    # Incoming stopping track is a path before the decay, not initial decay momentum.
    t = np.linspace(0, 1, 30)
    ax.scatter(-1.35+1.35*t, .86*(1-t)**1.25, s=6+14*t, color="#777777")
    ax.text(-1.47, 1.1, r"$\pi^+$ arrives and stops", fontsize=11, color="#555555")
    ax.scatter([0], [0], s=45, color="black", zorder=5)
    ax.add_patch(FancyArrowPatch((0, 0), (1.35, .43), arrowstyle="-|>",
                 mutation_scale=18, color=blue, lw=2.3))
    ax.add_patch(FancyArrowPatch((0, 0), (-1.35, -.43), arrowstyle="-|>",
                 mutation_scale=18, color=orange, lw=2.3, linestyle="--"))
    ax.text(.62, .6, r"$\mu^+$", color=blue, fontsize=15)
    ax.text(-1.48, -.7, r"$\nu_\mu$: inferred, no grain track", color=orange, fontsize=10)
    ax.text(-1.48, -.98, "Earlier path is not a third decay momentum.", fontsize=10)
    fig.text(.055, .135, rf"Rounded inputs: $m_\pi c^2=139.57$, $m_\mu c^2=105.66$ MeV", fontsize=10)
    fig.text(.055, .08, rf"$pc={pc:.2f}$ MeV     $T_\mu={tmu:.3f}$ MeV     $E_\nu={enu:.2f}$ MeV", fontsize=11)

    rng = np.random.default_rng(734)
    first = rng.normal(1., .06, 6000)
    # This mixture is a comparison response, not a pion-decay prediction.
    mixture = np.r_[rng.normal(1., .06, 3000), rng.normal(1.35, .06, 3000)]
    bins = np.linspace(.65, 1.65, 41)
    hist.hist(first, bins=bins, density=True, color=blue, alpha=.35,
              label="One chosen range: 1.00")
    hist.hist(mixture, bins=bins, density=True, histtype="step", color=orange,
              lw=2, label="Two chosen ranges: 1.00, 1.35")
    hist.set(xlabel="Stipulated range / arbitrary reference range",
             ylabel="Probability density", xlim=(.65, 1.65), ylim=(0, 7.9))
    hist.set_title("Synthetic response: chosen width σ = 0.06", fontsize=12, pad=18)
    hist.legend(frameon=False, fontsize=9, loc="upper right")
    hist.spines[["top", "right"]].set_visible(False)
    hist.grid(axis="y", alpha=.2)
    fig.text(.565, .08, "No energy-to-range calibration is assumed.", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
