"""Plot an exact scalar Gaussian update for two measurement variances.

Run from the desired output directory; writes a white, opaque PNG there.
Tested with the Python/numpy/matplotlib versions in pyproject.toml.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def density(x, mean, variance):
    return np.exp(-0.5 * (x - mean) ** 2 / variance) / np.sqrt(
        2 * np.pi * variance
    )


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    x = np.linspace(0, 23, 2401)
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 5.0), dpi=100, sharey=True)
    prior_mean, prior_variance, observation = 10.0, 4.0, 14.0
    for ax, measurement_variance in zip(axes, (1.0, 16.0), strict=True):
        gain = prior_variance / (prior_variance + measurement_variance)
        posterior_mean = prior_mean + gain * (observation - prior_mean)
        posterior_variance = (1 - gain) * prior_variance
        ax.plot(x, density(x, prior_mean, prior_variance), color="#2867a0",
                linewidth=2.3, label="Prediction: N(10, 4)")
        ax.plot(x, density(x, observation, measurement_variance),
                color="#27835f", linewidth=2.0, linestyle="--",
                label="Normalized likelihood")
        ax.plot(x, density(x, posterior_mean, posterior_variance),
                color="#cc6b20", linewidth=2.7,
                label=f"Posterior: N({posterior_mean:g}, {posterior_variance:g})")
        ax.axvline(observation, color="#666666", linestyle=":", linewidth=1.4)
        ax.set_title(f"Measurement variance R = {measurement_variance:g}"
                     f"\nGain K = {gain:g}")
        ax.set_xlim(0, 23)
        ax.set_ylim(0, 0.49)
        ax.set_xlabel("Scalar state x (illustrative units)")
        ax.grid(alpha=0.16)
        ax.legend(loc="upper left", fontsize=9.5, framealpha=0.95)
        ax.annotate(f"Posterior mean {posterior_mean:g}",
                    xy=(posterior_mean, 0), xytext=(posterior_mean, 0.055),
                    ha="center", color="#995017",
                    arrowprops={"arrowstyle": "->", "color": "#995017"})
    axes[0].set_ylabel("Density per state unit")
    fig.suptitle("The value 14 matters more when its measurement is precise",
                 fontsize=15, y=0.98)
    fig.text(0.5, 0.04,
             "The observation is not a known true state. "
             "Variances are in squared state units.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.98, top=0.80, bottom=0.19, wspace=0.13)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
