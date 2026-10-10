"""Ideal binary Gibbs energy and the two chemical-potential intercepts.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The curve and tangent are original ideal-model calculations.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    x = np.linspace(0.0001, 0.9999, 800)
    f = x * np.log(x) + (1 - x) * np.log1p(-x)
    x0 = 0.30
    f0 = x0 * np.log(x0) + (1 - x0) * np.log1p(-x0)
    slope = np.log(x0 / (1 - x0))
    intercept_b, intercept_a = np.log1p(-x0), np.log(x0)
    fig, ax = plt.subplots(figsize=(9.2, 5), dpi=110)
    fig.subplots_adjust(left=0.10, right=0.96, bottom=0.20, top=0.79)
    fig.suptitle("One ideal mixing curve determines both chemical potentials", y=0.965, fontsize=15)
    fig.text(0.5, 0.865, r"$f(x)=x\ln x+(1-x)\ln(1-x)$ at fixed $T,p$", ha="center")
    ax.plot(x, f, lw=2.8, color="#2368a2", label="Ideal mixing Gibbs energy / RT")
    ax.plot([0, 1], [intercept_b, intercept_a], lw=2, color="#bd5b19", label=r"Tangent at $x=0.30$")
    ax.scatter([x0], [f0], s=55, color="#bd5b19", zorder=5)
    ax.scatter([0, 1], [intercept_b, intercept_a], s=60, color="#bd5b19", zorder=5, clip_on=False)
    ax.axvline(x0, color="0.6", lw=1, ls=":")
    ax.axhline(0, color="0.6", lw=0.8)
    ax.annotate(r"B: $\ln(0.70)\approx-0.357$", xy=(0, intercept_b), xytext=(0.045, -0.16),
                arrowprops={"arrowstyle": "->", "color": "0.35"}, fontsize=11)
    ax.annotate(r"A: $\ln(0.30)\approx-1.204$", xy=(1, intercept_a), xytext=(0.53, -1.33),
                arrowprops={"arrowstyle": "->", "color": "0.35"}, fontsize=11)
    ax.set(xlim=(0, 1), ylim=(-1.45, 0.10), xlabel=r"Mole fraction $x=x_A$",
           ylabel="Dimensionless reference-subtracted energy")
    ax.grid(alpha=0.15)
    ax.legend(loc="lower left", frameon=False, fontsize=10)
    fig.text(0.5, 0.055,
             r"B intercept: $f-xf'=\ln(1-x)$     |     A intercept: $f+(1-x)f'=\ln x$",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
