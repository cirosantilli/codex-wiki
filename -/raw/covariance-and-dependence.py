"""Plot exact finite distributions, contrasting covariance and dependence."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def covariance(x, y):
    return np.mean((x - np.mean(x)) * (y - np.mean(y)))


def main():
    grid = np.array([-1.0, 0.0, 1.0])
    x = np.repeat(grid, 3)
    z = np.tile(grid, 3)
    y = 2 * x + z
    assert np.isclose(np.var(x), 2 / 3)
    assert np.isclose(covariance(x, y), 4 / 3)
    assert np.isclose(np.var(y), 10 / 3)
    assert np.isclose(np.var(x + y), 20 / 3)
    assert np.isclose(np.var(x - y), 4 / 3)
    assert np.isclose(np.corrcoef(x, y)[0, 1], 2 / np.sqrt(5))
    assert np.isclose(covariance(grid, grid**2), 0)
    assert np.isclose(np.var(grid**2), 2 / 9)
    assert np.isclose(np.corrcoef([1, 2, 3, 4], [2, 1, 4, 3])[0, 1], 0.6)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 8.3), dpi=120, facecolor="white")
    cases = [(x, y, r"$Y=2X+Z$", "Positive linear association", "#206a9d", (-3.5, 3.5)),
             (x, -2 * x + z, r"$Y=-2X+Z$", "Negative linear association", "#be7521", (-3.5, 3.5)),
             (x, z, r"$Y=Z$", "Independent variables", "#2f8a68", (-1.5, 1.5)),
             (grid, grid**2, r"$Y=X^2$", "Dependent, but uncorrelated", "#8255a2", (-0.2, 1.5))]
    for ax, (xs, ys, formula, title, color, ylim) in zip(axes.flat, cases):
        cov = covariance(xs, ys)
        corr = np.corrcoef(xs, ys)[0, 1]
        ax.axvline(np.mean(xs), color="#b4bcc2", lw=1)
        ax.axhline(np.mean(ys), color="#b4bcc2", lw=1)
        if len(xs) == 3:
            curve = np.linspace(-1.12, 1.12, 300)
            ax.plot(curve, curve**2, color=color, lw=1.5, alpha=0.45)
        ax.scatter(xs, ys, s=85, color=color, edgecolor="white", linewidth=1, zorder=4)
        ax.set(xlim=(-1.4, 1.4), ylim=ylim, xlabel="X", ylabel="Y",
               title=title + "\n" + formula, xticks=[-1, 0, 1])
        ax.text(0.5, -0.29, f"Cov(X, Y) = {cov:.3f};  correlation = {corr:.3f}",
                transform=ax.transAxes, fontsize=11, ha="center")
        ax.grid(color="#e7eaed")
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Exact distributions: shared variation, independence, and a nonlinear rule", fontsize=15)
    fig.subplots_adjust(left=0.09, right=0.98, top=0.865, bottom=0.12, wspace=0.28, hspace=0.9)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
