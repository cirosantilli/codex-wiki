"""Plot the von Mangoldt divisor weights of 12; Python 3.14, Matplotlib 3.10.7.

Run from _media; the opaque white PNG is written to the current directory.
"""
from math import isclose, log
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def prime_power_base(n):
    """Return the prime base of a positive-exponent prime power, or None."""
    if n < 2:
        return None
    base = 2
    while n % base:
        base += 1
    while n % base == 0:
        n //= base
    return base if n == 1 else None


def divisor_data(n):
    divisors = [d for d in range(1, n + 1) if n % d == 0]
    bases = [prime_power_base(d) for d in divisors]
    weights = np.array([log(p) if p else 0.0 for p in bases])
    return divisors, bases, weights


def main():
    divisors, bases, weights = divisor_data(12)
    assert divisors == [1, 2, 3, 4, 6, 12]
    assert bases == [None, 2, 3, 2, None, None]
    assert isclose(float(weights.sum()), log(12), abs_tol=1e-14)
    colors = {2: "#256aa5", 3: "#ce731e", None: "#79818a"}
    labels = ["0", r"$\log 2$", r"$\log 3$", r"$\log 2$", "0", "0"]
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.9), dpi=120,
                             gridspec_kw={"width_ratios": [3, 1]}, layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle(r"Divisor weights recover $\log 12$", fontsize=19)
    ax, total_ax = axes
    ax.set_facecolor("white")
    total_ax.set_facecolor("white")
    positions = np.arange(len(divisors))
    ax.bar(positions, weights, color=[colors[p] for p in bases], width=0.64, zorder=3)
    for pos, weight, label in zip(positions, weights, labels):
        ax.text(pos, weight + 0.045, label, ha="center", va="bottom", fontsize=13)
        if weight == 0:
            ax.plot(pos, 0, "o", color=colors[None], markersize=5, clip_on=False, zorder=4)
    ax.set_xticks(positions, divisors)
    ax.set(xlabel=r"Positive divisor $d$ of 12", ylabel=r"Weight $\Lambda(d)$",
           ylim=(0, 1.45), title=r"Only $2$, $3$, and $4$ contribute")
    ax.grid(axis="y", color="#e0e4e8", zorder=0)
    bottom = 0.0
    for p in (2, 2, 3):
        weight = log(p)
        total_ax.bar(0, weight, bottom=bottom, color=colors[p], width=0.7,
                     edgecolor="white", linewidth=1.5, zorder=3)
        total_ax.text(0, bottom + weight / 2, rf"$\log {p}$", ha="center",
                      va="center", color="white", fontsize=14)
        bottom += weight
    total_ax.set_xticks([0], [r"$2\log 2+\log 3$"])
    total_ax.set(xlim=(-0.65, 0.65), ylim=(0, 2.9), ylabel="Total weight",
                 title=r"$12=2^2\cdot3$")
    total_ax.text(0, bottom + 0.07, r"$\log 12$", ha="center", fontsize=15)
    total_ax.grid(axis="y", color="#e0e4e8", zorder=0)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
