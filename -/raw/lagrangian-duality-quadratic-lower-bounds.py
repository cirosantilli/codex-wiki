"""Plot the original quadratic duality example; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes the matching PNG to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (ax, dual) = plt.subplots(1, 2, figsize=(11, 4.8), layout="constrained")
    x = np.linspace(-1, 7, 1000)
    ax.axvspan(4, 7, color="#e7f3e9", zorder=0)
    ax.axvline(4, color="#3c7c47", lw=1)
    ax.plot(x, (x - 1)**2 + 2, color="#242c36", lw=2.5,
            label=r"$f(x)=(x-1)^2+2$")
    colors = ["#3478b5", "#d37517", "#8a58a6"]
    for lam, color in zip((2, 6, 9), colors):
        q = 2 + 3*lam - lam**2/4
        ax.plot(x, (x - 1)**2 + 2 + lam*(4 - x), color=color, lw=1.8,
                label=rf"$L(x,{lam})$,  $q({lam})={q:g}$")
        ax.axhline(q, color=color, ls="--", lw=0.9, alpha=0.8)
        ax.scatter(1 + lam/2, q, color=color, s=42, zorder=4)
    ax.scatter(4, 11, marker="*", color="#242c36", s=165, zorder=5)
    ax.annotate(r"$x_*=4$, $p_*=11$", (4, 11), xytext=(4.35, 20),
                arrowprops={"arrowstyle": "->", "color": "#242c36"})
    ax.text(5.7, 31.5, r"Feasible: $x\geq4$", ha="center", color="#35693e")
    ax.set(xlim=(-1, 7), ylim=(-1, 35), xlabel="Decision x", ylabel="Objective / Lagrangian value",
           title="Inner minima give lower bounds")
    ax.legend(loc="upper left", fontsize=9, framealpha=0.98)

    lam = np.linspace(0, 12, 1000)
    dual.plot(lam, 2 + 3*lam - lam**2/4, color="#3478b5", lw=2.5)
    dual.axhline(11, color="#242c36", ls="--", lw=1.2,
                 label=r"Primal value $p_*=11$")
    dual.axvline(6, color="#d37517", lw=1, ls=":")
    for value, color in zip((2, 6, 9), colors):
        dual.scatter(value, 2 + 3*value - value**2/4, color=color, s=55, zorder=4)
    dual.annotate(r"$\lambda_*=6$, $d_*=11$", (6, 11), xytext=(6.6, 7),
                  arrowprops={"arrowstyle": "->", "color": "#d37517"})
    dual.text(0.6, 12.6, r"$q(\lambda)=11-(\lambda-6)^2/4$", color="#3478b5")
    dual.set(xlim=(0, 12), ylim=(-1, 15), xlabel=r"Multiplier $\lambda\geq0$",
             ylabel="Dual lower bound", title="Maximize the concave dual function")
    dual.legend(loc="lower center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
