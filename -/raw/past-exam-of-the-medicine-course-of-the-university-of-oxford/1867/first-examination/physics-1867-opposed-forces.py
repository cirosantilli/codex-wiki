"""Original opposed-force diagrams; write the PNG to CWD.

Tested with Python 3.14.4, Matplotlib 3.10.7+dfsg1, NumPy 2.3.5.
Dependencies: repository pyproject.toml.
"""
from pathlib import Path
import os
root = next(p for p in Path(__file__).resolve().parents if (p / 'ourbigbook.json').is_file())
os.environ.setdefault('MPLCONFIGDIR', str(root / '_out/matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def arrow(ax, x, value, label, color):
    ax.annotate('', (x, value*0.45), (x, 0),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=2.8, mutation_scale=17))
    ax.text(x+0.12, value*0.24, label, color=color, fontsize=12, va='center')


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), layout='constrained')
    fig.set_facecolor('white')
    for ax in axes:
        ax.set_facecolor('white')
        ax.axhline(0, color='#888888', lw=1)
        ax.set(ylim=(-3, 3), yticks=[], xlabel='Position along the body (m)')
        for spine in ['left', 'right', 'top']:
            ax.spines[spine].set_visible(False)
    ax = axes[0]
    ax.set(xlim=(-2, 3.2), xticks=[-4/3, 0, 2],
           xticklabels=[r'$-4/3$', '0', '2'], title='Unequal forces: equivalent resultant outside')
    arrow(ax, 0, 5, r'$P=5$ N', '#24618b')
    arrow(ax, 2, -2, r'$Q=2$ N', '#24618b')
    ax.axvline(-4/3, color='#c46c25', ls=':', lw=1)
    arrow(ax, -4/3, 3, r'$R=3$ N', '#c46c25')
    ax.text(0.5, -2.4, 'Blue: original forces\nOrange: their equivalent, not an added force',
            ha='center', va='center', fontsize=11)
    ax = axes[1]
    ax.set(xlim=(-0.8, 3.2), xticks=[0, 2], title='Equal forces: a clockwise couple')
    arrow(ax, 0, 5, r'$P=5$ N', '#24618b')
    arrow(ax, 2, -5, r'$Q=5$ N', '#24618b')
    ax.text(1, 2.65, r'$R=0,\quad \tau=-Pd=-10\ {\rm N\,m}$', ha='center')
    ax.text(1, -2.65, 'A nonzero couple has no equivalent single force.', ha='center', fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
