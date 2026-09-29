"""Compound count coefficients, not observations; Python 3.14 / matplotlib 3.10.7.

Run from _media; writes the matching PNG to the current directory.
"""
from decimal import Decimal, localcontext
from math import factorial
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def model_coefficients(limit=20):
    with localcontext() as ctx:
        ctx.prec = 60
        p = [Decimal(-2).exp()]
        for n in range(1, limit+1):
            p.append((p[n-1] + (2*p[n-2] if n > 1 else 0))/n)
        for n, value in enumerate(p):
            exact = p[0]*sum((Decimal(1)/Decimal(factorial(n-2*b)*factorial(b))
                              for b in range(n//2+1)), Decimal())
            assert abs(value-exact) < Decimal('1e-58')
        tail = Decimal(1) - sum(p)
        return p, tail


def main():
    p, tail = model_coefficients()
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
    fig = plt.figure(figsize=(10, 6.5), dpi=120, facecolor='white')
    fig.suptitle('A random number of jumps changes both the mean and the spread',
                 fontsize=17, y=.97)
    flow = fig.add_axes([.03, .64, .94, .25])
    flow.set(xlim=(0, 1), ylim=(0, 1))
    flow.axis('off')
    boxes = [(.015, .25, .24, '#466b9c', 'Draw the count', r'$N\sim\mathrm{Poisson}(2)$'),
             (.365, .25, .28, '#168477', 'Attach N independent jumps', r'$P(Y_j=1)=P(Y_j=2)=1/2$'),
             (.755, .25, .23, '#99538a', 'Add the jumps', r'$S=\sum_{j=1}^{N}Y_j$')]
    for x, y, width, color, title, formula in boxes:
        flow.add_patch(FancyBboxPatch((x,y), width, .60,
                       boxstyle='round,pad=0.008,rounding_size=0.025',
                       facecolor=color+'15', edgecolor=color, linewidth=1.8))
        flow.text(x+width/2, y+.43, title, ha='center', va='center', fontsize=11)
        flow.text(x+width/2, y+.20, formula, ha='center', va='center', fontsize=13)
    for a, b in [(.27, .35), (.66, .74)]:
        flow.annotate('', xy=(b,.55), xytext=(a,.55),
                      arrowprops={'arrowstyle':'->', 'lw':2, 'color':'#405060'})
    flow.text(.5, .06, r'The count is independent of the entire jump sequence; $N=0$ gives $S=0$.',
              ha='center', fontsize=11)
    fig.text(.5, .60, r'$G_S(s)=G_N(G_Y(s))=e^{s+s^2-2}$', ha='center', fontsize=18)
    ax = fig.add_axes([.085, .17, .87, .35])
    ax.bar(range(21), [float(v) for v in p], color='#168477', width=.72)
    ax.set(xlim=(-.7, 20.8), ylim=(0, .235), xticks=range(0,21,2),
           xlabel='Aggregate count n', ylabel=r'$p_n=P(S=n)$')
    ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='y', alpha=.18)
    ax.set_axisbelow(True)
    ax.text(.985, .94, r'$p_0=e^{-2},\quad np_n=p_{n-1}+2p_{n-2}$'+'\n'
            +r'$\mathbb{E}[S]=3,\quad\mathrm{Var}(S)=5$'+'\n'
            +f'Omitted P(S > 20) = {tail:.6E}',
            transform=ax.transAxes, ha='right', va='top', fontsize=12,
            bbox={'facecolor':'white','edgecolor':'#b9c7cf','boxstyle':'round,pad=.6'})
    fig.text(.5, .065, 'Calculated model coefficients for n = 0,…,20 • no observed data • no renormalization',
             ha='center', fontsize=12)
    fig.savefig(Path(__file__).stem+'.png', facecolor='white')
    plt.close(fig)
    print(f'P(S > 20) = {tail}')


if __name__ == '__main__':
    main()
