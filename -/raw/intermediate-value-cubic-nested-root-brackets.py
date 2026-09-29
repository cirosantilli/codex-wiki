"""Draw a cubic and exact rational bisection brackets, not measured data.

Run from _media using Python 3.14, matplotlib 3.10.7, numpy 2.3.5:
MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../intermediate-value-cubic-nested-root-brackets.py
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**3 + x - 1


def brackets(updates=5):
    a, b = Fraction(0), Fraction(1)
    result = [(a, b)]
    for _ in range(updates):
        m = (a + b) / 2
        if f(m) == 0:
            result.append((m, m))
            break
        if f(m) < 0:
            a = m
        else:
            b = m
        result.append((a, b))
    return result


def main():
    plt.rcParams.update({"font.size": 11, "axes.facecolor": "white"})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 5.5), width_ratios=[1, 1.35], layout="constrained", facecolor="white")
    blue, red = "#235eab", "#b43b30"
    x = np.linspace(0, 1, 501)
    ax.plot(x, f(x), color=blue, linewidth=2.6)
    ax.axhline(0, color="#737b83", linewidth=1)
    # Independent polynomial solver supplies a display marker only.
    roots = np.roots([1, 0, 1, -1])
    r = float(next(z.real for z in roots if abs(z.imag) < 1e-12))
    assert abs(f(r)) < 1e-12
    assert 0 < r < 1
    ax.scatter([0, 1], [-1, 1], color=blue, s=40, zorder=4)
    ax.scatter([r], [0], color=red, s=40, zorder=5)
    ax.annotate(r"$r\approx0.682328$", xy=(r, 0), xytext=(0.15, 0.6), arrowprops={"arrowstyle": "->", "color": red}, color=red)
    ax.set(title=r"$f(x)=x^3+x-1$", xlabel="x", ylabel="f(x)", xlim=(-0.04, 1.04), ylim=(-1.15, 1.15))
    ax.text(0.03, 0.04, r"$f(0)<0<f(1)$" + "\n" + r"$f'(x)=3x^2+1>0$", transform=ax.transAxes, fontsize=11)

    rows = brackets()
    bx.axvline(r, color=red, linestyle="--", linewidth=1.4, zorder=0)
    for k, (a, b) in enumerate(rows):
        assert f(a) < 0 < f(b)
        assert b - a == Fraction(1, 2**k)
        bx.plot([float(a), float(b)], [k, k], color=blue, linewidth=4, solid_capstyle="butt")
        bx.scatter([float(a), float(b)], [k, k], color=blue, s=28, zorder=3)
        bx.text(1.06, k, f"[{a}, {b}]   width = {b-a}", va="center", fontsize=10)
    bx.set(title="Retained intervals after k halvings", xlabel="x (one shared scale)", xlim=(-0.04, 1.8), ylim=(5.65, -0.65))
    bx.set_xticks([0, 0.25, 0.5, 0.75, 1])
    bx.set_yticks(range(6), [f"k = {k}" for k in range(6)])
    bx.text(r + 0.035, 5.45, "Same root in every bracket", color=red, fontsize=10)
    for axis in (ax, bx):
        axis.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Original exact bisection construction — no measured data", fontsize=12)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
