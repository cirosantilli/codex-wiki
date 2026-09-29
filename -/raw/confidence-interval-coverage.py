"""Draw exact normal mean confidence intervals; tested with Python 3.14.4.

Run from _media with MPLBACKEND=Agg and MPLCONFIGDIR=/tmp.
Dependencies: NumPy and Matplotlib, as specified in the root pyproject.toml.
The fixed experiment uses PCG64 seed 42, 40 samples, and 16 observations each.
"""

from math import erf, sqrt
from pathlib import Path
from statistics import NormalDist

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def main():
    mu, sigma, n, repetitions, seed = 0.0, 2.0, 16, 40, 42
    standard_error = sigma / sqrt(n)
    quantile = NormalDist().inv_cdf(0.975)
    halfwidth = quantile * standard_error
    rng = np.random.Generator(np.random.PCG64(seed))
    samples = rng.normal(mu, sigma, size=(repetitions, n))
    means = samples.mean(axis=1)
    lower, upper = means - halfwidth, means + halfwidth
    covers = (lower <= mu) & (mu <= upper)
    count = int(covers.sum())
    analytic_coverage = erf(quantile / sqrt(2))
    assert abs(analytic_coverage - 0.95) < 1e-14
    assert count == 39 and np.flatnonzero(~covers).tolist() == [31]

    blue, orange = "#146b9b", "#b33e13"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(10, 8), layout="constrained", facecolor="white")
    grid = fig.add_gridspec(1, 2, width_ratios=(1.6, 1))
    ax = fig.add_subplot(grid[0])
    theory = fig.add_subplot(grid[1])
    for index, (mean, lo, hi, covered) in enumerate(zip(means, lower, upper, covers), 1):
        color = blue if covered else orange
        ax.plot([lo, hi], [index, index], color=color, linewidth=1.9)
        ax.plot(mean, index, "o", color=color, markersize=3.4)
        if not covered:
            ax.annotate(f"miss: sample {index}", (hi, index), xytext=(5, 0),
                        textcoords="offset points", va="center", color=orange,
                        fontsize=10)
    ax.axvline(mu, color="#222222", linestyle="--", linewidth=1.5)
    ax.set(xlabel=r"Mean estimate and interval endpoints", ylabel="Repeated sample",
           ylim=(repetitions + 1, 0), xlim=(-2.5, 2.5))
    ax.set_yticks([1, 5, 10, 15, 20, 25, 30, 32, 35, 40])
    ax.set_title(f"Realized intervals: {count}/{repetitions} cover μ = 0\n"
                 f"Observed fraction = {count/repetitions:.1%}; seed {seed}",
                 fontsize=12, pad=14)
    ax.grid(axis="x", color="#dddddd", linewidth=0.6)
    ax.legend(handles=[Line2D([0], [0], color=blue, label="Contains μ"),
                       Line2D([0], [0], color=orange, label="Misses μ"),
                       Line2D([0], [0], color="#222222", linestyle="--", label="Fixed μ")],
              loc="lower right", framealpha=1, fontsize=10)

    x = np.linspace(-2.0, 2.0, 1601)
    density = np.exp(-0.5 * (x / standard_error)**2) / (standard_error * sqrt(2*np.pi))
    theory.plot(x, density, color="#222222", linewidth=1.6)
    central = abs(x) <= halfwidth
    theory.fill_between(x, density, where=central, color=blue, alpha=0.25)
    theory.fill_between(x, density, where=~central, color=orange, alpha=0.65)
    for endpoint in [-halfwidth, halfwidth]:
        theory.axvline(endpoint, color=orange, linestyle="--", linewidth=1)
    theory.set(xlabel=r"Possible sample mean $\bar{X}$", ylabel="Probability density",
               xlim=(-2, 2), ylim=(0, 0.95))
    theory.set_xticks([-1.5, -halfwidth, 0, halfwidth, 1.5],
                     ["−1.5", "−0.980", "0", "0.980", "1.5"], rotation=35)
    theory.set_title("Analytic sampling distribution\n" + r"$\bar{X}\sim N(0,0.5^2)$",
                     fontsize=12, pad=14)
    theory.text(0, 0.37, "Central area\nexactly 95%", ha="center", color=blue,
                fontsize=12, fontweight="bold")
    theory.text(0.5, 0.91, "Each tail: 2.5%\n"
                "CI covers 0 precisely when\n" + r"$|\bar{X}|\leq0.979982\ldots$",
                transform=theory.transAxes, va="top", ha="center", fontsize=10)
    theory.spines["left"].set_color("#aaaaaa")
    fig.suptitle("A random interval, a fixed unknown mean\n"
                 r"$X_i\sim N(\mu,2^2)$ independently; $n=16$; "
                 r"$C=\bar{X}\pm z_{0.975}(2/\sqrt{16})$", fontsize=14)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Saved {output}")
    print(f"SE={standard_error}; half-width={halfwidth:.12f}; exact coverage={analytic_coverage:.12f}")
    print(f"Observed coverage={count}/{repetitions} ({count/repetitions:.1%}); missed sample=32")


if __name__ == "__main__":
    main()
