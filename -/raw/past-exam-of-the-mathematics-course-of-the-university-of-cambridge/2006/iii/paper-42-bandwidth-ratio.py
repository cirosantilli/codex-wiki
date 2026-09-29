"""Normal-density pointwise/global bandwidth ratio.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes an opaque PNG basename in the caller's current directory.
The caller may supply MPLCONFIGDIR; this script does not override it.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def ratio(x):
    return ((3 * np.sqrt(2) / 8) * np.exp(x * x / 2) / (x * x - 1) ** 2) ** 0.2


def main():
    fig, ax = plt.subplots(figsize=(6.0, 3.7), dpi=160, facecolor="white")
    ax.set_facecolor("white")
    for left, right in [(-4, -1.0005), (-0.9995, 0.9995), (1.0005, 4)]:
        x = np.unique(np.r_[np.linspace(left, right, 1000),
                             [t for t in (-np.sqrt(5), 0, np.sqrt(5)) if left <= t <= right]])
        ax.plot(x, ratio(x), color="#225ea8", linewidth=1.8)
    minima = np.array([-np.sqrt(5), np.sqrt(5)])
    rmin = ratio(minima[0])
    ax.scatter(minima, ratio(minima), color="#a63603", zorder=5)
    ax.axhline(rmin, color="#a63603", linestyle=":", linewidth=1)
    for x in (-1, 1):
        ax.axvline(x, color="0.55", linestyle="--", linewidth=1)
    ax.annotate(r"Global minimum at $x=\pm\sqrt{5}$", xy=(np.sqrt(5), rmin),
                xytext=(0.6, 1.48), arrowprops={"arrowstyle": "->", "color": "#a63603"},
                color="#a63603", fontsize=9)
    ax.set(xlim=(-4, 4), ylim=(0.7, 2.6), xlabel=r"Position $x$",
           ylabel=r"$h_{\mathrm{AMSE}}(x)/h_{\mathrm{AMISE}}$",
           title="Local bandwidth relative to the global optimum")
    ax.grid(alpha=0.18)
    fig.tight_layout()
    fig.savefig(Path("paper-42-bandwidth-ratio.png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
