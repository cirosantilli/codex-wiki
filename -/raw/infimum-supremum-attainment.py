"""Render bounds and attainment for four concrete real sets to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    finite = np.array([.2, .4, .6])
    assert finite.min() == .2 and finite.max() == .6
    assert .8 < .9 < 1
    for epsilon in [.2, .1, .01, .001]:
        n = int(np.floor(1/epsilon))+1
        assert 0 < 1/n < epsilon
    indices = np.array([1, 2, 3, 4, 6, 8, 12])
    reciprocal = 1/indices
    assert reciprocal.max() == 1 and np.all(reciprocal > 0)

    plt.rcParams.update({'font.size': 12, 'axes.titlesize': 13})
    fig, axes = plt.subplots(4, 1, figsize=(11.5, 7.2), dpi=120,
                             sharex=True, facecolor='white')
    blue, orange = '#246ea0', '#b85f20'
    for ax in axes:
        ax.axhline(0, color='#ced6dd', lw=1)
        ax.set(xlim=(-.10, 1.10), ylim=(-.5, .6))
        ax.set_yticks([])
        ax.spines[['left', 'right', 'top', 'bottom']].set_visible(False)
        ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    for ax, closed in zip(axes[:2], [False, True]):
        ax.plot([0, 1], [0, 0], color=blue, lw=4)
        ax.scatter([0, 1], [0, 0], s=100,
                   facecolor=blue if closed else 'white', edgecolor=blue,
                   linewidth=2, zorder=4)
    axes[0].set_title(r'$A=(0,1)$', loc='left')
    axes[1].set_title(r'$B=[0,1]$', loc='left')
    axes[2].set_title(r'$C=\{1/n:n\geq 1\}$ (selected members)', loc='left')
    axes[2].scatter(reciprocal, np.zeros_like(reciprocal), s=50, color=blue, zorder=4)
    axes[2].scatter([0], [0], s=100, facecolor='white', edgecolor=blue,
                    linewidth=2, zorder=4)
    axes[2].annotate('more values toward 0', xy=(.025, 0), xytext=(.28, -.38),
                     fontsize=10.5, ha='center', color=blue,
                     arrowprops={'arrowstyle': '->', 'color': blue})
    axes[3].set_title(r'$D=\{0.2,0.4,0.6\}$', loc='left')
    axes[3].scatter(finite, [0, 0, 0], s=80, color=blue, zorder=4)
    descriptions = [
        'inf = 0; no minimum\nsup = 1; no maximum',
        'inf = min = 0\nsup = max = 1',
        'inf = 0; no minimum\nsup = max = 1',
        'inf = min = 0.2\nsup = max = 0.6',
    ]
    for ax, text in zip(axes, descriptions):
        ax.text(1.025, .5, text, transform=ax.transAxes,
                va='center', color=orange, fontsize=12, linespacing=1.7)
        ax.text(0, .23, '0', ha='center', color='#586c7a', fontsize=10)
        ax.text(1, .23, '1', ha='center', color='#586c7a', fontsize=10)
    axes[-1].tick_params(axis='x', bottom=True, labelbottom=True)
    axes[-1].set_xticks([0, .2, .4, .6, .8, 1])
    axes[-1].set_xlabel('Real-number position')
    fig.suptitle('Exact bounds can exist without a smallest or largest member',
                 fontsize=16, y=.975)
    fig.text(.5, .025, 'Filled markers belong to the set; hollow edge markers do not.',
             ha='center', fontsize=12)
    fig.subplots_adjust(left=.075, right=.76, bottom=.12, top=.88, hspace=.65)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
