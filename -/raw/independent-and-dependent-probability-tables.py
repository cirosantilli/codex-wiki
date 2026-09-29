"""Joint laws versus products of marginals; tested with Python 3.14.4.

Uses the repository's matplotlib/numpy environment. Writes the PNG to CWD.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def fraction(value):
    return str(Fraction(float(value)).limit_denominator(100))


def draw_table(ax, matrix, x_values, title):
    """Show every mass plus both marginals and the grand total."""
    rows, columns = matrix.shape
    ax.axis("off")
    ax.set_title(title, fontsize=13, pad=10)
    data = []
    for i in range(rows):
        data.append([fraction(v) for v in matrix[i]] + [fraction(matrix[i].sum())])
    data.append([fraction(v) for v in matrix.sum(axis=0)] + ["1"])
    table = ax.table(
        cellText=data,
        rowLabels=[f"X = {x}" for x in x_values] + ["P(Y = y)"],
        colLabels=[f"Y = {y}" for y in range(columns)] + ["P(X = x)"],
        cellLoc="center",
        rowLoc="center",
        bbox=[0.18, 0.03, 0.81, 0.86],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#c3ccd6")
        if row == 0 or col == -1:
            cell.set_facecolor("#edf1f6")
        elif row == rows + 1 or col == columns:
            cell.set_facecolor("#edf6ed")
        else:
            value = matrix[row - 1, col]
            cell.set_facecolor(plt.cm.Blues(0.05 + 0.7 * value / 0.5))
        cell.set_text_props(color="#182332")


def main():
    independent = np.full((2, 2), 0.25)
    identical = np.diag([0.5, 0.5])
    squared = np.array([[0, 1 / 3], [1 / 3, 0], [0, 1 / 3]])
    cases = [
        (independent, [0, 1], "Independent fair bits: all four cells factor", 0),
        (identical, [0, 1], "Same fair bit, Y = X: matching marginals, different joint law", 0.25),
        (squared, [-1, 0, 1], "X uniform on {-1, 0, 1}, Y = X²: zero covariance, dependent", 0),
    ]
    plt.rcParams.update({"font.size": 12, "text.color": "#182332"})
    fig = plt.figure(figsize=(9.4, 9.2), facecolor="white")
    grid = fig.add_gridspec(6, 2, height_ratios=[0.3, 1, 0.3, 1, 0.3, 1.2],
                           hspace=0.30, wspace=0.18)
    for i, (joint, x_values, label, expected_covariance) in enumerate(cases):
        marginal_x = joint.sum(axis=1)
        marginal_y = joint.sum(axis=0)
        product = np.outer(marginal_x, marginal_y)
        assert np.isclose(joint.sum(), 1)
        assert np.isclose(product.sum(), 1)
        assert np.all(joint >= 0)
        assert np.allclose(product.sum(axis=1), marginal_x)
        assert np.allclose(product.sum(axis=0), marginal_y)
        x = np.array(x_values)
        y = np.arange(joint.shape[1])
        covariance = np.sum(joint * x[:, None] * y[None, :]) - (x @ marginal_x) * (y @ marginal_y)
        assert np.isclose(covariance, expected_covariance)
        assert np.allclose(joint, product) == (i == 0)
        heading = fig.add_subplot(grid[2 * i, :])
        heading.axis("off")
        heading.text(0.5, 0.5, label, ha="center", va="center", fontsize=12, weight="bold")
        draw_table(fig.add_subplot(grid[2 * i + 1, 0]), joint, x_values, "Actual joint probabilities")
        draw_table(fig.add_subplot(grid[2 * i + 1, 1]), product, x_values, "Product of the marginals")
    fig.suptitle("Independence requires equality in every joint cell", fontsize=17, weight="bold", y=0.98)
    fig.text(0.5, 0.02, "Blue: joint cells   •   Green: marginal totals   •   Each table sums to 1",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.04, right=0.98, bottom=0.065, top=0.94)
    fig.savefig(Path.cwd() / "independent-and-dependent-probability-tables.png",
                dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
