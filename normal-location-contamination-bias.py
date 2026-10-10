"""Exact population bias and its local influence approximation.

Models, not sampled observations: F_e = (1-e) N(0,1) + e delta_x.
The median uses the generalized inverse, and Huber roots use bisection
of an analytic normal-score expectation with known scale s=1.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the output basename matches this root generator.
"""

from math import erf, exp, pi, sqrt
from pathlib import Path
from statistics import NormalDist

import matplotlib.pyplot as plt
import numpy as np


K = 1.345
NORMAL = NormalDist()
DENOMINATOR = erf(K / sqrt(2))


def phi(t):
    return exp(-t * t / 2) / sqrt(2 * pi)


def cdf(t):
    return (1 + erf(t / sqrt(2))) / 2


def clip(t):
    return max(-K, min(t, K))


def normal_score(t):
    """E[clip(Z-t, -K, K)], Z standard normal, evaluated analytically."""
    a, b = t - K, t + K
    return phi(a) - phi(b) - t * (cdf(b) - cdf(a)) + K * (1 - cdf(b) - cdf(a))


def huber_root(epsilon, x):
    """Unique population root for epsilon < 1/2; no Monte Carlo."""
    if not 0 <= epsilon < 0.5:
        raise ValueError("Require 0 <= epsilon < 1/2")
    lo, hi = min(0.0, x) - K, max(0.0, x) + K
    for _ in range(100):
        t = (lo + hi) / 2
        score = (1 - epsilon) * normal_score(t) + epsilon * clip(x - t)
        if score > 0:
            lo = t
        else:
            hi = t
    return (lo + hi) / 2


def median_functional(epsilon, x):
    """Generalized-inverse median of the normal plus point-mass mixture."""
    if not 0 <= epsilon < 0.5:
        raise ValueError("Require 0 <= epsilon < 1/2")
    lower = NORMAL.inv_cdf((0.5 - epsilon) / (1 - epsilon))
    upper = NORMAL.inv_cdf(0.5 / (1 - epsilon))
    return max(lower, min(x, upper))


def main():
    fractions = np.linspace(0, 0.1, 201)
    colors = ["#2166ac", "#b35806", "#1b7837"]
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.5), layout="constrained")
    for ax, x in zip(axes, [1.0, 8.0]):
        actual = [fractions * x,
                  np.array([median_functional(e, x) for e in fractions]),
                  np.array([huber_root(e, x) for e in fractions])]
        influences = [x, sqrt(pi / 2), clip(x) / DENOMINATOR]
        for color, label, bias, influence in zip(colors, ["Mean", "Median", "Huber"], actual, influences):
            ax.plot(fractions, bias, color=color, lw=2.2, label=label)
            ax.plot(fractions, fractions * influence, color=color, lw=1.7, ls="--")
        ax.set(title=rf"Contaminating point $x={x:g}$", xlabel=r"Contamination fraction $\varepsilon$",
               ylabel="Population location bias")
        ax.grid(alpha=0.2)
        ax.legend(loc="upper left", fontsize=9)
        ax.set_xlim(0, 0.1)
        ax.set_ylim(bottom=0)
    fig.suptitle(r"$(1-\varepsilon)N(0,1)+\varepsilon\delta_x$: finite bias versus local prediction", fontsize=12)
    fig.supxlabel("Solid: exact functional (Huber: numerical root). Dashed: ε IF(x). Fixed Huber scale s=1, k=1.345.", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)
    for x in [1.0, 8.0]:
        for e in [0.01, 0.05]:
            print(f"x={x:g} epsilon={e:g}: mean={e*x:.9f}, median={median_functional(e,x):.9f}, "
                  f"Huber={huber_root(e,x):.9f}; local=({e*x:.9f}, {e*sqrt(pi/2):.9f}, "
                  f"{e*clip(x)/DENOMINATOR:.9f})")


if __name__ == "__main__":
    main()
