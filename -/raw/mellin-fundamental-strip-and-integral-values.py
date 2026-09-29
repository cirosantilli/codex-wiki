"""Plot Mellin convergence, isolated poles, and independent integral values.

Input: x**2 for 0 < x <= 1; x**(-3) for x > 1.
Quadrature uses log coordinates and truncates each end at |log x| = 60.
Run from _media; requires Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def integral_values(sigma):
    """Gauss-Legendre quadrature of each transformed half-line, not the formula."""
    nodes, weights = np.polynomial.legendre.leggauss(160)
    u = 30 * (nodes + 1)
    return np.array([30 * np.dot(weights, np.exp(-(s + 2) * u)
                                 + np.exp(-(3 - s) * u)) for s in sigma])


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "axes.titlesize": 12})
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.8), layout="constrained")
    ax = axes[0]
    ax.axvspan(-2, 3, color="#cce9dc", alpha=0.85)
    ax.axhline(0, color="#777777", lw=0.8)
    for boundary in [-2, 3]:
        ax.axvline(boundary, color="#596979", ls="--", lw=1.4)
    ax.scatter([-2, 3], [0, 0], marker="x", s=90, lw=2.2, color="#ac3030", zorder=5)
    ax.text(0.5, 1.35, "Integral converges\nabsolutely", ha="center")
    ax.text(-3.45, -1.45, "Zero endpoint\nfails", ha="center", fontsize=10)
    ax.text(4.0, -1.45, "Infinity endpoint\nfails", ha="center", fontsize=10)
    ax.text(0.5, -2.5, "×  Isolated poles of the continuation", ha="center", fontsize=10,
            color="#ac3030")
    ax.set(xlim=(-4.8, 5.4), ylim=(-3, 3), xlabel=r"$\sigma=\operatorname{Re}s$",
           ylabel=r"$\tau=\operatorname{Im}s$", title=r"Fundamental strip: $-2<\sigma<3$")
    ax.set_xticks([-4, -2, 0, 3, 5])
    ax.set_yticks([-2, 0, 2])
    ax = axes[1]
    sigma = np.linspace(-1.8, 2.8, 500)
    ax.plot(sigma, 1 / (sigma + 2) + 1 / (3 - sigma), color="#2368a0", lw=2,
            label=r"$1/(\sigma+2)+1/(3-\sigma)$")
    sample = np.linspace(-1.5, 2.5, 17)
    ax.scatter(sample, integral_values(sample), s=32, color="#c35c22", zorder=4,
               label="Independent quadrature")
    ax.set(xlim=(-2.2, 3.2), ylim=(0, 5.7), xlabel=r"Real argument $s=\sigma$",
           ylabel=r"$\mathcal{M}f(\sigma)$", title="Integral and formula agree")
    for boundary in [-2, 3]:
        ax.axvline(boundary, color="#596979", ls="--", lw=1)
    ax.legend(loc="upper center", fontsize=9.5, frameon=False)
    ax.grid(alpha=0.17)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
