"""Exact three-light-flavor weight construction; emits PNG in the working directory."""
from fractions import Fraction
from itertools import combinations_with_replacement
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

FLAVORS = {
    'u': (Fraction(1, 2), Fraction(1, 3), Fraction(2, 3)),
    'd': (Fraction(-1, 2), Fraction(1, 3), Fraction(-1, 3)),
    's': (Fraction(0), Fraction(-2, 3), Fraction(-1, 3)),
}


def states():
    """Yield symmetric flavor occupation states and exact (I3,Y,Q) labels."""
    for parts in combinations_with_replacement('uds', 3):
        yield ''.join(parts), tuple(sum((FLAVORS[p][i] for p in parts), Fraction(0)) for i in range(3))


def main():
    plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 5.3), gridspec_kw={'width_ratios': [1, 1.6]}, constrained_layout=True)
    ax, bx = axes
    colors = {'u': '#176f9c', 'd': '#b26010', 's': '#77519b'}
    triangle = np.array([[float(FLAVORS[p][0]), float(FLAVORS[p][1])] for p in 'uds'] + [[float(FLAVORS['u'][0]), float(FLAVORS['u'][1])]])
    ax.plot(triangle[:, 0], triangle[:, 1], color='#bdc6ce', lw=1.6)
    for p, (i3, y, q) in FLAVORS.items():
        ax.scatter(float(i3), float(y), s=100, color=colors[p], zorder=3)
        ax.annotate(f'{p}   Q={q}', (float(i3), float(y)), xytext=(0, 14 if p != 's' else -27), textcoords='offset points', ha='center', fontsize=12)
    ax.set(xlim=(-.86, .86), ylim=(-1.03, .76), xlabel=r'Isospin component $I_3$', ylabel=r'Flavor hypercharge $Y=B+S$', title='One quark: three flavor weights')
    ax.set_xticks([-.5, 0, .5], [r'$-1/2$', '0', r'$1/2$'])
    ax.set_yticks([-2/3, 0, 1/3], [r'$-2/3$', '0', r'$1/3$'])
    for name, (i3, y, q) in states():
        bx.scatter(float(i3), float(y), s=100, color=colors['s'] if name == 'sss' else '#176f9c', zorder=3)
        bx.annotate(f'{name}\nQ={q}', (float(i3), float(y)), xytext=(0, 10), textcoords='offset points', ha='center', va='bottom', fontsize=10.5)
    bx.plot([-1.5, 1.5, 0, -1.5], [1, 1, -2, 1], color='#bdc6ce', lw=1.5, zorder=0)
    bx.set(xlim=(-1.95, 1.95), ylim=(-2.42, 1.73), xlabel=r'Isospin component $I_3$', ylabel=r'Flavor hypercharge $Y=B+S$', title='Three symmetric flavors: ten weights')
    bx.set_xticks([-1.5, -1, -.5, 0, .5, 1, 1.5])
    bx.set_yticks([-2, -1, 0, 1])
    for panel in axes:
        panel.axhline(0, color='#c8ccd0', lw=.7, zorder=0)
        panel.axvline(0, color='#c8ccd0', lw=.7, zorder=0)
        panel.grid(alpha=.13)
        panel.spines[['top', 'right']].set_visible(False)
    fig.suptitle('Constituent addition fixes a flavor pattern, not a mass spectrum', fontsize=16)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=110, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
