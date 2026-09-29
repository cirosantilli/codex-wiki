"""Draw the static QED vertex response; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    alpha = 1 / 137
    anomaly = alpha / (2 * np.pi)
    plt.rcParams.update({'font.size': 12, 'axes.spines.top': False, 'axes.spines.right': False})
    fig = plt.figure(figsize=(11, 6.6), facecolor='white', layout='constrained')
    grid = fig.add_gridspec(2, 2, height_ratios=[1.25, 1])
    ax = fig.add_subplot(grid[0, :])
    ax.set(xlim=(0, 10), ylim=(0, 4)); ax.axis('off')
    ax.annotate('', (4.8, 1.9), (1.2, 1.9), arrowprops={'arrowstyle': '->', 'lw': 2.5, 'color': '#176591'})
    ax.annotate('', (8.8, 1.9), (5.2, 1.9), arrowprops={'arrowstyle': '->', 'lw': 2.5, 'color': '#176591'})
    ax.plot(5, 1.9, 'o', color='#ab4e16', ms=16)
    t = np.linspace(0, 1, 250)
    ax.plot(5 + .12 * np.sin(12 * np.pi * t), 2.05 + 1.2 * t, color='#ab4e16', lw=2)
    ax.text(2.1, 1.5, r'incoming electron $p$')
    ax.text(6.1, 1.5, r'outgoing electron $p^{\prime}$')
    ax.text(5.35, 3, r'external probe $q=p^{\prime}-p$')
    ax.text(5, .72, r'$\Gamma^\mu=\gamma^\mu F_1(q^2)+\frac{i\sigma^{\mu\nu}q_\nu}{2m}F_2(q^2)$', ha='center', fontsize=19)
    ax.text(5, .05, 'Extract the spin coefficient before taking the zero-transfer limit.', ha='center')
    colors = ['#73869a', '#ab4e16']
    left = fig.add_subplot(grid[1, 0])
    left.bar([0, 1], [1, 1], color=colors, width=.52)
    left.set(xticks=[0, 1], xticklabels=['Dirac baseline', 'Leading QED'], ylim=(0, 1.23), ylabel=r'$F_1(0)$', title='Charge is normalized to one')
    for i in [0, 1]: left.text(i, 1.025, '1', ha='center')
    right = fig.add_subplot(grid[1, 1])
    right.bar([0, 1], [0, anomaly * 1000], color=colors, width=.52)
    right.scatter([0], [0], color=colors[0], zorder=3)
    right.set(xticks=[0, 1], xticklabels=['Dirac baseline', 'Leading QED'], ylim=(-.05, 1.45), ylabel=r'$10^3 F_2(0)$', title='Extra magnetic response has its own scale')
    right.text(0, .06, '0', ha='center'); right.text(1, anomaly * 1000 + .05, f'{anomaly * 1000:.5f}', ha='center')
    fig.suptitle(r'An electron already has $g_s=2$ when $F_2=0$', fontsize=18)
    fig.supxlabel(r'Chosen $\alpha=1/137$; $g_s/2=F_1(0)+F_2(0)$; theoretical comparison', fontsize=12)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
