"""Exact discrete proportional updates over one fixed interval approach e."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    counts = np.arange(1, 1001)
    accumulated = np.exp(counts*np.log1p(1/counts))
    assert np.isclose(accumulated[0], 2)
    assert np.isclose(accumulated[1], 2.25)
    assert np.all(np.diff(accumulated) > 0)
    assert np.all(accumulated < np.e)
    logarithms = counts*np.log1p(1/counts)
    assert np.all(1/(1+1/counts) <= logarithms)
    assert np.all(logarithms <= 1)
    fig, ax = plt.subplots(figsize=(8.4, 4.7), dpi=120)
    blue, orange = "#176997", "#b55d20"
    ax.semilogx(counts, accumulated, color=blue, lw=2.5,
                label=r"$(1+1/n)^n$")
    ax.axhline(np.e, color=orange, ls="--", lw=1.7,
               label=r"Limit $e=2.7182818\ldots$")
    for n, label, xtext, ytext in [(1, "2", 1.5, 2.08), (2, "2.25", 3, 2.21),
                                  (10, "2.59374", 15, 2.49),
                                  (100, "2.70481", 80, 2.60),
                                  (1000, "2.71692", 360, 2.66)]:
        value=accumulated[n-1]
        ax.scatter(n, value, color=blue, s=35, zorder=4)
        ax.annotate(f"n = {n}: {label}", (n, value), xytext=(xtext, ytext), fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": blue})
    ax.set(xlim=(.85, 1200), ylim=(1.96, 2.79),
           xlabel="Number of equal updates n (logarithmic scale)",
           ylabel="Final value from a starting value of 1")
    ax.set_title("More steps, smaller increments, one fixed interval", fontsize=14, pad=13)
    ax.legend(loc="lower right", frameon=False, fontsize=11)
    ax.grid(alpha=.17, which="both")
    fig.text(.5, .025, "Each update multiplies the current value by 1 + 1/n; the total is below e at every finite n.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.095, right=.975, top=.86, bottom=.18)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
