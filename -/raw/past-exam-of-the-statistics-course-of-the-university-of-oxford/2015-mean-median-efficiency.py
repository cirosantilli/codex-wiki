#!/usr/bin/env python3
"""Compare leading estimator variances; write PNG in the current directory.

Uses the repository's Python/matplotlib environment from pyproject.toml.
"""
from pathlib import Path
import math
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white',
                         'axes.facecolor': 'white', 'savefig.facecolor': 'white'})
    figure, axes = plt.subplots(1, 2, figsize=(7.4, 3.4), sharey=True)
    models = [
        ('Normal location model', [1, math.pi/2], ['1', r'$\pi/2$'],
         r'Population variance: $\sigma^2$'),
        ('Laplace location model', [2, 1], ['2', '1'],
         r'Population variance: $2\sigma^2$'),
    ]
    for axis, (title, values, labels, subtitle) in zip(axes, models):
        axis.bar([0, 1], values, width=0.58, color=['#31688e', '#de8637'],
                 edgecolor='white', zorder=3)
        for position, value, label in zip([0, 1], values, labels):
            axis.text(position, value+0.06, label, ha='center', va='bottom')
        axis.set_xticks([0, 1], ['Sample mean', 'Sample median'])
        axis.set_ylim(0, 2.35)
        axis.set_xlim(-0.65, 1.65)
        axis.set_title(title, fontsize=11, pad=13)
        axis.text(0.5, -0.23, subtitle, transform=axis.transAxes,
                  ha='center', va='top', fontsize=9)
        axis.grid(axis='y', alpha=0.22, zorder=0)
        axis.spines[['top', 'right']].set_visible(False)
    axes[0].set_ylabel(r'Leading $n\,\mathrm{Var}(\widehat\theta)/\sigma^2$')
    figure.suptitle('Mean versus median: lower variance gives a shorter interval',
                    fontsize=11, y=0.98)
    figure.subplots_adjust(left=0.10, right=0.98, top=0.77, bottom=0.24, wspace=0.22)
    figure.savefig(Path('2015-mean-median-efficiency.png'), dpi=110)
    plt.close(figure)


if __name__ == '__main__':
    main()
