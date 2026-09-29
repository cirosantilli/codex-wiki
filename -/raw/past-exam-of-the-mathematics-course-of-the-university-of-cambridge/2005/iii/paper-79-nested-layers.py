#!/usr/bin/env python3
"""Plot matched square-root reaction layers; write the opaque PNG to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Dependencies are declared in the repository's pyproject.toml.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

EPSILON = 0.002
K = 1.0


def primitive_from_log_distance(log_distance, above=True):
    """Stable Phi for sqrt(Y)=k(1 +/- exp(log_distance))."""
    sign = 1 if above else -1
    w = K * (1 + sign * np.exp(log_distance))
    s = np.sqrt(K + 2 * w)
    log_ratio = np.log(2 * K) + log_distance - 2 * np.log(s + np.sqrt(3 * K))
    return np.sqrt(2 * K) * log_ratio + np.sqrt(6 * (K + 2 * w))


def invert_primitive(target, above=True):
    target = np.asarray(target, dtype=float)
    lo = np.full_like(target, -1000.0)
    hi = np.full_like(target, 100.0 if above else 0.0)
    for _ in range(70):
        mid = (lo + hi) / 2
        phi = primitive_from_log_distance(mid, above)
        lo = np.where(phi < target, mid, lo)
        hi = np.where(phi >= target, mid, hi)
    u = (lo + hi) / 2
    return (K * (1 + (1 if above else -1) * np.exp(u))) ** 2


def left(xi):
    values = invert_primitive(primitive_from_log_distance(0.0, False) - np.asarray(xi), False)
    return np.where(np.asarray(xi) == 0, 0.0, values)


def right(xi):
    return invert_primitive(xi, True)


def transition_position():
    # At y(1)=1, sqrt(Y)=1/epsilon, with Y=y/epsilon^2.
    boundary_log_distance = np.log(1 / (EPSILON * K) - 1)
    return 1 - EPSILON * primitive_from_log_distance(boundary_log_distance)


def main():
    x_star = transition_position()
    x = np.unique(np.r_[np.linspace(0, 1, 1800), np.linspace(0, 16 * EPSILON, 250),
                        np.linspace(x_star - 15 * EPSILON, x_star + 25 * EPSILON, 500)])
    x = x[(x >= 0) & (x <= 1)]
    composite = EPSILON**2 * (left(x / EPSILON) + right((x - x_star) / EPSILON) - K**2)
    plt.rcParams.update({'font.size': 11, 'axes.titlesize': 12, 'axes.labelsize': 11})
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.4), dpi=100, facecolor='white')
    ax = axes[0]
    ax.plot(x, composite, color='#1466a3', lw=2.4, label='Matched profile')
    ax.axvline(x_star, color='#a45424', ls='--', lw=1.2, label='Thin right transition')
    ax.set(xlabel=r'$x$', ylabel=r'$y$', xlim=(0, 1), ylim=(-0.035, 1.08), title='Full interval')
    ax.text(0.13, 0.11, r'Plateau: $y\simeq\varepsilon^2 k^2$', fontsize=10)
    ax.legend(loc='upper left', fontsize=9)
    ax = axes[1]
    xi = np.linspace(0, 14, 450)
    ax.plot(xi, left(xi) / K**2, color='#1466a3', lw=2.4)
    ax.axhline(1, color='#777777', ls='--', lw=1.2)
    ax.set(xlabel=r'$\xi=x/\varepsilon$', ylabel=r'$y/(\varepsilon^2 k^2)$',
           xlim=(0, 14), ylim=(-0.04, 1.12), title=r'Left layer: width $O(\varepsilon)$')
    ax = axes[2]
    xi = np.linspace(-12, 25, 600)
    ax.semilogy(xi, right(xi) / K**2, color='#1466a3', lw=2.4, label='Thin-layer profile')
    xi_asymp = np.linspace(7, 25, 240)
    ax.semilogy(xi_asymp, xi_asymp**4 / (144 * K**2), color='#a45424', ls='--', lw=1.5,
                label=r'Overlap: $\xi^4/(144k^2)$')
    ax.set(xlabel=r'$\xi=(x-x_*)/\varepsilon$', ylabel=r'$y/(\varepsilon^2 k^2)$',
           xlim=(-12, 25), title='Thin transition into broad right layer')
    ax.legend(loc='upper left', fontsize=9)
    for ax in axes:
        ax.grid(alpha=0.18)
        ax.spines[['top', 'right']].set_visible(False)
    fig.suptitle(r'Square-root reaction layers: $\varepsilon=0.002$, $k=1$', fontsize=14)
    fig.subplots_adjust(left=0.063, right=0.985, bottom=0.17, top=0.78, wspace=0.36)
    output = Path.cwd() / 'paper-79-nested-layers.png'
    fig.savefig(output, facecolor='white', transparent=False)
    plt.close(fig)
    assert output.is_file()


if __name__ == '__main__':
    main()
