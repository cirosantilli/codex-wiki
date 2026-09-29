"""Original exact fronts; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media. Curves have their own smooth initial conditions, not exact
step initial data. No experimental data or numerical PDE solver are used.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.4, 5), dpi=100, facecolor="white")
    ax.set_facecolor("white")
    z = np.linspace(-3, 3, 2001)
    ax.plot([-3, 0, 0, 3], [2, 2, 0, 0], color="#555555", lw=1.8,
            ls="--", label="Inviscid entropy shock (limit)")
    for viscosity, color in [(0.5, "#277da1"), (0.2, "#ee8959"), (0.08, "#7b4ca0")]:
        profile = 1 - np.tanh(z / (2 * viscosity))
        ax.plot(z, profile, color=color, lw=2.2, label=f"ν = {viscosity:g}")
    ax.axvline(0, color="#777777", lw=0.8, alpha=0.5)
    ax.scatter([0], [1], s=30, color="black", zorder=5)
    ax.annotate("Common center: u = 1\nMoves at speed s = 1", xy=(0, 1),
                xytext=(0.8, 1.16), arrowprops={"arrowstyle": "->"}, fontsize=10)
    ax.text(-2.9, 1.77, "Left state uL = 2", fontsize=10)
    ax.text(1.8, 0.16, "Right state uR = 0", fontsize=10)
    ax.set(xlim=(-3, 3), ylim=(-0.07, 2.12), xlabel="Moving coordinate z = x − t",
           ylabel="u(x, t)", title="Viscous Burgers front: u = 1 − tanh((x − t)/(2ν))")
    ax.legend(loc="upper right", fontsize=10, framealpha=1)
    ax.grid(alpha=0.15)
    fig.text(0.5, 0.025, "Exact profiles with smooth initial data; dimensionless calculation, no measurements",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.055, 1, 1))
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
