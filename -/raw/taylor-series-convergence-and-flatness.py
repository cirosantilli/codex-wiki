"""Exact geometric-series truncations and a smooth nonanalytic flat function."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, .94, 701)
    z = np.linspace(-1, 1, 1001)
    flat = np.zeros_like(z)
    nonzero = z != 0
    flat[nonzero] = np.exp(-1/z[nonzero]**2)
    assert flat[len(z)//2] == 0
    assert np.isclose(flat[np.argmin(abs(z-.5))], np.exp(-4))
    colors = ["#176997", "#b55d20", "#43804d"]
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.8), dpi=120)
    ax = axes[0]
    ax.plot(x, 1/(1-x), color="#243746", lw=2.8, label=r"$1/(1-x)$")
    for n, color in zip([1, 5, 20], colors):
        total = sum(x**k for k in range(n+1))
        assert np.allclose(1/(1-x)-total, x**(n+1)/(1-x))
        ax.plot(x, total, color=color, lw=1.8, label=f"Degree {n} partial sum")
    ax.scatter([.9], [4.68559], color=colors[1], s=32, zorder=4)
    ax.vlines(.9, 4.68559, 10, color=colors[1], ls=":", lw=1.6)
    ax.text(.58, 10.5, "At x = 0.9:\nT₅ = 4.68559\nremainder = 5.31441", fontsize=10)
    ax.set(xlim=(0, .94), ylim=(0, 18), xlabel="Input x", ylabel="Function or partial sum")
    ax.set_title("Convergence can still need many terms", fontsize=12)
    ax.legend(loc="upper left", fontsize=9, frameon=False)
    ax.grid(alpha=.15)
    ax = axes[1]
    ax.plot(z, flat, color=colors[0], lw=2.5, label=r"$h(x)=e^{-1/x^2}$ off zero")
    ax.axhline(0, color=colors[1], lw=2, ls="--", label="Every Taylor polynomial at 0")
    ax.scatter([0], [0], color="#243746", s=40, zorder=4)
    ax.scatter([.5], [np.exp(-4)], color=colors[0], s=35, zorder=4)
    ax.annotate(r"$h(1/2)=e^{-4}>0$", (.5, np.exp(-4)), xytext=(.02, .18), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": colors[0]})
    ax.text(-.85, .23, "All derivatives at 0 vanish.\nThe function is not zero nearby.", fontsize=10)
    ax.set(xlim=(-1, 1), ylim=(-.035, .41), xlabel="Input x", ylabel="Function value")
    ax.set_title("Smooth does not imply represented by its series", fontsize=11)
    ax.legend(loc="upper center", fontsize=9, frameon=False)
    ax.grid(alpha=.15)
    fig.suptitle("A Taylor series needs both convergence and equality to the function", fontsize=14)
    fig.subplots_adjust(left=.06, right=.97, bottom=.15, top=.80, wspace=.27)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
