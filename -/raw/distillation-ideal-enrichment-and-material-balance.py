"""Original stipulated equilibrium and product-balance diagram. Python 3.14/matplotlib 3.10."""
from pathlib import Path
from fractions import Fraction
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np


def main():
    fig = plt.figure(figsize=(11.5, 6.5), dpi=140, facecolor='white')
    fig.text(.045, .95, 'Enrichment and recovery answer different questions', fontsize=19, weight='bold')
    fig.text(.045, .905, 'Stipulated models only • no named liquid • no measured data or temperature curve', fontsize=11, color='#555555')
    ax = fig.add_axes([.075, .23, .39, .60])
    u = np.linspace(0, 1, 500)
    ax.plot(u, 2*u/(1+u), color='#216c9a', lw=2.5, label=r'$y=2x/(1+x)$, $\alpha=2$')
    ax.plot(u, u, color='#929da5', lw=1.2, ls='--', label=r'$y=x$')
    stages = [Fraction(3, 10)]
    for _ in range(3):
        stages.append(2*stages[-1]/(1+stages[-1]))
    for i, (a, b) in enumerate(zip(stages, stages[1:])):
        x, y = float(a), float(b)
        ax.plot([x, x, y], [x, y, y], color='#c27025', lw=1.7)
        ax.scatter([x], [y], color='#c27025', zorder=5, s=34)
        ax.annotate(f'{i+1}', (x, y), xytext=(-14, 6), textcoords='offset points', fontsize=10, color='#9b4e16')
    ax.scatter([.3], [.3], color='#c27025', s=26, zorder=5)
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel=r'Liquid mole fraction $x$', ylabel=r'Equilibrium vapor mole fraction $y$')
    ax.set_title('A. Formal repeated equilibration', loc='left', fontsize=13, pad=14)
    ax.set_aspect('equal')
    ax.legend(loc='upper left', fontsize=10, frameon=False)
    ax.grid(alpha=.15)
    ax.spines[['top', 'right']].set_visible(False)
    fig.text(.067, .13, '0.300000 → 0.461538 → 0.631579 → 0.774194', fontsize=11, color='#9b4e16')
    fig.text(.067, .055, 'Condense completely between formal steps.\nNot a reflux design or a single pot’s time history.', fontsize=10.5, linespacing=1.65)

    bx = fig.add_axes([.52, .22, .46, .61])
    bx.set(xlim=(-.2, 10), ylim=(0, 10))
    bx.axis('off')
    bx.text(0, 10, 'B. Independent overall material balance', fontsize=13, va='bottom')
    def box(x, y, w, h, text, fill):
        bx.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.14',
                                   facecolor=fill, edgecolor='#627d8e', lw=1.4))
        bx.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=11, linespacing=1.6)
    box(.1, 4.5, 2.4, 2.1, 'Feed\nF = 1 mol\nz = 0.35', '#eef3f7')
    box(3.3, 4.5, 2.2, 2.1, 'Separation\noverall\nboundary', '#f7f5ed')
    box(6.7, 6.6, 3.0, 2.2, 'Distillate\nD = 5/14 mol\nxᴅ = 0.80', '#e5f1f7')
    box(6.7, 2.0, 3.0, 2.2, 'Bottoms\nB = 9/14 mol\nxʙ = 0.10', '#f7eadb')
    for start, end in [((2.65, 5.55), (3.1, 5.55)), ((5.65, 5.8), (6.5, 7.5)), ((5.65, 5.2), (6.5, 3.1))]:
        bx.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>', mutation_scale=16, lw=1.5, color='#496b7d'))
    bx.text(0.15, .4, r'$D+B=1$ mol' '\n' r'$0.80D+0.10B=0.35$ mol', fontsize=12, linespacing=1.7)
    fig.text(.535, .14, 'Component A recovered in distillate: 40/49 ≈ 81.63%', fontsize=10.5, color='#216c9a')
    fig.text(.535, .045, 'Balance only: does not determine heat,\ntemperatures, stage count, or feasibility.', fontsize=10.5, linespacing=1.65)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', dpi=140)
    plt.close(fig)


if __name__ == '__main__':
    main()
