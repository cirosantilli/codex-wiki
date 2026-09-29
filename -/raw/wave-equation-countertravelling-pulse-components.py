"""Synthetic wave solutions; tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes the matching PNG basename in the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def bump(x):
    """C-infinity compact pulse, support [-1, 1], peak one."""
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)
    inside = np.abs(x) < 1
    y[inside] = np.exp(1 - 1 / (1 - x[inside] ** 2))
    return y


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    x = np.linspace(-3.2, 3.2, 1601)
    fig, axes = plt.subplots(3, 2, figsize=(10.8, 7.4), sharex=True, sharey=True)
    for row, t in enumerate((0, 0.5, 1.5)):
        for col in (0, 1):
            ax = axes[row, col]
            right = (0.5 if col == 0 else 1) * bump(x - t)
            left = 0.5 * bump(x + t) if col == 0 else np.zeros_like(x)
            ax.plot(x, right + left, color="#242424", lw=2.5, label="Total displacement")
            ax.plot(x, left, color="#cf4b39", lw=2, linestyle=":", label="Left component G(x+t)")
            ax.plot(x, right, color="#1976a3", lw=1.8, linestyle="--", label="Right component F(x−t)")
            ax.set_ylim(-0.06, 1.14)
            ax.set_xlim(-3.2, 3.2)
            ax.set_yticks((0, 0.5, 1))
            ax.grid(alpha=0.2)
            ax.text(0.025, 0.86, f"t = {t:g}", transform=ax.transAxes,
                    bbox={"facecolor": "white", "edgecolor": "none"})
            if col == 0:
                ax.set_ylabel("Displacement u / A")
            if row == 2:
                ax.set_xlabel("Position x / a")
                if col == 0:
                    ax.annotate("Left", (-1.5, 0.5), (-2.5, 0.85),
                                arrowprops={"arrowstyle": "->", "color": "#cf4b39"}, color="#af392c")
                    ax.annotate("Right", (1.5, 0.5), (2, 0.85),
                                arrowprops={"arrowstyle": "->", "color": "#1976a3"}, color="#1976a3")
                else:
                    ax.annotate("Right", (1.5, 1), (2.2, 0.65),
                                arrowprops={"arrowstyle": "->", "color": "#1976a3"}, color="#1976a3")
    axes[0, 0].set_title("Release from rest: g = 0\nF = f / 2,  G = f / 2", pad=10)
    axes[0, 1].set_title("Launch to the right: g = −c f′\nF = f,  G = 0", pad=10)
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=3, frameon=False, fontsize=10,
               bbox_to_anchor=(0.5, 0.045))
    fig.suptitle("Two directions of travel from the same initial shape", fontsize=16, y=0.985)
    fig.text(0.5, 0.016, "Synthetic analytical solutions: f(x) = b(x), c = a = A = 1; time in units a / c.",
             ha="center", fontsize=10, color="#555555")
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.84, hspace=0.24, wspace=0.15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
