"""Draw an exact toy target search; output the matching PNG to the CWD.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    blue, red, green = "#2166ac", "#bd4c32", "#28855d"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    a, b = Fraction(0), Fraction(3)
    brackets, candidates = [(a, b)], []
    for _ in range(4):
        m = (a + b) / 2
        residual = m**3 + m - 10
        candidates.append((m, residual))
        if residual < 0:
            a = m
        else:
            b = m
        assert a < 2 < b
        brackets.append((a, b))
    assert brackets[-1] == (Fraction(15, 8), Fraction(33, 16))

    fig, (graph, rows) = plt.subplots(
        2, 1, figsize=(9, 6.8), gridspec_kw={"height_ratios": [1.2, 1]},
        layout="constrained")
    fig.suptitle("Find the input whose output is 10", fontsize=17)
    x = np.linspace(0, 3, 601)
    graph.plot(x, x**3 + x, color=blue, lw=2.5, label=r"$f(x)=x^3+x$")
    graph.axhline(10, color=green, lw=1.7, label="Target output 10")
    graph.axvline(2, color=green, ls=":", lw=1.3)
    graph.scatter([2], [10], color=green, zorder=5)
    offsets = [(-47, -26), (14, 8), (-73, -15), (15, 13)]
    for k, ((m, residual), offset) in enumerate(zip(candidates, offsets), 1):
        color = blue if residual < 0 else red
        graph.scatter([float(m)], [float(m**3 + m)], color=color, zorder=5)
        graph.annotate(f"{k}: {m}", (float(m), float(m**3 + m)),
                       xytext=offset, textcoords="offset points", fontsize=10,
                       color=color, arrowprops={"arrowstyle": "-", "color": color})
    graph.set(xlim=(-0.05, 3.08), ylim=(-1, 32), ylabel="Output f(x)")
    graph.legend(loc="upper left", frameon=False)
    graph.grid(alpha=0.14)

    for k, (left, right) in enumerate(brackets):
        y = 4 - k
        rows.plot([0, 3], [y, y], color="#e7e7e7", lw=6, solid_capstyle="butt")
        rows.plot([float(left), float(right)], [y, y], color=blue, lw=6,
                  solid_capstyle="butt")
        rows.scatter([float(left), float(right)], [y, y], color=blue, s=30, zorder=3)
        rows.text(3.15, y, f"[{left}, {right}]   width {right-left}",
                  va="center", fontsize=10)
        if k < 4:
            mid, residual = candidates[k]
            rows.scatter([float(mid)], [y], marker="v", s=65,
                         color=blue if residual < 0 else red, zorder=5)
    rows.axvline(2, color=green, ls=":", lw=1.5)
    rows.set(yticks=range(5), yticklabels=["k = 4", "k = 3", "k = 2", "k = 1", "k = 0"],
             xlim=(-0.05, 4.9), ylim=(-0.55, 4.6), xticks=[0, 1, 2, 3], xlabel="Input x")
    rows.set_title("Blue = retained bracket; triangle = next tested midpoint", fontsize=11)
    rows.spines["left"].set_visible(False)
    rows.tick_params(axis="y", length=0)
    rows.text(0, -0.43, "Exact solution x* = 2 stays inside every bracket.", fontsize=10,
              color=green)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
