#!/usr/bin/env python3
"""Plot the derived self-weight deflection, without reproducing an exam diagram.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5, as declared
in the repository pyproject.toml. Writes the PNG basename into the current
working directory; run from the matching directory beneath _media.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    xi = np.linspace(0.0, 1.0, 501)
    deflection = (16.0 / 5.0) * (xi**4 - 2.0 * xi**3 + xi)
    fig, ax = plt.subplots(figsize=(7.2, 3.5), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.axhline(0, color="0.55", linestyle="--", linewidth=1)
    ax.plot(xi, deflection, color="#175d9e", linewidth=2.5)
    ax.plot([0, 1], [0, 0], "o", color="#175d9e", markersize=5)
    ax.plot([0.5], [1], "o", color="#175d9e", markersize=5)
    ax.annotate(r"$y_{\max}=5qL^4/(384EI)$", xy=(0.5, 1),
                xytext=(0.55, 0.55), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "0.25"})
    ax.set(xlim=(-0.025, 1.025), ylim=(1.14, -0.14),
           xlabel=r"Position $x/L$", ylabel=r"Downward deflection $y/y_{\max}$",
           title="Beam deflection from a uniform self-weight load")
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_yticks([0, 0.5, 1])
    ax.grid(alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
