"""Draw exact Laplace/normal densities and tails with matched variance.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from the desired output directory; the PNG is written to the CWD.
"""

from math import erfc, pi, sqrt
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    blue, orange = "#176ca4", "#ce6010"
    x = np.linspace(-6, 6, 2401)
    r = np.linspace(0, 8, 801)
    # Laplace b=1 and normal sigma=sqrt(2), both with variance 2.
    laplace_pdf = np.exp(-np.abs(x)) / 2
    normal_pdf = np.exp(-x**2 / 4) / (2 * sqrt(pi))
    laplace_tail = np.exp(-r)
    normal_tail = np.array([erfc(float(t) / 2) for t in r])

    fig, (density, tail) = plt.subplots(1, 2, figsize=(10, 4.7), dpi=120)
    fig.patch.set_facecolor("white")
    fig.suptitle("Same variance, different peaks and tails", fontsize=16, y=0.98)
    fig.text(0.5, 0.90, r"Both centered at 0; variance $=2$", ha="center")
    for ax in (density, tail):
        ax.set_facecolor("white")
        ax.grid(alpha=0.22)
        ax.spines[["top", "right"]].set_visible(False)

    density.plot(x, laplace_pdf, color=blue, lw=2.6, label=r"Laplace: $b=1$")
    density.plot(x, normal_pdf, color=orange, lw=2.3, ls="--",
                 label=r"Normal: $\sigma=\sqrt{2}$")
    density.set(title="Probability density", xlabel=r"Value $x$",
                ylabel=r"Density $f(x)$", xlim=(-6, 6), ylim=(0, 0.57))
    density.legend(loc="upper right", frameon=False, fontsize=10)
    density.annotate("Finite corner,\nno point mass", xy=(0, 0.5),
                     xytext=(-5.6, 0.43), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": blue})

    tail.semilogy(r, laplace_tail, color=blue, lw=2.6, label=r"$e^{-r}$")
    tail.semilogy(r, normal_tail, color=orange, lw=2.3, ls="--",
                  label=r"$\mathrm{erfc}(r/2)$")
    tail.set(title="Two-sided tail probability (log scale)", xlabel=r"Distance $r$",
             ylabel=r"$\mathbb{P}(|X|>r)$", xlim=(0, 8), ylim=(1e-8, 1.5))
    tail.set_yticks([1, 1e-2, 1e-4, 1e-6, 1e-8])
    tail.legend(loc="lower left", frameon=False, fontsize=11)
    tail.text(4.9, 0.012, "Laplace", color=blue)
    tail.text(5.8, 1.2e-6, "Normal", color=orange)

    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.14, top=0.79, wspace=0.32)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
