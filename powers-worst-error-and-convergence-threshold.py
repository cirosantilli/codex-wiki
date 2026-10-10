"""Compare supremum errors and exact strict-tolerance thresholds.

Emit the matching opaque PNG in the CWD. Tested with Python 3.14,
matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), dpi=120)
    fig.patch.set_facecolor("white")
    eps = 0.01
    n = np.arange(1, 41)
    left, right = axes
    left.semilogy(n, np.ones_like(n), color="#a74368", lw=2.5,
                  label="[0, 1] or [0, 1): error = 1")
    left.semilogy(n, 0.8**n, color="#2264a5", lw=2.5,
                  label=r"[0, 0.8]: error = $0.8^n$")
    left.axhline(eps, color="#333333", ls="--", lw=1.5,
                 label=r"tolerance $\varepsilon=0.01$")
    left.axvline(21, color="#2264a5", ls=":", lw=1.4)
    left.scatter([20, 21], [0.8**20, 0.8**21], color="#2264a5", s=35, zorder=5)
    left.annotate("first successful index: 21", xy=(21, 0.8**21),
                  xytext=(7, 0.0012), fontsize=10,
                  arrowprops={"arrowstyle": "->", "color": "#2264a5"})
    left.set(xlim=(1, 40), ylim=(0.0001, 1.7), xlabel="index n",
             ylabel="supremum error (log scale)")
    left.legend(loc="upper right", bbox_to_anchor=(1, 0.86), fontsize=9)
    left.set_title("One bound over the whole domain", pad=13)
    x = np.linspace(0.25, 0.995, 3500)
    threshold = np.floor(np.log(eps) / np.log(x)) + 1
    right.semilogy(x, threshold, color="#29957a", lw=2.3,
                   label=r"pointwise $N(x,0.01)$")
    right.axhline(21, color="#2264a5", ls="--", lw=1.7,
                  label="common N = 21 on [0, 0.8]")
    right.axvspan(0.25, 0.8, color="#2264a5", alpha=0.065)
    right.axvline(0.8, color="#2264a5", ls=":", lw=1.4)
    for xpos, value, offset in [(0.5, 7, (8, -16)), (0.8, 21, (8, 10)),
                                 (0.99, 459, (-86, 0))]:
        right.scatter([xpos], [value], color="#29957a", s=35, zorder=5)
        right.annotate(f"({xpos:g}, {value})", xy=(xpos, value),
                       xytext=offset, textcoords="offset points", fontsize=10)
    right.set(xlim=(0.25, 1.01), ylim=(2, 1400), xlabel="fixed input x < 1",
              ylabel="first successful index N (log scale)")
    right.legend(loc="upper left", fontsize=9)
    right.set_title("Separate thresholds grow without bound", pad=13)
    for ax in axes:
        ax.grid(alpha=0.18, which="both")
    fig.suptitle(r"How late must $x^n$ be to make the error less than 0.01?",
                 fontsize=14, y=0.98)
    fig.text(0.5, 0.025,
             "At x = 1 the pointwise error is zero; inputs just below 1 defeat every common threshold.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.18, top=0.81, wspace=0.30)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
