"""Exact constructed ridge line fits; write the matching PNG to the CWD.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
The points are synthetic, and the curves show training fit only.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def fit(penalty):
    """Scalar centered solution for x=(0,1,2,3,4), y=(1,2,2,4,5)."""
    slope = 10.0 / (10.0 + np.asarray(penalty))
    intercept = 14.0 / 5.0 - 2.0 * slope
    rss = 4.0 / 5.0 + 10.0 * (1.0 - slope) ** 2
    return intercept, slope, rss


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, (ax_fit, ax_rss) = plt.subplots(
        1, 2, figsize=(10.5, 5.2), dpi=100, facecolor="white",
        gridspec_kw={"width_ratios": [1.1, 1]}, layout="constrained",
    )
    fig.suptitle("Ridge regression on five constructed points", fontsize=15)
    x = np.arange(5, dtype=float)
    y = np.array([1, 2, 2, 4, 5], dtype=float)
    colors = ["#185f9b", "#cf6425", "#6c4895"]
    xx = np.linspace(-0.2, 4.2, 150)
    for penalty, color, exact_rss in zip([0, 10, 30], colors, ["4/5", "33/10", "257/40"]):
        intercept, slope, rss = fit(penalty)
        prediction = intercept + slope * x
        assert np.isclose(np.sum((y - prediction) ** 2), rss)
        ax_fit.plot(xx, intercept + slope * xx, color=color, lw=2.2,
                    label=rf"$\lambda={penalty}$, slope ${slope:g}$")
        ax_rss.scatter([penalty], [rss], color=color, s=65, zorder=4)
        ax_rss.annotate(rf"$\lambda={penalty}$: RSS $={exact_rss}$",
                        (penalty, rss), xytext=(9, 10), textcoords="offset points",
                        fontsize=10, color=color)
    # Only the lambda=10 residuals are drawn to keep the fit panel readable.
    intercept, slope, _ = fit(10)
    ax_fit.vlines(x, np.minimum(y, intercept + slope * x),
                  np.maximum(y, intercept + slope * x), color=colors[1],
                  lw=1.5, linestyles="dotted", zorder=1)
    ax_fit.scatter(x, y, s=50, color="#222222", zorder=5, label="Constructed responses")
    ax_fit.scatter([2], [2.8], marker="+", color="#222222", s=140, lw=2, zorder=6)
    ax_fit.annotate(r"Mean point $(2,14/5)$", (2, 2.8), xytext=(-90, 35),
                    textcoords="offset points", arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax_fit.set(xlabel="Predictor x", ylabel="Response / fitted response",
               title="The free intercept preserves the mean", xlim=(-0.25, 4.25), ylim=(0.3, 5.5))
    ax_fit.set_xticks(range(5))
    ax_fit.legend(loc="lower right", fontsize=9, framealpha=1, facecolor="white")
    penalties = np.linspace(0, 55, 350)
    ax_rss.plot(penalties, fit(penalties)[2], color="#444444", lw=2)
    ax_rss.set(xlabel=r"Penalty $\lambda$ (summed RSS convention)",
               ylabel="Training residual sum of squares", xlim=(-2, 57), ylim=(0, 9.5),
               title="Shrinking the slope costs training fit")
    ax_rss.text(0.05, 0.91, r"RSS $=4/5+10(1-\widehat\beta_\lambda)^2$",
                transform=ax_rss.transAxes, fontsize=10)
    for ax in (ax_fit, ax_rss):
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
