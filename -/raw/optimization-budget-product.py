"""Illustrate product maximization on a budget segment; save basename.png to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/optimization-mpl python3 ../optimization-budget-product.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    budget = 10.0
    optimum = np.full(2, budget / 2)
    multiplier = budget / 2  # L = xy - lambda (x + y - budget).
    x = np.linspace(0, budget, 1001)
    y = budget - x
    product = x * y

    # Check the global bound, feasibility and the chosen multiplier convention.
    assert np.allclose(x + y, budget)
    assert np.all(x >= 0) and np.all(y >= 0)
    assert np.allclose(product, 25 - (x - 5) ** 2)
    assert np.max(product) == 25 and x[np.argmax(product)] == 5
    assert np.allclose(optimum[::-1] - multiplier * np.ones(2), 0)
    assert product[0] == product[-1] == 0
    assert np.isclose((10.1**2 - budget**2) / 4, 0.5025)

    blue, green, orange = "#3476a5", "#20745c", "#b65318"
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.7), layout="constrained",
                             facecolor="white")
    ax, curve = axes
    positive_x = np.linspace(0.05, 10.5, 1800)
    for level in (10, 16, 25, 36):
        color = "#ae5560" if level == 36 else blue
        ax.plot(positive_x, level / positive_x, color=color,
                lw=1.8 if level == 25 else 1.1,
                ls="--" if level == 36 else "-")
        label_x = {10: 8.5, 16: 8.8, 25: 8.8, 36: 8.8}[level]
        ax.text(label_x, level / label_x + 0.22, f"xy = {level}",
                color=color, fontsize=9,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.8})
    ax.plot(x, y, color=green, lw=3, label="Feasible segment")
    ax.scatter([0, 10], [10, 0], color=green, s=25, zorder=5, clip_on=False)
    ax.scatter(2, 8, color=blue, s=32, zorder=6)
    ax.annotate("(2, 8): 16", (2, 8), xytext=(2.3, 8.6), color=blue,
                fontsize=9,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.2})
    ax.scatter(*optimum, color=orange, s=65, zorder=7)
    ax.annotate("(5, 5): 25", optimum, xytext=(1.8, 4.5), color=orange,
                arrowprops={"arrowstyle": "-", "color": orange}, fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.2})
    ax.annotate("", xy=(6.35, 6.35), xytext=optimum,
                arrowprops={"arrowstyle": "->", "color": "#333333", "lw": 1.7})
    ax.text(5.45, 6.75, r"$\nabla f=5\nabla g$", fontsize=10)
    ax.text(5.7, 0.35, r"$x+y=10$", color=green, fontsize=11)
    ax.set(xlim=(0, 10.5), ylim=(0, 10.5), aspect="equal",
           xlabel="x", ylabel="y", title="The highest reachable product contour")
    ax.set_xticks([0, 2, 5, 8, 10])
    ax.set_yticks([0, 2, 5, 8, 10])
    ax.grid(alpha=0.15)

    curve.plot(x, product, color=blue, lw=2.3)
    curve.scatter([0, 10], [0, 0], color=green, s=30, zorder=5, clip_on=False)
    curve.scatter([2, 8], [16, 16], color=blue, s=32, zorder=5)
    curve.scatter(5, 25, color=orange, s=65, zorder=6)
    curve.axvline(5, color=orange, ls=":", lw=1.1)
    curve.annotate("Maximum: 25", (5, 25), xytext=(5.7, 26.8),
                   color=orange, fontsize=10,
                   arrowprops={"arrowstyle": "-", "color": orange})
    curve.text(1.1, 7.0, r"$q(x)=25-(x-5)^2$", color=blue, fontsize=12)
    curve.annotate("16", (2, 16), xytext=(1.0, 17.0), color=blue)
    curve.annotate("16", (8, 16), xytext=(8.35, 17.0), color=blue)
    curve.set(xlim=(0, 10), ylim=(0, 29), xlabel="x (with y = 10 − x)",
              ylabel="Product xy", title="Restricting the objective to feasible points")
    curve.set_xticks([0, 2, 5, 8, 10])
    curve.set_yticks([0, 10, 16, 25])
    curve.grid(alpha=0.15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Optimum {optimum.tolist()}, product 25, multiplier {multiplier:g}")


if __name__ == "__main__":
    main()
