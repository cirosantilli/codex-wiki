"""Compare one-period multipliers with instantaneous and asymptotic rates.

Emit the PNG into the current directory. Tested with Python 3.14,
NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    period = 2 * np.pi
    n = np.arange(9)
    t = np.linspace(0, 2 * period, 1201)
    cases = [(-0.2, "#2476aa"), (0.0, "#25834d"), (0.2, "#bf5229")]
    fig, (left, right) = plt.subplots(1, 2, figsize=(11, 5.4), layout="constrained")
    fig.suptitle(r"$y'= (a+\cos t)y$: factor per period versus rate per unit time", fontsize=16)
    for a, color in cases:
        multiplier = np.exp(a * period)
        left.semilogy(n, multiplier ** n, "o-", color=color, lw=2, ms=5,
                      label=f"a = {a:+.1f}, m = {multiplier:.4f}")
        right.plot(t / period, a + np.cos(t), color=color, lw=2,
                   label=f"a = {a:+.1f}")
        right.axhline(a, color=color, ls="--", lw=1.6)
    left.set(title=r"Same phase every period: $y(nT)=m^n$", xlabel=r"Number of periods $n$",
             ylabel=r"Sampled value $y(nT)$ (log scale)", xlim=(-0.15, 8.15))
    left.set_xticks(n)
    left.legend(loc="upper left", framealpha=0.95, fontsize=10)
    left.text(0.04, 0.03, r"$\log y(nT)=n\log m=nTa$", transform=left.transAxes,
              bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    right.set(title="Instantaneous oscillation and long-term rate",
              xlabel=r"Time $t/T$, with $T=2\pi$", ylabel="Logarithmic growth rate",
              xlim=(0, 2), ylim=(-1.45, 1.45))
    right.set_xticks([0, 0.5, 1, 1.5, 2])
    right.legend(loc="upper right", fontsize=10)
    right.text(0.03, 0.04, "Solid: instantaneous rate  a + cos t\nDashed: long-term rate  log(m)/T = a",
               transform=right.transAxes, fontsize=10,
               bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.94})
    for ax in [left, right]:
        ax.grid(alpha=0.18)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
