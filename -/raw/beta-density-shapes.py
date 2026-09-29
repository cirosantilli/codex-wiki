"""Render beta density shapes to cwd; tested with Python 3.14.4.

Uses the project's NumPy and Matplotlib dependencies. Singular densities are
evaluated only in the interior; their displayed area is calculated analytically.
"""

from math import asin, lgamma, pi, sqrt
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def beta_density(x, alpha, beta):
    """Evaluate the normalized density at strictly interior coordinates."""
    log_normalizer = lgamma(alpha) + lgamma(beta) - lgamma(alpha + beta)
    return np.exp((alpha - 1) * np.log(x)
                  + (beta - 1) * np.log1p(-x) - log_normalizer)


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, (regular, singular) = plt.subplots(
        1, 2, figsize=(11.5, 5.6), dpi=120, facecolor="white")
    x = np.linspace(0.001, 0.999, 4001)
    for alpha, beta, color, style, label in [
        (1, 1, "#596674", "--", r"Beta(1, 1): $f(x)=1$"),
        (2, 2, "#0072b2", "-", r"Beta(2, 2): $6x(1-x)$"),
        (2, 5, "#d55e00", "-.", r"Beta(2, 5): $30x(1-x)^4$"),
    ]:
        # These three continuous extensions have finite exact endpoint values.
        endpoint = 1 if alpha == beta == 1 else 0
        regular.plot(np.r_[0, x, 1],
                     np.r_[endpoint, beta_density(x, alpha, beta), endpoint],
                     color=color, linestyle=style, lw=2.5, label=label)
    regular.set(title="Flat, central, and asymmetric shapes",
                xlim=(0, 1), ylim=(0, 2.7))
    regular.legend(loc="upper right", fontsize=10.5, framealpha=1)

    color = "#007c68"
    singular.plot(x, beta_density(x, 0.5, 0.5), color=color, lw=2.5,
                  label=r"Beta(½, ½): $1/(\pi\sqrt{x(1-x)})$")
    central_x = np.linspace(0.1, 0.9, 2001)
    singular.fill_between(central_x, beta_density(central_x, 0.5, 0.5),
                          color=color, alpha=0.22)
    central_area = 1 - 4 * asin(sqrt(0.1)) / pi
    singular.text(0.5, 4.9,
                  "Shaded interval: 0.1 < X < 0.9\n"
                  f"Exact probability = {central_area:.4f}",
                  ha="center", color=color, fontsize=12)
    singular.text(0.5, 3.0,
                  "Both endpoint densities diverge;\n"
                  "neither endpoint has probability mass",
                  ha="center", fontsize=11)
    for edge in [0.001, 0.999]:
        singular.annotate("", xy=(edge, 11.1), xytext=(edge, 10.2),
                          arrowprops={"arrowstyle": "->", "color": color})
    singular.set(title="Arcsine: an integrable boundary singularity",
                 xlim=(0, 1), ylim=(0, 11.6))
    singular.legend(loc="upper center", fontsize=11, framealpha=1)
    for ax in [regular, singular]:
        ax.set(xlabel="Outcome x", ylabel="Probability density f(x)")
        ax.grid(color="#e6eaed", zorder=0)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Beta distributions: probability is area, not height", fontsize=16)
    fig.text(0.5, 0.035,
             "Each full density has total area 1.\n"
             "Right curve shown only for 0.001 ≤ x ≤ 0.999; "
             "the cutoff is for plotting, not renormalization.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.16,
                        top=0.85, wspace=0.28)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
