"""Plot Q10's trial energy; tested with Python 3.14.4 and pyproject.toml deps.

Run from any directory. The PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    # V0=1 illustrates the shape proved for every positive well depth.
    well_depth = 1.0
    lower, upper = 0.0, 2.0
    for _ in range(70):
        midpoint = (lower + upper) / 2
        if midpoint * (1 + midpoint) ** 3 < well_depth**2:
            lower = midpoint
        else:
            upper = midpoint
    minimum = (lower + upper) / 2
    zero = (np.sqrt(1 + 16 * well_depth**2) - 1) / 2

    def energy(a):
        return a / 2 - well_depth * np.sqrt(a / (1 + a))

    a = np.linspace(0, 4.6, 1300)
    fig, ax = plt.subplots(figsize=(7.2, 4.5), layout="constrained")
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    ax.plot(a, energy(a), color="#175d9c", lw=2.3, label=r"$E(a)=a/2-\sqrt{a/(1+a)}$")
    ax.plot(a, a / 2 - well_depth, "--", color="#888888", lw=1.3, label=r"Asymptote $a/2-1$")
    ax.axhline(0, color="#333333", lw=0.8)
    ax.axvline(0, color="#333333", lw=0.8)
    ax.scatter([0], [0], s=55, facecolors="white", edgecolors="#175d9c", zorder=5)
    ax.scatter([minimum, zero], [energy(minimum), 0], s=35, color="#175d9c", zorder=5)
    ax.annotate("Limiting value only\n(trial at a=0 inadmissible)", xy=(0, 0), xytext=(0.22, 0.35), fontsize=9, arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.annotate(r"Unique minimum $a_*$", xy=(minimum, energy(minimum)), xytext=(1.0, -0.64), fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.annotate(r"Positive zero $a_z$", xy=(zero, 0), xytext=(2.0, -0.25), fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.set(xlim=(-0.06, 4.6), ylim=(-0.77, 1.55), xlabel=r"Width parameter $a$", ylabel=r"Trial energy $E(a)$", title=r"Gaussian variational energy ($V_0=1$)")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.15)
    ax.legend(loc="upper left", frameon=False, bbox_to_anchor=(0.01, 0.99), fontsize=10)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
