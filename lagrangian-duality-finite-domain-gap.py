"""Explain an original finite-domain duality gap; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes the matching PNG to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (ax, dual) = plt.subplots(1, 2, figsize=(11, 4.6), layout="constrained")
    x = np.linspace(-2.4, 2.4, 600)
    colors = ["#8a58a6", "#3478b5", "#d37517"]
    for nu, color in zip((-1, 0, 1), colors):
        q = -2*abs(nu)
        ax.plot(x, q - nu*x, color=color, lw=1.8,
                label=rf"$\nu={nu}$:  $t={q:g}{'-' if nu >= 0 else '+'}{abs(nu):g}x$")
    ax.plot([-2, 2], [0, 0], color="#242c36", ls=":", lw=2.2, zorder=3)
    ax.scatter([-2, 2], [0, 0], color="#242c36", s=70, zorder=5)
    ax.scatter(0, 3, color="#327847", s=100, zorder=5)
    ax.scatter(0, 0, facecolors="white", edgecolors="#242c36", s=70, zorder=5)
    ax.annotate("Only feasible decision\n(0, 3)", (0, 3), xytext=(0, 3.5), ha="center",
                color="#327847", arrowprops={"arrowstyle": "->", "color": "#327847"})
    ax.annotate("Averaged cost-residual pair;\nnot attainable", (0, 0),
                xytext=(-0.6, 1.15), ha="center",
                arrowprops={"arrowstyle": "->", "color": "#242c36"})
    ax.text(-2, 0.24, "(-2, 0)", ha="center")
    ax.text(2, 0.24, "(2, 0)", ha="center")
    ax.set(xlim=(-2.6, 2.6), ylim=(-4.8, 4.6), xlabel="Equality residual h(x) = x",
           ylabel="Cost t", title="Every supporting line stays below cost 3")
    ax.legend(loc="lower center", fontsize=9, framealpha=0.97)

    nu = np.linspace(-2, 2, 1001)
    dual.plot(nu, -2*np.abs(nu), color="#3478b5", lw=2.5,
              label=r"$q(\nu)=-2|\nu|$")
    dual.axhline(3, color="#327847", ls="--", lw=1.5,
                 label=r"Primal value $p_*=3$")
    dual.axhline(0, color="#242c36", lw=0.9, ls=":")
    dual.scatter(0, 0, color="#3478b5", s=65, zorder=4)
    dual.annotate("", (0.65, 3), (0.65, 0),
                  arrowprops={"arrowstyle": "<->", "color": "#d37517", "lw": 1.8})
    dual.text(0.78, 1.45, "Duality\ngap = 3", color="#995210", va="center")
    dual.annotate(r"$\nu_*=0$, $d_*=0$", (0, 0), xytext=(-1.8, 0.8),
                  arrowprops={"arrowstyle": "->", "color": "#3478b5"})
    dual.set(xlim=(-2.1, 2.1), ylim=(-4.8, 4.6), xlabel=r"Unrestricted multiplier $\nu$",
             ylabel="Dual lower bound", title="Dual attainment leaves a positive gap")
    dual.legend(loc="lower center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
