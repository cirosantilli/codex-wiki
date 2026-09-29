"""Plot theta, psi, and their exact prime-power gap through 10.

Python 3.14, Matplotlib 3.10.7, NumPy 2.3.5; run from _media.
The matching opaque white PNG is written to the current directory.
"""
from math import isclose, log
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def enumerated_weights(limit):
    """Sieve primes and enumerate their powers using integer multiplication."""
    primes = []
    for candidate in range(2, limit + 1):
        if all(candidate % p for p in primes if p * p <= candidate):
            primes.append(candidate)
    theta = np.zeros(limit + 1)
    psi = np.zeros(limit + 1)
    powers = []
    for p in primes:
        theta[p] = log(p)
        power, exponent = p, 1
        while power <= limit:
            psi[power] = log(p)
            powers.append((power, p, exponent))
            power *= p
            exponent += 1
    return theta, psi, sorted(powers)


def draw_stair(ax, values, color, label, offset=0):
    x = np.arange(len(values))
    ax.step(x, values, where="post", color=color, linewidth=2.5, label=label, zorder=3)
    for n in range(1, len(values)):
        if values[n] > values[n - 1]:
            ax.plot(n, values[n - 1], "o", markerfacecolor="white", markeredgecolor=color,
                    markersize=6 + offset, zorder=4)
            ax.plot(n, values[n], "o", color=color, markersize=6 + offset, zorder=5)


def main():
    theta_weights, psi_weights, powers = enumerated_weights(10)
    assert powers == [(2, 2, 1), (3, 3, 1), (4, 2, 2), (5, 5, 1),
                      (7, 7, 1), (8, 2, 3), (9, 3, 2)]
    theta, psi = np.cumsum(theta_weights), np.cumsum(psi_weights)
    gap = psi - theta
    assert isclose(theta[10], log(210), abs_tol=1e-14)
    assert isclose(psi[10], log(2520), abs_tol=1e-14)
    assert isclose(gap[10], log(12), abs_tol=1e-14)
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 1, figsize=(9, 7.2), dpi=120, sharex=True,
                             gridspec_kw={"height_ratios": [2, 1]}, layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("Prime weights and the extra prime-power jumps", fontsize=18)
    blue, orange, green = "#256aa5", "#ce731e", "#287b50"
    ax, gap_ax = axes
    for panel in axes:
        panel.set_facecolor("white")
        panel.set_xlim(0, 10.7)
        panel.set_xticks(range(11))
        panel.grid(axis="y", color="#e0e4e8", zorder=0)
    draw_stair(ax, psi, orange, r"$\psi(x)$: prime powers")
    draw_stair(ax, theta, blue, r"$\vartheta(x)$: primes", offset=-1)
    ax.set(ylabel="Accumulated natural-log weight", ylim=(-0.35, 9.4))
    ax.legend(loc="upper left", frameon=False)
    ax.text(10.15, psi[10] + 0.18, r"$\log2520$", ha="right", fontsize=13)
    ax.text(10.15, theta[10] + 0.18, r"$\log210$", ha="right", fontsize=13)
    draw_stair(gap_ax, gap, green, r"$\psi(x)-\vartheta(x)$")
    gap_ax.set(ylabel=r"Gap $\psi-\vartheta$", xlabel=r"Inclusive real cutoff $x$",
               ylim=(-0.18, 3.4))
    for n, label in [(4, r"$4=2^2$"), (8, r"$8=2^3$"), (9, r"$9=3^2$")]:
        gap_ax.annotate(label + "\n" + (r"$+\log2$" if n != 9 else r"$+\log3$"),
                        xy=(n, gap[n]), xytext=(n - 0.6, gap[n] + 0.6),
                        fontsize=11, ha="center", arrowprops={"arrowstyle": "-", "color": green})
    gap_ax.text(10.25, gap[10] - 0.35, r"$\log12$", ha="right", fontsize=13, color=green)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
