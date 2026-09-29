"""Original normalized fourth-power interface example, with no material fit.

Tested with Python 3.14, numpy 2.3 and matplotlib 3.10. Run from _media.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.8), facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.23, top=0.77, wspace=0.34)
    fig.suptitle("A chosen fourth-power thermal boundary model", fontsize=16, y=0.97)
    fig.text(0.5, 0.865, r"$q=\Sigma(T_h^4-T_c^4)$,  $\Sigma>0$;  illustrative, no experimental fit",
             ha="center", fontsize=12)
    hot = np.linspace(1, 1.65, 250)
    axes[0].plot(hot, hot**4 - 1, color="#236d91", lw=2.5, label="Exact chosen law")
    axes[0].plot(hot, 4 * (hot - 1), color="#bb7335", lw=2, ls="--", label="Tangent at equilibrium")
    axes[0].plot(1.2, 1.2**4 - 1, "o", color="#236d91")
    axes[0].annotate("(1.2, 1.0736)", (1.2, 1.2**4 - 1), xytext=(1.04, 3.3),
                     arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    axes[0].set(xlabel=r"Hot-side temperature $T_h/T_0$", ylabel=r"Heat flux $q/(\Sigma T_0^4)$",
                title=r"Fixed cold side: $T_c=T_0$", xlim=(1, 1.65), ylim=(0, 6.6))
    axes[0].legend(loc="upper left", frameon=False, fontsize=9)
    temp = np.linspace(0.7, 2, 250)
    axes[1].plot(temp, temp**-3, color="#684f9b", lw=2.5)
    axes[1].plot([1, 2], [1, 1/8], "o", color="#684f9b")
    axes[1].annotate("Eight times smaller", (2, 1/8), xytext=(1.12, 1.75),
                     arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    axes[1].text(0.95, 2.6, r"$R_K(T)=1/(4\Sigma T^3)$", fontsize=12)
    axes[1].set(xlabel=r"Common equilibrium temperature $T/T_0$",
                ylabel=r"Areal resistance $R_K(T)/R_K(T_0)$", title="Differential resistance near equilibrium",
                xlim=(0.7, 2.05), ylim=(0, 3.1))
    for ax in axes:
        ax.grid(alpha=0.18)
    fig.text(0.5, 0.065, r"$T_0>0$ is a reference scale; whole-interface resistance is $R_K/A$.",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
