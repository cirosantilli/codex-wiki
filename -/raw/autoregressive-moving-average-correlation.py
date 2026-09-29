"""Compare exact ACFs; output the matching PNG to CWD.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    lags = np.arange(11)
    ma = np.zeros(len(lags))
    ma[0] = 1
    ma[1] = 0.7 / (1 + 0.7**2)
    cases = [
        (0.7**lags, r"AR(1): $\phi=0.7$", "Positive persistence", "#236ca0"),
        ((-0.7)**lags, r"AR(1): $\phi=-0.7$", "Alternating signs", "#b54b36"),
        (ma, r"MA(1): $\theta=0.7$", "Zero after lag one", "#288269"),
    ]
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(3, 1, figsize=(8.4, 7.8), dpi=120,
                             sharex=True, sharey=True, facecolor="white")
    for ax, (acf, title, note, color) in zip(axes, cases):
        ax.set_facecolor("white")
        ax.axhline(0, color="#65717a", linewidth=1)
        ax.vlines(lags, 0, acf, color=color, linewidth=3)
        ax.scatter(lags, acf, color=color, s=38, zorder=3)
        ax.set(title=title, ylabel=r"$\rho(h)$", ylim=(-0.88, 1.12),
               xlim=(-0.45, 10.45), yticks=[-0.7, 0, 0.7, 1])
        ax.text(0.98, 0.84, note, transform=ax.transAxes, ha="right",
                color=color, fontsize=12)
        ax.grid(axis="y", color="#e3e7ea")
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].annotate("0.7, 0.49, 0.343", xy=(2, 0.49), xytext=(3.2, 0.70),
                     arrowprops={"arrowstyle": "->", "color": "#236ca0"})
    axes[1].annotate("-0.7, 0.49, -0.343", xy=(2, 0.49), xytext=(3.2, 0.70),
                     arrowprops={"arrowstyle": "->", "color": "#b54b36"})
    axes[2].annotate(r"$\rho(1)=0.7/1.49\approx0.4698$", xy=(1, ma[1]),
                     xytext=(2.2, 0.70),
                     arrowprops={"arrowstyle": "->", "color": "#288269"})
    axes[-1].set(xlabel="Lag h (observation intervals)", xticks=lags)
    fig.suptitle("Theoretical autocorrelation: feedback versus a finite noise filter",
                 fontsize=15)
    fig.text(0.5, 0.012, "Exact model values; negative lags mirror positive lags.",
             ha="center", fontsize=11)
    fig.tight_layout(rect=(0, 0.035, 1, 0.955), h_pad=1.3)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
