#!/usr/bin/env python3
"""Draw a synthetic resistance experiment; output the PNG basename to CWD.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
No experimental data: r_normal(t)=0.18+0.72*t**2, with an idealized
superconducting branch r=0 for t<1 and r=r_normal for t>=1.
The +/-0.045 resolution band is a stipulated pedagogical scale.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    blue, orange, ink = "#1768a5", "#bd6313", "#233541"
    fig = plt.figure(figsize=(10.4, 5.4), dpi=110)
    fig.suptitle("Finding a superconducting resistance transition", y=0.97,
                 fontsize=17, weight="bold", color=ink)
    fig.text(0.5, 0.903, "Synthetic teaching diagram — no measured curves or material-specific scales",
             ha="center", fontsize=11, color="#555555")
    gs = fig.add_gridspec(1, 2, left=0.04, right=0.98, bottom=0.18,
                         top=0.80, width_ratios=[1, 1.12], wspace=0.23)
    circuit = fig.add_subplot(gs[0, 0])
    circuit.set(xlim=(0, 10), ylim=(0, 8))
    circuit.axis("off")
    circuit.set_title("A. Four separate contacts", loc="left", fontsize=12,
                      weight="bold", pad=12)
    circuit.add_patch(Rectangle((1.4, 2.4), 7.2, 1.25, facecolor="#e5eff6",
                                edgecolor=blue, linewidth=1.8))
    circuit.add_patch(Rectangle((2.8, 2.4), 4.4, 1.25, facecolor="#d2e5f3",
                                edgecolor="none"))
    circuit.text(5, 2.85, "sensed sample interval", ha="center", va="center", color=ink)
    for x, tag in [(1.8, "I+"), (3.2, "V+"), (6.8, "V−"), (8.2, "I−")]:
        circuit.plot(x, 3.65, "o", color=ink, markersize=5)
        circuit.text(x, 3.9, tag, ha="center", fontsize=11, color=ink)
    # Independent sense pair; its instrument draws negligible current.
    circuit.plot([3.2, 3.2, 4.45], [3.65, 6.1, 6.1], color=orange, lw=2)
    circuit.plot([6.8, 6.8, 5.55], [3.65, 6.1, 6.1], color=orange, lw=2)
    circuit.add_patch(Circle((5, 6.1), 0.55, facecolor="white", edgecolor=orange, lw=2))
    circuit.text(5, 6.1, "V", ha="center", va="center", color=orange, fontsize=13)
    circuit.text(5, 7.25, "Sense voltage; negligible current", ha="center", fontsize=10)
    # Closed current circuit through the sample, separate from sense wiring.
    circuit.plot([1.8, 0.8, 0.8, 4.45], [3.65, 3.65, 0.8, 0.8], color=blue, lw=2)
    circuit.plot([8.2, 9.2, 9.2, 5.55], [3.65, 3.65, 0.8, 0.8], color=blue, lw=2)
    circuit.add_patch(Circle((5, 0.8), 0.55, facecolor="white", edgecolor=blue, lw=2))
    circuit.add_patch(FancyArrowPatch((5.35, 0.8), (4.65, 0.8), arrowstyle="->",
                                     mutation_scale=12, color=blue, lw=1.6))
    circuit.text(5, -0.1, "Small reversible current source", ha="center", fontsize=10)
    circuit.text(5, 1.8, "Thermometer close to sample", ha="center", fontsize=10, color="#555555")
    plot = fig.add_subplot(gs[0, 1])
    t = np.linspace(0.2, 1.4, 601)
    normal = 0.18 + 0.72 * t**2
    plot.axhspan(-0.045, 0.045, color="#dddddd", label="illustrative resolution band")
    plot.plot(t, normal, color=orange, lw=2.4, linestyle="--",
              label="normal-state continuation (toy)")
    below = np.linspace(0.2, 1, 201)
    above = np.linspace(1, 1.4, 201)
    plot.plot(below, np.zeros_like(below), color=blue, lw=3,
              label="ideal superconducting sample")
    plot.plot(above, 0.18 + 0.72 * above**2, color=blue, lw=3)
    plot.plot([1, 1], [0, 0.9], color=blue, lw=1.7, linestyle=":")
    plot.axvline(1, color="#888888", lw=1, linestyle="--", zorder=0)
    plot.text(1.015, 1.0, "$T_c$", color=ink, fontsize=12)
    plot.annotate("cooling", xy=(0.88, 1.72), xytext=(1.15, 1.72),
                  arrowprops={"arrowstyle": "->", "color": ink}, va="center",
                  color=ink, fontsize=10)
    plot.set(xlim=(0.2, 1.4), ylim=(-0.08, 1.83),
             xlabel="Temperature $T/T_c$", ylabel="Resistance $R/R_*$")
    plot.set_title("B. An abrupt idealized transition", loc="left", fontsize=12,
                   weight="bold", pad=12)
    plot.set_xticks([0.2, 0.6, 1.0, 1.4])
    plot.set_yticks([0, 0.5, 1, 1.5])
    plot.grid(alpha=0.18)
    plot.legend(loc="upper left", fontsize=8.5, frameon=False)
    fig.text(0.5, 0.07, "A zero reading gives a bound: unresolved resistance is at most about δV / |I|.",
             ha="center", fontsize=11, color=ink)
    fig.savefig(Path("superconductivity-resistance-experiment.png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
