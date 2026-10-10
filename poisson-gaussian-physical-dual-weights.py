"""Original Gaussian sample diagrams; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes this script's basename with a .png suffix to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 2, figsize=(10, 6.6), layout="constrained")
    fig.patch.set_facecolor("white")
    points = np.arange(-8, 9)
    grid = np.linspace(-8.5, 8.5, 1701)
    for row, a in enumerate((0.04, 25.0)):
        for col, (b, scale, color, label) in enumerate((
                (a, 1.0, "#1864ab", "Physical"),
                (1 / a, a ** -0.5, "#b45b08", "Dual"))):
            ax = axes[row, col]
            weights = scale * np.exp(-np.pi * b * points ** 2)
            ax.plot(grid, scale * np.exp(-np.pi * b * grid ** 2),
                    color=color, alpha=0.35, linewidth=1.8)
            stems = ax.stem(points, weights, basefmt=" ")
            plt.setp(stems.markerline, color=color, markersize=4.5)
            plt.setp(stems.stemlines, color=color, linewidth=1.5)
            ax.set(xlim=(-8.5, 8.5), ylim=(-0.04 * scale, 1.15 * scale),
                   xlabel="Integer position n" if col == 0 else "Integer frequency k",
                   ylabel="Summand weight", title=f"{label} samples, a = {a:g}")
            ax.set_xticks(np.arange(-8, 9, 2))
            ax.grid(alpha=0.16)
            if b > 1:
                ax.text(0.03, 0.90, f"Zero weight = {scale:g}\n"
                        f"Each ±1 weight ≈ {scale * np.exp(-np.pi * b):.3g}",
                        transform=ax.transAxes, va="top", fontsize=10)
    fig.suptitle("Poisson summation exchanges broad and narrow Gaussian samples", fontsize=15)
    fig.supxlabel(r"Dots and stems are summands; faint curves guide the eye. "
                  r"$\widehat f_a(\xi)=a^{-1/2}e^{-\pi\xi^2/a}$", fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
