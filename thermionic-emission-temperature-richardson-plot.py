"""Chosen Richardson-Dushman model; never experimental measurements.

Python 3.14; numpy 2.3.5, matplotlib 3.10.7. Run from _media.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    kb_ev = 8.617333262e-5
    barrier_ev = 2.0
    coefficient = 120.0  # A cm^-2 K^-2, deliberately chosen model.
    reference = 120.0
    temperature = np.linspace(900, 1500, 401)
    current = coefficient * temperature**2 * np.exp(-barrier_ev / (kb_ev * temperature))
    selected = np.array([1000.0, 1200.0, 1400.0])
    selected_current = coefficient * selected**2 * np.exp(-barrier_ev / (kb_ev * selected))
    y = np.log(current / (reference * temperature**2))
    y_selected = np.log(selected_current / (reference * selected**2))
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.9), dpi=120, facecolor="white")
    blue, orange = "#165e99", "#d35416"
    left, right = axes
    left.semilogy(temperature, current, color=blue, lw=2.3)
    left.scatter(selected, selected_current, color=orange, zorder=3, s=35)
    left.set(xlabel=r"Temperature $T$ (K)", ylabel=r"Emitted $J$ (A cm$^{-2}$)",
             title="Rapid growth with temperature", xlim=(880, 1520))
    right.plot(1000 / temperature, y, color=blue, lw=2.3)
    right.scatter(1000 / selected, y_selected, color=orange, zorder=3, s=35)
    right.set(xlabel=r"Inverse temperature $1000\,\mathrm{K}/T$",
              ylabel=r"$\ln[J/(A_{\mathrm{ref}}T^2)]$",
              title="The same model becomes a straight line")
    for t, j, r in zip(selected, selected_current, y_selected):
        left.annotate(f"{t:.0f} K", (t, j), xytext=(6, 8), textcoords="offset points",
                      fontsize=10)
        right.annotate(f"{t:.0f} K", (1000 / t, r), xytext=(7, 7),
                       textcoords="offset points", fontsize=10)
    right.text(.97, .09, "Slope = −23.209\nW = 2.0 eV", transform=right.transAxes,
               ha="right", fontsize=11,
               bbox={"facecolor": "white", "edgecolor": "#ccd4dc", "pad": 6})
    for ax in axes:
        ax.grid(True, which="major", color="#dce2e8", lw=.7)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Chosen model: W = 2.0 eV, A = Aref = 120 A cm⁻² K⁻²", fontsize=14, y=.98)
    fig.text(.5, .035, "Curves and marked values are calculated; no particular material is represented.",
             ha="center", fontsize=11, color="#4d5966")
    fig.subplots_adjust(left=.09, right=.97, bottom=.20, top=.83, wspace=.32)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
