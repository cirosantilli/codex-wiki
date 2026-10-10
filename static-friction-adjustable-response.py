"""Plot an original static-friction feasibility model.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; output is static-friction-adjustable-response.png in CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


MASS = 2.0
GRAVITY = 9.8
MU_STATIC = 0.4
LIMIT = MU_STATIC * MASS * GRAVITY


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(9, 5.8), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.axhspan(-LIMIT, LIMIT, color="#e1eef8", label="Admissible static friction")
    for y in (-LIMIT, LIMIT):
        ax.axhline(y, color="#47728e", lw=1.4, ls=":")
    applied = np.linspace(-LIMIT, LIMIT, 300)
    ax.plot(applied, -applied, lw=3, color="#15699b", label=r"Rest requires $f_s=-F$")
    for sign in (-1, 1):
        outside = sign * np.linspace(LIMIT, 11, 120)
        ax.plot(outside, -outside, color="#b34730", ls="--", lw=2)
    for f in (2.0, 6.0):
        ax.scatter(f, -f, s=65, color="#15699b", edgecolors="white", zorder=5)
        ax.annotate(f"F = {f:g} N: rest", (f, -f), xytext=((f-2.2, -f-2.2) if f == 2 else (f+1.2, -f+2.2)),
                    arrowprops={"arrowstyle": "-", "color": "#34505f"}, fontsize=11)
    ax.scatter([10, -10], [-10, 10], marker="x", s=100, lw=2.5,
               color="#b34730", zorder=6, label="Demand exceeds bound: no rest")
    ax.scatter([LIMIT, -LIMIT], [-LIMIT, LIMIT], color="#15699b", s=45, zorder=6)
    ax.text(-10.6, -LIMIT + 0.5, r"$f_s=-7.84\,\mathrm{N}$", fontsize=11, color="#335a72")
    ax.text(3.1, LIMIT + 0.45, r"$f_s=+7.84\,\mathrm{N}$", fontsize=11, color="#335a72")
    ax.text(0.98, 0.03, "Dashed demand is not a sliding-force law.",
            transform=ax.transAxes, ha="right", fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 1})
    ax.axhline(0, color="#83929a", lw=0.7)
    ax.axvline(0, color="#83929a", lw=0.7)
    ax.set(xlim=(-11.3, 11.3), ylim=(-12, 12),
           xlabel="Applied horizontal force F (N); right is positive",
           ylabel=r"Required signed static friction $f_s$ (N)",
           title="Static friction adjusts within a bound")
    ax.set_xticks([-10, -6, -2, 0, 2, 6, 10])
    ax.set_yticks([-10, -7.84, 0, 7.84, 10])
    ax.grid(alpha=0.18)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18),
              frameon=False, fontsize=10, ncol=1)
    fig.text(0.5, 0.905, r"Stipulated model: $m=2\,\mathrm{kg}$, $g=9.8\,\mathrm{m/s^2}$, $\mu_s=0.40$; $N=19.6\,\mathrm{N}$",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.12, right=0.97, bottom=0.26, top=0.85)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
