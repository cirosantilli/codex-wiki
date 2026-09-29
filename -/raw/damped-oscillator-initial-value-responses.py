"""Ideal free responses; run from _media. Python 3.14, matplotlib 3.10.7, numpy 2.3.5."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def response(tau, zeta, x0=1.0, v0=0.0):
    """Return X, dX/dtau, d²X/dtau² for X'' + 2*zeta*X' + X = 0."""
    tau = np.asarray(tau, dtype=float)
    if zeta < 1:
        w = np.sqrt(1 - zeta**2)
        a = x0
        b = (v0 + zeta*x0)/w
        c, s = np.cos(w*tau), np.sin(w*tau)
        e = np.exp(-zeta*tau)
        x = e*(a*c + b*s)
        v = e*((-zeta*a + w*b)*c + (-zeta*b - w*a)*s)
        acc = e*(((zeta**2 - w**2)*a - 2*zeta*w*b)*c
                 + ((zeta**2 - w**2)*b + 2*zeta*w*a)*s)
    elif zeta == 1:
        a, b = x0, v0 + x0
        e = np.exp(-tau)
        x = (a + b*tau)*e
        v = (b - a - b*tau)*e
        acc = (a - 2*b + b*tau)*e
    else:
        s = np.sqrt(zeta**2 - 1)
        slow = -1/(zeta + s)
        fast = -zeta - s
        a = (v0 - fast*x0)/(slow - fast)
        b = (slow*x0 - v0)/(slow - fast)
        es, ef = np.exp(slow*tau), np.exp(fast*tau)
        x = a*es + b*ef
        v = slow*a*es + fast*b*ef
        acc = slow**2*a*es + fast**2*b*ef
    return x, v, acc


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white',
                         'axes.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), layout='constrained')
    tau = np.linspace(0, 14, 1401)
    for zeta, color, label in [(0.25, '#2467a5', 'Underdamped: ζ = 0.25'),
                               (1, '#c13b35', 'Critical: ζ = 1'),
                               (2, '#27834d', 'Overdamped: ζ = 2')]:
        x, v, acc = response(tau, zeta)
        assert np.max(np.abs(acc + 2*zeta*v + x)) < 1e-12
        assert abs(x[0] - 1) < 1e-12 and abs(v[0]) < 1e-12
        axes[0].plot(tau, x, color=color, lw=2.3, label=label)
    axes[0].set(title='Release from rest', xlim=(0, 14), ylim=(-0.5, 1.06),
                xlabel='Dimensionless time τ = ω₀t', ylabel='Displacement X = x/x₀')
    axes[0].legend(loc='upper right', fontsize=9)
    axes[0].text(6.5, -0.43, 'X(0) = 1, X′(0) = 0', fontsize=10)
    tau = np.linspace(0, 7, 701)
    for v0, color in [(0, '#c13b35'), (-1, '#7b4f9f'), (-2, '#ad751a')]:
        x, v, acc = response(tau, 1, v0=v0)
        assert np.max(np.abs(acc + 2*v + x)) < 1e-12
        assert x[0] == 1 and v[0] == v0
        axes[1].plot(tau, x, color=color, lw=2.3,
                     label=rf"$X'(0)={v0:g}$")
    axes[1].scatter([1], [0], color='#ad751a', zorder=5)
    axes[1].annotate('One crossing at τ = 1', xy=(1, 0), xytext=(2.1, 0.28),
                     arrowprops={'arrowstyle': '->', 'color': '#555'}, fontsize=10)
    axes[1].set(title='Critical damping: initial velocity matters', xlim=(0, 7),
                ylim=(-0.22, 1.06), xlabel='Dimensionless time τ = ω₀t',
                ylabel='Displacement X = x/x₀')
    axes[1].legend(fontsize=9)
    for ax in axes:
        ax.axhline(0, color='#666', lw=0.8)
        ax.grid(alpha=0.17)
    fig.suptitle('Ideal viscous oscillator: X″ + 2ζX′ + X = 0', fontsize=14)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
