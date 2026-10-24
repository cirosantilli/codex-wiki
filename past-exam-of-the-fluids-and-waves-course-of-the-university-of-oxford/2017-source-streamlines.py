"""Oxford A10 (2017), question 1(b): outward radial streamlines.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are declared in the repository root pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(5.0, 5.0), facecolor="white")
    for theta in np.linspace(0, 2 * np.pi, 16, endpoint=False):
        direction = np.array([np.cos(theta), np.sin(theta)])
        ax.plot(*(direction[:, None] * np.array([0.08, 1.48])), color="#176b93", lw=1.5)
        ax.annotate("", xy=direction * 1.05, xytext=direction * 0.77,
                    arrowprops={"arrowstyle": "->", "color": "#176b93", "lw": 1.6})
    ax.add_patch(plt.Circle((0, 0), 0.58, fill=False, ls="--", lw=1, color="0.5"))
    ax.plot(0, 0, "o", color="#b4591c", ms=6)
    ax.text(0.08, 0.06, r"$Q>0$", color="#b4591c", fontsize=12)
    ax.text(-1.47, -1.43, r"$\theta=\mathrm{constant},\quad u_r=Q/(2\pi r)$", fontsize=12)
    ax.set(xlim=(-1.6, 1.6), ylim=(-1.6, 1.6), xlabel="$x$", ylabel="$y$",
           title="Outward rays from a line source", aspect="equal")
    ax.set_facecolor("white")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    output = Path.cwd()
    fig.savefig(output / Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
