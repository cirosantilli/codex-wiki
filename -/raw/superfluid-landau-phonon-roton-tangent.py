"""Stipulated dimensionless dispersion and Landau tangent, not helium data.

Tested with Python 3.14, numpy 2.3.5, matplotlib 3.10.7. Run from _media.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    q = np.linspace(0, 3.4, 1601)
    phonon = 2 * q
    roton = 0.6 + 2 * (q - 2) ** 2
    energy = np.minimum(phonon, roton)
    tangent_q = np.sqrt(4.3)
    critical = 4 * (tangent_q - 2)
    tangent_e = critical * tangent_q
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.7), facecolor="white")
    ax = axes[0]
    ax.plot(q, energy, color="#1976a5", lw=2.7, label=r"$e(q)=\min\{2q,\,0.6+2(q-2)^2\}$")
    ax.plot(q, critical * q, color="#b45121", lw=1.8, label="Tangent from origin")
    ax.plot([2], [0.6], "o", color="#1976a5")
    ax.plot([tangent_q], [tangent_e], "o", color="#b45121")
    ax.annotate("Roton minimum", xy=(2, 0.6), xytext=(0.8, 0.15),
                arrowprops=dict(arrowstyle="->", color="#555555"), fontsize=10)
    ax.annotate(r"$q_L=\sqrt{4.3}$", xy=(tangent_q, tangent_e), xytext=(2.25, 1.35),
                arrowprops=dict(arrowstyle="->", color="#b45121"), color="#b45121")
    ax.text(0.12, 1.25, "Phonon\nslope = 2", color="#1976a5", fontsize=10)
    ax.set(xlim=(0, 3.4), ylim=(0, 3.1), xlabel=r"Momentum $q=p/p_*$", ylabel=r"Energy $e=\epsilon/E_*$")
    ax.set_title("Lowest slope from the origin")
    ax.legend(loc="upper center", fontsize=8.5, frameon=False)
    ax = axes[1]
    positive = q > 0
    ax.plot(q[positive], energy[positive] / q[positive], color="#1976a5", lw=2.7)
    ax.axhline(critical, color="#b45121", lw=1.7, linestyle="--")
    ax.plot([tangent_q], [critical], "o", color="#b45121")
    ax.text(0.2, critical + 0.13, rf"$v_L/v_*={critical:.4f}$", color="#b45121")
    ax.text(0.2, 1.7, "Phonon-only threshold: 2", fontsize=10)
    ax.set(xlim=(0, 3.4), ylim=(0, 2.35), xlabel=r"Momentum $q=p/p_*$", ylabel=r"Ratio $e(q)/q=(\epsilon/p)/v_*$")
    ax.set_title("Minimize the ratio, not the energy")
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.18)
    fig.text(0.5, 0.025, r"Original model; $v_*=E_*/p_*$. Piecewise branches are stipulated, not a measured helium spectrum.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.985, bottom=0.19, top=0.89, wspace=0.3)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
