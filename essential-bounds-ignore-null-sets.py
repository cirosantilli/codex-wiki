"""Render an isolated exceptional value and essential bounds to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    x = np.asarray(x)
    return np.where(x == .5, 10., x)


def superlevel_lebesgue_measure(threshold):
    # An exceptional singleton never changes interval length.
    return min(1., max(0., 1.-threshold))


def main():
    assert f(.5) == 10
    assert f(1) == 1 and f(0) == 0
    assert np.isclose(superlevel_lebesgue_measure(.8), .2)
    assert superlevel_lebesgue_measure(1) == 0
    assert superlevel_lebesgue_measure(9) == 0
    assert superlevel_lebesgue_measure(-1) == 1
    assert all(superlevel_lebesgue_measure(1-epsilon) > 0
               for epsilon in [.5, .1, .01, .001])
    assert f(.5) == 10  # The Dirac measure at this input sees the exceptional value.
    left = np.linspace(0, .5, 500, endpoint=False)
    right = np.linspace(np.nextafter(.5, 1), 1, 500)
    assert np.isclose(np.trapezoid(np.linspace(0, 1, 1001),
                                   np.linspace(0, 1, 1001)), .5)
    plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14})
    fig, (full, zoom) = plt.subplots(1, 2, figsize=(11.6, 5.8), dpi=120,
                                    facecolor='white')
    for ax in (full, zoom):
        ax.plot(left, left, color='#246ea0', lw=3)
        ax.plot(right, right, color='#246ea0', lw=3)
        ax.scatter([.5], [.5], facecolor='white', edgecolor='#246ea0',
                   linewidth=2, s=65, zorder=5)
        ax.set(xlim=(0, 1), xlabel='Input x')
        ax.grid(color='#e6eaed')
        ax.spines[['top', 'right']].set_visible(False)
    full.scatter([.5], [10], color='#b85f20', s=85, zorder=5)
    full.axhline(10, color='#b85f20', ls='--', lw=1.5, label='sup f = 10')
    full.axhline(1, color='#277c54', ls=':', lw=2, label='ess sup f = 1')
    full.annotate('one exceptional input', xy=(.5, 10), xytext=(.05, 7.5),
                  arrowprops={'arrowstyle': '->', 'color': '#b85f20'},
                  color='#965225', fontsize=11)
    full.set(ylim=(-.25, 11), ylabel='Value f(x)', title='Full graph: the singleton is visible')
    full.legend(loc='center right', frameon=False)
    zoom.axhline(.8, color='#b85f20', ls='--', lw=1.5)
    zoom.axvspan(.8, 1, color='#277c54', alpha=.15)
    zoom.plot([.8, 1], [.035, .035], color='#277c54', lw=6, solid_capstyle='butt')
    zoom.text(.48, .15, 'x > 0.8 occupies length 0.2', fontsize=11,
              color='#20614c', ha='center')
    zoom.text(.045, 1.075, 'f(0.5) = 10 lies above this zoom', fontsize=11,
              color='#965225')
    zoom.text(.05, .83, 'threshold 0.8', fontsize=11, color='#965225')
    zoom.set(ylim=(0, 1.17), ylabel='Value near the ramp',
              title='Every threshold below 1 fails on positive measure')
    fig.suptitle('Lebesgue measure ignores an isolated change; the supremum does not',
                 fontsize=16, y=.975)
    fig.text(.5, .035, 'There is no vertical graph segment at x = 0.5: its value is one isolated point at height 10.',
             ha='center', fontsize=11)
    fig.subplots_adjust(left=.075, right=.975, bottom=.17, top=.84, wspace=.3)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
