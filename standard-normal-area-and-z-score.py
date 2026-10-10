"""Show corresponding normal areas and z-scores; opaque basename PNG to CWD.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def phi(z):
    return np.exp(-z**2 / 2) / np.sqrt(2 * np.pi)


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    blue, orange = "#246bce", "#bf5520"
    z = np.linspace(-4, 4, 1601)
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.7), dpi=100)
    for ax, mean, sigma, title in zip(
        axes, [100, 0], [15, 1],
        [r"Toy measurement: $X\sim N(100,15^2)$", r"Standardized: $Z=(X-100)/15\sim N(0,1)$"],
    ):
        x, y = mean + sigma * z, phi(z) / sigma
        ax.plot(x, y, color="#24384b", linewidth=2.4)
        for lower, upper, color in [(-1, 0, blue), (0, 1, orange)]:
            section = np.linspace(lower, upper, 301)
            ax.fill_between(mean + sigma * section, phi(section) / sigma,
                            color=color, alpha=0.52)
        for threshold in [-1, 0, 1]:
            ax.vlines(mean + sigma * threshold, 0, phi(threshold) / sigma,
                      colors="#24384b", linestyles=":", linewidth=1)
        ax.set_title(title, fontsize=12.5, pad=12)
        ax.set(xlim=(mean - 4 * sigma, mean + 4 * sigma),
               ylim=(0, 0.52 / sigma))
        ax.set_xticks(mean + sigma * np.arange(-3, 4))
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
        ax.text(0.5, 0.92, "Blue + orange: 0.6826894921", transform=ax.transAxes,
                ha="center", fontsize=11, color="#24384b")
        ax.text(0.5, 0.85, "Orange alone: 0.3413447461", transform=ax.transAxes,
                ha="center", fontsize=11, color=orange)
    axes[0].set(xlabel="Measurement x (unspecified units)",
                ylabel="Density (per measurement unit)")
    axes[1].set(xlabel="Standard score z (dimensionless)", ylabel=r"Standard normal density $\phi(z)$")
    fig.suptitle("Same probabilities, different coordinates and density heights",
                 fontsize=15.5, weight="bold", y=0.975)
    fig.text(0.5, 0.14, r"$x=85,100,115\ \longleftrightarrow\ z=-1,0,1$     |     $f_X(x)=\phi(z)/15$,  $dx=15\,dz$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.07, r"Areas are probabilities. A single outcome has no area: $P(X=100)=P(Z=0)=0$.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.085, right=0.975, bottom=0.28, top=0.80, wspace=0.29)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
