#!/usr/bin/env python3
"""Original sketches for Oxford A6 2023, Question 3(b).

Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7 (repository environment).
Run in the intended image output directory; writes 2023-boundary-layers.png.
Only the derived leading composite approximations are plotted, not exact BVPs.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0.0, 1.0, 2001)
    fig, axes = plt.subplots(1, 2, figsize=(9.8, 3.7), sharey=True)
    fig.patch.set_facecolor("white")
    outer = np.exp(-x*x/2)
    for eps, color in [(0.04, "#176aa5"), (0.08, "#bc5426")]:
        axes[0].plot(x, np.exp(-x/eps), color=color, lw=2,
                     label=rf"$\epsilon={eps:.2f}$")
        axes[1].plot(x, outer-np.exp(-0.5)*np.exp(-(1-x)/eps),
                     color=color, lw=2, label=rf"$\epsilon={eps:.2f}$")
    axes[0].plot(x, np.zeros_like(x), "--", color="#555555", lw=1.6,
                 label="outer = 0", zorder=5)
    axes[1].plot(x, outer, "--", color="#555555", lw=1.6,
                 label=r"outer = $e^{-x^2/2}$", zorder=5)
    axes[0].set_title(r"(i) $+\epsilon y''$: left layer", fontsize=12)
    axes[1].set_title(r"(ii) $-\epsilon y''$: right layer", fontsize=12)
    for ax in axes:
        ax.set(xlim=(0, 1), ylim=(-0.035, 1.06), xlabel="$x$")
        ax.set_xticks(np.linspace(0, 1, 6))
        ax.grid(alpha=0.18)
        ax.legend(loc="upper right", fontsize=9, framealpha=0.94)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("leading composite $y$")
    axes[0].annotate("rapid descent", xy=(0.045, np.exp(-0.045/0.04)),
                     xytext=(0.30, 0.56), arrowprops={"arrowstyle": "->"},
                     fontsize=10)
    axes[1].annotate("rapid descent", xy=(0.965, 0.37),
                     xytext=(0.45, 0.29), arrowprops={"arrowstyle": "->"},
                     fontsize=10)
    fig.tight_layout(pad=1.2)
    fig.savefig(Path("2023-boundary-layers.png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
