"""Original Newtonian model diagram; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media. G is the 2022 CODATA recommended value verified in NIST's
complete listing, https://physics.nist.gov/cuu/Constants/Table/allascii.txt.
The curves are model predictions and inference biases, never experimental data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (force_ax, bias_ax) = plt.subplots(1, 2, figsize=(10.5, 4.9))
    fig.subplots_adjust(left=0.085, right=0.975, bottom=0.19, top=0.82, wspace=0.35)
    fig.suptitle("Gravitational constant: signal scale and model sensitivity", y=0.965, fontsize=15)
    gravity_constant = 6.67430e-11
    separation = np.geomspace(0.1, 1.0, 300)
    force_nn = gravity_constant / separation**2 * 1e9
    force_ax.loglog(separation, force_nn, color="#175a91", lw=2.5)
    force_ax.set(title="Two 1 kg point masses", xlabel="Actual center separation r (m)",
                 ylabel="Predicted attraction F (nN)", xlim=(0.085, 1.16), ylim=(0.045, 11))
    force_ax.set_xticks([0.1, 0.2, 0.5, 1.0], labels=["0.1", "0.2", "0.5", "1"])
    force_ax.set_yticks([0.1, 1, 10], labels=["0.1", "1", "10"])
    force_ax.minorticks_off()
    force_ax.grid(alpha=0.2)
    force_ax.scatter([0.1, 1], [6.67430, 0.0667430], color="#175a91", s=32, zorder=4)
    force_ax.annotate("6.6743 nN", (0.1, 6.6743), xytext=(12, -5), textcoords="offset points")
    force_ax.annotate("0.066743 nN", (1, 0.066743), xytext=(-104, 14), textcoords="offset points")
    force_ax.text(0.31, 0.48, r"$F=GMm/r^2$", fontsize=14, transform=force_ax.transAxes)

    separation_error_um = np.linspace(-10, 10, 401)
    true_separation = 0.1
    inferred_ratio = (1 + separation_error_um * 1e-6 / true_separation)**2
    bias_ppm = (inferred_ratio - 1) * 1e6
    bias_ax.plot(separation_error_um, bias_ppm, color="#c15716", lw=2.5)
    bias_ax.axhline(0, color="0.65", lw=0.8)
    bias_ax.axvline(0, color="0.65", lw=0.8)
    bias_ax.scatter([1], [(1.00001**2 - 1) * 1e6], color="#c15716", zorder=4)
    bias_ax.annotate("+1 μm → +20.0001 ppm", (1, 20.0001), xytext=(-125, 51),
                     textcoords="offset points", arrowprops={"arrowstyle": "->", "color": "0.3"})
    bias_ax.set(title="Same force; wrong entered distance", xlabel="Entered separation error δr (μm)",
                ylabel="Bias in inferred G (ppm)", xlim=(-10, 10), ylim=(-225, 225))
    bias_ax.text(0.08, 0.08, r"$G_{\rm inferred}/G_{\rm true}=(1+\delta r/r)^2$" + "\n" + r"True $r=0.100$ m; $F,M,m$ fixed",
                 transform=bias_ax.transAxes, fontsize=11,
                 bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    bias_ax.grid(alpha=0.2)
    fig.text(0.5, 0.045, "Ideal point-mass calculations • 2022 CODATA G • no measurement data", ha="center", color="0.35", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
