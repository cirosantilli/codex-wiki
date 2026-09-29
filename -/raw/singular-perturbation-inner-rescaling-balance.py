"""Explain inner rescaling and signed derivative balance with two panels.

Python 3.14, NumPy 2.3, Matplotlib 3.10. Run from _media to emit the PNG there.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.5, 4.8), layout="constrained")
    colors = ("#0072B2", "#D55E00", "#009E73")
    for epsilon, color, style in zip((0.2, 0.05, 0.01), colors, ("-", "--", ":")):
        # The epsilon=0.2 domain ends at X=5, rather than extending past x=1.
        X = np.linspace(0, min(6, 1 / epsilon), 601)
        Y = np.expm1(-X) / np.expm1(-1 / epsilon)
        left.plot(X, Y, style, color=color, linewidth=2.6,
                  label=rf"Exact, $\epsilon={epsilon:g}$")
    mark_X = np.arange(0, 6.01, 0.6)
    left.plot(mark_X, -np.expm1(-mark_X), "o", color="black", fillstyle="none",
              markersize=5, label=r"Inner limit $1-e^{-X}$")
    left.text(0.45, 0.22, "Profiles nearly collapse after rescaling.\n"
              r"Finite-$\epsilon$ normalization still matters.", fontsize=10)
    left.set(xlim=(0, 6), ylim=(-0.025, 1.06), xlabel=r"Inner coordinate $X=x/\epsilon$",
             ylabel=r"$Y_\epsilon(X)=y_\epsilon(\epsilon X)$", title="The layer has a fixed inner shape")
    left.legend(loc="center right", frameon=False, fontsize=9.5)
    X = np.linspace(0, 6, 601)
    epsilon = 0.05
    magnitude = np.exp(-X) / (-np.expm1(-1 / epsilon))
    right.plot(X, magnitude, color="#0072B2", linewidth=2.6,
               label=r"$\epsilon y_\epsilon'=Y_\epsilon'$ ")
    right.plot(X, -magnitude, color="#D55E00", linewidth=2.6,
               label=r"$\epsilon^2y_\epsilon''=Y_\epsilon''$")
    right.axhline(0, color="#333333", linestyle="--", linewidth=1.2)
    right.text(1.6, -0.72, r"$Y_\epsilon''+Y_\epsilon'=0$" + "\n"
               + "Equal magnitudes, opposite signs.", fontsize=11)
    right.set(xlim=(0, 6), ylim=(-1.1, 1.1), xlabel=r"Inner coordinate $X=x/\epsilon$",
              ylabel="Signed equation terms, multiplied by ε",
              title=r"Both derivative terms survive ($\epsilon=0.05$)")
    right.legend(loc="upper right", frameon=False, fontsize=10)
    for ax in (left, right):
        ax.grid(alpha=0.18)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
