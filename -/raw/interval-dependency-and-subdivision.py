"""Dependency, exact subdivision enclosures and a square-range comparison.

Save interval-dependency-and-subdivision.png to the current working directory.
Bounds and verification use Fraction; floats are used only for drawing.
Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
"""

from fractions import Fraction as Q
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def subtract(x, y):
    return x[0] - y[1], x[1] - y[0]


def multiply(x, y):
    products = [u * v for u in x for v in y]
    return min(products), max(products)


def square_range(x):
    squares = [u * u for u in x]
    return (Q(0) if x[0] <= 0 <= x[1] else min(squares), max(squares))


def enclosure(x):
    return multiply(x, subtract((Q(1), Q(1)), x))


def pieces(n):
    return [(Q(j, n), Q(j + 1, n)) for j in range(n)]


def verify():
    unit = (Q(0), Q(1))
    assert subtract(unit, unit) == (Q(-1), Q(1))
    expected = {
        1: [(Q(0), Q(1))],
        2: [(Q(0), Q(1, 2))] * 2,
        4: [(Q(0), Q(1, 4)), (Q(1, 8), Q(3, 8)),
            (Q(1, 8), Q(3, 8)), (Q(0), Q(1, 4))],
    }
    for n, bounds in expected.items():
        assert [enclosure(x) for x in pieces(n)] == bounds
        for x in pieces(n):
            low, high = enclosure(x)
            for j in range(101):
                t = x[0] + (x[1] - x[0]) * Q(j, 100)
                assert low <= t * (1 - t) <= high
    z = subtract(unit, (Q(1, 2), Q(1, 2)))
    assert square_range(z) == (Q(0), Q(1, 4))
    assert multiply(z, z) == (Q(-1, 4), Q(1, 4))
    assert subtract((Q(1, 4), Q(1, 4)), square_range(z)) == (Q(0), Q(1, 4))
    assert subtract((Q(1, 4), Q(1, 4)), multiply(z, z)) == (Q(0), Q(1, 2))


def main():
    verify()
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig = plt.figure(figsize=(10, 7), dpi=100, facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=(1.25, 1), hspace=0.53, wspace=0.37)
    cartesian = fig.add_subplot(grid[0, 0])
    local = fig.add_subplot(grid[0, 1])
    bars = fig.add_subplot(grid[1, :])
    fig.suptitle("Interval dependency: one input, two independent copies", fontsize=16, y=0.97)

    # The color field is illustrative; all interval bounds are exact Fractions.
    u, v = np.meshgrid(np.linspace(0, 1, 151), np.linspace(0, 1, 151))
    cartesian.pcolormesh(u, v, u * (1 - v), shading="auto", cmap="Blues", vmin=0, vmax=1)
    cartesian.plot([0, 1], [0, 1], color="#bb3e28", lw=3)
    cartesian.scatter([1], [0], color="#bb3e28", zorder=4)
    cartesian.annotate("u = 1, v = 0\noutput = 1", (1, 0), (0.57, 0.14),
                       arrowprops={"arrowstyle": "->", "color": "#bb3e28"}, fontsize=10)
    cartesian.text(0.06, 0.72, "Actual inputs:\nu = v only", color="#9b291c",
                   bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    cartesian.set(title="Independent evaluation: u(1 − v)", xlabel="First copy u", ylabel="Second copy v",
                  xlim=(0, 1), ylim=(0, 1), xticks=(0, 0.5, 1), yticks=(0, 0.5, 1))

    for x in pieces(4):
        low, high = enclosure(x)
        local.add_patch(Rectangle((float(x[0]), float(low)), float(x[1] - x[0]),
                                  float(high - low), facecolor="#dbe9f4", edgecolor="#3479a7", lw=1.5))
    samples = [Q(j, 400) for j in range(401)]
    local.plot([float(x) for x in samples], [float(x * (1 - x)) for x in samples],
               color="#bb3e28", lw=2.5, label="Actual f(x) = x(1 − x)")
    local.axhline(float(Q(1, 4)), color="#bb3e28", ls=":", lw=1)
    local.set(title="Four pieces: local enclosing rectangles", xlabel="Same input x in both factors",
              ylabel="Output", xlim=(0, 1), ylim=(0, 0.42), xticks=(0, 0.25, 0.5, 0.75, 1),
              yticks=(0, 0.125, 0.25, 0.375), yticklabels=("0", "1/8", "1/4", "3/8"))
    local.legend(loc="upper center", bbox_to_anchor=(0.5, -0.23), frameon=False, fontsize=10)

    labels = ["One piece", "Two pieces", "Four pieces", "Square range"]
    uppers = [max(enclosure(x)[1] for x in pieces(n)) for n in (1, 2, 4)] + [Q(1, 4)]
    endpoint_labels = ["1", "1/2", "3/8", "1/4 (exact)"]
    for index, (upper, endpoint) in enumerate(zip(uppers, endpoint_labels)):
        color = "#bb3e28" if index == 3 else "#3479a7"
        bars.plot([0, float(upper)], [index, index], color=color, lw=8, solid_capstyle="butt")
        bars.scatter([0, float(upper)], [index, index], s=35, color=color, zorder=3)
        bars.text(float(upper) + 0.02, index, endpoint, va="center", color=color)
    bars.axvline(float(Q(1, 4)), ls=":", color="#bb3e28", lw=1.3)
    bars.set(title="Enclosure of the full output range", xlim=(-0.02, 1.14), ylim=(3.6, -0.7),
             yticks=range(4), yticklabels=labels, xticks=(0, 0.25, 0.5, 0.75, 1),
             xticklabels=("0", "1/4", "1/2", "3/4", "1"), xlabel="Output value")
    bars.tick_params(axis="y", length=0)
    for ax in (local, bars):
        ax.spines[["top", "right"]].set_visible(False)
    bars.spines["left"].set_visible(False)
    fig.subplots_adjust(left=0.14, right=0.96, bottom=0.09, top=0.87)
    fig.savefig(Path.cwd() / "interval-dependency-and-subdivision.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
