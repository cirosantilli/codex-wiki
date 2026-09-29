"""Render fixed-mean beta concentrations to cwd; tested with Python 3.14.4.

Uses only the project's NumPy and Matplotlib dependencies and the standard
library. The density normalization is evaluated using log-gamma arithmetic.
"""

from math import lgamma
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def beta_density(x, alpha, beta):
    log_normalizer = lgamma(alpha) + lgamma(beta) - lgamma(alpha + beta)
    return np.exp((alpha - 1) * np.log(x)
                  + (beta - 1) * np.log1p(-x) - log_normalizer)


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, (density, variance) = plt.subplots(
        1, 2, figsize=(11.5, 5.6), dpi=120, facecolor="white")
    mean = 0.3
    x = np.linspace(0.00001, 0.99999, 6001)
    for concentration, color, style in [
        (5, "#0072b2", "-"),
        (20, "#d55e00", "--"),
        (80, "#007c68", "-."),
    ]:
        alpha = mean * concentration
        beta = (1 - mean) * concentration
        value = mean * (1 - mean) / (concentration + 1)
        density.plot(np.r_[0, x, 1],
                     np.r_[0, beta_density(x, alpha, beta), 0],
                     color=color, linestyle=style, lw=2.5,
                     label=f"κ = {concentration}: Beta({alpha:g}, {beta:g})")
        variance.scatter(concentration, value, color=color, s=65, zorder=4)
        variance.annotate(f"κ = {concentration}\nv = {value:.8g}",
                          xy=(concentration, value),
                          xytext=(12 if concentration < 80 else -12, 12),
                          textcoords="offset points",
                          ha="left" if concentration < 80 else "right",
                          fontsize=11, color=color)
    density.axvline(mean, color="#596674", lw=1.4, linestyle=":")
    density.annotate("Mean = 0.3", xy=(mean, 6.4), xytext=(0.44, 6.4),
                     fontsize=11, va="center",
                     arrowprops={"arrowstyle": "->", "color": "#596674"})
    density.set(title="Same mean; increasing concentration",
                xlabel="Outcome x", ylabel="Probability density f(x)",
                xlim=(0, 1), ylim=(0, 8.6))
    density.legend(loc="upper right", fontsize=10.5, framealpha=1)
    kappa = np.linspace(5, 85, 2001)
    variance.plot(kappa, mean * (1 - mean) / (kappa + 1),
                  color="#596674", lw=2)
    variance.text(0.43, 0.61, r"$v=\frac{0.3(1-0.3)}{\kappa+1}$",
                  transform=variance.transAxes, fontsize=19)
    variance.set(title="Spread decreases as κ increases",
                 xlabel="Concentration κ = α + β", ylabel="Variance v",
                 xlim=(0, 90), ylim=(0, 0.042))
    for ax in [density, variance]:
        ax.grid(color="#e6eaed")
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Beta mean and concentration: α = 0.3κ, β = 0.7κ", fontsize=16)
    fig.text(0.5, 0.035,
             "Each density integrates to 1. "
             "A taller, narrower curve concentrates probability near the same mean.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.16,
                        top=0.85, wspace=0.3)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
