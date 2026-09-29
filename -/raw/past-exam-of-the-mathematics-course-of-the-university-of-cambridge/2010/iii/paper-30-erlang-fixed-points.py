"""Plot the alternative-routing residual; write the PNG to the caller's CWD.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def erlang_b(load, capacity):
    """Stable recursion, vectorized over offered loads."""
    load = np.asarray(load, dtype=float)
    blocking = np.ones_like(load)
    for circuits in range(1, capacity + 1):
        blocking = load * blocking / (circuits + load * blocking)
    return blocking


def residual(blocking):
    return erlang_b(2000 * (1 + 2 * blocking * (1 - blocking)), 2100) - blocking


def root(left, right):
    left_sign = float(residual(left))
    for _ in range(55):
        middle = (left + right) / 2
        if float(residual(middle)) * left_sign > 0:
            left = middle
        else:
            right = middle
    return (left + right) / 2


def main():
    witnesses = np.array([0.0, 0.01, 0.125, 1.0])
    signs = residual(witnesses)
    if not (signs[0] > 0 and signs[1] < 0 and signs[2] > 0 and signs[3] < 0):
        raise ValueError("The chosen finite-capacity example lost its sign changes")
    roots = [root(a, b) for a, b in zip(witnesses[:-1], witnesses[1:])]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.3), dpi=100)
    fig.set_facecolor("white")
    for ax, end in zip(axes, [0.34, 0.014]):
        b = np.linspace(0, end, 1000)
        ax.plot(b, residual(b), color="#176a9e", linewidth=2,
                label=r"$E(2000[1+2B(1-B)],2100)-B$")
        ax.axhline(0, color="black", linewidth=0.8)
        for value in roots:
            if value < end:
                ax.scatter([value], [0], color="#b84431", zorder=3)
                if end < 0.02 or value > 0.01:
                    ax.annotate(f"B = {value:.5f}", (value, 0),
                                xytext=(0, 13), textcoords="offset points",
                                ha="center", fontsize=9)
        ax.set_xlim(0, end)
        ax.set_xlabel("Blocking probability B")
        ax.set_ylabel("Fixed-point residual")
        ax.grid(alpha=0.25)
    axes[0].set_title("Three distinct equilibrium approximations")
    axes[1].set_title("Low-blocking root, enlarged")
    axes[0].legend(fontsize=9, loc="lower left")
    fig.suptitle("Alternative routing: offered load 2000, capacity 2100")
    fig.tight_layout()
    output = Path.cwd() / "paper-30-erlang-fixed-points.png"
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"{output.name}: roots {', '.join(f'{r:.8f}' for r in roots)}")


if __name__ == "__main__":
    main()
