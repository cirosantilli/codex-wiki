"""Exact block inversion example; save the matching PNG in the working directory."""

from fractions import Fraction as F
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def verify():
    m = [[F(2), F(0), F(1)], [F(0), F(3), F(2)], [F(1), F(2), F(5)]]
    numerators = [[11, 2, -3], [2, 9, -4], [-3, -4, 6]]
    inv = [[F(v, 19) for v in row] for row in numerators]
    for a, b in ((m, inv), (inv, m)):
        assert [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)]
                for i in range(3)] == [[F(i == j) for j in range(3)] for i in range(3)]
    answer = [F(23, 19), F(-1, 19), F(11, 19)]
    assert [sum(m[i][j]*answer[j] for j in range(3)) for i in range(3)] == [3, 1, 4]
    assert F(5)-F(1, 2)-F(4, 3) == F(19, 6)
    return m, inv


def matrix(ax, values, name):
    colours = {(True, True): '#dceaf6', (True, False): '#ffe9cf',
               (False, True): '#e7ddf1', (False, False): '#daf0e6'}
    for i, row in enumerate(values):
        for j, value in enumerate(row):
            ax.add_patch(Rectangle((j, 2-i), 1, 1, facecolor=colours[(i < 2, j < 2)],
                                   edgecolor='white', linewidth=1))
            label = str(value.numerator) if value.denominator == 1 else f'{value.numerator}/{value.denominator}'
            ax.text(j+.5, 2.5-i, label, fontsize=15, ha='center', va='center')
    ax.plot([2, 2], [0, 3], color='#555555', linewidth=2)
    ax.plot([0, 3], [1, 1], color='#555555', linewidth=2)
    ax.set(xlim=(0, 3), ylim=(0, 3), aspect='equal', title=name)
    ax.axis('off')


def main():
    m, inv = verify()
    fig = plt.figure(figsize=(9.4, 4.2), dpi=125, layout='constrained', facecolor='white')
    gs = fig.add_gridspec(2, 3, height_ratios=[5, 1], width_ratios=[3, 2.8, 3])
    matrix(fig.add_subplot(gs[0, 0]), m, r'Original matrix $M$')
    matrix(fig.add_subplot(gs[0, 2]), inv, r'Inverse $M^{-1}$')
    ax = fig.add_subplot(gs[0, 1]); ax.axis('off')
    ax.text(.5, .80, r'$A=\mathrm{diag}(2,3)$', ha='center', fontsize=14)
    ax.text(.5, .64, r'$S=5-\frac{1}{2}-\frac{4}{3}=\frac{19}{6}$', ha='center', fontsize=16)
    ax.annotate('', xy=(.98, .43), xytext=(.02, .43),
                arrowprops={'arrowstyle': '->', 'lw': 2, 'color': '#333333'})
    ax.text(.5, .26, r'Lower-right block: $S^{-1}=6/19$', ha='center', fontsize=11)
    ax.text(.5, .13, r'Not $D^{-1}=1/5$', ha='center', fontsize=11)
    note = fig.add_subplot(gs[1, :]); note.axis('off')
    note.text(.5, .5, r'$M^{-1}(3,1,4)^T=(23,-1,11)^T/19$; both matrix products give $I_3$',
              ha='center', va='center', fontsize=13)
    fig.suptitle('Coupling changes the inverse of the retained block', fontsize=15)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
