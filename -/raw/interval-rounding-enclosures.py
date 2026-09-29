"""Decimal toy outward rounding and sign-changing interval multiplication.

Save interval-rounding-enclosures.png to the current working directory.
Fraction supplies every enclosure and endpoint; floats only position the drawing.
The decimal grid is illustrative and does not simulate binary floating point.
Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
"""

from fractions import Fraction as Q
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def grid_down(value, step):
    return (value // step) * step


def grid_up(value, step):
    return -((-value) // step) * step


def verify():
    value, step = Q(1, 3), Q(1, 1000)
    down, up = grid_down(value, step), grid_up(value, step)
    assert (down, up) == (Q(333, 1000), Q(334, 1000))
    nearest = down if value - down < up - value else up
    assert nearest == down and nearest != value
    # Check both rounding directions on signed values and exact grid points.
    for value in (Q(-1, 3), Q(0), Q(1, 3), Q(334, 1000)):
        low, high = grid_down(value, step), grid_up(value, step)
        assert low <= value <= high and high - low <= step
    products = [x * y for x in (Q(-2), Q(3)) for y in (Q(-4), Q(1))]
    assert products == [Q(8), Q(-2), Q(-12), Q(3)]
    assert (min(products), max(products)) == (Q(-12), Q(8))


def main():
    verify()
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig = plt.figure(figsize=(10, 6.4), dpi=100, facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=(1, 1.2), width_ratios=(1, 1.45), hspace=0.7, wspace=0.48)
    rounding = fig.add_subplot(grid[0, :])
    corners = fig.add_subplot(grid[1, 0])
    bars = fig.add_subplot(grid[1, 1])
    fig.suptitle("Two ways an alleged enclosure can miss valid values", fontsize=16, y=0.97)

    value, step = Q(1, 3), Q(1, 1000)
    down, up = grid_down(value, step), grid_up(value, step)
    # Coordinates in thousandths above 0.333 avoid unreadable tiny tick offsets.
    def pos(number):
        return float((number - down) / step)

    rounding.plot([pos(down), pos(up)], [0, 0], color="#3479a7", lw=7, solid_capstyle="butt")
    rounding.scatter([pos(down), pos(up)], [0, 0], color="#3479a7", s=55, zorder=3)
    rounding.scatter([pos(down)], [1], marker="x", s=100, color="#bb3e28", lw=2.5, zorder=3)
    rounding.axvline(pos(value), color="#222222", ls="--", lw=1.5)
    rounding.text(pos(value), 1.43, "Exact 1/3", ha="center")
    rounding.text(0.53, 1, "Nearest: [0.333, 0.333] misses 1/3", va="center", color="#bb3e28")
    rounding.text(0.53, 0.24, "Outward: [0.333, 0.334] encloses 1/3", color="#3479a7")
    rounding.set(title="Illustrative decimal grid: step 0.001 (not binary rounding)",
                 xlim=(-0.06, 1.1), ylim=(-0.4, 1.8), yticks=(),
                 xticks=(0, pos(value), 1), xticklabels=("0.333", "1/3", "0.334"))

    x, y = (Q(-2), Q(3)), (Q(-4), Q(1))
    corners.add_patch(Rectangle((float(x[0]), float(y[0])), float(x[1] - x[0]), float(y[1] - y[0]),
                                facecolor="#edf3f7", edgecolor="#3479a7", lw=1.5))
    corners.axhline(0, color="#999999", lw=0.7)
    corners.axvline(0, color="#999999", lw=0.7)
    products = []
    for a in x:
        for b in y:
            p = a * b
            products.append(p)
            color = "#bb3e28" if p < 0 else "#3479a7"
            corners.scatter([float(a)], [float(b)], color=color, s=40, zorder=3)
            corners.annotate(str(p), (float(a), float(b)),
                             xytext=(7 if a == x[0] else -7, 8 if b == y[0] else -17),
                             textcoords="offset points", ha="left" if a == x[0] else "right",
                             color=color, fontsize=12, weight="bold")
    corners.set(title="Four corner products xy", xlim=(-2.7, 3.7), ylim=(-4.7, 1.7),
                xticks=(-2, 0, 3), yticks=(-4, 0, 1), xlabel="x ∈ [−2, 3]", ylabel="y ∈ [−4, 1]")

    wrong = sorted((x[0] * y[0], x[1] * y[1]))
    correct = min(products), max(products)
    for row, bounds, color in ((1, wrong, "#bb3e28"), (0, correct, "#3479a7")):
        bars.plot([float(p) for p in bounds], [row, row], lw=8, color=color, solid_capstyle="butt")
        bars.scatter([float(p) for p in bounds], [row, row], s=40, color=color, zorder=3)
    bars.text(-12, 1.44, "Same-side shortcut: [3, 8]", color="#bb3e28")
    bars.text(-12, 0.36, "All four products: [−12, 8]", color="#3479a7")
    bars.scatter([float(p) for p in products], [-0.48] * 4, marker="|", s=140, color="#222222")
    bars.text(-12, -0.78, "Ticks: −12, −2, 3, 8", fontsize=10)
    bars.set(title="Correct interval product: [−12, 8]", xlim=(-13, 9), ylim=(-1, 1.8),
             yticks=(), xticks=(-12, -2, 0, 3, 8), xlabel="Possible product value")
    for ax in (rounding, corners, bars):
        ax.spines[["top", "right"]].set_visible(False)
    for ax in (rounding, bars):
        ax.spines["left"].set_visible(False)
    fig.subplots_adjust(left=0.09, right=0.96, bottom=0.1, top=0.84)
    fig.savefig(Path.cwd() / "interval-rounding-enclosures.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
