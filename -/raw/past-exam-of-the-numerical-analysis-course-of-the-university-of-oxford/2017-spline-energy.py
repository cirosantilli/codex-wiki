"""Compare a clamped cubic spline with its nodal Hermite polynomial.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7, as declared
in the repository's pyproject.toml. Run this script to regenerate the
PNG in the current working directory; the example is original and is not an examination statement.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0.0, 2.0, 601)
    t = np.minimum(x, 2.0 - x)
    spline = 3.0 * t**2 - 2.0 * t**3
    hermite = x**2 * (2.0 - x) ** 2
    spline_second = 6.0 - 12.0 * t
    hermite_second = 12.0 * x**2 - 24.0 * x + 8.0

    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.7), layout="constrained")
    fig.set_facecolor("white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_xlim(0, 2)
        ax.set_xticks([0, 1, 2])
        ax.set_xlabel("x")
        ax.grid(alpha=0.18)

    axes[0].plot(x, spline, color="#1565c0", lw=2.3, label="Cubic spline S")
    axes[0].plot(x, hermite, color="#c65a13", lw=2.0, ls="--",
                 label="Hermite polynomial T")
    axes[0].fill_between(x, spline, hermite, color="#c65a13", alpha=0.13)
    axes[0].scatter([0, 1, 2], [0, 1, 0], color="black", s=23, zorder=4)
    axes[0].set_title("Same values and zero slopes at each knot")
    axes[0].set_ylabel("Function value")
    axes[0].legend(loc="upper left", fontsize=9, framealpha=0.95)

    axes[1].plot(x, spline_second, color="#1565c0", lw=2.3, label="S''")
    axes[1].plot(x, hermite_second, color="#c65a13", lw=2.0, ls="--", label="T''")
    axes[1].set_title("Squared second derivatives\nmeasure roughness")
    axes[1].set_ylabel("Second derivative")
    axes[1].legend(loc="upper right", fontsize=9)
    axes[1].text(0.5, 0.56,
                 "$J(S)=24$\n$J(T)=128/5$\n$J(T)-J(S)=J(T-S)=8/5$",
                 transform=axes[1].transAxes, ha="center", va="center", fontsize=10,
                 bbox={"facecolor": "white", "edgecolor": "#cccccc", "alpha": 0.95})

    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
