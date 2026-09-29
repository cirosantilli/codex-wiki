"""Original London-model profiles; run from _media to write the matching PNG.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
All curves are analytic illustrations, not measured material data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.7), layout="constrained")
    field_color, current_color = "#176b9c", "#ba521b"
    u = np.linspace(0, 6, 601)
    ax = axes[0]
    ax.axvspan(-1, 0, color="#edf1f4")
    ax.plot([-1, 0], [1, 1], color=field_color, lw=2.5)
    ax.plot(u, np.exp(-u), color=field_color, lw=2.5, label=r"$B_x/B_0$")
    ax.plot(u, -np.exp(-u), color=current_color, lw=2.5,
            label=r"$\mu_0\lambda_L J_y/B_0$")
    ax.plot([-1, 0], [0, 0], color=current_color, lw=2.5)
    ax.axvline(0, color="#555555", ls=":")
    ax.text(-0.5, 0.45, "vacuum", rotation=90, ha="center")
    ax.text(3, 0.77, r"$z\geq 0$: Meissner half-space", ha="center")
    ax.set(xlim=(-1, 6), ylim=(-1.13, 1.13), xlabel=r"Depth $z/\lambda_L$ (surface at 0)",
           ylabel="Normalized field and signed current", title="A. One surface: exponential screening")
    ax.legend(loc="lower right", frameon=False)
    ax = axes[1]
    s = np.linspace(-1, 1, 501)
    b = np.cosh(s) / np.cosh(1)
    j = np.sinh(s) / np.cosh(1)
    ax.plot(s, b, color=field_color, lw=2.5, label=r"$B_x/B_0$")
    ax.plot(s, j, color=current_color, lw=2.5, label=r"$\mu_0\lambda_L J_y/B_0$")
    for edge in (-1, 1):
        ax.axvline(edge, color="#555555", ls=":")
    ax.plot([-1.4, -1], [1, 1], color=field_color, lw=2.5)
    ax.plot([1, 1.4], [1, 1], color=field_color, lw=2.5)
    ax.scatter([0], [1 / np.cosh(1)], color=field_color, zorder=4)
    ax.annotate(r"Center: $B_x/B_0\simeq0.648$", (0, 1 / np.cosh(1)),
                xytext=(-0.94, 0.26), arrowprops={"arrowstyle": "->", "color": field_color})
    ax.set(xlim=(-1.4, 1.4), ylim=(-1.13, 1.13), xlabel=r"Position $z/\lambda_L$ (center at 0)",
           title=r"B. Two surfaces: slab $d=2\lambda_L$")
    ax.legend(loc="lower right", frameon=False)
    for ax in axes:
        ax.axhline(0, color="#888888", lw=0.7, zorder=0)
        ax.grid(alpha=0.16)
    fig.suptitle(r"Finite penetration: $\mathbf{B}=B_x\widehat{\mathbf{x}}$, "
                 r"$\mathbf{J}=J_y\widehat{\mathbf{y}}$", fontsize=15)
    fig.supxlabel("Homogeneous, local linear London model; weak tangential field; no vortices. Analytic illustrations.",
                  fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
