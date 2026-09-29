"""Plot cosine iteration and write the PNG basename to cwd.

Uses numpy/matplotlib from pyproject.toml; tested with Python 3.14.4.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-mpl python ../contraction-cosine-iteration.py
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def compute_and_check():
    """Compare contraction bounds against a root independently found by bisection."""
    lower, upper = 0.0, 1.0
    for _ in range(52):
        midpoint = (lower + upper) / 2
        if math.cos(midpoint) > midpoint:
            lower = midpoint
        else:
            upper = midpoint
    root = (lower + upper) / 2
    assert upper - lower < 5e-16
    assert abs(math.cos(root) - root) < 5e-16
    contraction = math.sin(1)
    values = [0.0]
    for _ in range(91):
        values.append(math.cos(values[-1]))
    values = np.array(values)
    steps = np.arange(values.size)
    initial_bounds = contraction**steps / (1 - contraction)
    latest_bounds = contraction * np.abs(np.diff(values)) / (1 - contraction)
    errors = np.abs(values - root)
    # Floating arithmetic is not interval certification; stop the comparison
    # while errors remain far larger than machine precision.
    assert np.all(errors[:41] <= initial_bounds[:41])
    assert np.all(errors[1:41] <= latest_bounds[:40])
    assert np.all((values >= 0) & (values <= 1))
    assert np.all((values[:41] - root) * (values[1:42] - root) < 0)
    samples = np.linspace(0, 1, 1001)
    assert np.max(np.sin(samples)) == contraction
    assert initial_bounds[90] >= 1e-6 > initial_bounds[91]
    assert latest_bounds[39] < 7.20e-7
    print(f"L={contraction:.15f}; independently computed root={root:.15f}")
    for n in (4, 10, 20, 40):
        print(f"n={n}: x={values[n]:.15f}, error={errors[n]:.9g}, "
              f"initial bound={initial_bounds[n]:.9g}, "
              f"latest bound={latest_bounds[n - 1]:.9g}")
    print("Initial bound crosses 1e-6 at n=91; latest-step bound is below 1e-6 at n=40.")
    return values, root, initial_bounds, latest_bounds, errors


def main():
    values, root, initial_bounds, latest_bounds, errors = compute_and_check()
    plt.rcParams.update({"font.size": 11, "axes.facecolor": "white"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.5, 4.6),
                                    layout="constrained", facecolor="white")
    grid = np.linspace(0, 1, 401)
    left.plot(grid, np.cos(grid), color="#2873a7", linewidth=2.5, label=r"$y=\cos x$")
    left.plot(grid, grid, color="#666666", linewidth=1.8, label=r"$y=x$")
    path_x, path_y = [values[0]], [0.0]
    for n in range(12):
        path_x.extend([values[n], values[n + 1]])
        path_y.extend([values[n + 1], values[n + 1]])
    left.plot(path_x, path_y, color="#d07628", linewidth=1.3, alpha=0.9,
              label="First 12 iterations")
    left.scatter([root], [root], color="#238b68", s=55, zorder=5)
    left.annotate(r"$x_*\approx0.739085$", (root, root), xytext=(0.18, 0.42),
                  arrowprops={"arrowstyle": "->", "color": "#238b68"},
                  color="#187451")
    left.set(xlabel=r"$x$", ylabel=r"$y$", xlim=(-0.03, 1.04), ylim=(-0.03, 1.04),
             title="Iterates alternate around the fixed point")
    left.set_aspect("equal", adjustable="box")
    left.legend(loc="upper left", fontsize=9)
    left.grid(alpha=0.18)

    n = np.arange(41)
    right.semilogy(n, initial_bounds[:41], color="#666666", linewidth=2.2,
                    linestyle="--", label=r"Initial: $L^n/(1-L)$")
    right.semilogy(n[1:], latest_bounds[:40], color="#d07628", linewidth=2.2,
                    label=r"Latest: $L|x_n-x_{n-1}|/(1-L)$")
    right.semilogy(n, errors[:41], color="#2873a7", linewidth=2.4,
                    label=r"Measured: $|x_n-x_*|$")
    right.axhline(1e-6, color="#238b68", linestyle=":", linewidth=1.4)
    right.text(1.1, 1.5e-6, r"Tolerance $10^{-6}$", color="#187451", fontsize=10)
    right.set(xlabel=r"Iteration number $n$", ylabel="Error or bound (log scale)",
              title=r"Guaranteed bounds with $L=\sin 1$",
              xlim=(0, 41), ylim=(2e-8, 12))
    right.legend(loc="upper right", fontsize=9)
    right.grid(which="major", alpha=0.2)
    fig.suptitle(r"A contraction turns repeated approximation into a guarantee", fontsize=15)
    destination = Path.cwd() / "contraction-cosine-iteration.png"
    fig.savefig(destination, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Saved {destination.name}")


if __name__ == "__main__":
    main()
