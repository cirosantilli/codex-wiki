#!/usr/bin/env python3
"""Plot analytic field-history idealizations; output PNG basename to CWD.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Planar stationary half-space, tangential surface field Bs=B0, no flux tubes.
Perfect conduction freezes B at its initial value (B0 or zero).
Equilibrium local London theory gives B/B0=exp(-z/lambda_L) in both histories.
No measured data, realistic transition kinetics, or fitted material parameters.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    ink, blue, orange = "#233541", "#1768a5", "#bd6313"
    fig = plt.figure(figsize=(10.4, 6.8), dpi=110)
    fig.suptitle("Zero resistance and magnetic expulsion are different tests", y=0.97,
                 fontsize=16, weight="bold", color=ink)
    fig.text(0.5, 0.916, "Analytic idealizations — not measured profiles; same final applied field $B_0$",
             ha="center", fontsize=11, color="#555555")
    gs = fig.add_gridspec(2, 2, left=0.24, right=0.97, bottom=0.21,
                         top=0.79, wspace=0.27, hspace=0.55)
    u = np.linspace(0, 6, 601)
    for row in range(2):
        for col in range(2):
            ax = fig.add_subplot(gs[row, col])
            ax.axhline(1, color="#aaaaaa", linestyle=":", linewidth=1)
            ax.set(xlim=(0, 6), ylim=(-0.07, 1.16))
            ax.set_xticks([0, 2, 4, 6])
            ax.set_yticks([0, 0.5, 1])
            ax.set_ylabel("Interior $B(z)/B_0$", fontsize=10)
            ax.grid(alpha=0.15)
            if row == 0:
                title = "Perfect conductor" if col == 0 else "Equilibrium Meissner screening"
                ax.set_title(title, fontsize=12, weight="bold", pad=15)
            if row == 1:
                ax.set_xlabel(r"Depth $z/\lambda_L$", fontsize=11)
            if col == 0:
                initial = 1 if row == 0 else 0
                ax.plot(u, np.full_like(u, initial), color=orange, lw=3)
                label = "Pre-existing field stays" if row == 0 else "New field is excluded"
                ax.text(0.42, 0.55, label, fontsize=10, color=orange,
                        transform=ax.transAxes, ha="center")
            else:
                ax.plot(u, np.exp(-u), color=blue, lw=3)
                ax.text(2.2, 0.64, r"$B/B_0=e^{-z/\lambda_L}$", fontsize=12, color=blue)
                ax.text(2.2, 0.39, "Same equilibrium profile", fontsize=9.8, color=blue)
    fig.text(0.025, 0.724, "FIELD COOLED", fontsize=12, weight="bold", color=ink)
    fig.text(0.025, 0.662, "Start normal with $B_0$.\nCool in that fixed field.\nInitial interior $B=B_0$.",
             fontsize=10.5, color=ink, va="top", linespacing=1.7)
    fig.text(0.025, 0.403, "ZERO-FIELD COOLED", fontsize=11, weight="bold", color=ink)
    fig.text(0.025, 0.341, "Cool with no field.\nThen apply $B_0$.\nInitial interior $B=0$.",
             fontsize=10.5, color=ink, va="top", linespacing=1.7)
    fig.text(0.5, 0.067, "Stationary half-space $z>0$; magnetic field parallel to the planar surface.",
             fontsize=10.5, ha="center", color=ink)
    fig.text(0.5, 0.03, r"$\lambda_L$ is a screening depth only for superconductivity; it sets a shared horizontal scale here.",
             fontsize=9.8, ha="center", color="#555555")
    fig.savefig(Path("superconductivity-field-history.png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
