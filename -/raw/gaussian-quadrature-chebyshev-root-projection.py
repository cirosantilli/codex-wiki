"""Original root geometry; tested with Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media. Curves are mathematical models, not measured data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    n = 8
    angles = (2*np.arange(1, n + 1) - 1)*np.pi/(2*n)
    roots = np.cos(angles)
    heights = np.sin(angles)
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(9.5, 6.3), layout="constrained",
                                    gridspec_kw={"height_ratios": [1.2, 1]})
    fig.suptitle(r"Chebyshev roots: $T_8(\cos\theta)=\cos(8\theta)$", fontsize=17)
    theta = np.linspace(0, np.pi, 501)
    top.plot(np.cos(theta), np.sin(theta), color="#2366a0", lw=2)
    top.axhline(0, color="0.45", lw=1)
    for r, h in zip(roots, heights):
        top.plot([r, r], [0, h], color="#8aa9bd", lw=1.2, ls="--")
    top.scatter(roots, heights, color="#2366a0", s=35, zorder=3)
    top.scatter(roots, np.zeros(n), color="#b64b23", s=42, zorder=4)
    top.text(0, 0.56, r"$\theta_k=(2k-1)\pi/16$" + "\nEqual angle gaps: π/8",
             ha="center", va="center", bbox={"facecolor": "white", "edgecolor": "none"})
    top.set(xlim=(-1.08, 1.08), ylim=(-0.08, 1.12), aspect="equal", xlabel=r"$x=\cos\theta$",
            ylabel=r"$\sin\theta$", title="Semicircle projection crowds roots near ±1")
    top.set_xticks([-1, -0.5, 0, 0.5, 1])
    top.set_yticks([0, 0.5, 1])

    x = np.linspace(-1, 1, 1501)
    # Explicit degree-eight polynomial, independent of the angle construction.
    t8 = 128*x**8 - 256*x**6 + 160*x**4 - 32*x**2 + 1
    bottom.plot(x, t8, color="#2366a0", lw=2, label=r"$T_8(x)$")
    bottom.axhline(0, color="0.45", lw=1)
    for r in roots:
        bottom.axvline(r, color="#8aa9bd", lw=0.9, ls="--")
    bottom.scatter(roots, np.zeros(n), color="#b64b23", s=42, zorder=4,
                   label="8 roots / interpolation nodes")
    bottom.set(xlim=(-1.08, 1.08), ylim=(-1.15, 1.15), xlabel="$x$", ylabel=r"$T_8(x)$",
               title="The same projected locations are the polynomial zeros")
    bottom.set_xticks([-1, -0.5, 0, 0.5, 1])
    bottom.set_yticks([-1, 0, 1])
    bottom.legend(loc="upper center", bbox_to_anchor=(0.5, -0.23), frameon=False, ncol=2)
    fig.supxlabel("Analytical illustration: these are roots, not endpoint-inclusive Lobatto nodes.",
                  fontsize=11)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=100, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
