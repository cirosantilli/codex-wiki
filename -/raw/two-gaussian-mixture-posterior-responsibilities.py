"""Analytic latent-label probabilities; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-2, 2, 1601)
    r2 = 1 / (1 + 0.5 * np.exp(-4 * x))
    r1 = 1 - r2
    boundary = -np.log(2) / 4
    point = np.log(2) / 4
    fig, ax = plt.subplots(figsize=(8.4, 4.8), dpi=100, facecolor="white")
    ax.plot(x, r1, color="#007b91", lw=2.6, label="r₁(x): posterior for component 1")
    ax.plot(x, r2, color="#c65c22", lw=2.6, label="r₂(x): posterior for component 2")
    ax.axhline(1 / 3, color="#007b91", lw=1.3, linestyle=":")
    ax.axhline(2 / 3, color="#c65c22", lw=1.3, linestyle=":")
    ax.text(-1.94, 1 / 3 + 0.025, "π₁ = ⅓", color="#007b91", fontsize=10)
    ax.text(-1.94, 2 / 3 + 0.025, "π₂ = ⅔", color="#c65c22", fontsize=10)
    ax.axvline(boundary, color="#777777", lw=1.1, linestyle="--")
    ax.plot(boundary, 0.5, "o", color="#333333", ms=5)
    ax.annotate("Equal responsibilities\nx* = −log(2)/4 ≈ −0.1733",
                xy=(boundary, 0.5), xytext=(0.4, 0.45), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.plot([0, point], [2 / 3, 4 / 5], "o", color="#c65c22", ms=5)
    ax.annotate("r₂(0) = ⅔", xy=(0, 2 / 3), xytext=(-1.08, 0.84),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.annotate("r₂(log(2)/4) = ⅘", xy=(point, 4 / 5), xytext=(0.72, 0.72),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.set(xlim=(-2, 2), ylim=(-0.02, 1.02), xlabel="Value x (label unobserved)",
           ylabel="Probability of component label", title="Learning x changes the membership probabilities")
    ax.set_xticks(np.arange(-2, 2.1, 0.5))
    ax.grid(color="#e5e5e5", lw=0.6)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_facecolor("white")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.19),
              ncol=2, fontsize=9.5, frameon=False)
    fig.text(0.5, 0.035, "Stipulated Gaussian mixture: weights ⅓ and ⅔, means −2 and +2, variances 1.",
             ha="center", fontsize=9.5)
    fig.subplots_adjust(left=0.10, right=0.97, bottom=0.27, top=0.90)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
