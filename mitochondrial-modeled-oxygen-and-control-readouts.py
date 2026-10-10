"""Plot chosen exemplar slopes, never measured mitochondrial respiration data.

Emit the matching PNG to the current working directory.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


MINUTES = np.arange(8, dtype=float)
RATES = np.array([5, 25, 5, 25, 6, 32, 1], dtype=float)
INITIAL_OXYGEN = 220.0


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    oxygen = np.r_[INITIAL_OXYGEN, INITIAL_OXYGEN - np.cumsum(RATES * np.diff(MINUTES))]
    fig, (ax, flux) = plt.subplots(2, 1, figsize=(11.4, 7.4), dpi=100,
                                 sharex=True, gridspec_kw={"height_ratios": [1.2, 1]},
                                 facecolor="white")
    fig.subplots_adjust(left=0.1, right=0.98, top=0.78, bottom=0.15, hspace=0.15)
    fig.suptitle("MODELED oxygen traces — chosen values, not experimental data", y=0.97, fontsize=16)
    fig.text(0.5, 0.92, "Closed 2 mL suspension • initial oxygen 220 µmol/L • negligible addition volume",
             ha="center", fontsize=11)
    events = [(1, "ADP pulse"), (2, "Pulse used"), (3, "Excess ADP"),
              (4, "Oligomycin"), (5, "FCCP"), (6, "Antimycin A")]
    colors = ["#edf2f7", "#e3f0e8", "#edf2f7", "#e3f0e8", "#fff0cf", "#f9e2dc", "#eeeeee"]
    for i, color in enumerate(colors):
        ax.axvspan(i, i + 1, facecolor=color, zorder=0)
        flux.axvspan(i, i + 1, facecolor=color, zorder=0)
    for time, label in events:
        ax.axvline(time, color="#888888", lw=0.8, ls="--")
        flux.axvline(time, color="#888888", lw=0.8, ls="--")
        ax.annotate(label, xy=(time, 1.0), xycoords=("data", "axes fraction"),
                    xytext=(0, 10), textcoords="offset points", rotation=38,
                    ha="left", va="bottom", fontsize=10)
    ax.plot(MINUTES, oxygen, color="#235789", lw=3)
    ax.scatter(MINUTES, oxygen, s=20, color="#235789", zorder=3)
    ax.set(ylabel="Oxygen concentration\n(µmol/L)", ylim=(105, 235), xlim=(0, 7))
    ax.text(0.035, 0.14, "Steeper decline = faster oxygen consumption", transform=ax.transAxes,
            fontsize=11, color="#235789")
    flux.stairs(RATES, MINUTES, color="#235789", linewidth=2.7)
    for i, rate in enumerate(RATES):
        flux.text(i + 0.5, rate + 1.5, str(int(rate)), ha="center", fontsize=12, weight="bold")
    flux.set(ylabel="Consumption slope magnitude\n(µmol/L/min)", xlabel="Model time (min)", ylim=(0, 39))
    for a in (ax, flux):
        a.spines[["top", "right"]].set_visible(False)
        a.tick_params(axis="both", labelsize=10)
    fig.text(0.5, 0.065, "Oligomycin remains present after FCCP: faster respiration can coexist with inhibited ATP synthase.",
             ha="center", fontsize=11, weight="bold")
    fig.text(0.5, 0.025, "Substrates assumed supplied • simplified addition sequence • no measured ATP or oxygen values reproduced",
             ha="center", fontsize=10, color="#555555")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
