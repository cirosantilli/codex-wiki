"""Finite windows of three explicitly infinite cofinite sets; no metric is assigned."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    labels = np.arange(1, 17)
    exclusions = [{2, 5, 8}, {1, 3, 7}, {1, 2, 3, 5, 7, 8}]
    assert exclusions[0] | exclusions[1] == exclusions[2]
    assert all(k not in exclusions[2] for k in [4, 6, 9, 10, 16, 1000])
    fig, ax = plt.subplots(figsize=(9.6, 3.8), dpi=125, layout='constrained', facecolor='white')
    names = [r'$U=X\setminus\{2,5,8\}$', r'$V=X\setminus\{1,3,7\}$',
             r'$U\cap V=X\setminus\{1,2,3,5,7,8\}$']
    for y, (exclude, colour) in enumerate(zip(exclusions, ['#0072b2', '#d55e00', '#009e73'])):
        included = np.array([k not in exclude for k in labels])
        ax.scatter(labels[included], np.full(included.sum(), 2-y), color=colour, s=90, zorder=3)
        ax.scatter(labels[~included], np.full((~included).sum(), 2-y), color='#888888',
                   marker='x', s=90, linewidths=2, zorder=3)
        ax.text(17, 2-y, '…', fontsize=25, va='center', ha='center', color=colour)
        for k in labels:
            ax.text(k, 2-y-.23, str(k), ha='center', va='top', fontsize=10)
    ax.set(yticks=[2, 1, 0], yticklabels=names, xlim=(.5, 17.7), ylim=(-.6, 2.6),
           title=r'$X=\mathbb{N}_{>0}$: removing finitely many points leaves infinitely many')
    ax.set_xticks([]); ax.tick_params(axis='y', length=0, labelsize=11)
    for spine in ax.spines.values(): spine.set_visible(False)
    fig.supxlabel('Filled circle: included; cross: excluded. Drawing is a window, not a finite space.',
                  fontsize=11)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
