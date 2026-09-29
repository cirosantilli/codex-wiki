"""Draw a deterministic Little's-law example; write the PNG to the CWD.

Tested with Python 3.14.4, matplotlib 3.10.7, and numpy 2.3.5.
Run from _media: MPLBACKEND=Agg python3 ../little-law-sample-path.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch


def main():
    arrivals = np.array([0., 1., 4.])
    starts = np.array([0., 2., 4.])
    departures = np.array([2., 3., 5.])
    times = np.array([0., 1., 2., 3., 4., 5., 6.])
    midpoints = (times[:-1] + times[1:]) / 2
    population = np.sum((arrivals[:, None] <= midpoints)
                        & (midpoints < departures[:, None]), axis=0)
    area = np.dot(np.diff(times), population)
    assert area == 5 == np.sum(departures - arrivals)
    assert np.sum(starts - arrivals) == 1
    assert np.sum(departures - starts) == 4

    plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14})
    blue, orange = '#246da4', '#d0802a'
    fig, (occupancy, visits) = plt.subplots(
        2, 1, figsize=(8.4, 6.5), dpi=120, sharex=True,
        gridspec_kw={'height_ratios': [1, 1.2]}, facecolor='white')
    occupancy.stairs(population, times, fill=True, color=blue, alpha=.2)
    occupancy.stairs(population, times, color=blue, linewidth=2.4)
    for left, n in zip(times[:-1], population):
        if n:
            occupancy.text(left + .5, n / 2, str(n), ha='center', va='center',
                           color='#16496f', fontsize=14, weight='bold')
    occupancy.text(3.2, 1.9, 'Area = 5 customer-minutes\nL = 5/6 customer',
                   fontsize=13, color='#16496f', va='center',
                   bbox={'facecolor': 'white', 'edgecolor': 'none'})
    occupancy.set(ylim=(0, 2.6), yticks=[0, 1, 2], ylabel='Customers N(t)',
                  title='Count by time: height × duration')

    for row, name, arrival, start, departure in zip(
            [3, 2, 1], ['A', 'B', 'C'], arrivals, starts, departures):
        if start > arrival:
            visits.broken_barh([(arrival, start - arrival)], (row - .22, .44),
                              facecolors=orange)
        visits.broken_barh([(start, departure - start)], (row - .22, .44),
                          facecolors=blue)
        visits.text((arrival + departure) / 2, row + .3,
                    f'{departure - arrival:g} min in system',
                    ha='center', fontsize=11)
        visits.plot([arrival, departure], [row, row], 'o', color='#18364d',
                    markersize=4)
    visits.text(5.9, 2.65, '2 + 2 + 1 = 5\ncustomer-minutes', ha='right',
                color='#16496f', fontsize=12)
    visits.set(yticks=[1, 2, 3], yticklabels=['C', 'B', 'A'], ylim=(.3, 3.8),
               xlim=(-.1, 6.1), xticks=times, xlabel='Time (minutes)',
               ylabel='Customer', title='Count by customer: duration of each visit')
    visits.legend(handles=[Patch(color=blue, label='Service: total 4 min'),
                           Patch(color=orange, label='Waiting: total 1 min')],
                  loc='lower left', frameon=False, fontsize=10)
    for ax in (occupancy, visits):
        ax.grid(axis='x', color='#dde3e8', linewidth=.8)
        ax.set_axisbelow(True)
        ax.spines[['top', 'right']].set_visible(False)
    fig.suptitle("Little's law without random arrivals", fontsize=17, y=.98)
    fig.text(.5, .035, '3 customers / 6 minutes × 5/3 minutes per customer = 5/6 customer',
             ha='center', fontsize=11)
    fig.subplots_adjust(left=.105, right=.975, top=.87, bottom=.14, hspace=.42)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
