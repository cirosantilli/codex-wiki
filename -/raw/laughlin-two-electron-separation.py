"""Original normalized two-electron Laughlin relative-coordinate example.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
Writes laughlin-two-electron-separation.png to the CWD.
This is not a thermodynamic pair distribution or experimental data.
"""

from math import factorial, pi, sqrt
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def area_density(u, m):
    return u ** (2 * m) * np.exp(-u * u / 4) / (pi * 4 ** (m + 1) * factorial(m))


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    u = np.linspace(0, 9, 1801)
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.4), facecolor="white")
    fig.subplots_adjust(left=0.085, right=0.97, bottom=0.23, top=0.78, wspace=0.30)
    fig.suptitle("Two electrons: pair avoidance and the radial Jacobian", fontsize=16, y=0.97)
    fig.text(0.5, 0.87, r"$\Psi_m\propto(z_1-z_2)^m\exp[-(|z_1|^2+|z_2|^2)/(4\ell_B^2)]$    ·    odd $m$: exchange sign $-1$",
             ha="center", fontsize=12)
    colors = {1: "#176b92", 3: "#bd4a20"}
    for m in (1, 3):
        density = area_density(u, m)
        radial = 2 * pi * u * density
        axes[0].plot(u, density, color=colors[m], lw=2.5, label=fr"$m={m}$")
        axes[1].plot(u, radial, color=colors[m], lw=2.5, label=fr"$m={m}$")
        for ax, peak, label in [(axes[0], 2 * sqrt(m), "$2$" if m == 1 else fr"$2\sqrt{{{m}}}$"),
                                (axes[1], sqrt(4 * m + 2), fr"$\sqrt{{{4*m+2}}}$")]:
            y = float(area_density(peak, m))
            if ax is axes[1]:
                y *= 2 * pi * peak
            ax.plot(peak, y, "o", color=colors[m], ms=6)
            ax.annotate(label, (peak, y), xytext=(4, 10), textcoords="offset points", color=colors[m], fontsize=11)
    axes[0].set_title("Density per unit area", fontsize=13, pad=12)
    axes[1].set_title("Density of separation", fontsize=13, pad=12)
    axes[0].set_ylabel(r"$D_m(u)$")
    axes[1].set_ylabel(r"$p_m(u)=2\pi uD_m(u)$")
    axes[0].set_ylim(0, 0.038)
    axes[1].set_ylim(0, 0.49)
    for ax in axes:
        ax.set_xlim(0, 9)
        ax.set_xlabel(r"separation $u=|z_1-z_2|/\ell_B$")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.18)
        ax.legend(frameon=False, loc="upper right")
    fig.text(0.5, 0.09, r"Normalization: $\int_0^\infty 2\pi uD_m(u)\,du=\int_0^\infty p_m(u)\,du=1$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.025, "Chosen finite two-particle model · not the pair distribution of an infinite fluid", ha="center", fontsize=10, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
