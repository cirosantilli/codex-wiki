"""Show how reversing nodes changes Newton prefixes, but not the full fit.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media; writes this script's basename.png to the current directory.
"""
from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def coefficients(nodes):
    values = [Fraction(x**3-2*x+1) for x in nodes]
    result = [values[0]]
    for k in range(1, len(nodes)):
        values = [(values[i+1]-values[i])/(nodes[i+k]-nodes[i])
                  for i in range(len(nodes)-k)]
        result.append(values[0])
    return result


def main():
    assert coefficients([-1, 0, 2, 3]) == [2, -1, 1, 1]
    assert coefficients([3, 2, 0, -1]) == [22, 17, 5, 1]
    blue, orange, green = '#1967a5', '#b55a16', '#167343'
    plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white'})
    fig = plt.figure(figsize=(9.6, 6.8), layout='constrained')
    gs = fig.add_gridspec(2, 2, height_ratios=[0.9, 1.6])
    fig.suptitle('Different Newton paths, the same final polynomial', fontsize=16)
    for col, color, title, lines in [
        (0, blue, r'Order A: $(-1,0,2,3)$',
         [r'Coefficients: $(2,-1,1,\mathbf{1})$',
          r'$p_0=2$', r'$p_1=2-(x+1)$',
          r'$p_2=2-(x+1)+(x+1)x$',
          r'$p_3=p_2+(x+1)x(x-2)$']),
        (1, orange, r'Order B: $(3,2,0,-1)$',
         [r'Coefficients: $(22,17,5,\mathbf{1})$',
          r'$q_0=22$', r'$q_1=22+17(x-3)$',
          r'$q_2=22+17(x-3)+5(x-3)(x-2)$',
          r'$q_3=q_2+(x-3)(x-2)x$'])]:
        top = fig.add_subplot(gs[0, col])
        top.axis('off')
        top.set_title(title, color=color, fontsize=13)
        for i, line in enumerate(lines):
            top.text(0.03, 0.87-i*0.18, line, color=color, transform=top.transAxes,
                     va='center', fontsize=11.5)
    ax = fig.add_subplot(gs[1, :])
    x = np.linspace(-1.25, 3.25, 450)
    ax.plot(x, x*x+1, color=blue, lw=2, label=r'$p_2=x^2+1$ (fits $-1,0,2$)')
    ax.plot(x, 5*x*x-8*x+1, color=orange, lw=2, ls='--',
            label=r'$q_2=5x^2-8x+1$ (fits $3,2,0$)')
    ax.plot(x, x**3-2*x+1, color=green, lw=2.6,
            label=r'$p_3=q_3=x^3-2x+1$ (fits all four)')
    nodes = np.array([-1, 0, 2, 3])
    ax.scatter(nodes, nodes**3-2*nodes+1, color=green, edgecolor='white', s=65, zorder=5)
    ax.scatter([3], [10], facecolor='white', edgecolor=blue, s=60, lw=1.6, zorder=5)
    ax.scatter([-1], [14], facecolor='white', edgecolor=orange, s=60, lw=1.6, zorder=5)
    for node, before, after, label, color, labelx in [
        (3, 10, 22, '+12', blue, 2.66), (-1, 14, 2, '−12', orange, -0.73)]:
        ax.annotate('', xy=(node, after), xytext=(node, before),
                    arrowprops={'arrowstyle': '->', 'lw': 1.8, 'color': color})
        ax.text(labelx, (before+after)/2, label, color=color, fontsize=12,
                va='center', ha='center', bbox={'facecolor':'white', 'edgecolor':'none', 'pad':2})
    ax.set(xlim=(-1.25, 3.25), ylim=(-4, 29), xlabel='x', ylabel='Interpolant value',
           xticks=[-1, 0, 1, 2, 3])
    ax.grid(alpha=0.18)
    ax.legend(loc='upper center', fontsize=10.5, framealpha=0.96)
    ax.spines[['top', 'right']].set_visible(False)
    fig.savefig(Path(__file__).stem+'.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
