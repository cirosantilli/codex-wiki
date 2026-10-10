"""Purity and X-measurement probability along a qubit polarization family.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; writes an opaque white PNG in cwd.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    p = np.linspace(0, 1, 501)
    purity = (1 + p**2) / 2
    probability = (1 + p) / 2
    fig, ax = plt.subplots(figsize=(8, 4.9), dpi=130)
    ax.plot(p, probability, color="#ba601b", lw=2.6,
            label=r"X outcome $P(+)= (1+p)/2$")
    ax.plot(p, purity, color="#245f91", lw=2.8,
            label=r"Purity $\mathrm{Tr}(\rho_p^2)=(1+p^2)/2$")
    sample_p = np.array([0, 0.5, 1])
    ax.scatter(sample_p, (1 + sample_p**2) / 2, color="#245f91", s=45, zorder=4)
    ax.scatter(sample_p, (1 + sample_p) / 2, color="#ba601b", s=25, zorder=5)
    ax.plot([0.5, 0.5], [0.625, 0.75], color="#777777", ls=":", lw=1.2)
    ax.annotate(r"$p=1/2$: purity $5/8$", (0.5, 0.625), xytext=(0.56, 0.55),
                color="#245f91", fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#245f91"})
    ax.annotate(r"$P(+)=3/4$", (0.5, 0.75), xytext=(0.2, 0.78),
                color="#ba601b", fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#ba601b"})
    ax.annotate(r"$I/2$: maximally mixed", (0, 0.5), xytext=(0.055, 0.47),
                fontsize=11)
    ax.annotate(r"$|+\rangle$: pure", (1, 1), xytext=(0.77, 1.04),
                fontsize=11, arrowprops={"arrowstyle": "->", "color": "#444444"})
    ax.set(xlim=(-0.02, 1.03), ylim=(0.44, 1.09), xticks=[0, 0.25, 0.5, 0.75, 1],
           yticks=[0.5, 0.625, 0.75, 1],
           xlabel=r"Polarization $p$: Bloch vector $(p,0,0)$",
           ylabel="Purity or outcome probability",
           title=r"$\rho_p=p|+\rangle\langle+|+(1-p)I/2$,  $0\leq p\leq 1$")
    ax.legend(frameon=False, fontsize=11, loc="upper left")
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
