"""Compare degree-10 Runge interpolants at two node sets; write PNG to cwd.

Direct-product barycentric weights suffice for these eleven nodes. Products
can underflow or overflow for much larger degrees or badly scaled intervals.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def barycentric_weights(nodes):
    nodes = np.asarray(nodes, dtype=float)
    differences = nodes[:, None] - nodes[None, :]
    np.fill_diagonal(differences, 1.0)
    assert np.all(differences != 0), "Interpolation nodes must be distinct."
    weights = 1.0 / np.prod(differences, axis=1)
    assert np.all(np.isfinite(weights))
    return weights / np.max(np.abs(weights))


def barycentric_evaluate(x, nodes, values, weights):
    x = np.asarray(x, dtype=float)
    nodes, values = np.asarray(nodes), np.asarray(values)
    differences = x.reshape(-1, 1) - nodes[None, :]
    hits = differences == 0
    exact = hits.any(axis=1)
    result = np.empty(x.size)
    # Return stored data exactly; do not divide by zero or use a tolerance
    # that would snap nearby evaluation points to an interpolation node.
    result[exact] = values[np.argmax(hits[exact], axis=1)]
    terms = weights / differences[~exact]
    # Common row scaling protects evaluations extremely close to a node.
    terms /= np.max(np.abs(terms), axis=1, keepdims=True)
    result[~exact] = (terms @ values) / terms.sum(axis=1)
    return result.reshape(x.shape)


def runge(x):
    return 1 / (1 + 25 * x**2)


def main():
    n = 10
    grid = np.linspace(-1, 1, 20001)
    target = runge(grid)
    cases = [
        ("Equally spaced nodes", np.linspace(-1, 1, n + 1), "#b43b35"),
        ("Chebyshev–Lobatto nodes", np.cos(np.arange(n + 1) * np.pi / n), "#25834a"),
    ]
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(2, 2, figsize=(10.4, 6.8), layout="constrained",
                             sharex=True, sharey="row")
    fig.patch.set_facecolor("white")
    fig.suptitle(r"Same function, same degree: $f(x)=1/(1+25x^2)$, $n=10$", fontsize=15)
    maxima = []
    for col, (label, nodes, color) in enumerate(cases):
        values = runge(nodes)
        weights = barycentric_weights(nodes)
        np.testing.assert_array_equal(
            barycentric_evaluate(nodes, nodes, values, weights), values)
        # Verify reproduction with known coefficients, independently of f.
        coefficients = np.array([1, -0.2, 0.3, 0.1, -0.4, 0.15, 0.25,
                                 -0.1, 0.2, 0.12, -0.08])
        known = np.polynomial.polynomial.polyval(grid, coefficients)
        known_values = np.polynomial.polynomial.polyval(nodes, coefficients)
        np.testing.assert_allclose(
            barycentric_evaluate(grid, nodes, known_values, weights), known,
            rtol=0, atol=2e-13)
        p = barycentric_evaluate(grid, nodes, values, weights)
        assert np.all(np.isfinite(p))
        np.testing.assert_allclose(
            barycentric_evaluate(grid, nodes, values, -7 * weights), p,
            rtol=0, atol=3e-13)
        errors = np.abs(p - target)
        peak = int(np.argmax(errors))
        maxima.append(errors[peak])
        print(f"{label}: node error = 0; grid max error = {errors[peak]:.10f}; "
              f"x = {grid[peak]:.5f}; {grid.size} grid points")

        ax = axes[0, col]
        ax.plot(grid, target, color="#292929", lw=2, label="Target function")
        ax.plot(grid, p, color=color, lw=2, label="Degree-10 interpolant")
        ax.scatter(nodes, values, color=color, edgecolors="white", s=35, zorder=5,
                   label="11 interpolation nodes")
        ax.set(title=label, ylim=(-0.45, 2.15), ylabel="Function value" if col == 0 else "")
        ax.legend(loc="upper center", fontsize=9, framealpha=1)
        ax = axes[1, col]
        # Log axes cannot display zero; leave exact zeros as gaps.
        ax.semilogy(grid, np.where(errors > 0, errors, np.nan), color=color, lw=1.7)
        ax.scatter([grid[peak]], [errors[peak]], color=color, s=35, zorder=5)
        ax.text(0.5, 0.96, f"Grid maximum: {errors[peak]:.6f}",
                transform=ax.transAxes, ha="center", va="top", fontsize=11,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.95})
        ax.text(0.5, 0.035, "Error is exactly zero at every node",
                transform=ax.transAxes, ha="center", fontsize=9,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.95})
        ax.set(ylim=(1e-7, 4), xlabel="$x$",
               ylabel="Absolute error (log scale)" if col == 0 else "")
    assert 1.91 < maxima[0] < 1.92
    assert 0.132 < maxima[1] < 0.133
    print(f"Grid maximum ratio = {maxima[0] / maxima[1]:.3f}")
    for ax in axes.flat:
        ax.set(xlim=(-1.03, 1.03), xticks=[-1, -0.5, 0, 0.5, 1])
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / "interpolation-node-placement.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
