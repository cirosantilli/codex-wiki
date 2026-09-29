"""Original Haar projection comparison, saved as an opaque PNG in CWD.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from math import erf, pi, sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-3, 3, 1000)
    density = np.exp(-x**2 / 2) / sqrt(2 * pi)
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 3.7), dpi=100)
    for ax, j in zip(axes, (0, 2, 4)):
        width = 2.0**(-j)
        edges = np.arange(-3, 3 + width / 2, width)
        cdf = np.array([(1 + erf(t / sqrt(2))) / 2 for t in edges])
        heights = np.diff(cdf) / width
        if not np.isclose(np.sum(heights) * width, cdf[-1] - cdf[0]):
            raise ValueError("Projection mass does not equal density mass in the view")
        ax.stairs(heights, edges, color="#d96d20", lw=1.8, label="Cell mean")
        ax.plot(x, density, color="#253c57", lw=1.8, label="Density")
        ax.set(xlim=(-3, 3), ylim=(0, 0.44), xlabel="x",
               title=f"j = {j}; cell width = {width:g}")
        ax.grid(alpha=0.2)
        ax.legend(fontsize=9, loc="upper right")
    axes[0].set_ylabel("Density / projected density")
    fig.suptitle("Haar projections of the standard normal density", fontsize=13)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "paper-33-haar-projections.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
