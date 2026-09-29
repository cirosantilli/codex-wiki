"""Stipulated Gaussian mixture, no sampled data; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-6, 6, 2401)
    left = np.exp(-0.5 * (x + 2)**2) / (3 * np.sqrt(2 * np.pi))
    right = 2 * np.exp(-0.5 * (x - 2)**2) / (3 * np.sqrt(2 * np.pi))
    fig, ax = plt.subplots(figsize=(8.4, 4.8), dpi=100, facecolor="white")
    ax.fill_between(x, 0, left, color="#007b91", alpha=0.13)
    ax.fill_between(x, 0, right, color="#c65c22", alpha=0.13)
    ax.plot(x, left, color="#007b91", lw=2.5,
            label="⅓ φ(x + 2): component 1, area ⅓")
    ax.plot(x, right, color="#c65c22", lw=2.5,
            label="⅔ φ(x − 2): component 2, area ⅔")
    ax.plot(x, left + right, color="#222222", lw=2.3, linestyle="--",
            label="f(x): sum of the two weighted densities")
    x0 = 0.0
    lower = np.exp(-2) / (3 * np.sqrt(2 * np.pi))
    ax.plot([x0, x0], [0, lower], color="#007b91", lw=5)
    ax.plot([x0, x0], [lower, 3 * lower], color="#c65c22", lw=5)
    ax.plot(x0, 3 * lower, "o", color="#222222", ms=5)
    ax.annotate("At x = 0, add both contributions", xy=(0, 3 * lower),
                xytext=(-4.7, 0.22), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.set(xlim=(-6, 6), ylim=(0, 0.32), xlabel="Value x",
           ylabel="Probability density", title="Overlapping components, unequal weights")
    ax.set_xticks(np.arange(-6, 7, 2))
    ax.grid(color="#e5e5e5", lw=0.6)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_facecolor("white")
    ax.legend(loc="upper left", fontsize=10, frameon=False)
    fig.text(0.5, 0.035,
             "Stipulated model: means −2 and +2, variances 1. Analytic curves; no observed or fitted data.",
             ha="center", fontsize=9.5)
    fig.subplots_adjust(left=0.10, right=0.97, bottom=0.16, top=0.90)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
