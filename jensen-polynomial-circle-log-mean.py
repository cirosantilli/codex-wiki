"""Plot a polynomial's circle log-mean against natural log-radius.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; the opaque PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(7.2, 4.5))
    colors = ("#2878a6", "#c47a13", "#448655")
    intervals = ((0.08, 0.25), (0.25, 0.5), (0.5, 1.0))
    for slope, ((left, right), color) in enumerate(zip(intervals, colors)):
        x = np.linspace(np.log(left), np.log(right), 250)
        radius = np.exp(x)
        mean = np.log(3) + np.log(np.maximum(radius, 0.25)) + np.log(np.maximum(radius, 0.5))
        ax.plot(x, mean, color=color, linewidth=2.8,
                label=f"Slope {slope}: {slope} interior zero" + ("s" if slope != 1 else ""))
    for radius, height in ((0.25, np.log(3 / 8)), (0.5, np.log(3 / 4))):
        ax.axvline(np.log(radius), color="#888888", linestyle="--", linewidth=1)
        ax.scatter([np.log(radius)], [height], facecolors="white",
                   edgecolors="#333333", s=60, zorder=5)
        ax.text(np.log(radius) + 0.035, 1.12, f"R = {radius:g}",
                fontsize=10, rotation=90, va="top", color="#555555")
    for radius, height, offset in ((0.2, np.log(3 / 8), (-50, 28)),
                                    (0.4, np.log(3 / 5), (14, -24)),
                                    (0.75, np.log(27 / 16), (0, -38))):
        ax.scatter([np.log(radius)], [height], color="#222222", s=28, zorder=6)
        ax.annotate(f"R = {radius:g}\nL = {height:.6f}",
                    (np.log(radius), height), xytext=offset,
                    textcoords="offset points", fontsize=10,
                    ha="center", va="center")
    ax.set_title(r"Circle log-mean of $3(z-1/4)(z+1/2)$", fontsize=14, pad=12)
    ax.set_xlabel(r"Natural log-radius $x=\log R$", fontsize=11)
    ax.set_ylabel(r"Circle log-mean $L_f(R)$", fontsize=11)
    ax.set_xlim(np.log(0.08), 0.03)
    ax.set_ylim(-1.35, 1.25)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.18)
    ax.legend(loc="upper left", frameon=False, fontsize=10)
    fig.text(0.5, 0.025, "Open markers: excluded radii with a zero on the boundary circle.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
