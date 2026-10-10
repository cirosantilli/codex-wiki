"""Plot central Student t densities and their tails; emit a PNG in CWD.

Tested with Python 3.14, matplotlib 3.10.7. No SciPy is required.
"""
from math import exp, gamma, pi, sqrt
from pathlib import Path

import matplotlib.pyplot as plt


def student_t_pdf(t, nu):
    """Unit-scale density for any positive degrees of freedom used here."""
    if nu <= 0:
        raise ValueError("degrees of freedom must be positive")
    return gamma((nu + 1) / 2) / (sqrt(nu * pi) * gamma(nu / 2)) * (1 + t * t / nu) ** (-(nu + 1) / 2)


def normal_pdf(t):
    return exp(-t * t / 2) / sqrt(2 * pi)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), layout="constrained", facecolor="white")
    curves = [(1, "#be4b20"), (3, "#287a49"), (10, "#3660ad")]
    for ax, lo, hi in [(axes[0], -5, 5), (axes[1], 2, 10)]:
        xs = [lo + (hi - lo) * j / 1000 for j in range(1001)]
        for nu, color in curves:
            ax.plot(xs, [student_t_pdf(x, nu) for x in xs], color=color, lw=2.3, label=rf"$t_{{{nu}}}$")
        ax.plot(xs, [normal_pdf(x) for x in xs], color="#222222", lw=2, ls="--", label=r"$N(0,1)$")
        ax.set_xlabel("Value t")
        ax.set_ylabel("Probability density")
        ax.grid(alpha=0.18)
    axes[0].set_title("Center: same location and scale")
    axes[0].set_ylim(0, 0.43)
    axes[0].legend(frameon=False, loc="upper right")
    axes[1].set_title("Right tail: logarithmic density axis")
    axes[1].set_yscale("log")
    axes[1].set_ylim(1e-10, 0.1)
    axes[1].text(0.04, 0.06, "Every finite ν has polynomial tails", transform=axes[1].transAxes, fontsize=10)
    fig.suptitle("Student t: uncertainty in the denominator adds heavy tails", fontsize=15)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
