"""Seeded, exactly stationary Gaussian paths with unit marginal variance.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
Output the matching PNG to CWD. No burn-in or zero initialization is used.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def stationary_ar1(rng, phi, n):
    """Unit stationary variance: X_0 ~ N(0,1), noise variance 1-phi^2."""
    path = np.empty(n)
    path[0] = rng.normal()
    noise = rng.normal(scale=np.sqrt(1 - phi**2), size=n - 1)
    for t in range(1, n):
        path[t] = phi * path[t - 1] + noise[t - 1]
    return path


def stationary_ma1(rng, theta, n):
    """Include epsilon_{-1}; noise variance 1/(1+theta^2)."""
    noise = rng.normal(scale=1 / np.sqrt(1 + theta**2), size=n + 1)
    return noise[1:] + theta * noise[:-1]


def main():
    rng = np.random.default_rng(20261012)
    n = 100
    cases = [
        (stationary_ar1(rng, 0.7, n), r"AR(1): $\phi=0.7$",
         "Positive persistence", "#236ca0"),
        (stationary_ar1(rng, -0.7, n), r"AR(1): $\phi=-0.7$",
         "Alternating tendency", "#b54b36"),
        (stationary_ma1(rng, 0.7, n), r"MA(1): $\theta=0.7$",
         "Only adjacent values share noise", "#288269"),
    ]
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(3, 1, figsize=(9.0, 7.4), dpi=120,
                             sharex=True, sharey=True, facecolor="white")
    for ax, (path, title, note, color) in zip(axes, cases):
        ax.set_facecolor("white")
        ax.axhline(0, color="#65717a", linewidth=1)
        ax.plot(np.arange(n), path, color=color, linewidth=1.6)
        ax.set(title=title, ylabel=r"$X_t$", ylim=(-3.7, 3.7), xlim=(0, n - 1),
               yticks=[-3, 0, 3])
        ax.text(0.985, 0.9, note, transform=ax.transAxes, ha="right",
                color=color, fontsize=11,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
        ax.grid(axis="y", color="#e3e7ea")
        ax.spines[["top", "right"]].set_visible(False)
    axes[-1].set_xlabel("Time t (observation intervals)")
    fig.suptitle("Random paths with the same mean 0 and stationary variance 1", fontsize=15)
    fig.text(0.5, 0.012,
             "Gaussian noise; stationary initial states; seed 20261012. These are finite random examples.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.035, 1, 0.955), h_pad=1.3)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
