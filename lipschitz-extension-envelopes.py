"""Illustrate the extremal real-valued McShane-Whitney extensions.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Save an opaque white PNG with this script's basename in the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def envelopes(x, anchors, values, bound):
    distances = np.abs(np.asarray(x)[..., None] - anchors)
    upper = np.min(values + bound * distances, axis=-1)
    lower = np.max(values - bound * distances, axis=-1)
    return lower, upper


def main():
    anchors = np.array([0., 1., 2.])
    values = np.array([0., .5, 0.])
    bound = 1.
    assert np.all(np.abs(values[:, None] - values[None, :])
                  <= bound * np.abs(anchors[:, None] - anchors[None, :]))
    low, high = envelopes(anchors, anchors, values, bound)
    assert np.allclose(low, values) and np.allclose(high, values)
    low, high = envelopes(np.array([.5, 1.5, 2.5]), anchors, values, bound)
    assert np.allclose(low, [0, 0, -.5])
    assert np.allclose(high, [.5, .5, .5])
    x = np.linspace(-.6, 2.7, 1101)
    lower, upper = envelopes(x, anchors, values, bound)
    interpolant = np.interp(x, anchors, values)  # Constant outside the data interval.
    assert np.all(lower <= upper + 1.e-14)
    assert np.all(lower <= interpolant + 1.e-14)
    assert np.all(interpolant <= upper + 1.e-14)
    # Pairwise distances independently check all sampled envelope constraints.
    distances = np.abs(x[:, None] - x[None, :])
    for curve in [lower, upper, interpolant, .3*lower + .7*upper]:
        assert np.all(np.abs(curve[:, None] - curve[None, :])
                      <= bound * distances + 1.e-13)

    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.8), dpi=110, facecolor='white')
    colors = ['#4b7e96', '#9a6a34', '#7273a2']
    for a, value, color in zip(anchors, values, colors):
        axes[0].plot(x, value + bound*np.abs(x-a), color=color, lw=1.4, ls='--',
                     label=rf'$f({int(a)})+|x-{int(a)}|$')
    axes[0].plot(x, upper, color='#226f97', lw=3, label='F: minimum of upper constraints')
    axes[0].set(title='Every sample places an upper constraint', ylim=(-.15, 2.25))
    axes[0].legend(loc='upper left', fontsize=9.5, framealpha=.95)
    axes[1].fill_between(x, lower, upper, color='#e2edf3', label='Every allowed extension lies here')
    axes[1].plot(x, upper, color='#226f97', lw=2.5, label='F: largest allowed extension')
    axes[1].plot(x, lower, color='#b46930', lw=2.5, label='G: smallest allowed extension')
    axes[1].plot(x, interpolant, color='#53734c', lw=1.8, ls='--',
                 label='One possible interpolation')
    axes[1].plot([.5, .5], [0, .5], color='#4e5861', lw=2)
    axes[1].scatter([.5, .5], [0, .5], color='#4e5861', s=20)
    axes[1].annotate(r'$0\leq H(1/2)\leq1/2$', xy=(.5, .25), xytext=(1.12, .79),
                     fontsize=11, arrowprops={'arrowstyle': '->', 'color': '#4e5861'})
    axes[1].set(title='Upper and lower envelopes leave freedom', ylim=(-.8, 1.))
    axes[1].legend(loc='lower center', fontsize=9.5, framealpha=.96)
    for ax in axes:
        ax.scatter(anchors, values, color='#27343d', s=55, zorder=5)
        ax.set(xlim=(-.6, 2.7), xlabel='x', ylabel='value')
        ax.set_xticks([0, .5, 1, 1.5, 2, 2.5])
        ax.grid(color='#e4e8eb', lw=.7)
        ax.spines[['top', 'right']].set_visible(False)
        ax.title.set_fontsize(12)
    fig.suptitle('Extending three samples without exceeding a Lipschitz bound', fontsize=16, y=.96)
    fig.text(.5, .875, r'$f(0)=0,\quad f(1)=1/2,\quad f(2)=0,\qquad L=1$', ha='center', fontsize=14)
    fig.text(.5, .04, 'F and G match all samples. A finite bound controls missing values without forcing a unique curve.',
             ha='center', fontsize=11.5)
    fig.subplots_adjust(left=.065, right=.975, bottom=.16, top=.76, wspace=.27)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
