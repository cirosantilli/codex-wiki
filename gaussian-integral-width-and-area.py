"""Gaussian widths, full-line areas, and normalized densities; PNG to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-3, 3, 1000)
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.6), dpi=120)
    fig.patch.set_facecolor("white")
    for a, color in [(1, "#2768a6"), (4, "#238367")]:
        kernel = np.exp(-a * x*x)
        axes[0].plot(x, kernel, color=color, lw=2.3,
                     label=rf"$a={a}$: area $\sqrt{{\pi/{a}}}$")
        axes[0].fill_between(x, kernel, color=color, alpha=0.12)
        density = np.sqrt(a/np.pi) * kernel
        axes[1].plot(x, density, color=color, lw=2.3,
                     label=rf"$a={a}$: area $1$")
        axes[1].fill_between(x, density, color=color, alpha=0.12)
    for ax in axes:
        ax.set_facecolor("white")
        ax.set(xlim=(-3, 3), ylim=(0, 1.25), xlabel="x")
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(loc="upper right", frameon=False, fontsize=10)
    axes[0].set(ylabel="Height", title=r"Peak height stays 1: $e^{-ax^2}$")
    axes[1].set(title=r"Area stays 1: $\sqrt{a/\pi}\,e^{-ax^2}$")
    fig.suptitle("Narrowing and normalization are different operations",
                 fontsize=14)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
