"""Taylor-sheet confinement enhancement; write the figure to cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    d = np.linspace(.25, 6, 800)
    enhancement = (np.sinh(d)**2+d*d)/(np.sinh(d)**2-d*d)
    fig, ax = plt.subplots(figsize=(8, 4.2), dpi=100, facecolor="white")
    ax.semilogy(d, enhancement, lw=2.5, color="#1766aa", label="Exact leading-order ratio")
    small = np.linspace(.25, 1, 150)
    ax.semilogy(small, 6/small**2, "--", color="#d87922", label=r"Narrow-gap limit $6/d^2$")
    ax.axhline(1, color="0.45", ls=":", lw=1.5, label="Unbounded-fluid value")
    ax.set(xlim=(.25, 6), ylim=(.85, 120), xlabel=r"Dimensionless wall distance $d$",
           ylabel=r"Speed enhancement $\overline{U}_2/U_2$",
           title="A rigid wall enhances transverse Taylor-sheet propulsion")
    ax.grid(alpha=.2, which="both")
    ax.legend(frameon=False, fontsize=10)
    ax.text(.97, .28, r"Small-wave approximation: $\epsilon\ll d$ and $\epsilon\ll1$",
            transform=ax.transAxes, ha="right", fontsize=10)
    fig.tight_layout()
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
