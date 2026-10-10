"""Illustrate one-loop SU(3) running; chosen calibrations, no fitted data.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; writes qcd-fixed-flavor-running-coupling.png to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    q = np.geomspace(10.0, 150.0, 450)
    q0, alpha0 = 20.0, 0.16
    fig, ax = plt.subplots(figsize=(8.2, 4.8), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    for nf, color in [(0, "#913c8b"), (3, "#c86616"), (5, "#126b98")]:
        beta0 = 11.0 - 2.0 * nf / 3.0
        alpha = 1.0 / (1.0 / alpha0 + beta0 / (2.0 * np.pi) * np.log(q / q0))
        ax.plot(q, alpha, lw=2.5, color=color, label=rf"$n_f={nf}$, $\beta_0={beta0:.3g}$")
    ax.scatter([q0], [alpha0], c="black", s=35, zorder=4)
    ax.annotate("Chosen common calibration\n" + r"$\alpha_s(20\,\mathrm{GeV})=0.16$",
                xy=(q0, alpha0), xytext=(35, 0.184), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#444444"})
    ax.set_xscale("log")
    ax.set_xticks([10, 20, 50, 100, 150], ["10", "20", "50", "100", "150"])
    ax.set(xlim=(10, 150), ylim=(0.095, 0.205), xlabel=r"Scale $Q$ (GeV), with $\mu=Q$",
           ylabel=r"Dimensionless coupling $\alpha_s(Q)$",
           title="Asymptotic freedom: the coupling falls at higher energy")
    ax.grid(alpha=0.2)
    ax.legend(loc="lower left", framealpha=1, fontsize=11)
    fig.text(0.5, 0.025, "Separate fixed-flavor theories; mass thresholds omitted. Original toy curves, not data.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
