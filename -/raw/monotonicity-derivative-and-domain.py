"""Illustrate derivative signs and the interval hypothesis; output PNG to cwd.

Uses the repository's Python 3.14, NumPy, and Matplotlib environment.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-1.4, 1.4, 701)
    x[len(x) // 2] = 0.0
    derivative = 3 * x**2
    assert np.all(np.diff(x**3) > 0) and np.all(derivative >= 0)
    assert derivative[len(x) // 2] == 0
    for value in (-1.5, 1.5):
        shift = 0 if value < 0 else 10
        h = 1e-5
        numerical_derivative = ((value + h - shift) - (value - h - shift)) / (2 * h)
        assert np.isclose(numerical_derivative, 1, atol=1e-9, rtol=0)
    assert -1.5 > 1.5 - 10

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 3, figsize=(11.2, 4.6), dpi=120, facecolor="white",
                             gridspec_kw={"width_ratios": [1, 1, 1.35]})
    blue, orange, red = "#246b9e", "#b4611c", "#a52f43"
    axes[0].plot(x, x**3, color=blue, lw=2.7)
    axes[0].plot([-0.8, 0.8], [0, 0], color=orange, ls="--", lw=2, label="Horizontal tangent")
    axes[0].scatter([0], [0], color=blue, s=55, zorder=5)
    axes[0].set(title="Still strictly increasing\n" + r"$f(x)=x^3$", ylabel="Function value",
                xlim=(-1.4, 1.4), ylim=(-3, 3))
    axes[0].legend(loc="upper left", fontsize=9, frameon=False)
    axes[1].plot(x, derivative, color=orange, lw=2.7)
    axes[1].scatter([0], [0], color=orange, s=55, zorder=5)
    axes[1].set(title="Derivative zero at one point\n" + r"$f'(x)=3x^2\geq0$", ylabel="Derivative value",
                xlim=(-1.4, 1.4), ylim=(-0.4, 6.4))
    ax = axes[2]
    left, right = np.linspace(-2, -1, 201), np.linspace(1, 2, 201)
    ax.axvspan(-1, 1, facecolor="#edf0f2", zorder=0)
    ax.plot(left, left, color=blue, lw=2.7)
    ax.plot(right, right - 10, color=blue, lw=2.7)
    ax.scatter([-2, -1, 1, 2], [-2, -1, -9, -8], s=70, facecolors="white",
               edgecolors=blue, linewidths=2, zorder=5)
    ax.scatter([-1.5, 1.5], [-1.5, -8.5], color=red, s=55, zorder=6)
    ax.text(-1.5, -3.0, r"$f(-1.5)=-1.5$", ha="center", color=red, fontsize=10)
    ax.text(1.5, -6.8, r"$f(1.5)=-8.5$", ha="center", color=red, fontsize=10)
    ax.text(0, -5, "Outside\nthe domain", ha="center", va="center", color="#5f6870", fontsize=10)
    ax.text(-1.52, -0.15, r"$f(x)=x$", color=blue, ha="center", fontsize=11)
    ax.text(1.5, -9.85, r"$f(x)=x-10$", color=blue, ha="center", fontsize=11)
    ax.set(title="Disconnected domain\n" + r"$f'(x)=1$ everywhere in $D$", ylabel="Function value",
           xlim=(-2.5, 2.5), ylim=(-10.5, 0.8), xticks=[-2, -1, 0, 1, 2])
    notes = ["A horizontal tangent does not\ncreate a flat interval.",
             "Strict increase does not require\na positive derivative at every point.",
             "Larger input, smaller output across the gap:\npositive derivatives alone do not suffice."]
    for ax, note in zip(axes, notes):
        ax.set_xlabel("Input x")
        ax.grid(color="#e1e6e9")
        ax.spines[["top", "right"]].set_visible(False)
        ax.text(0.5, -0.28, note, transform=ax.transAxes, ha="center", va="top", fontsize=10)
    fig.suptitle("Derivative tests need an interval connecting the inputs", fontsize=16, y=0.98)
    fig.subplots_adjust(left=0.065, right=0.985, bottom=0.24, top=0.78, wspace=0.38)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Checks passed: cubic strict ordering and derivative zero; both component slopes = 1.")
    print("Across the domain gap: x = -1.5 < 1.5, but f(x) = -1.5 > -8.5.")


if __name__ == "__main__":
    main()
