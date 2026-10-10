"""Plot exact solutions and bounds; emit the PNG into the current directory.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    period = 2 * np.pi
    cases = [(-0.2, "#2476aa", "decay"), (0.0, "#25834d", "periodic"),
             (0.2, "#bf5229", "growth")]
    fig, axes = plt.subplots(3, 2, figsize=(11, 8.8), layout="constrained")
    fig.suptitle(r"Periodic coefficient, three different fates: $y'= (a+\cos t)y$, $y(0)=1$",
                 fontsize=16)
    for row, (a, color, label) in enumerate(cases):
        for col, count in enumerate([1, 4]):
            ax = axes[row, col]
            t = np.linspace(0, count * period, count * 600 + 1)
            trend = np.exp(a * t)
            y = np.exp(a * t + np.sin(t))
            lower, upper = trend / np.e, trend * np.e
            ax.fill_between(t / period, lower, upper, color=color, alpha=0.13)
            ax.plot(t / period, y, color=color, lw=2.3)
            ax.plot(t / period, trend, color="#444444", lw=1.4, ls="--")
            n = np.arange(count + 1)
            ax.scatter(n, np.exp(a * n * period), color=color, s=25, zorder=3)
            ax.set_xlim(0, count)
            ax.set_xticks(np.arange(count + 1))
            ax.grid(alpha=0.18)
            ax.set_xlabel(r"Time $t/T$, with $T=2\pi$")
            if col == 0:
                ax.set_ylim(0, 1.04 * upper.max())
                ax.set_ylabel(r"$y(t)$")
                ax.set_title(f"a = {a:+.1f}: {label} — one period", loc="left")
                ax.text(0.97, 0.91, f"y(T) = {np.exp(a * period):.4f}",
                        transform=ax.transAxes, ha="right", va="top", color=color)
            else:
                ax.set_yscale("log")
                ax.set_ylabel(r"$y(t)$ (log scale)")
                ax.set_title("Four periods — modulation inside the bounds", loc="left")
    fig.legend(handles=[Line2D([], [], color="#333333", lw=2.3, label=r"Exact solution $e^{at+\sin t}$"),
                        Line2D([], [], color="#444444", lw=1.4, ls="--", label=r"Trend $e^{at}$"),
                        Patch(facecolor="#777777", alpha=0.18, label=r"Bounds $e^{at-1}$ to $e^{at+1}$")],
               loc="outside lower center", ncol=3, frameon=False)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
