"""Plot the exact hypergeometric likelihood for M=20, C=25, R=5.

Tested with Python 3.14.4 and Matplotlib 3.10.7 (Debian +dfsg1 build).
Run from _media; write an opaque white PNG with this script's basename to CWD.
The range 40..300 is a plotting window, never an inference cutoff.
"""

from fractions import Fraction
from math import comb
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def likelihood(n, m=20, c=25, r=5):
    if n < m + c - r:
        return Fraction(0)
    return Fraction(comb(m, r) * comb(n - m, c - r), comb(n, c))


def main():
    ns = list(range(40, 301))
    exact = [likelihood(n) for n in ns]
    peak = max(exact)
    assert [n for n, value in zip(ns, exact) if value == peak] == [99, 100]
    # Consecutive ratios cross one exactly at N=99 and decrease thereafter.
    # Their numerator minus denominator is 500 - 5*(N+1), so the entire
    # unbounded integer domain has these maxima, not just the plotted range.
    for n in ns[:-1]:
        ratio = Fraction((n - 19) * (n - 24), (n + 1) * (n - 39))
        assert likelihood(n + 1) / likelihood(n) == ratio
    lp = Fraction(20 * 25, 5)
    chapman = Fraction(21 * 26, 6) - 1
    assert (lp, chapman) == (100, 90)
    relative = [float(value / peak) for value in exact]
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.6, 5.8), dpi=100)
    ax.plot(ns, relative, color="#24669b", linewidth=2.1, label="Exact likelihood / its maximum")
    ax.axvline(float(chapman), color="#b56118", linewidth=1.8, linestyle="--", label="Chapman estimate: 90")
    ax.axvline(float(lp), color="#754a9f", linewidth=1.7, linestyle=":", label="Ratio estimate: 100")
    ax.scatter([99, 100], [1, 1], color="#24669b", s=30, zorder=5)
    ax.annotate("Integer maxima: 99 and 100", xy=(99.5, 1), xytext=(140, 0.91),
                arrowprops={"arrowstyle": "->", "color": "#303030"}, fontsize=11)
    ax.annotate("Positive tail continues\nbeyond the display", xy=(295, relative[-6]),
                xytext=(210, 0.34), arrowprops={"arrowstyle": "->", "color": "#303030"}, fontsize=11)
    ax.set(xlim=(40, 300), ylim=(0, 1.08), xlabel="Candidate population size N (integer, N ≥ 40)",
           ylabel="Relative likelihood  L(N) / max L")
    ax.set_xticks([40, 60, 90, 100, 150, 200, 250, 300])
    ax.grid(alpha=0.2)
    ax.legend(loc="upper right", bbox_to_anchor=(1, 0.79), framealpha=1, fontsize=10)
    ax.set_title("M = 20 marked, C = 25 sampled, R = 5 recaptured", fontsize=14, pad=12)
    fig.suptitle("Population likelihood from a small overlap", y=0.98, fontsize=16, weight="bold")
    fig.text(0.5, 0.035, "Toy data.  N = 40 is the observed minimum; 300 is only a plotting limit.  This is not a posterior.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=0.105, right=0.975, top=0.83, bottom=0.17)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
