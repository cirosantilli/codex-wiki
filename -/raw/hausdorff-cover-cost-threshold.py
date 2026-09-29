"""Costs of specific Cantor interval covers; not minimized Hausdorff content."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.4), layout="constrained")
    d = np.log(2) / np.log(3)
    levels = np.arange(0, 19)
    for exponent, color, label in [
        (.4, "#bd632c", "s = 0.4 (below d)"),
        (d, "#167e8d", r"$s=d=\log 2/\log 3$"),
        (1., "#6d61a2", "s = 1 (above d)"),
    ]:
        cost = np.exp(levels * (np.log(2) - exponent * np.log(3)))
        assert np.allclose(cost, 2. ** levels * (3. ** (-levels)) ** exponent)
        if exponent == d:
            assert np.allclose(cost, 1)
        axes[0].semilogy(levels, cost, color=color, lw=2.5, marker="o", markersize=3, label=label)
    axes[0].set(xlabel="Construction level n", ylabel=r"Chosen-cover cost $2^n(3^{-n})^s$",
                xticks=[0, 3, 6, 9, 12, 15, 18])
    axes[0].set_title("A change of exponent reverses the trend", fontsize=14)
    axes[0].legend(loc="upper left", fontsize=10)
    axes[0].grid(alpha=.2)
    x = np.linspace(0, 1, 400)
    axes[1].plot(x, x, color="#6d61a2", lw=2.5, label="Uniform mass on [0, 1]")
    # Exact cumulative distribution of uniform mass on level-7 Cantor intervals.
    intervals = [(0., 1.)]
    for _ in range(7):
        intervals = [(a + off * (b - a) / 3, a + (off + 1) * (b - a) / 3)
                     for a, b in intervals for off in (0, 2)]
    knots = np.unique([0., 1.] + [v for interval in intervals for v in interval])
    cdf = np.zeros_like(knots)
    for a, b in intervals:
        cdf += np.clip((knots - a) / (b - a), 0, 1) / len(intervals)
    assert np.all(np.diff(cdf) >= -1e-12) and np.isclose(cdf[-1], 1)
    assert np.isclose(np.interp(1 / 3, knots, cdf), .5)
    assert np.isclose(np.interp(2 / 3, knots, cdf), .5)
    axes[1].plot(knots, cdf, color="#167e8d", lw=2.5, label="Cantor mass: level-7 approximation")
    axes[1].axvspan(1 / 3, 2 / 3, color="#e5ecee")
    axes[1].text(.5, .18, "No mass in\nmiddle third", ha="center", fontsize=11)
    axes[1].set(xlim=(0, 1), ylim=(0, 1.03), xlabel="Position x", ylabel="Accumulated probability mass",
                xticks=[0, 1 / 3, 2 / 3, 1], xticklabels=["0", "1/3", "2/3", "1"])
    axes[1].set_title("Mass is shared equally at every split", fontsize=14)
    axes[1].legend(loc="upper left", fontsize=9)
    axes[1].grid(alpha=.18)
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("The Cantor exponent balances shrinking covers and distributed mass", fontsize=16)
    fig.get_layout_engine().set(rect=(0, .09, 1, .91))
    fig.text(.5, .035, "The plotted cover costs are upper bounds. A mass-distribution argument supplies the lower bound.",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
