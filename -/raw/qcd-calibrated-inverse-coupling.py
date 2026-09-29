"""Explain calibration and residual scale dependence in an original QCD toy.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; writes qcd-calibrated-inverse-coupling.png to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import numpy as np


def main():
    q0, alpha0, nf = 20.0, 0.16, 5
    beta0 = 11.0 - 2.0 * nf / 3.0
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.6), dpi=120, facecolor="white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.2)
    q = np.geomspace(10.0, 150.0, 400)
    inverse = 1.0 / alpha0 + beta0 / (2.0 * np.pi) * np.log(q / q0)
    axes[0].plot(np.log(q / q0), inverse, lw=2.5, color="#126b98")
    axes[0].scatter([0], [1.0 / alpha0], c="black", s=30, zorder=3)
    axes[0].annotate("Calibration sets the intercept\n" + r"$1/\alpha_s(Q_0)=6.25$",
                     xy=(0, 6.25), xytext=(0.28, 5.8), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": "#444444"})
    axes[0].text(0.06, 0.87, r"Slope $=\beta_0/(2\pi)=23/(6\pi)$", transform=axes[0].transAxes, fontsize=11)
    axes[0].set(xlabel=r"$\ln(Q/Q_0)$, with $Q_0=20$ GeV", ylabel=r"$1/\alpha_s(Q)$",
                title="One calibration fixes the running curve")
    ratio = np.geomspace(0.5, 2.0, 400)
    alpha = 1.0 / (1.0 / alpha0 + beta0 / (2.0 * np.pi) * np.log(ratio))
    a = alpha / np.pi
    b = beta0 / 4.0
    r1 = 1.0 + a
    r2 = r1 + b * a**2 * np.log(ratio**2)
    axes[1].plot(ratio, r1, color="#c86616", lw=2.5, label=r"$R_1=1+a(\mu)$")
    axes[1].plot(ratio, r2, color="#126b98", lw=2.5,
                 label=r"$R_2=R_1+b\,a^2\ln(\mu^2/Q_h^2)$")
    axes[1].axvline(1.0, color="#555555", lw=1, ls="--")
    axes[1].set_xscale("log")
    axes[1].set_xticks([0.5, 1, 2], ["0.5", "1", "2"])
    axes[1].xaxis.set_minor_formatter(NullFormatter())
    axes[1].set(xlim=(0.5, 2), ylim=(1.042, 1.061), xlabel=r"Auxiliary scale $\mu/Q_h$, at fixed $Q_h=20$ GeV",
                ylabel="Dimensionless toy observable", title="Explicit logarithms cancel leading scale drift")
    axes[1].legend(loc="upper right", fontsize=9, framealpha=1)
    fig.text(0.5, 0.025, r"Chosen $n_f=5$, $\alpha_s(20\,\mathrm{GeV})=0.16$; $a=\alpha_s/\pi$, $b=\beta_0/4$. Not measured data or an uncertainty bound.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
