"""Exact cubic roots, crossing parity, and a repeated-root perturbation."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-2, 3.5, 1001)
    p = lambda t: (t + 1) * (t - 2) ** 2
    assert p(-1) == 0 and p(2) == 0 and p(3) == 4
    assert p(-1.01) < 0 < p(-0.99)
    assert p(1.99) > 0 and p(2.01) > 0
    assert np.allclose(p(x), x**3 - 3*x**2 + 4)
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2), dpi=120)
    blue, orange, green = "#176997", "#b55d20", "#43804d"
    ax = axes[0]
    ax.plot(x, p(x), color=blue, lw=2)
    ax.axhline(0, color="#74818c", lw=0.9)
    ax.axvline(0, color="#aeb8c0", lw=0.7)
    ax.scatter([-1, 2], [0, 0], color=[green, orange], s=50, zorder=4)
    ax.annotate("simple root: crosses", xy=(-1, 0), xytext=(-1.8, 8),
                fontsize=11, color=green,
                arrowprops={"arrowstyle": "->", "color": green})
    ax.annotate("double root: touches", xy=(2, 0), xytext=(0.5, -8),
                fontsize=11, color=orange,
                arrowprops={"arrowstyle": "->", "color": orange})
    ax.set_xlim(-2, 3.5)
    ax.set_ylim(-18, 12)
    ax.set_xticks([-2, -1, 0, 1, 2, 3])
    ax.set_xlabel("Real input x")
    ax.set_ylabel("Polynomial value")
    ax.set_title(r"$p(x)=(x+1)(x-2)^2=x^3-3x^2+4$", fontsize=13)
    ax = axes[1]
    ax.axhline(0, color="#74818c", lw=1)
    ax.axvline(2, color="#d0d7dd", lw=0.8, ls=":")
    roots_real = [1.8, 2.2]
    roots_complex = [2 + 0.2j, 2 - 0.2j]
    for z in roots_real:
        assert abs((z - 2) ** 2 - 0.04) < 1e-12
    for z in roots_complex:
        assert abs((z - 2) ** 2 + 0.04) < 1e-12
    ax.scatter(roots_real, [0, 0], color=green, s=65, zorder=4)
    ax.scatter([2, 2], [0.2, -0.2], color=blue, s=65, zorder=4)
    ax.scatter([2], [0], facecolor="white", edgecolor=orange, s=140, lw=2, zorder=5)
    for start, end, color in [((2, 0), (1.8, 0), green), ((2, 0), (2.2, 0), green),
                              ((2, 0), (2, 0.2), blue), ((2, 0), (2, -0.2), blue)]:
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "color": color,
                                "shrinkA": 10, "shrinkB": 8, "lw": 1.5})
    ax.text(1.8, -0.055, "1.8", ha="center", color=green, fontsize=11)
    ax.text(2.2, -0.055, "2.2", ha="center", color=green, fontsize=11)
    ax.text(2.025, 0.2, "2 + 0.2i", va="center", color=blue, fontsize=11)
    ax.text(2.025, -0.2, "2 − 0.2i", va="center", color=blue, fontsize=11)
    ax.text(1.62, 0.30, r"$\varepsilon=+0.04$: two real roots", color=green, fontsize=10)
    ax.text(1.62, -0.31, r"$\varepsilon=-0.04$: two complex roots", color=blue, fontsize=10)
    ax.set_xlim(1.58, 2.45)
    ax.set_ylim(-0.36, 0.36)
    ax.set_aspect("equal")
    ax.set_xlabel("Real part of root")
    ax.set_ylabel("Imaginary part")
    ax.set_title(r"Roots of $(x-2)^2-\varepsilon$", fontsize=13)
    fig.suptitle("A repeated factor changes both graph shape and root sensitivity",
                 fontsize=15, y=0.97)
    fig.subplots_adjust(left=0.07, right=0.975, top=0.81, bottom=0.15, wspace=0.30)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
