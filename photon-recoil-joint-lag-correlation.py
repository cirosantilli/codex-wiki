"""Chosen analytic lag model and separate exact Bernoulli comparison.

No historical data. Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media; output basename.png to the current directory.
"""
from pathlib import Path
from math import erf, sqrt

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, (ax, joint) = plt.subplots(1, 2, figsize=(11, 5.5),
                                   gridspec_kw={"width_ratios": [1.3, 1]})
    fig.patch.set_facecolor("white")
    fig.suptitle("Pairing adds information that the two singles totals cannot supply", fontsize=14)
    lag = np.linspace(-8, 8, 1601)  # milliseconds
    baseline = np.ones_like(lag)  # T r_e r_gamma / 1000 per ms
    density = baseline + 100/np.sqrt(2*np.pi)*np.exp(-lag**2/2)
    ax.plot(lag, density, color="#2574a9", lw=2, label="Correlated-pair expectation")
    ax.plot(lag, baseline, color="#b55220", ls="--", lw=2, label="Independent-pair baseline")
    ax.fill_between(lag, 0, density, where=np.abs(lag) <= 1, color="#2574a9", alpha=.2)
    ax.axvspan(4, 6, color="#b55220", alpha=.13)
    ax.annotate("", xy=(1, 33), xytext=(-1, 33), arrowprops=dict(arrowstyle="<->"))
    ax.text(0, 29, "Full width w = 2 ms", ha="center", fontsize=10)
    center = 2 + 100*erf(1/sqrt(2))
    delayed = 2 + 50*(erf(6/sqrt(2))-erf(4/sqrt(2)))
    ax.text(-7.7, 38, f"Central window: {center:.2f}\nDelayed window: {delayed:.3f}", fontsize=10)
    ax.text(5, 6, "Delayed\nwindow", ha="center", fontsize=10, color="#85421c")
    ax.set(xlabel=r"Lag $\ell=t_\gamma-t_e$ (ms)", ylabel="Expected pairs per ms", xlim=(-8, 8), ylim=(0, 46))
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    ax.grid(alpha=.15)
    joint.axis("off")
    joint.set(xlim=(0, 1), ylim=(0, 1))
    joint.text(.5, .95, "Separate ideal bin model (no timing spread)", ha="center", fontsize=11)
    joint.text(.5, .86, "1,000,000 bins; each bin is 1 ms", ha="center", fontsize=10)
    rows = [["Electron singles", "2,000", "2,000"],
            ["Photon singles", "500", "500"],
            ["Both in same bin", "1", "101"]]
    table = joint.table(cellText=rows, colLabels=["Expected counts", "Independent", "Correlated"],
                        cellLoc="center", colWidths=[.48, .26, .26], bbox=[0, .35, 1, .42])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#bbbbbb")
        if row == 0:
            cell.set_facecolor("#eef5fa")
        if row == 3:
            cell.set_facecolor("#fff0dc")
    joint.text(.5, .25, "Same marginals, different joint probability", ha="center", fontsize=11)
    joint.text(.5, .13, "All numbers are chosen model expectations.\nNeither panel reproduces historical counts.", ha="center", fontsize=10)
    fig.text(.5, .025, r"Lag model: $T=1000$ s, $r_e=2$ s$^{-1}$, $r_\gamma=0.5$ s$^{-1}$, $S=0.1$ s$^{-1}$, $\sigma=1$ ms", ha="center", fontsize=11)
    fig.subplots_adjust(left=.075, right=.985, bottom=.15, top=.87, wspace=.26)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
