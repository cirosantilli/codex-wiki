"""Draw the solution set of x**3 - x + parameter = 0 and its folds.

Original mathematical illustration, not measured data or a benchmark.
Run from the output directory; dependency versions are in pyproject.toml.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-1.3, 1.3, 1001)
    lam = x - x**3
    fold_x = np.array([-1.0, 1.0]) / np.sqrt(3)
    fold_lam = 2 * fold_x / 3
    roots = np.sort(np.roots([1.0, 0.0, -1.0, 0.2]).real)
    assert np.max(np.abs(roots**3 - roots + 0.2)) < 1e-14
    assert np.max(np.abs(fold_x**3 - fold_x + fold_lam)) < 1e-14
    assert np.max(np.abs(3 * fold_x**2 - 1)) < 1e-14

    fig, ax = plt.subplots(figsize=(8.2, 5.0), dpi=120, layout="constrained")
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    ax.axhline(0, color="#cbd5e1", lw=0.8)
    ax.axvline(0, color="#cbd5e1", lw=0.8)
    ax.plot(x, lam, color="#176b8e", lw=2.5, label=r"$F=0$: $\lambda=x-x^3$")
    ax.axhline(0.2, color="#64748b", ls="--", lw=1.3, label=r"Fixed $\lambda=0.2$")
    ax.scatter(roots, np.full(3, 0.2), color="#64748b", s=40, zorder=4)
    ax.scatter(fold_x, fold_lam, color="#b45309", s=60, zorder=5, label="Folds")
    for left in (-1.10, -0.67, -0.05, 0.51, 0.98):
        right = left + 0.13
        ax.annotate("", xy=(right, right - right**3), xytext=(left, left - left**3),
                    arrowprops={"arrowstyle": "->", "color": "#176b8e", "lw": 2})
    ax.annotate(r"$(-1/\sqrt{3},\,-2/(3\sqrt{3}))$", xy=(fold_x[0], fold_lam[0]),
                xytext=(-1.21, -0.66), fontsize=11,
                arrowprops={"arrowstyle": "-", "color": "#b45309"})
    ax.annotate(r"$(1/\sqrt{3},\,2/(3\sqrt{3}))$", xy=(fold_x[1], fold_lam[1]),
                xytext=(0.10, 0.66), fontsize=11,
                arrowprops={"arrowstyle": "-", "color": "#b45309"})
    ax.set(xlabel=r"State $x$", ylabel=r"Parameter $\lambda$",
           xlim=(-1.3, 1.3), ylim=(-0.82, 0.82),
           title="A fold reverses the parameter direction; the curve continues")
    ax.legend(loc="lower right", fontsize=10, framealpha=1)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
