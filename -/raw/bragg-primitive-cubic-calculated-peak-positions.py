"""Original position strips; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Primitive cubic point lattice with one identical scatterer per primitive cell.
Run from _media; no intensity model is specified or plotted.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def peak_positions(a_nm=.400, wavelength_nm=.154):
    hkl = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1], [2, 0, 0]])
    s = np.sum(hkl**2, axis=1)
    d_nm = a_nm / np.sqrt(s)
    argument = wavelength_nm / (2 * d_nm)
    if np.any(argument > 1):
        raise ValueError("A requested reflection has no real Bragg angle")
    return hkl, s, d_nm, 2 * np.degrees(np.arcsin(argument))


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    hkl, s, d_nm, angles = peak_positions()
    fig, ax = plt.subplots(figsize=(10, 5.9), facecolor="white")
    fig.subplots_adjust(left=.23, right=.96, top=.73, bottom=.22)
    colors = ["#2166ac", "#27877a", "#925aa5", "#c45b10"]
    for i, (indices, ss, dd, angle, color) in enumerate(zip(hkl, s, d_nm, angles, colors)):
        row = 3 - i
        ax.hlines(row, 0, 55, color="#e0e4ea", lw=1.4)
        ax.vlines(angle, row - .28, row + .28, color=color, lw=3)
        ax.plot(angle, row, "o", color=color, ms=6)
        ax.text(angle + 1, row + .15, f"{angle:.3f}°", color=color, fontsize=13)
    ax.set_yticks([3, 2, 1, 0],
                 [f"({''.join(map(str, indices))})    S = {ss}\nd = {dd:.5f} nm"
                  for indices, ss, dd in zip(hkl, s, d_nm)])
    ax.set(xlim=(0, 55), ylim=(-.65, 3.65), xlabel=r"Scattering deflection $2\theta$ (degrees)")
    ax.set_xticks(np.arange(0, 56, 5))
    ax.grid(axis="x", color="#eef0f4", lw=.7)
    ax.tick_params(axis="y", length=0, pad=12)
    for side in ("left", "right", "top"):
        ax.spines[side].set_visible(False)
    fig.text(.5, .94, "Calculated Bragg positions: primitive cubic point lattice",
             ha="center", fontsize=16, weight="bold")
    fig.text(.5, .865, r"$a=0.400$ nm,  $\lambda=0.154$ nm; one identical point scatterer per cell",
             ha="center", fontsize=12)
    fig.text(.5, .795, r"$S=h^2+k^2+l^2,\quad d_{hkl}=a/\sqrt{S},\quad 2\theta=2\arcsin(\lambda\sqrt{S}/2a)$",
             ha="center", fontsize=14)
    fig.text(.5, .08, "Each strip marks an angle only. Row positions and marker lengths encode no intensity.",
             ha="center", fontsize=12)
    fig.text(.5, .035, "Chosen ideal model, not measured data. Other reflections beyond these four are not shown.",
             ha="center", fontsize=11, color="#596574")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
