"""Plot the two stationary optical rays; save the PNG in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from the corresponding _media directory using the repository environment.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-1, 1, 801)
    fig, ax = plt.subplots(figsize=(7.0, 4.5))
    fig.set_facecolor("white")
    ax.plot(x, 1 + x**2 / 4, color="#1764ab", linewidth=2.4, label=r"$y=1+x^2/4$")
    ax.plot(x, 0.25 + x**2, color="#bb4c22", linewidth=2.4, label=r"$y=1/4+x^2$")
    ax.scatter([-1, 1], [1.25, 1.25], s=35, color="black", zorder=5)
    ax.text(-1, 1.31, r"Source $(-1,5/4)$", ha="left", fontsize=10)
    ax.text(1, 1.31, r"Observer $(1,5/4)$", ha="right", fontsize=10)
    ax.axhline(0, color="0.55", linestyle="--", linewidth=1)
    ax.text(0, 0.04, "Boundary of the medium", color="0.4", ha="center", fontsize=9)
    ax.axvline(0, color="0.87", linewidth=0.8, zorder=0)
    ax.set_xlim(-1.18, 1.18)
    ax.set_ylim(-0.04, 1.48)
    ax.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1, 1.25])
    ax.set_aspect("equal")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.set_title(r"Two stationary optical rays for $n(y)=4\sqrt{y}$", fontsize=12)
    ax.legend(loc="center", bbox_to_anchor=(0.5, 0.48), frameon=False, fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
