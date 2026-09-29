"""Original illustrative RL curves, log slopes and a finite-observation bound.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes this script's basename with a .png suffix to CWD.
No plotted quantity is a historical measurement.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})
    inductance = 1e-6
    hours = np.linspace(0, 24, 481)
    resistances = (0, 1e-13, 1e-11)
    colors = ("#23806c", "#185b97", "#bb472a")
    fig, axes = plt.subplots(1, 3, figsize=(11, 4.4), facecolor="white")
    for resistance, color in zip(resistances, colors):
        log_ratio = -resistance * (hours * 3600) / inductance
        ratio = np.exp(log_ratio)
        label = "$R=0$" if resistance == 0 else rf"$R=10^{{{int(np.log10(resistance))}}}\,\Omega$"
        axes[0].plot(hours, ratio, color=color, label=label, lw=2)
        axes[1].plot(hours, log_ratio, color=color, lw=2)
    axes[0].set(xlabel="Elapsed time (hours)", ylabel="$I(t)/I_0$",
                ylim=(.38, 1.025), title="A  Chosen decay models")
    axes[0].legend(loc="lower left", fontsize=9)
    axes[1].set(xlabel="Elapsed time (hours)", ylabel=r"$\ln[I(t)/I_0]$",
                title="B  Logarithmic slope")
    axes[1].text(.05, .07, r"$d\ln I/dt=-R/L$" + "\nConstant $L$, constant $R$, no drive",
                 transform=axes[1].transAxes, fontsize=9)
    epsilon = .001
    duration_hours = np.linspace(1, 24, 300)
    resistance_bound = -inductance * np.log1p(-epsilon) / (duration_hours * 3600)
    axes[2].plot(duration_hours, resistance_bound, color="#654b96", lw=2)
    chosen_bound = -inductance * np.log1p(-epsilon) / (3 * 3600)
    axes[2].plot(3, chosen_bound, "o", color="#654b96")
    axes[2].annotate("3 h: $R\\leq9.26\\times10^{-14}\\,\\Omega$", xy=(3, chosen_bound),
                     xytext=(5, 1.6e-13), fontsize=9,
                     arrowprops={"arrowstyle": "-", "color": "#654b96"})
    axes[2].set(xlabel="Observation window (hours)", ylabel="Resistance upper bound (ohms)",
                yscale="log", ylim=(9e-15, 3.1e-13), title="C  Unresolved loss ≤ 0.1%")
    for ax in axes:
        ax.set_xlim(0, 24)
        ax.set_xticks((0, 6, 12, 18, 24))
        ax.grid(alpha=.22)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Illustrative closed loop: $L=1\\,\\mu\\mathrm{H}$; no historical data", fontsize=13)
    fig.text(.5, .025, "A bound requires a calibrated current ratio including field-background, gain and geometry drift.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.065, right=.985, bottom=.19, top=.79, wspace=.36)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
