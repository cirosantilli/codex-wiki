"""Show each half-plane and their incompatibility; save PNG to cwd (Python 3.14)."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    c = np.array([[-1, 0], [0, -1], [1, 1]])
    d = np.array([-1, -1, 1])
    multipliers = np.ones(3, dtype=int)
    assert np.array_equal(c.T @ multipliers, [0, 0])
    assert d @ multipliers == -1
    pair_points = np.array([[1, 1], [1, 0], [0, 1]])
    for point, rows in zip(pair_points, [(0, 1), (0, 2), (1, 2)]):
        satisfied = c @ point <= d
        assert np.all(satisfied[list(rows)]) and not np.all(satisfied)
    assert np.array_equal(np.column_stack((c, -c, np.eye(3, dtype=int))).T
                          @ multipliers, [0, 0, 0, 0, 1, 1, 1])
    upper_bound_multipliers = np.array([0, 0, 1])
    bound_rhs = np.array([0, 0, 1])
    assert np.array_equal(c.T @ upper_bound_multipliers, [1, 1])
    assert bound_rhs @ upper_bound_multipliers == 1
    assert np.all(c @ np.array([1, 0]) <= bound_rhs)

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(2, 2, figsize=(9, 8), dpi=120, facecolor="white")
    lo, hi = -1, 3
    grid = np.linspace(lo, hi, 401)
    xx, yy = np.meshgrid(grid, grid)
    masks = [xx >= 1, yy >= 1, xx + yy <= 1]
    colors = ["#397ca5", "#458667", "#be633c"]
    titles = [r"First requirement: $x\geq1$", r"Second requirement: $y\geq1$",
              r"Third requirement: $x+y\leq1$", "All three: no common point"]

    def shade(ax, mask, color):
        ax.contourf(xx, yy, mask.astype(int), levels=[0.5, 1.5],
                    colors=[color], alpha=0.18, zorder=0)

    for i, (ax, title) in enumerate(zip(axes.flat, titles)):
        if i < 3:
            shade(ax, masks[i], colors[i])
        else:
            first_two = masks[0] & masks[1]
            assert not np.any(first_two & masks[2])
            shade(ax, first_two, "#397ca5")
            shade(ax, masks[2], colors[2])
        if i in (0, 3):
            ax.axvline(1, color=colors[0], lw=2)
        if i in (1, 3):
            ax.axhline(1, color=colors[1], lw=2)
        if i in (2, 3):
            ax.plot(grid, 1 - grid, color=colors[2], lw=2)
        ax.axvline(0, color="#c2c7cc", lw=0.8, zorder=0)
        ax.axhline(0, color="#c2c7cc", lw=0.8, zorder=0)
        ax.set(xlim=(lo, hi), ylim=(lo, hi), aspect="equal", title=title,
               xlabel="x", ylabel="y", xticks=[-1, 0, 1, 2, 3], yticks=[-1, 0, 1, 2, 3])
        ax.spines[["top", "right"]].set_visible(False)
    final = axes[1, 1]
    final.text(1.22, 2.48, r"$x\geq1,\ y\geq1$" + "\n" + r"so $x+y\geq2$",
               color=colors[0], fontsize=11)
    final.text(-0.72, -0.72, r"$x+y\leq1$", color=colors[2], fontsize=11)
    final.scatter(pair_points[:, 0], pair_points[:, 1], s=28, color="#343c42", zorder=4)
    final.annotate("(1,1)", xy=(1, 1), xytext=(1.16, 1.28), fontsize=9)
    final.annotate("(1,0)", xy=(1, 0), xytext=(1.24, 0.06), fontsize=9)
    final.annotate("(0,1)", xy=(0, 1), xytext=(-0.77, 1.2), fontsize=9)
    fig.suptitle("Each shaded half-plane is possible on its own", y=0.98, fontsize=16)
    fig.text(0.5, 0.065, r"Multipliers $(1,1,1)$:  $(-x)+(-y)+(x+y)\leq-1-1+1$",
             ha="center", fontsize=13)
    fig.text(0.5, 0.025, r"The variables cancel:  $0\leq-1$  is impossible",
             ha="center", fontsize=13, color="#9b3827")
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.91, hspace=0.38, wspace=0.2)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
