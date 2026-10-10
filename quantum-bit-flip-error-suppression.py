"""Plot the exact ideal three-qubit bit-flip logical error map.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: MPLBACKEND=Agg python3 ../quantum-bit-flip-error-suppression.py
Writes quantum-bit-flip-error-suppression.png to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def failure(p):
    return 3 * p**2 * (1 - p) + p**3


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    blue, orange, gray = "#176a92", "#a94b12", "#555555"
    fig, (ax, zoom) = plt.subplots(1, 2, figsize=(9.6, 4.8), dpi=100)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.75, wspace=0.30)
    fig.suptitle("Ideal bit-flip correction: two physical flips cause a logical error",
                 fontsize=14, y=0.97)
    fig.text(0.5, 0.905, "Independent X errors; perfect encoding, checks, recovery and decoding",
             ha="center", fontsize=11)
    p = np.linspace(0, 1, 1001)
    ax.plot(p, p, "--", color=gray, lw=1.6, label="Unencoded: p")
    ax.plot(p, failure(p), color=blue, lw=2.4, label=r"One level: $3p^2-2p^3$")
    ax.axvline(0.5, ls=":", color=gray, lw=1)
    ax.scatter([0.5], [0.5], color=blue, s=30, zorder=5)
    ax.fill_between(p, failure(p), p, where=p <= 0.5, color=blue, alpha=0.10)
    ax.text(0.19, 0.45, "Improvement", color=blue, ha="center")
    ax.text(0.72, 0.35, "Worse above ½", color=gray, ha="center")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Full probability range", fontsize=12)
    ax.set_ylabel("Logical X-error probability")
    ax.legend(loc="upper left", frameon=False, fontsize=10)

    small = np.linspace(0, 0.12, 601)
    zoom.plot(small, small, "--", color=gray, lw=1.6, label="Unencoded")
    zoom.plot(small, failure(small), color=blue, lw=2.4, label="One level: 3 qubits")
    zoom.plot(small, failure(failure(small)), color=orange, lw=2.4,
              label="Two levels: 9 qubits")
    zoom.set_xlim(0, 0.12)
    zoom.set_ylim(0, 0.12)
    zoom.set_xticks([0, 0.04, 0.08, 0.12])
    zoom.set_title("Rare independent errors", fontsize=12)
    zoom.legend(loc="upper left", frameon=False, fontsize=10)
    zoom.scatter([0.1, 0.1], [failure(0.1), failure(failure(0.1))],
                 c=[blue, orange], s=30, zorder=5)
    zoom.annotate("p = 0.1 → 0.028", xy=(0.1, failure(0.1)),
                  xytext=(0.045, 0.05), fontsize=10, color=blue,
                  arrowprops={"arrowstyle": "->", "color": blue})
    zoom.annotate("→ 0.002308096", xy=(0.1, failure(failure(0.1))),
                  xytext=(0.023, 0.014), fontsize=10, color=orange,
                  arrowprops={"arrowstyle": "->", "color": orange})
    for axis in (ax, zoom):
        axis.set_xlabel("Physical X-error probability p")
        axis.set_axisbelow(True)
        axis.grid(color="#e5e5e5", lw=0.7)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
