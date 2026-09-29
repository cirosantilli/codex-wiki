"""Original tight-binding effective-mass curve; write PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib; see root pyproject.toml.
The curve is the specified model, not a microscopic small-spacing prediction.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    spacing = np.linspace(.28, 6.7, 1200)
    mass = np.exp(spacing - 2) * (2 / spacing)**2
    fig, ax = plt.subplots(figsize=(6.2, 3.8), facecolor="white")
    ax.plot(spacing, mass, lw=2, color="#1768ab")
    ax.scatter([2], [1], s=34, color="#bd6426", zorder=3)
    ax.axvline(2, ls=":", lw=1, color="#9ba5ae")
    ax.axhline(1, ls=":", lw=1, color="#9ba5ae")
    ax.annotate(r"Minimum: $a=2a_1$", xy=(2, 1), xytext=(2.65, 3.3),
                arrowprops={"arrowstyle": "->", "color": "#586572"}, fontsize=10)
    ax.set(xlim=(0, 6.7), ylim=(0, 10), xlabel=r"$a/a_1$", ylabel=r"$m^*(a)/m^*_{\min}$")
    ax.set_title(r"$m^*(a)\propto e^{a/a_1}/a^2$")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
