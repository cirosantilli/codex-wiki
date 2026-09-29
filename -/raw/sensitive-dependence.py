"""Compare contraction and sensitive logistic evolution.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes sensitive-dependence.png to the caller's working directory.
Uses only the dependencies in the repository's pyproject.toml.
"""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def orbit(r, initial, steps):
    values = np.empty(steps + 1)
    values[0] = initial
    for n in range(steps):
        values[n + 1] = r * values[n] * (1 - values[n])
    return values


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axes = plt.subplots(2, 2, figsize=(11, 6.5), layout="constrained", facecolor="white")
    steps = np.arange(56)
    initial = 0.2
    epsilon = 1e-8
    for col, r in enumerate((2.8, 4.0)):
        first = orbit(r, initial, 55)
        second = orbit(r, initial + epsilon, 55)
        upper, lower = axes[:, col]
        upper.plot(steps, first, color="#2166ac", lw=1.4, label=r"$x_0=0.2$")
        upper.plot(steps, second, color="#cf651a", lw=1.2, ls="--",
                   label=r"$y_0=0.2+10^{-8}$")
        upper.set(xlim=(0, 55), ylim=(0, 1), xlabel="Iteration n", ylabel="State",
                  title=f"r = {r:g}: " + ("nearby orbits converge" if col == 0 else "nearby orbits separate"))
        upper.legend(loc="lower left", fontsize=10, framealpha=0.95)
        separation = np.abs(first - second)
        # Mask exact zeros rather than assigning them a fictitious log distance.
        lower.semilogy(steps, np.where(separation > 0, separation, np.nan),
                       ".-", ms=4, color="#2166ac", lw=1.4, label="Computed separation")
        if col == 0:
            lower.semilogy(steps, epsilon * 0.8 ** steps, ls="--", color="#666666", lw=1,
                           label=r"Reference slope: $(0.8)^n$")
        else:
            growth_steps = steps[steps <= 26]
            lower.semilogy(growth_steps, epsilon * 2.0 ** growth_steps,
                           ls="--", color="#666666", lw=1,
                           label=r"Reference slope: $2^n$")
            lower.axhline(0.1, color="#9e2929", lw=0.9, ls=":")
            lower.text(54, 0.13, "separation = 0.1", color="#9e2929", ha="right", fontsize=9)
        lower.set(xlim=(0, 55), ylim=(1e-15, 2), xlabel="Iteration n",
                  ylabel=r"Separation $|x_n-y_n|$",
                  title="Log scale reveals shrinking errors" if col == 0 else "Growth fluctuates, then is bounded by 1")
        lower.legend(loc="lower left", fontsize=9, framealpha=0.95)
        for ax in (upper, lower):
            ax.set_facecolor("white")
            ax.grid(alpha=0.18)
    fig.savefig(Path.cwd() / "sensitive-dependence.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
