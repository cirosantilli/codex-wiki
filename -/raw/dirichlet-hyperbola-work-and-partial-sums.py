"""Compare exact floor-division counts and the N=12 expression prefixes.

Run from _media; tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Counts concern the two displayed algorithms, not bit operations or timings.
"""

from math import isqrt
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, (work, partial) = plt.subplots(1, 2, figsize=(10.0, 4.5), layout="constrained", facecolor="white")
    blue, orange = "#007b9e", "#d55e00"
    ns = np.unique(np.geomspace(1, 1_000_000, 500).astype(int))
    roots = np.array([isqrt(int(n)) for n in ns])
    work.loglog(ns, ns, color=blue, linewidth=2, label=r"Direct: $N$ divisions")
    work.loglog(ns, roots, color=orange, linewidth=2, label=r"Balanced: $\lfloor\sqrt{N}\rfloor$ divisions")
    work.scatter([1_000_000], [1_000_000], color=blue, zorder=4)
    work.scatter([1_000_000], [1000], color=orange, zorder=4)
    work.annotate("1,000,000", (1_000_000, 1_000_000), (900, 250_000), color=blue,
                  arrowprops={"arrowstyle": "->", "color": blue})
    work.annotate("1,000", (1_000_000, 1000), (7000, 130), color=orange,
                  arrowprops={"arrowstyle": "->", "color": orange})
    work.set(xlabel="Input N", ylabel="Number of floor divisions", title="Exact arithmetic work")
    work.grid(which="major", color="#dddddd", linewidth=0.6)
    work.legend(loc="upper left", fontsize=9)
    n = 12
    r = isqrt(n)
    terms = np.array([n // a for a in range(1, n + 1)])
    direct = np.cumsum(terms)
    balanced = 2 * np.cumsum(terms[:r]) - r * r
    assert direct.tolist() == [12, 18, 22, 25, 27, 29, 30, 31, 32, 33, 34, 35]
    assert balanced.tolist() == [15, 27, 35]
    assert direct[-1] == balanced[-1] == 35
    partial.plot(range(1, n + 1), direct, "o-", color=blue, linewidth=2, markersize=4,
                 label=r"Direct prefix $\sum_{a=1}^j\lfloor12/a\rfloor$")
    partial.plot(range(1, r + 1), balanced, "s-", color=orange, linewidth=2, markersize=5,
                 label=r"Balanced prefix $2\sum_{a=1}^j\lfloor12/a\rfloor-9$")
    partial.axhline(35, color="#666666", linewidth=1, linestyle=":")
    partial.annotate("35 after 3 divisions", (3, 35), (4.5, 30.3), color=orange,
                     arrowprops={"arrowstyle": "->", "color": orange})
    partial.annotate("35 after 12 divisions", (12, 35), (5.1, 39), color=blue,
                     arrowprops={"arrowstyle": "->", "color": blue})
    partial.set(xlim=(0.7, 12.4), ylim=(9, 42), xlabel="Floor divisions evaluated, j",
                ylabel="Value of the expression prefix", title="Same exact answer for N = 12")
    partial.set_xticks([1, 3, 6, 9, 12])
    partial.grid(color="#dddddd", linewidth=0.6)
    partial.legend(loc="lower right", fontsize=8.5)
    fig.suptitle("The balanced divisor sum reuses one short sum", fontsize=14)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
