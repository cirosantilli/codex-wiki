"""SU(3) weights in the examination's Cartan coordinates.

Run with Python 3.14 and matplotlib 3.10; output is written to the caller's CWD.
"""
from math import sqrt
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT3 = sqrt(3)
OUTPUT = Path('paper-45-su3-weights.png')


def coordinates(h1, h2):
    return h1, (h1 + 2 * h2) / ROOT3


def monomial(a, b, c):
    terms = []
    for i, power in enumerate((a, b, c), 1):
        if power:
            terms.append(f'z_{i}' + (f'^{{{power}}}' if power > 1 else ''))
    return '$' + ''.join(terms) + '$'


def main():
    fundamental = [(1, 0, '$e_1$'), (-1, 1, '$e_2$'), (0, -1, '$e_3$')]
    adjoint = [(2, -1, '$E_{12}$'), (-2, 1, '$E_{21}$'),
               (-1, 2, '$E_{23}$'), (1, -2, '$E_{32}$'),
               (1, 1, '$E_{13}$'), (-1, -1, '$E_{31}$'),
               (0, 0, '$H_1,H_2$ (2 states)')]
    cubic = [(a-b, b-c, monomial(a, b, c))
             for c in range(4) for b in range(4-c) for a in [3-b-c]]
    panels = [(fundamental, '$(1,0)$: dimension 3'),
              (adjoint, '$(1,1)$: dimension 8'),
              (cubic, '$(3,0)$: dimension 10')]
    fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.4), layout='constrained',
                             facecolor='white')
    for ax, (states, title) in zip(axes, panels):
        ax.set_facecolor('white')
        ax.axhline(0, color='#b9c0c9', linewidth=.8, zorder=0)
        ax.axvline(0, color='#b9c0c9', linewidth=.8, zorder=0)
        ax.set_xlim(-3.8, 3.8)
        ax.set_ylim(-4.2, 2.6)
        ax.set_aspect('equal')
        ax.set_xticks(range(-3, 4))
        ax.set_yticks([-2*ROOT3, -ROOT3, 0, ROOT3],
                      ['$-2\\sqrt{3}$', '$-\\sqrt{3}$', '0', '$\\sqrt{3}$'])
        ax.grid(alpha=.12)
        for h1, h2, label in states:
            x, y = coordinates(h1, h2)
            ax.scatter(x, y, s=48 if (h1, h2) != (0, 0) else 78,
                       color='#215e9b', zorder=3)
            ax.annotate(label, (x, y), xytext=(0, 9), textcoords='offset points',
                        ha='center', va='bottom', fontsize=10)
        ax.set_xlabel('$h_1$', fontsize=12)
        ax.set_ylabel('$(h_1+2h_2)/\\sqrt{3}$', fontsize=12)
        ax.set_title(title, fontsize=13, pad=14)
        ax.spines[['top', 'right']].set_visible(False)
    fig.savefig(OUTPUT, dpi=150, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
