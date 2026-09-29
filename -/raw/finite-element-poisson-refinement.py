"""Compare exact Poisson solution and P1 refinements; opaque PNG to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def solution(n):
    nodes = np.linspace(0, 1, n + 1)
    matrix = np.zeros((n + 1, n + 1))
    load = np.zeros(n + 1)
    for j, length in enumerate(np.diff(nodes)):
        matrix[j:j + 2, j:j + 2] += np.array([[1., -1.], [-1., 1.]]) / length
        load[j:j + 2] += length / 2
    values = np.zeros(n + 1)
    values[1:-1] = np.linalg.solve(matrix[1:-1, 1:-1], load[1:-1])
    np.testing.assert_allclose(values, nodes * (1 - nodes) / 2, atol=2e-15)
    return nodes, values


def main():
    x = np.linspace(0, 1, 1601)
    exact = x * (1 - x) / 2
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.5), layout="constrained",
                             facecolor="white")
    axes[0].plot(x, exact, color="#292929", lw=2.3, label="Exact parabola")
    errors = []
    for n, color, marker in [(4, "#b43b35", "o"), (8, "#2166ac", "s")]:
        nodes, values = solution(n)
        h = 1 / n
        approx = np.interp(x, nodes, values)
        error = exact - approx
        np.testing.assert_allclose(error.max(), h**2 / 8, atol=2e-15)
        # Two-point Gauss quadrature integrates the squared derivative error exactly.
        midpoints = (nodes[:-1] + nodes[1:]) / 2
        gauss_x = midpoints[:, None] + h / (2 * np.sqrt(3)) * np.array([-1., 1.])
        discrete_slopes = np.diff(values) / h
        derivative_error = 0.5 - gauss_x - discrete_slopes[:, None]
        energy_squared = (h / 2 * derivative_error**2).sum()
        np.testing.assert_allclose(energy_squared, h**2 / 12, atol=2e-16)
        np.testing.assert_allclose(np.interp(nodes, x, error), 0, atol=2e-15)
        errors.append((error.max(), np.sqrt(energy_squared)))
        axes[0].plot(nodes, values, color=color, lw=2, marker=marker, markersize=4,
                     label=f"P1, {n} intervals ({n - 1} unknowns)")
        axes[1].plot(x, error, color=color, lw=2,
                     label=rf"$n={n}$: max $=1/{8 * n**2}$")
        print(f"n={n}: max error={error.max():.9f}, energy error={np.sqrt(energy_squared):.9f}")
    np.testing.assert_allclose(np.array(errors[0]) / np.array(errors[1]), [4, 2], atol=1e-12)
    assert np.interp(3 / 8, *solution(4)) == 7 / 64

    axes[0].set(ylabel="$u(x)$ or $u_h(x)$", ylim=(-0.006, 0.151),
                title="Exact at nodes, approximate between them")
    axes[0].legend(loc="lower center", fontsize=10, framealpha=1)
    axes[1].set(ylabel="$u(x)-u_h(x)$", ylim=(-0.0003, 0.0106),
                title="Half the spacing, one quarter the value error")
    axes[1].legend(loc="upper center", fontsize=10, framealpha=1)
    axes[1].ticklabel_format(axis="y", style="plain", useOffset=False)
    for ax in axes:
        ax.set(xlim=(-0.02, 1.02), xlabel="$x$", xticks=[0, 0.25, 0.5, 0.75, 1])
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / "finite-element-poisson-refinement.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Nodal exactness, midpoint error, energy integral and refinement ratios verified.")


if __name__ == "__main__":
    main()
