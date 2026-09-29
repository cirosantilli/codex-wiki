"""Illustrate an exactly integrated cutoff subtraction with a local counterterm.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; writes cutoff-subtraction-local-counterterm.png to CWD.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    r = np.geomspace(0.5, 1e4, 700)
    # J(x)=16*pi^2 I(Lambda,M), x=Lambda/M; choose M=2*mu.
    def j(x):
        return np.log1p(x*x) - x*x/(1+x*x)
    raw = j(r/2)
    counterterm = -j(r)
    total = raw + counterterm
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.2), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.25, top=0.80, wspace=0.27)
    colors = ["#1665a0", "#b04b27", "#25804c"]
    axes[0].semilogx(r, raw, color=colors[0], lw=2.4, label=r"Bare loop $16\pi^2 I_\Lambda(2\mu)$")
    axes[0].semilogx(r, counterterm, color=colors[1], lw=2.4,
                     label=r"Local subtraction $-16\pi^2 I_\Lambda(\mu)$")
    axes[0].semilogx(r, total, color=colors[2], lw=2.4, label="Their sum")
    axes[0].set(ylabel="Dimensionless correction", title="Two growing terms cancel")
    axes[0].legend(fontsize=8.5, loc="upper left")
    axes[1].semilogx(r, total, color=colors[2], lw=2.4, label="Subtracted correction")
    axes[1].axhline(-np.log(4), color="#555555", ls="--", lw=1.5,
                    label=r"Limit $-\log 4$")
    axes[1].set(ylim=(-1.55, 0.1), title="The finite remainder survives")
    axes[1].legend(fontsize=9, loc="upper right")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set(xlabel=r"Cutoff ratio $\Lambda/\mu$", xlim=(0.5, 1e4))
        ax.grid(alpha=0.23)
    fig.suptitle("A momentum-independent counterterm removes the cutoff divergence", fontsize=13, y=0.96)
    fig.text(0.075, 0.13,
             r"Toy integral: $I_\Lambda(M)=\int_{|k_E|<\Lambda}d^4k_E/[(2\pi)^4(k_E^2+M^2)^2]$;  $M=2\mu$.",
             fontsize=10.5)
    fig.text(0.075, 0.065,
             "The reference scale is fixed. This local scalar example does not prove gauge-theory renormalizability.",
             fontsize=10, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
