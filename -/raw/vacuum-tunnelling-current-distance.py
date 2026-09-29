"""Illustrative vacuum junction and current-distance law; no experimental data.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLBACKEND=Agg; writes matching basename to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    # SI constants; phi is an effective energy above the tunnelling electrons.
    electron_mass, hbar, ev = 9.1093837139e-31, 1.054571817e-34, 1.602176634e-19
    phi_ev, reference_nm, reference_na = 4.0, 0.4, 1.0
    decay = np.sqrt(2*electron_mass*phi_ev*ev)/hbar
    gap_nm = np.linspace(0.3, 0.8, 500)
    current_na = reference_na*np.exp(-2*decay*(gap_nm-reference_nm)*1e-9)
    slope = np.polyfit(gap_nm, np.log(current_na), 1)[0]
    assert abs(slope/(-2*decay*1e-9)-1) < 1e-12
    ratio_angstrom = np.exp(-2*decay*1e-10)
    assert 0.128 < ratio_angstrom < 0.130
    fig, (apparatus, curve) = plt.subplots(1, 2, figsize=(10.4, 5.4),
                                         layout="constrained", facecolor="white")
    blue, orange = "#1764a1", "#bc531d"
    apparatus.set(xlim=(0, 10), ylim=(0, 10))
    apparatus.axis("off")
    apparatus.add_patch(Rectangle((0.5, 4), 9, 5.6, fill=False, ec="#707b85", lw=1.4, ls="--"))
    apparatus.text(0.8, 9.2, "Vacuum chamber / vibration isolation", fontsize=11)
    apparatus.add_patch(Rectangle((4.1, 7.6), 1.8, 0.9, fc="#d7e6ef", ec=blue))
    apparatus.text(5, 8.05, "Piezo drive", ha="center", va="center", fontsize=10)
    apparatus.add_patch(Polygon([(4.4, 7.6), (5.6, 7.6), (5, 6)], fc="#a3b7c7", ec=blue))
    apparatus.text(6.1, 7.05, "Conducting tip", fontsize=11)
    apparatus.add_patch(Rectangle((2, 4.65), 6.0, 0.5, fc="#a3b7c7", ec=blue))
    apparatus.text(3.0, 4.85, "Conducting sample", fontsize=10)
    apparatus.annotate("gap s", (6.5, 5.65), ha="left", color=orange, fontsize=11)
    apparatus.annotate("", (6.25, 6), (6.25, 5.15),
                       arrowprops={"arrowstyle": "<->", "color": orange, "lw": 1.6})
    apparatus.add_patch(FancyArrowPatch((5, 5.95), (5, 5.2), arrowstyle="-|>",
                                      color=orange, lw=2, mutation_scale=16))
    apparatus.text(3.5, 5.65, "tunnelling", color=orange, ha="center", fontsize=10)
    apparatus.plot([4.4, 1.1, 1.1, 2.3], [7.3, 7.3, 3.55, 3.55], color=blue, lw=1.5)
    apparatus.text(0.65, 6.1, "Bias\nV", color=blue, fontsize=11,
                   bbox={"facecolor": "white", "edgecolor": blue, "boxstyle": "round,pad=0.25"})
    apparatus.plot([7, 7, 5.5], [4.65, 3.55, 3.55], color=blue, lw=1.5)
    apparatus.add_patch(Rectangle((2.3, 3), 3.2, 1.1, fc="white", ec=blue, lw=1.4))
    apparatus.text(3.9, 3.55, "Current readout I", ha="center", va="center", fontsize=11)
    apparatus.text(5, 1.9, "Distance sweep: vary s at fixed V\nImaging: feedback varies s to hold I fixed", ha="center", fontsize=11)
    apparatus.text(5, 0.7, "Schematic only; dimensions are not to scale", ha="center", fontsize=10, color="#555555")
    apparatus.set_title("What is controlled and what is read", fontsize=13)
    curve.semilogy(gap_nm, current_na, color=blue, lw=2.4)
    s1, s2 = reference_nm, reference_nm+0.1
    i1, i2 = reference_na, reference_na*ratio_angstrom
    curve.plot([s1, s2], [i1, i1], color=orange, ls="--", lw=1.4)
    curve.plot([s2, s2], [i1, i2], color=orange, ls="--", lw=1.4)
    curve.scatter([s1, s2], [i1, i2], color=orange, zorder=4)
    curve.text(0.515, 0.37, f"+0.1 nm = +1 Å\nI multiplied by {ratio_angstrom:.3f}", fontsize=11, color=orange)
    curve.text(0.96, 0.93, r"$I(s)=I(s_0)e^{-2\kappa(s-s_0)}$"+"\n"+
               r"$\Phi=4$ eV, $s_0=0.4$ nm"+"\n"+r"$I(s_0)=1$ nA (chosen)",
               transform=curve.transAxes, ha="right", va="top", fontsize=11,
               bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    curve.set(xlim=(0.3, 0.8), ylim=(1e-4, 15), xlabel="Gap s (nm)", ylabel="Current magnitude I (nA)",
              title="Straight line on a logarithmic current axis")
    curve.grid(which="both", alpha=0.16)
    fig.suptitle("Vacuum tunnelling current versus distance — illustrative model, not measurements", fontsize=14)
    fig.savefig(Path.cwd()/(Path(__file__).stem+".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
