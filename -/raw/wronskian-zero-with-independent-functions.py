"""Explain how a zero Wronskian can miss global independence.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
Run from _media; the PNG is written to the current working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white',
                         'axes.facecolor': 'white', 'savefig.facecolor': 'white'})
    blue, orange, green = '#2269a8', '#c65b18', '#28704e'
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.5))
    fig.subplots_adjust(left=0.075, right=0.97, bottom=0.25, top=0.78, wspace=0.28)
    fig.suptitle('Zero Wronskian, yet independent functions', y=0.97, fontsize=17)
    x = np.linspace(-1.25, 1.25, 601)
    f = x**4
    g = x*np.abs(x)**3
    ax = axes[0]
    ax.plot(x, f, color=blue, lw=3, label=r'$f=x^4$')
    ax.plot(x, g, color=orange, lw=2.5, ls='--', label=r'$g=x|x|^3$')
    ax.scatter([-1, 1], [1, 1], color=blue, zorder=4)
    ax.scatter([-1, 1], [-1, 1], color=orange, s=20, zorder=5)
    ax.axvline(0, color='0.6', ls=':', lw=1)
    ax.axhline(0, color='0.6', lw=0.8)
    ax.set(xlabel=r'$x$', ylabel='Function value', title=r'Both have $f(0)=g(0)=f\prime(0)=g\prime(0)=0$')
    ax.legend(loc='lower right', fontsize=10, frameon=False)
    ax.grid(alpha=0.15)

    ax = axes[1]
    ax.plot([-1.25, 0], [-1, -1], color=orange, lw=3)
    ax.plot([0, 1.25], [1, 1], color=orange, lw=3, label=r'$g/f$ (undefined at $0$)')
    ax.scatter([0, 0], [-1, 1], facecolors='white', edgecolors=orange, s=65, lw=2, zorder=5)
    ax.plot(x, np.zeros_like(x), color=green, lw=2, ls='--', label=r'$W(f,g)=0$ everywhere')
    ax.text(-0.66, -0.72, r'$g=-f$', ha='center', color=orange)
    ax.text(0.65, 0.72, r'$g=f$', ha='center', color=orange)
    ax.set(xlabel=r'$x$', ylim=(-1.55, 1.55), title='Local proportionality changes across zero')
    ax.set_yticks([-1, 0, 1])
    ax.text(0, 0.18, r'$W(f,g)=0$ everywhere', ha='center', color=green, fontsize=10)
    ax.set_ylabel(r'Ratio $g/f$; Wronskian $W$')
    ax.grid(alpha=0.15)
    fig.text(0.5, 0.065, r'$af+bg=0$: at $x=-1$, $a-b=0$; at $x=1$, $a+b=0$. Hence $a=b=0$.',
             ha='center', fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100, transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
