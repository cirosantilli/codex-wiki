"""Generate markov-chain-convergence.png in cwd; Python 3.14, NumPy, Matplotlib."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


def main():
    p = np.array([[0.8, 0.2], [0.4, 0.6]])
    pi = np.array([2 / 3, 1 / 3])
    n = np.arange(9)
    sunny = 2 / 3 + (1 / 3) * 0.4**n
    rainy = 2 / 3 - (2 / 3) * 0.4**n
    np.testing.assert_allclose(p.sum(axis=1), 1)
    np.testing.assert_allclose(pi @ p, pi)
    np.testing.assert_allclose(p @ p, [[0.72, 0.28], [0.56, 0.44]])
    np.testing.assert_allclose(pi[:, None] * p, (pi[:, None] * p).T)
    for k in n:
        np.testing.assert_allclose(np.linalg.matrix_power(p, int(k))[:, 0], [sunny[k], rainy[k]])
    assert abs(1 / (1 - p[0, 0]) - 5) < 1e-12

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, (diagram, ax) = plt.subplots(1, 2, figsize=(10, 4.4), facecolor="white", gridspec_kw={"width_ratios": [1, 1.35]})
    fig.subplots_adjust(left=0.035, right=0.97, top=0.78, bottom=0.20, wspace=0.25)
    fig.suptitle("Two states, one equilibrium", fontsize=17, y=0.98)
    fig.text(0.5, 0.875, "Constructed sunny/rainy model • one step = one day", ha="center", fontsize=11)

    diagram.set_title("One-step transition probabilities")
    diagram.set_aspect("equal")
    diagram.set_xlim(-1.8, 1.8)
    diagram.set_ylim(-1.15, 1.25)
    diagram.axis("off")
    for x, label, fill, color in [(-0.85, "Sunny\nS", "#fff0bd", "#9a5b00"), (0.85, "Rainy\nR", "#dceeff", "#1765a8")]:
        diagram.add_patch(Circle((x, 0), 0.38, facecolor=fill, edgecolor=color, lw=2))
        diagram.text(x, 0, label, ha="center", va="center", fontsize=12, color=color)
        # A curved self-transition leaves and returns to the same state.
        outer = -1 if x < 0 else 1
        diagram.add_patch(FancyArrowPatch((x + outer * 0.17, 0.33), (x + outer * 0.33, -0.18), connectionstyle=f"arc3,rad={-1.65 * outer}", arrowstyle="-|>", mutation_scale=15, lw=1.8, color=color))
        diagram.text(x + outer * 0.72, 0.43, "0.8" if x < 0 else "0.6", ha="center", color=color)
    diagram.add_patch(FancyArrowPatch((-0.49, 0.16), (0.49, 0.16), connectionstyle="arc3,rad=-0.45", arrowstyle="-|>", mutation_scale=15, lw=1.8, color="#586675"))
    diagram.add_patch(FancyArrowPatch((0.49, -0.16), (-0.49, -0.16), connectionstyle="arc3,rad=-0.45", arrowstyle="-|>", mutation_scale=15, lw=1.8, color="#586675"))
    diagram.text(0, 0.48, "0.2", ha="center", color="#586675")
    diagram.text(0, -0.61, "0.4", ha="center", color="#586675")
    diagram.text(0, -1.05, "Rows: today    Columns: tomorrow", ha="center", fontsize=10)

    ax.set_title("Probability of sunshine after n steps")
    ax.plot(n, sunny, "o-", lw=2, ms=5, color="#9a5b00", label="Start sunny: q₀ = 1")
    ax.plot(n, rainy, "s-", lw=2, ms=5, color="#1765a8", label="Start rainy: q₀ = 0")
    ax.axhline(2 / 3, color="#576b39", ls="--", lw=1.8, label="Start stationary: q₀ = 2/3")
    ax.annotate("q₂ = 0.72", xy=(2, sunny[2]), xytext=(3.25, 0.88), arrowprops={"arrowstyle": "->", "color": "#9a5b00"}, fontsize=10, color="#9a5b00")
    ax.set_xlim(-0.15, 8.15)
    ax.set_ylim(-0.03, 1.05)
    ax.set_xticks(n)
    ax.set_yticks([0, 1 / 3, 2 / 3, 1], labels=["0", "1/3", "2/3", "1"])
    ax.set_xlabel("Number of steps n")
    ax.set_ylabel("Sunny probability qₙ")
    ax.grid(color="#e3e7eb", lw=0.7)
    ax.legend(loc="lower right", frameon=False, fontsize=9.5)
    fig.text(0.5, 0.045, r"$q_n=\frac{2}{3}+(q_0-\frac{2}{3})\,0.4^n$     •     Stationary law: π = (2/3, 1/3)", ha="center", fontsize=12)
    fig.savefig(Path.cwd() / "markov-chain-convergence.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
