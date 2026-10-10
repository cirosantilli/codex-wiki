"""Draw exact M/M/1 congestion curves; write the PNG to the CWD.

Tested with Python 3.14.4, matplotlib 3.10.7, and numpy 2.3.5.
Run from _media: MPLBACKEND=Agg python3 ../queue-utilization-delay.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    mu = 5.  # customers per hour
    rho = np.linspace(0, .98, 801)
    population = rho / (1 - rho)
    waiting_population = rho**2 / (1 - rho)
    duration = 1 / (mu * (1 - rho))
    waiting_duration = rho / (mu * (1 - rho))
    assert np.allclose(population - waiting_population, rho)
    assert np.allclose(duration - waiting_duration, 1 / mu)
    assert np.allclose(mu * rho * duration, population)

    plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14})
    blue, orange = '#246da4', '#d0802a'
    fig, (count, delay) = plt.subplots(1, 2, figsize=(10, 5.3), dpi=120,
                                     facecolor='white')
    count.plot(rho, population, color=blue, linewidth=2.5, label='L: whole system')
    count.plot(rho, waiting_population, color=orange, linestyle='--',
               linewidth=2, label='Lq: waiting only')
    delay.plot(rho, duration, color=blue, linewidth=2.5, label='W: whole system')
    delay.plot(rho, waiting_duration, color=orange, linestyle='--',
               linewidth=2, label='Wq: waiting only')
    for load, customer_count, hours in [(0.8, 4, 1), (0.9, 9, 2), (0.98, 49, 10)]:
        for ax, y in [(count, customer_count), (delay, hours)]:
            ax.scatter(load, y, color=blue, s=34, zorder=4)
            suffix = ' customers' if ax is count else ' h'
            offset = (-108, 1) if load == .98 else (-100, 5)
            ax.annotate(f'ρ = {load:g}: {y:g}{suffix}', (load, y),
                        xytext=offset, textcoords='offset points', fontsize=10,
                        color='#16496f',
                        arrowprops={'arrowstyle': '-', 'color': '#768b9b'})
    count.set(ylabel='Mean customers', title='Population', ylim=(0, 55))
    delay.set(ylabel='Mean duration (hours)', title='Time per customer', ylim=(0, 11.3))
    for ax in (count, delay):
        ax.axvline(1, color='#8f5353', linestyle=':', linewidth=1.5)
        ax.set(xlim=(0, 1.025), xlabel='Server utilization ρ = λ / μ',
               xticks=[0, .2, .4, .6, .8, 1])
        ax.legend(loc='upper left', frameon=False, fontsize=10)
        ax.grid(color='#e4e8ec', linewidth=.8)
        ax.spines[['top', 'right']].set_visible(False)
    fig.suptitle('M/M/1 congestion: a small capacity margin means a long wait',
                 fontsize=16, y=.97)
    fig.text(.5, .045, 'μ = 5 customers/hour; mean service time = 12 min.  '
             'Curves stop at ρ = 0.98; no stationary law at ρ ≥ 1.',
             ha='center', fontsize=10.5)
    fig.subplots_adjust(left=.075, right=.975, top=.82, bottom=.19, wspace=.30)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
