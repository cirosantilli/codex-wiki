"""Plot normal location and scale; write an opaque basename PNG to CWD.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def density(x, mean, sigma):
    return np.exp(-0.5 * ((x - mean) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    x = np.linspace(-7, 7, 2801)
    colors = ["#b5531d", "#246bce", "#39834b"]
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.2, 5.1), dpi=100)
    for sigma, color in zip([0.5, 1, 2], colors):
        left.plot(x, density(x, 0, sigma), color=color, linewidth=2.5,
                  label=rf"$\sigma={sigma:g}$; peak {density(0, 0, sigma):.3f}")
    left.set(xlim=(-6, 6), ylim=(0, 0.86), xlabel="Outcome x",
             ylabel="Density (per unit of x)")
    left.set_title(r"Scale: $\mu=0$, three different widths", fontsize=13)
    left.legend(frameon=False, fontsize=10.5, loc="upper right")
    for mean, color in zip([-2, 0, 2], colors):
        right.plot(x, density(x, mean, 1), color=color, linewidth=2.5,
                   label=rf"$\mu={mean:g}$")
        right.axvline(mean, color=color, linestyle=":", alpha=0.5, linewidth=1)
    right.set(xlim=(-6, 6), ylim=(0, 0.46), xlabel="Outcome x",
              ylabel="Density (per unit of x)")
    right.set_title(r"Location: $\sigma=1$, three different centers", fontsize=13)
    right.legend(frameon=False, fontsize=11, loc="upper right")
    for ax in (left, right):
        ax.grid(alpha=0.17)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Normal distributions: moving and stretching one shape",
                 fontsize=16, weight="bold", y=0.97)
    fig.text(0.5, 0.035, "Each curve has total area 1 on the whole real line; only a finite window is shown.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.17, top=0.80, wspace=0.29)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
