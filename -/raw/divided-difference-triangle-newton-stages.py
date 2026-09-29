"""Draw an original divided-difference ledger and incremental Newton fit.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media; writes this script's basename.png to the current directory.
"""
from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    nodes = [-1, 0, 2, 3]
    columns = [[Fraction(x**3 - 2*x + 1) for x in nodes]]
    for k in range(1, len(nodes)):
        old = columns[-1]
        columns.append([(old[i+1]-old[i]) / (nodes[i+k]-nodes[i])
                        for i in range(len(nodes)-k)])
    assert columns == [[2, 1, 5, 22], [-1, 2, 17], [1, 5], [1]]
    blue, gray, green = '#1967a5', '#64748b', '#167343'
    plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white'})
    fig = plt.figure(figsize=(9.6, 7.2), layout='constrained')
    gs = fig.add_gridspec(2, 1, height_ratios=[1.5, 1])
    ax = fig.add_subplot(gs[0])
    ax.set(xlim=(-0.8, 8.6), ylim=(-0.65, 4.25))
    ax.axis('off')
    ax.set_title('Divided differences feed successive Newton terms', fontsize=16, pad=12)
    ax.text(4, 3.95, r'$f(x)=x^3-2x+1$  at nodes $(-1,0,2,3)$', ha='center')
    xs = [0.9, 3.0, 5.1, 7.2]
    ax.text(-0.25, 3.55, 'node', ha='center', color=gray)
    for k in range(4):
        ax.text(xs[k], 3.55, ['value', '1st order', '2nd order', '3rd order'][k],
                ha='center', color=gray)
    for k in range(1, 4):
        for i in range(4-k):
            dest = (xs[k], 3-i-k/2)
            for j in [i, i+1]:
                src = (xs[k-1], 3-j-(k-1)/2)
                ax.annotate('', xy=(dest[0]-0.24, dest[1]),
                            xytext=(src[0]+0.24, src[1]),
                            arrowprops={'arrowstyle': '->', 'color': '#cbd5e1', 'lw': 1.3},
                            zorder=0)
    for i, node in enumerate(nodes):
        ax.text(-0.25, 3-i, str(node), va='center', ha='center', color=gray)
    for k, column in enumerate(columns):
        for i, value in enumerate(column):
            x, y = xs[k], 3-i-k/2
            ax.add_patch(FancyBboxPatch((x-0.25, y-0.2), 0.5, 0.4,
                         boxstyle='round,pad=0.07', facecolor='#e7f1fb' if i==0 else 'white',
                         edgecolor=blue if i==0 else '#cbd5e1', linewidth=1.5))
            ax.text(x, y, str(value), ha='center', va='center', fontsize=15,
                    color=blue if i==0 else '#1e293b')
    ax.text(4, -0.45, r'Blue entries: Newton coefficients $(2,-1,1,1)$',
            color=blue, ha='center')
    ax2 = fig.add_subplot(gs[1])
    ax2.axis('off')
    ax2.set_title('Each correction keeps the earlier node values', fontsize=14, pad=10)
    rows = [
        [r'$p_0=2$', r'$-1$', '—', r'$2$', r'$2$'],
        [r'$p_1=1-x$', r'$0$', r'$2$', r'$-(x+1)=-1$', r'$1$'],
        [r'$p_2=x^2+1$', r'$2$', r'$-1$', r'$(x+1)x=6$', r'$5$'],
        [r'$p_3=x^3-2x+1$', r'$3$', r'$10$', r'$(x+1)x(x-2)=12$', r'$22$'],
    ]
    table = ax2.table(cellText=rows,
                      colLabels=['New interpolant', 'New node', 'Before', 'Added at new node', 'After'],
                      colWidths=[0.25, 0.12, 0.10, 0.41, 0.12],
                      cellLoc='center', bbox=[0, 0.21, 1, 0.75])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor('#d7dee7')
        if row==0:
            cell.set_facecolor('#edf2f7')
            cell.set_text_props(weight='bold', fontsize=10)
        elif col==4:
            cell.set_facecolor('#e9f5ed')
            cell.set_text_props(color=green)
    ax2.text(0.5, 0.06, 'Every correction factor vanishes at all earlier nodes.',
             transform=ax2.transAxes, ha='center', color=gray)
    fig.savefig(Path(__file__).stem+'.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
