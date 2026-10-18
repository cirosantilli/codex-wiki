"""Original pure-pair information and filtering plots; Python 3.14,
NumPy 2.3.5, Matplotlib 3.10.7. Writes only the same-basename CWD PNG.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def binary_entropy(alpha):
    alpha = np.asarray(alpha, dtype=float)
    entropy = np.zeros_like(alpha)
    interior = (alpha > 0) & (alpha < 1)
    x = alpha[interior]
    entropy[interior] = -x * np.log2(x) - (1 - x) * np.log2(1 - x)
    return entropy


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    blue, orange, green, gray = "#126782", "#b55d15", "#287d53", "#5b6570"
    fig, (ax, filt) = plt.subplots(1, 2, figsize=(11.5, 6.8),
                                  gridspec_kw={"width_ratios": (1.3, 1)})
    alpha = np.linspace(0, 1, 2001)
    info = 2 * binary_entropy(alpha)
    # The requested I=1 crossing; no auxiliary solver or dependency is needed.
    threshold = 0.11002786443835955
    shade_x = np.linspace(threshold, 1 - threshold, 1001)
    ax.fill_between(shade_x, 1, 2 * binary_entropy(shade_x), color=green, alpha=0.18,
                    label=r"$I>1$ witnesses entanglement")
    ax.plot(alpha, info, color=blue, lw=2.5, label=r"$I(A:B)=2h_2(\alpha)$")
    ax.axhline(1, color=orange, lw=1.5, ls="--", label=r"$I=1$ bit")
    for x in (threshold, 1 - threshold):
        ax.plot([x, x], [0, 1], color=gray, lw=1, ls=":")
        ax.scatter([x], [1], color=orange, s=30, zorder=4)
    ax.scatter([0, 1], [0, 0], color=blue, s=30, zorder=4)
    ax.text(0.5, 1.5, r"$I>1$", ha="center", color=green, fontsize=14)
    ax.set(xlim=(-0.025, 1.025), ylim=(-0.05, 2.2), yticks=(0, 0.5, 1, 1.5, 2),
           xticks=(0, threshold, 0.5, 1 - threshold, 1),
           xticklabels=("0", r"$\alpha_\star$", "0.5", r"$1-\alpha_\star$", "1"),
           xlabel=r"Input pair parameter $\alpha$", ylabel="Quantum mutual information (bits)",
           title="Pure-pair mutual information")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), frameon=False, fontsize=10)
    ax.grid(alpha=0.16)
    reflection = np.linspace(0, 1, 1001)
    optimum = (1 - reflection) / (2 - reflection)
    success = 2 * optimum
    filt.plot(reflection, optimum, color=blue, lw=2.5, label=r"$\alpha_{\mathrm{opt}}=(1-R)/(2-R)$")
    filt.plot(reflection, success, color=orange, lw=2.5, label=r"$P_{\mathrm{succ}}=2(1-R)/(2-R)$")
    filt.scatter([1], [0], facecolors="white", edgecolors=gray, s=60, zorder=4, lw=1.5)
    filt.text(0.05, 0.16, "Maximally entangled output\nconditioned on success", color=green, fontsize=11)
    filt.text(0.40, 0.88, r"$R\to1$: success vanishes", color=gray, fontsize=10)
    filt.set(xlim=(0, 1.025), ylim=(-0.025, 1.06), xticks=(0, 0.25, 0.5, 0.75, 1),
             yticks=(0, 0.25, 0.5, 0.75, 1), xlabel=r"Loss probability $R$ ($0\leq R<1$)",
             ylabel="Parameter / probability", title="Filter compensation and yield")
    filt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), frameon=False, fontsize=10)
    filt.grid(alpha=0.16)
    fig.suptitle("Pure entangled pairs: information and successful filtering", fontsize=17, y=0.97)
    fig.text(0.5, 0.90,
             r"$|\psi_\alpha\rangle=\sqrt{\alpha}\,|11\rangle+\sqrt{1-\alpha}\,|00\rangle$"
             r"     $h_2(x)=-x\log_2x-(1-x)\log_2(1-x)$", ha="center", fontsize=13)
    fig.text(0.5, 0.125,
             r"$I>1$ for $\alpha_\star<\alpha<1-\alpha_\star$, with "
             r"$\alpha_\star\simeq0.110028$ and $1-\alpha_\star\simeq0.889972$.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.065, r"This pure family is entangled for every $0<\alpha<1$, including the regions with $I\leq1$.",
             ha="center", fontsize=13, color=green, weight="bold")
    fig.text(0.5, 0.018, r"Only $\alpha=0,1$ are product states. At $R=1$ the compensated limit has zero success probability.",
             ha="center", fontsize=10, color=gray)
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.37, top=0.79, wspace=0.28)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white", transparent=False,
                metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
