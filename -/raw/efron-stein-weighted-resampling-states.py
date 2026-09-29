"""Weighted one-coordinate replacement for a constructed Bernoulli model.

Tested with Python 3.14, matplotlib 3.10.7. Run from _media; output to CWD.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def main():
    p = (Fraction(3, 10), Fraction(3, 5))
    mass = {x: (p[0] if x[0] else 1-p[0]) * (p[1] if x[1] else 1-p[1])
            for x in product((0, 1), repeat=2)}
    terms = []
    for i in range(2):
        terms.append(sum(mass[x] * (p[i] if y else 1-p[i])
                         * (max(x)-max(x[:i]+(y,)+x[i+1:]))**2
                         for x in mass for y in (0, 1)))
    assert terms == [Fraction(21, 125), Fraction(42, 125)]
    plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white', 'savefig.facecolor': 'white'})
    fig = plt.figure(figsize=(11, 6.5), dpi=100)
    grid = fig.add_axes((0.035, 0.18, 0.57, 0.70))
    note = fig.add_axes((0.64, 0.17, 0.34, 0.70))
    grid.set(xlim=(-0.65, 2.65), ylim=(-0.65, 2.65))
    grid.axis('off'); note.axis('off')
    blue, orange, gray = '#1764a0', '#c56812', '#b5bbc3'
    for a, b in [((0, 1), (1, 1)), ((1, 0), (1, 1))]:
        grid.plot([2*a[0], 2*b[0]], [2*a[1], 2*b[1]], '--', color=gray, lw=2, zorder=1)
    for a, b, color, weight, axis in [((0, 0), (1, 0), blue, 0.084, 0),
                                      ((0, 0), (0, 1), orange, 0.168, 1)]:
        for reverse, shift in [(False, -0.13), (True, 0.13)]:
            u, v = (b, a) if reverse else (a, b)
            start = [2*u[0], 2*u[1]]; end = [2*v[0], 2*v[1]]
            start[1-axis] += shift; end[1-axis] += shift
            grid.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>', mutation_scale=17,
                                          shrinkA=40, shrinkB=40, lw=2, color=color, zorder=2))
            xy = (1, shift*2.6) if axis == 0 else (shift*2.5, 1)
            grid.text(*xy, f'{weight:.3f}', ha='center', va='center', color=color,
                      fontsize=11, bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})
    for x, q in mass.items():
        grid.text(2*x[0], 2*x[1], f'{x}\nP = {float(q):.2f}\nZ = {max(x)}',
                  ha='center', va='center', fontsize=11, zorder=4,
                  bbox={'boxstyle': 'round,pad=0.5', 'facecolor': '#edf5fc' if max(x)==0 else '#f4f5f7',
                        'edgecolor': '#617487', 'linewidth': 1.4})
    grid.text(1, 2.56, r'$X_1$ increases to the right; $X_2$ upward', ha='center', fontsize=12)
    grid.text(1, 1.57, 'Dashed edges:\nZ stays 1', ha='center', va='center', color='#66717d', fontsize=11)
    note.text(0, 0.96, 'Replace one input; keep the other.', weight='bold', fontsize=12, va='top')
    note.text(0, 0.86, r'$X_1\sim\mathrm{Bernoulli}(0.3)$'+'\n'+r'$X_2\sim\mathrm{Bernoulli}(0.6)$'+'\nIndependent inputs; '+r'$Z=\max(X_1,X_2)$', linespacing=1.65, va='top')
    note.text(0, 0.56, r'Resample $X_1$ when $X_2=0$'+'\n0.4 × (0.7 × 0.3 + 0.3 × 0.7)\n= 0.168', color=blue, linespacing=1.55, va='top')
    note.text(0, 0.32, r'Resample $X_2$ when $X_1=0$'+'\n0.7 × (0.4 × 0.6 + 0.6 × 0.4)\n= 0.336', color=orange, linespacing=1.55, va='top')
    note.text(0, 0.08, 'Bound = (0.168 + 0.336) / 2 = 0.252', weight='bold', fontsize=11)
    fig.suptitle('Efron–Stein: weight both directions of each effective replacement', y=0.97, fontsize=17)
    fig.text(0.5, 0.08, 'Arrow weights include the original state probability and the replacement probability.', ha='center', fontsize=12)
    fig.text(0.5, 0.035, 'Constructed model • A replacement can repeat the old value; such cases contribute zero.', ha='center', fontsize=11, color='#566271')
    fig.savefig(Path(__file__).stem+'.png', dpi=100, transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
