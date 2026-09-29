"""Compare geometric partial sums with exact, uniform truncation errors.

Run from the desired output directory. All curves follow finite identities;
the plot is not a fitted or sampled approximation.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def partial_sum(x, degree):
    x = np.asarray(x)
    result = np.ones_like(x, dtype=float)
    term = np.ones_like(x, dtype=float)
    for _ in range(degree):
        term = term * x
        result = result + term
    return result


def minimum_degree(radius, tolerance):
    # Test the bound directly to avoid a rounding error at exact integer logs.
    degree = 0
    while radius ** (degree + 1) / (1 - radius) > tolerance:
        degree += 1
    return degree


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 5.7), dpi=100)
    x = np.linspace(-0.95, 0.95, 1401)
    axes[0].plot(x, 1 / (1 - x), color="#333333", linewidth=2.5,
                 label="Exact 1/(1 − x)")
    for degree, color in [(2, "#27835f"), (5, "#7755a3"), (15, "#c47724"), (40, "#2867a0")]:
        axes[0].plot(x, partial_sum(x, degree), color=color, linewidth=1.8,
                     linestyle="--", label=f"Degree N = {degree}")
    axes[0].set_title("Finite polynomials approximate an infinite sum")
    axes[0].set_xlabel("Real x, strictly inside |x| < 1")
    axes[0].set_ylabel("Partial sum / function value")
    axes[0].set_xlim(-0.95, 0.95)
    axes[0].set_ylim(0, 21)
    axes[0].legend(loc="upper left", fontsize=9.5)
    degrees = np.arange(0, 1201)
    tolerance = 0.001
    for radius, color in [(0.5, "#27835f"), (0.9, "#c47724"), (0.99, "#2867a0")]:
        errors = radius ** (degrees + 1) / (1 - radius)
        mask = errors > 1e-7
        axes[1].semilogy(degrees[mask], errors[mask], color=color,
                         linewidth=2.3, label=f"Closed disk |z| ≤ {radius:g}")
        needed = minimum_degree(radius, tolerance)
        actual = radius ** (needed + 1) / (1 - radius)
        axes[1].scatter([needed], [actual], color=color, s=35, zorder=4)
        text_xy = {0.5: (100, 0.018), 0.9: (400, 0.0035), 0.99: (825, 0.020)}
        axes[1].annotate(f"N = {needed}", xy=(needed, actual),
                         xytext=text_xy[radius], color=color, fontsize=10,
                         arrowprops={"arrowstyle": "->", "color": color})
    axes[1].axhline(tolerance, color="#666666", linestyle=":", linewidth=1.4)
    axes[1].text(620, tolerance * 0.65, "Tolerance 10⁻³", fontsize=10, color="#444444")
    axes[1].set_title("Near the boundary, more terms may be needed")
    axes[1].set_xlabel("Polynomial degree N")
    axes[1].set_ylabel("Exact worst-case error rᴺ⁺¹ / (1 − r)")
    axes[1].set_xlim(0, 1200)
    axes[1].set_ylim(1e-5, 200)
    axes[1].legend(loc="upper right", fontsize=9.5)
    for ax in axes:
        ax.grid(alpha=0.18)
    fig.suptitle("A radius of convergence gives a domain; a remainder gives a stopping rule",
                 fontsize=15, y=0.975)
    fig.text(0.5, 0.035,
             "Degrees count from the constant term. "
             "The error bound is attained at the positive real point z = r.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.975, top=0.82, bottom=0.19, wspace=0.28)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
