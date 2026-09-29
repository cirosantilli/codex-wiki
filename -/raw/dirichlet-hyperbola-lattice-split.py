"""Draw the positive-integer lattice split for N=12.

Run from _media; tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from math import isqrt
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


def main():
    n = 12
    r = isqrt(n)
    pairs = [(a, b) for a in range(1, n + 1) for b in range(1, n + 1) if a * b <= n]
    groups = [
        ([(a, b) for a, b in pairs if a <= r and b > r], "#007b9e", r"$a\leq3$, $b>3$: 13 points"),
        ([(a, b) for a, b in pairs if b <= r and a > r], "#d55e00", r"$b\leq3$, $a>3$: 13 points"),
        ([(a, b) for a, b in pairs if a <= r and b <= r], "#7655a4", r"Overlap $a,b\leq3$: 9 points"),
    ]
    assert [len(group) for group, _, _ in groups] == [13, 13, 9]
    assert len(pairs) == 2 * sum(n // a for a in range(1, r + 1)) - r * r == 35
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(7.4, 6.5), layout="constrained", facecolor="white")
    ax.set_facecolor("white")
    x = np.linspace(1, n, 500)
    ax.plot(x, n / x, color="#333333", linewidth=1.8, zorder=2)
    ax.axvspan(0.5, r + 0.5, color="#007b9e", alpha=0.06)
    ax.axhspan(0.5, r + 0.5, color="#d55e00", alpha=0.06)
    ax.axvline(r + 0.5, color="#007b9e", linestyle="--", linewidth=1.4)
    ax.axhline(r + 0.5, color="#d55e00", linestyle="--", linewidth=1.4)
    for group, color, label in groups:
        a, b = zip(*group)
        ax.scatter(a, b, s=55, color=color, edgecolors="white", linewidths=0.6, label=label, zorder=4)
    ax.scatter([4], [4], s=65, marker="x", color="#666666", linewidths=1.8, zorder=4)
    ax.annotate("First excluded corner\n4 × 4 = 16 > 12", (4, 4), (6.0, 5.4),
                arrowprops={"arrowstyle": "->", "color": "#666666"}, color="#444444")
    ax.text(7.4, 2.2, r"$ab=12$", color="#333333")
    ax.set(xlim=(0.5, 12.5), ylim=(0.5, 12.5), xlabel="Positive integer a", ylabel="Positive integer b")
    ax.set_xticks(range(1, n + 1))
    ax.set_yticks(range(1, n + 1))
    ax.set_aspect("equal")
    ax.grid(color="#dddddd", linewidth=0.5, zorder=0)
    handles, labels = ax.get_legend_handles_labels()
    handles.append(Line2D([0], [0], color="#333333", linewidth=1.8))
    labels.append(r"Hyperbola $ab=12$; boundary points included")
    ax.legend(handles, labels, loc="upper right", framealpha=1, fontsize=10)
    ax.set_title("Counting ab ≤ 12 with a square-root split\n22 in each strip − 9 in their overlap = 35", fontsize=14, pad=13)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
