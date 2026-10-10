"""Compare exact Euclidean massive-vector propagator eigenvalues.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; writes massive-vector-propagator-scaling.png to CWD.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    q = np.geomspace(0.05, 1000.0, 800)
    fig, ax = plt.subplots(figsize=(9.0, 5.5), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.12, right=0.97, bottom=0.24, top=0.86)
    ax.set_facecolor("white")
    ax.loglog(q, np.ones_like(q), color="#b04b27", lw=2.6,
              label=r"Unitary gauge: longitudinal $m^2D_L=1$")
    ax.loglog(q, 1/(q*q+1), color="#1665a0", lw=2.6,
              label=r"$R_\xi$, $\xi=1$: $m^2D_L=1/(q^2+1)$")
    ax.loglog(q, 10/(q*q+10), color="#25804c", lw=2.6,
              label=r"$R_\xi$, $\xi=10$: $m^2D_L=10/(q^2+10)$")
    ax.loglog(q[q>5], 10/q[q>5]**2, "--", color="#666666", lw=1.2,
              label=r"Large-$q$ guide: $10/q^2$")
    ax.set(xlabel=r"Euclidean momentum $q=|k_E|/m$",
           ylabel=r"Dimensionless propagator eigenvalue $m^2D_L$",
           xlim=(0.05, 1000), ylim=(5e-7, 2.0))
    ax.grid(which="major", alpha=0.22)
    ax.legend(loc="lower left", fontsize=10, framealpha=1)
    fig.suptitle("A gauge choice changes the visible large-momentum behavior", fontsize=14, y=0.97)
    fig.text(0.12, 0.095,
             r"All gauges: $m^2D_T=1/(q^2+1)$.  At fixed finite $\xi>0$, $D_L\sim\xi/k_E^2$.",
             fontsize=11)
    fig.text(0.12, 0.045,
             "These are off-shell eigenvalues, not scattering probabilities or measured spectra.",
             fontsize=10, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
