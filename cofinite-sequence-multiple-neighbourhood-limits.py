"""Neighbourhood membership of x_n=n in an infinite cofinite space."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    indices = np.arange(1, 19)
    cases = [(1, {2, 5, 8}, 9, '#0072b2'), (2, {1, 3, 7}, 8, '#d55e00')]
    fig, axes = plt.subplots(2, 1, figsize=(9.6, 4.3), dpi=125, layout='constrained',
                             sharex=True, facecolor='white')
    for ax, (limit, excluded, cutoff, colour) in zip(axes, cases):
        assert limit not in excluded and cutoff == max(excluded)+1
        assert all(n not in excluded for n in range(cutoff, 1001))
        inside = np.array([n not in excluded for n in indices])
        ax.axvspan(cutoff-.5, 18.5, color=colour, alpha=.10)
        ax.axvline(cutoff-.5, color=colour, linewidth=1.5, linestyle='--')
        ax.scatter(indices[inside], np.zeros(inside.sum()), s=80, color=colour, zorder=3)
        ax.scatter(indices[~inside], np.zeros((~inside).sum()), marker='x', s=90,
                   linewidths=2, color='#888888', zorder=3)
        ax.text(cutoff+.2, .29, f'All terms with n ≥ {cutoff} are inside',
                color=colour, fontsize=11)
        ax.text(19.05, 0, '…', fontsize=24, ha='center', va='center', color=colour)
        excluded_label = ','.join(str(x) for x in sorted(excluded))
        ax.set(ylim=(-.30, .70), xlim=(.5, 19.6), yticks=[],
               title=rf'$U_{limit}=X\setminus\{{{excluded_label}\}}$ is a neighbourhood of {limit}')
        for spine in ax.spines.values(): spine.set_visible(False)
        ax.tick_params(axis='x', length=0)
    axes[-1].set_xticks(indices)
    axes[-1].set_xlabel(r'Index $n$; sequence value $x_n=n$', fontsize=11)
    fig.suptitle('The same sequence eventually stays in both sample neighbourhoods', fontsize=14)
    fig.supxlabel('General reason: every finite excluded set has a last visit. No distance is used.',
                  fontsize=11)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
