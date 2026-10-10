"""Original ideal pressure calibration and invented dilute-gas models; no data.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib:
python ../temperature-thermometry-pressure-extrapolation.py
Tested: Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
The output basename is derived from this script and written to the CWD.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.5, 4.6), dpi=120)
    fig.patch.set_facecolor("white")
    for ax in (left, right):
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=.22)
    fig.suptitle("Gas thermometry: an absolute ratio, then a dilute limit", fontsize=16, weight="bold", y=.98)
    temperature = np.linspace(0, 500, 251)
    left.plot(temperature, .4 * temperature, color="#28729c", lw=2.5)
    left.scatter([300, 400], [120, 160], color=["#28729c", "#cb6c16"], zorder=4)
    left.plot([300, 300, 0], [0, 120, 120], color="#28729c", ls="--", lw=1)
    left.plot([400, 400, 0], [0, 160, 160], color="#cb6c16", ls="--", lw=1)
    left.text(235, 139, "$P_0=120$ kPa\n$T_0=300$ K", ha="right", fontsize=10)
    left.text(409, 145, "$P=160$ kPa\n$T=400$ K", fontsize=10)
    left.set(xlim=(0, 525), ylim=(0, 210), xlabel="Absolute temperature $T$ (K)", ylabel="Absolute pressure $P$ (kPa)")
    left.set_title("Ideal model: fixed $N$, fixed $V$", fontsize=12, pad=11)
    left.text(15, 187, "$P/P_0=T/T_0=4/3$", fontsize=12)
    left.text(220, 18, "Ideal-law extrapolation;\nno gas cooled to 0 K", fontsize=9, color="#555555")

    x = np.linspace(0, 1, 251)
    apparent_a = 400 * (1 + .03 * x) / (1 + .01 * x)
    apparent_b = 400 * (1 - .02 * x) / (1 + .01 * x)
    right.plot(x, apparent_a, color="#cb6c16", lw=2.5, label="Invented model A")
    right.plot(x, apparent_b, color="#28729c", lw=2.5, label="Invented model B")
    right.axhline(400, color="#444444", ls="--", lw=1)
    right.scatter([0], [400], color="#333333", zorder=5)
    right.annotate("Common intercept: 400 K", xy=(0, 400), xytext=(.12, 391),
                   arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    right.text(.69, 410, "407.92 K", color="#cb6c16", fontsize=10)
    right.text(.69, 386, "388.12 K", color="#28729c", fontsize=10)
    right.set(xlim=(-.03, 1.04), ylim=(383, 414), xlabel=r"Dimensionless fill $x=\rho_N/\rho_*$",
              ylabel="Apparent temperature $T_0P/P_0$ (K)")
    right.set_title("Same $T_0=300$ K and true $T=400$ K", fontsize=12, pad=11)
    right.legend(loc="upper left", fontsize=9, frameon=False)
    fig.text(.5, .035, "All values are stipulated toy calculations • no measured data • volume and tube corrections omitted", ha="center", fontsize=10, color="#555555")
    fig.subplots_adjust(left=.075, right=.98, bottom=.19, top=.8, wspace=.34)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
