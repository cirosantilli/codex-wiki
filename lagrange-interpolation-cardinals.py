"""Plot three Lagrange cardinal polynomials and their interpolant; PNG to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def cardinals(x):
    x = np.asarray(x, dtype=float)
    return np.stack(((x - 1) * (x - 2) / 2,
                     -x * (x - 2), x * (x - 1) / 2))


def main():
    nodes = np.array([0.0, 1.0, 2.0])
    values = np.array([1.0, 2.0, 5.0])
    x = np.linspace(0, 2, 801)
    basis = cardinals(x)
    p = values @ basis
    np.testing.assert_array_equal(cardinals(nodes), np.eye(3))
    np.testing.assert_allclose(basis.sum(axis=0), 1, rtol=0, atol=5e-16)
    np.testing.assert_allclose(p, x**2 + 1, rtol=0, atol=2e-15)
    np.testing.assert_array_equal(values @ cardinals(nodes), values)
    np.testing.assert_array_equal(cardinals(0.5), [3 / 8, 3 / 4, -1 / 8])
    assert values @ cardinals(0.5) == 1.25
    # The Newton coefficients are 1, 1, 1, from divided differences 1, 3, 1.
    first = np.diff(values) / np.diff(nodes)
    second = (first[1] - first[0]) / (nodes[2] - nodes[0])
    np.testing.assert_array_equal(first, [1.0, 3.0])
    assert second == 1.0
    np.testing.assert_allclose(1 + x + x * (x - 1), p, rtol=0, atol=2e-15)

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.6), layout="constrained")
    fig.patch.set_facecolor("white")
    colors = ["#2166ac", "#25834a", "#b43b35"]
    ax = axes[0]
    for i, color in enumerate(colors):
        ax.plot(x, basis[i], color=color, lw=2.2, label=rf"$\ell_{i}(x)$")
        ax.scatter(nodes, cardinals(nodes)[i], color=color, s=45, zorder=5,
                   marker=["o", "s", "^"][i])
    ax.axhline(1, color="0.45", ls="--", lw=1.2,
               label=r"$\ell_0+\ell_1+\ell_2=1$")
    ax.axhline(0, color="0.6", lw=0.8)
    ax.set(ylim=(-0.25, 1.38), ylabel="Cardinal value",
           title="Each basis polynomial selects one node")
    ax.legend(loc="upper center", ncols=2, fontsize=10, framealpha=1)
    ax.annotate("Negative between nodes", (0.5, -0.125),
                xytext=(0.95, -0.23), fontsize=9,
                arrowprops={"arrowstyle": "->", "color": "0.4"})

    ax = axes[1]
    for i, color in enumerate(colors):
        ax.plot(x, values[i] * basis[i], color=color, lw=1.5, ls="--",
                label=rf"${int(values[i])}\ell_{i}(x)$")
    ax.plot(x, p, color="#292929", lw=2.7, label=r"Sum: $p(x)=x^2+1$")
    ax.scatter(nodes, values, color="black", s=55, zorder=6)
    for a, b in zip(nodes, values):
        ax.annotate(f"({int(a)}, {int(b)})", (a, b), xytext=(5, 8),
                    textcoords="offset points", fontsize=10)
    ax.scatter([0.5], [1.25], color="#7952a3", s=45, zorder=6)
    ax.annotate(r"$p(1/2)=5/4$", (0.5, 1.25), xytext=(0.68, 2.75),
                fontsize=11, color="#7952a3",
                arrowprops={"arrowstyle": "->", "color": "#7952a3"})
    ax.set(ylim=(-0.85, 5.65), ylabel="Weighted contribution or sum",
           title="Data values are the basis coefficients")
    ax.legend(loc="upper left", fontsize=10, framealpha=1)
    for ax in axes:
        ax.set(xlim=(-0.06, 2.16), xticks=[0, 0.5, 1, 1.5, 2], xlabel="$x$")
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / "lagrange-interpolation-cardinals.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Cardinal identity, sum-to-one, nodal values, p(1/2)=5/4, and Newton form verified.")


if __name__ == "__main__":
    main()
