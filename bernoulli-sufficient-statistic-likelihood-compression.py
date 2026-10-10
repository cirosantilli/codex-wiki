"""Illustrate likelihood compression and parameter-free reconstruction.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The PNG is written to the working directory with this script's basename.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def main():
    fig = plt.figure(figsize=(10, 6.5), dpi=110, facecolor="white")
    flow = fig.add_axes((0.025, 0.68, 0.95, 0.30))
    flow.set(xlim=(0, 10), ylim=(0, 2))
    flow.axis("off")
    flow.text(0, 1.83, "Sufficient compression preserves likelihood comparisons", fontsize=16, weight="bold")
    boxes = [(0.1, 0.23, 2.65, 1.03, "0011, 0101, 1010, …\nDifferent sequences\nSame n = 4 and T = 2"), (3.63, 0.23, 2.08, 1.03, "Record (n, T) = (4, 2)\nDiscard arrangement"), (6.65, 0.23, 3.03, 1.03, "$L_T(p)=6p^2(1-p)^2$\nSix arrangements contribute\nFactor 6 is independent of p")]
    for x, y, w, h, label in boxes:
        flow.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04", facecolor="#eef3fa", edgecolor="#536e94"))
        flow.text(x + w / 2, y + h / 2, label, fontsize=11, ha="center", va="center", linespacing=1.6)
    for start, end in [(2.83, 3.55), (5.79, 6.57)]:
        flow.annotate("", xy=(end, 0.74), xytext=(start, 0.74), arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#536e94"})

    p = np.linspace(0, 1, 501)
    sequence = p**2 * (1 - p)**2
    count = 6 * sequence
    ax = fig.add_axes((0.085, 0.35, 0.40, 0.29))
    ax.plot(p, count, color="#b15b22", lw=2.5, label=r"Count: $L_T(p)$")
    ax.plot(p, sequence, color="#275d9b", lw=2.5, label=r"Sequence: $L_x(p)$")
    ax.set(xlim=(0, 1), ylim=(0, 0.41), xlabel="Success probability p", ylabel="Likelihood", title="Absolute likelihoods differ")
    ax.legend(fontsize=10, loc="upper left", frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.15)

    ax2 = fig.add_axes((0.59, 0.35, 0.35, 0.29))
    ax2.plot(p, count / count.max(), color="#b15b22", lw=3.5, label="Count")
    ax2.plot(p, sequence / sequence.max(), color="#275d9b", lw=2, ls="--", label="Sequence")
    ax2.set(xlim=(0, 1), ylim=(0, 1.1), xlabel="Success probability p", ylabel="Likelihood / maximum", title="Normalized curves coincide")
    ax2.legend(fontsize=10, frameon=False)
    ax2.spines[["top", "right"]].set_visible(False)
    ax2.grid(alpha=0.15)

    reverse = fig.add_axes((0.04, 0.035, 0.93, 0.20))
    reverse.set(xlim=(0, 10), ylim=(0, 2))
    reverse.axis("off")
    reverse.text(0, 1.7, "Reconstruct a sample's law from the count", fontsize=13, weight="bold")
    reverse.text(0, 1.1, "T = 2", fontsize=13, va="center", bbox={"facecolor": "#eef3fa", "edgecolor": "#536e94", "boxstyle": "round,pad=0.3"})
    reverse.annotate("", xy=(2.4, 1.1), xytext=(0.8, 1.1), arrowprops={"arrowstyle": "->", "lw": 1.8})
    reverse.text(2.65, 1.12, "Draw uniformly: 0011, 0101, 0110, 1001, 1010, 1100", fontsize=12, va="center")
    reverse.text(2.65, 0.50, "Each has probability 1/6; this step needs no unknown p.", fontsize=12)
    reverse.text(0, 0.04, "This restores the probability law, not the particular sequence that was discarded.", fontsize=11, color="#435366")
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
