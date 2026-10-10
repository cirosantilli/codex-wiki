"""Functional attosecond generation and timing diagram; no experimental data.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    blue, red, purple, ink = "#156a9a", "#b84435", "#7850a1", "#223347"
    fig = plt.figure(figsize=(11.2, 7.2), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=[1.1, 1])
    flow = fig.add_subplot(grid[0, :])
    flow.set(xlim=(0, 12), ylim=(0, 4.2))
    flow.axis("off")
    flow.set_title("Generate a short burst; measure an electron response", loc="left", weight="bold")

    def box(x, y, w, h, label, color):
        flow.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.07",
                                     facecolor="white", edgecolor=color, linewidth=1.6))
        flow.text(x + w / 2, y + h / 2, label, ha="center", va="center", color=ink)

    def arrow(start, end, color, bend=0):
        flow.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=14,
                                      linewidth=1.7, color=color,
                                      connectionstyle=f"arc3,rad={bend}"))

    box(.15, 2.55, 1.55, .9, "Short-pulse\nlaser", red)
    box(2.65, 2.55, 1.7, .9, "Generation\ngas", blue)
    box(5.25, 2.55, 1.85, .9, "Spectral selection\nand refocusing", blue)
    box(8.05, 2.55, 1.55, .9, "Analyser\ngas", purple)
    box(10.35, 2.55, 1.45, .9, "Electron\nspectrometer", purple)
    box(3.1, .65, 2.4, .85, "Reference field\nadjustable delay  τ", red)
    arrow((1.77, 3), (2.56, 3), red)
    arrow((4.42, 3), (5.16, 3), blue)
    arrow((7.17, 3), (7.96, 3), blue)
    arrow((9.67, 3), (10.27, 3), purple)
    arrow((1.25, 2.46), (3, 1.08), red, .15)
    arrow((5.59, 1.08), (8.8, 2.46), red, .15)
    flow.text(4.82, 3.65, "High harmonics", ha="center", color=blue)
    flow.text(7.56, 3.65, "XUV", ha="center", color=blue)
    flow.text(10, 3.65, "e⁻", ha="center", color=purple)
    flow.text(8.3, .72, "Vary delay → record electron energy distribution",
              ha="center", color=ink, fontsize=10)
    flow.text(.2, .12, "Functional layout only: generation gas and analyser gas have different jobs.",
              color="#4c5a65", fontsize=10)

    left = fig.add_subplot(grid[1, 0])
    delay = np.linspace(-1.5, 1.5, 1400)
    omega = 2 * np.pi / (800 / 299.792458)
    phase = .8
    signal = 1 + .7 * np.cos(2 * omega * delay - phase)
    left.plot(delay, signal, color=blue, linewidth=2)
    left.set(xlabel="Reference delay τ (fs)", ylabel="Sideband signal (arbitrary units)",
             title="Weak reference: two paths interfere", ylim=(0, 2.15))
    left.text(.03, .94, r"$S(\tau)=1+0.7\cos(2\omega\tau-0.8)$",
              transform=left.transAxes, va="top", fontsize=11)
    left.text(.03, .80, "Chosen phase; target phase set to zero",
              transform=left.transAxes, va="top", fontsize=9)

    right = fig.add_subplot(grid[1, 1])
    vector_potential = .1 * np.sin(omega * delay)
    energy = (2 - vector_potential)**2 / 2
    right.plot(delay, energy, color=purple, linewidth=2)
    right.axhline(2, color="#83929d", linestyle=":", linewidth=1)
    right.set(xlabel="Emission time relative to reference (fs)",
              ylabel="Final kinetic energy (atomic units)", ylim=(1.73, 2.37),
              title="Classical streaking limit: a momentum kick")
    right.text(.03, .94, r"$K_f=[2-0.1\sin(\omega t_i)]^2/2$",
               transform=right.transAxes, va="top", fontsize=11)
    right.text(.03, .80, "Sharp initial momentum; ionic force neglected",
               transform=right.transAxes, va="top", fontsize=9)
    for ax in [left, right]:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=.16)
        ax.title.set_fontsize(11)
    fig.supxlabel("Idealized calculations, not measured traces. XUV = extreme ultraviolet.", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
