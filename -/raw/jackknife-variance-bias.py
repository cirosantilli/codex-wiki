"""Compare jackknife variance and bias calculations; tested with Python 3.14.4.

Dependencies: Matplotlib and NumPy from the root pyproject.toml.
Run through make _media/jackknife-variance-bias.png. The opaque white PNG
is written in the current directory with the script's basename (1200 x 720).
"""

from math import isclose, sqrt
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def calculations(data):
    """Recompute each mean and centered divisor-m variance after deletion."""
    n = data.size
    reduced = [np.delete(data, i) for i in range(n)]
    means = np.array([row.mean() for row in reduced])
    variances = np.array([row.var(ddof=0) for row in reduced])
    contributions = (n - 1) / n * (means - means.mean())**2
    empirical = data.var(ddof=0)
    bias = (n - 1) * (variances.mean() - empirical)
    return means, variances, contributions, empirical, bias, empirical - bias


def main():
    data = np.array([1., 2., 3., 4., 10.])
    means, variances, parts, empirical, bias, corrected = calculations(data)
    np.testing.assert_allclose(means, [4.75, 4.5, 4.25, 4, 2.5], atol=0, rtol=0)
    np.testing.assert_allclose(variances, [9.6875, 11.25, 12.1875, 12.5, 1.25], atol=0, rtol=0)
    np.testing.assert_allclose(parts, [0.45, 0.2, 0.05, 0, 1.8], atol=1e-14, rtol=0)
    assert empirical == 10 and variances.mean() == 9.375 and bias == -2.5
    assert corrected == 12.5 and data.var(ddof=1) == 12.5
    assert isclose(parts.sum(), 2.5) and isclose(parts.sum(), data.var(ddof=1) / data.size)
    # Check both algebraic identities on further deterministic data, including n=2.
    for other in (np.array([2., 7.]), np.array([3., 3., 3.]),
                  np.array([-4., 0., 1., 2., 6., 11.])):
        _, _, other_parts, _, _, other_corrected = calculations(other)
        assert isclose(other_corrected, other.var(ddof=1), rel_tol=1e-12, abs_tol=1e-12)
        assert isclose(other_parts.sum(), other.var(ddof=1) / other.size,
                       rel_tol=1e-12, abs_tol=1e-12)

    blue, orange, green = "#176b91", "#b94a15", "#237347"
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(10, 6), layout="constrained", facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=[2.6, 1.45], width_ratios=[1, 1.15])
    left = fig.add_subplot(grid[:, 0])
    right = fig.add_subplot(grid[0, 1])
    comparison = fig.add_subplot(grid[1, 1])
    fig.suptitle("One set of deletions, two different targets\nData (1, 2, 3, 4, 10)", fontsize=16)

    indices = np.arange(data.size)
    colors = [blue] * 4 + [orange]
    left.bar(indices, parts, color=colors, width=0.65)
    for i, value in enumerate(parts):
        left.text(i, value + 0.035, f"{value:g}", ha="center", va="bottom")
    left.set_xticks(indices, [f"Omit\n{x:g}" for x in data])
    left.set(ylim=(0, 2.55), ylabel="Contribution to variance estimate of the mean")
    left.set_title("Variance of the sample mean", fontsize=13, pad=12)
    left.text(0.5, 0.94, r"$(4/5)(\bar{x}_{(-i)}-4)^2$" + "\nSum = 2.5; SE = √2.5 ≈ 1.581",
              transform=left.transAxes, ha="center", va="top", fontsize=12)
    left.grid(axis="y", color="#e2e2e2", linewidth=0.6)
    left.set_axisbelow(True)

    right.axhline(variances.mean(), color=green, linestyle="--", linewidth=1.4,
                 label="Deletion average = 9.375")
    right.scatter(indices, variances, color=colors, s=55, zorder=3)
    for i, value in enumerate(variances):
        right.annotate(f"{value:g}", (i, value), xytext=(0, 10),
                       textcoords="offset points", ha="center", fontsize=10)
    right.set_xticks(indices, [f"Omit {x:g}" for x in data])
    right.set(xlim=(-0.6, 4.6), ylim=(0, 15.5), ylabel="Divisor-4 variance")
    right.set_title("Bias correction of the empirical variance", fontsize=12, pad=12)
    right.grid(axis="y", color="#e2e2e2", linewidth=0.6)
    right.legend(loc="lower left", framealpha=1, fontsize=10)

    comparison.barh([1, 0], [empirical, corrected], color=[blue, green], height=0.5)
    comparison.set_yticks([1, 0], ["Original", "Corrected"])
    comparison.set(xlim=(0, 15), ylim=(-0.5, 1.7), xlabel="Variance estimate of individual observations")
    for y, value in zip([1, 0], [empirical, corrected]):
        comparison.text(value + 0.25, y, f"{value:g}", va="center", fontsize=11)
    comparison.set_title("Estimated bias = 4(9.375 − 10) = −2.5\n"
                         "Corrected = 10 − (−2.5) = 12.5", fontsize=11, pad=10)
    comparison.grid(axis="x", color="#e2e2e2", linewidth=0.6)
    comparison.set_axisbelow(True)
    comparison.spines["left"].set_visible(False)
    comparison.tick_params(axis="y", length=0)

    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Saved {output} (1200 x 720)")
    print(f"s²={data.var(ddof=1):g}; Vmean={parts.sum():g}; SE={sqrt(parts.sum()):.12f}")
    print(f"Variance contributions={parts.tolist()}")
    print(f"Deletion empirical variances={variances.tolist()}")
    print(f"T={empirical:g}; average={variances.mean():g}; bias={bias:g}; corrected={corrected:g}")
    print("Additional identity checks passed: n=2, constant data, signed six-point data.")


if __name__ == "__main__":
    main()
