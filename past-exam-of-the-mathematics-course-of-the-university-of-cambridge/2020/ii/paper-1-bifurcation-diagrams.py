#!/usr/bin/env python3
"""Plot the bifurcation diagrams in 2020 Part II Paper 1, Question 32E."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT = Path(Path(__file__).stem + ".png")



def equilibria(mu: float, a: float, epsilon: float) -> list[tuple[float, bool]]:
    """Return real equilibria and whether each is linearly stable."""
    roots = np.roots([1.0, 0.0, a - 3.0 * mu, 0.0, 2.0 * mu * (mu - a), -epsilon])
    answer = []
    for root in roots:
        if abs(root.imag) < 1e-7:
            x = float(root.real)
            derivative = -(
                5.0 * x**4
                + 3.0 * (a - 3.0 * mu) * x**2
                + 2.0 * mu * (mu - a)
            )
            answer.append((x, derivative < 0.0))
    return answer


mu_values = np.linspace(-1.45, 1.75, 900)
fig, axes = plt.subplots(2, 3, figsize=(11.2, 7.0), sharex=True, sharey=True)

for row, epsilon in enumerate((0.0, 0.035)):
    for column, a in enumerate((-1.0, 0.0, 1.0)):
        ax = axes[row, column]
        roots_by_mu = [sorted(equilibria(mu, a, epsilon)) for mu in mu_values]
        for root_count in (1, 3, 5):
            for root_index in range(root_count):
                stable_x = np.full(mu_values.shape, np.nan)
                unstable_x = np.full(mu_values.shape, np.nan)
                for index, roots in enumerate(roots_by_mu):
                    if len(roots) == root_count:
                        x, stable = roots[root_index]
                        (stable_x if stable else unstable_x)[index] = x
                ax.plot(mu_values, stable_x, color="#176b87", linewidth=1.5)
                ax.plot(
                    mu_values,
                    unstable_x,
                    color="#c75146",
                    linewidth=1.35,
                    linestyle="--",
                )
        ax.axhline(0.0, color="0.78", linewidth=0.6)
        ax.axvline(0.0, color="0.78", linewidth=0.6)
        ax.set_title(f"$a={a:g}$")
        if column == 0:
            ax.set_ylabel("$x$\n" + ("$\\epsilon=0$" if row == 0 else "$\\epsilon=0.035$"))
        if row == 1:
            ax.set_xlabel("$\\mu$")
        ax.set_xlim(mu_values[0], mu_values[-1])
        ax.set_ylim(-2.15, 2.15)

handles = [
    plt.Line2D([], [], color="#176b87", linewidth=1.5, label="stable"),
    plt.Line2D([], [], color="#c75146", linewidth=1.35, linestyle="--", label="unstable"),
]
fig.legend(handles=handles, loc="upper center", ncol=2, frameon=False)
fig.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig(OUTPUT, dpi=160, facecolor="white")
