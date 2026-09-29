"""Compare unnormalized Gamma integral kernels, including their total areas.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write an opaque white PNG to the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0, 12, 1201)
    fig, axes = plt.subplots(1, 3, figsize=(9.0, 3.9), dpi=130,
                             sharex=True, sharey=True, facecolor="white")
    for ax, shape, area, color in zip(axes, [1, 2, 4], [1, 1, 6],
                                    ["#2866a3", "#25816b", "#b84f24"]):
        kernel = t ** (shape - 1) * np.exp(-t)
        ax.set_facecolor("white")
        ax.fill_between(t, kernel, color=color, alpha=0.22)
        ax.plot(t, kernel, color=color, lw=2.2)
        ax.set(xlim=(0, 12), ylim=(0, 1.52), xticks=[0, 3, 6, 9, 12],
               xlabel=r"Integration variable $t$",
               title=rf"$s={shape}$: total area $\Gamma({shape})={area}$")
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel(r"Kernel $t^{s-1}e^{-t}$")
    fig.suptitle("Gamma integral kernels: divide by the total area for a density",
                 fontsize=12)
    fig.text(0.5, 0.015, r"Unit rate; shaded range ends at 12, but total areas integrate to infinity.",
             ha="center", fontsize=9, color="#444444")
    fig.tight_layout(rect=(0, 0.065, 1, 0.94))
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
