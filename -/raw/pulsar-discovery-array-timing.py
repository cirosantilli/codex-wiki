"""Original pulsar discovery functional/timing illustration; Python 3.14, NumPy, Matplotlib.

Run from _media: python ../pulsar-discovery-array-timing.py
Synthetic signal only; apparatus values from Hewish et al., Nature 217, 709 (1968).
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
    fig = plt.figure(figsize=(10, 7.2), facecolor='white', layout='constrained')
    gs = fig.add_gridspec(3, 2, height_ratios=[1.25, 1, 1.1])
    flow = fig.add_subplot(gs[0, :])
    flow.set(xlim=(0, 10), ylim=(0, 3.3))
    flow.axis('off')
    boxes = [(0.1, 'Dipole array\n2,048 elements\n16 rows', '#e7f0f9'),
             (3.5, 'Phasing + receivers\n81.5 MHz centre\n1 MHz bandwidth', '#e9f4ec'),
             (6.9, 'Pen recorder\nSignal versus time\nCompare with second pips', '#fff1dc')]
    for x, label, color in boxes:
        flow.add_patch(FancyBboxPatch((x, 1.1), 2.9, 1.45, boxstyle='round,pad=0.08', fc=color, ec='#415367'))
        flow.text(x + 1.45, 1.83, label, ha='center', va='center', fontsize=11)
    for x in [3.03, 6.43]:
        flow.annotate('', xy=(x + .35, 1.8), xytext=(x, 1.8), arrowprops={'arrowstyle': '->', 'lw': 1.8})
    flow.text(5, .6, 'Four declination channels; two array halves used as an east–west interferometer', ha='center', fontsize=10.5)
    flow.text(5, .16, 'Functional diagram only: layout and traces are not historical reproductions', ha='center', color='#555555', fontsize=10)
    t = np.linspace(0, 7, 5000)
    pulse = sum(np.exp(-.5 * ((t - p) / .055) ** 2) for p in np.arange(.6, 7, 1.4))
    ax = fig.add_subplot(gs[1, 0])
    # Compress the same pulse train to show why record speed matters, without simulating a specific instrument.
    ax.plot(t, pulse, color='#26718f', lw=1)
    ax.set(xlim=(0, 7), ylim=(-.06, 1.15), xlabel='Time (s)', ylabel='Chosen signal', title='Same signal, compressed time axis')
    ax.set_box_aspect(.23)
    ax = fig.add_subplot(gs[1, 1])
    ax.plot(t, pulse, color='#26718f', lw=1.7)
    ax.annotate('', xy=(2, 1.03), xytext=(.6, 1.03), arrowprops={'arrowstyle': '<->', 'color': '#a04d10'})
    ax.text(1.3, 1.1, 'Chosen P = 1.4 s', ha='center', color='#a04d10', fontsize=10)
    ax.set(xlim=(0, 4.8), ylim=(-.06, 1.32), xlabel='Time (s)', title='Expanded time axis resolves pulses')
    ax = fig.add_subplot(gs[2, :])
    days = np.arange(11)
    ax.plot(days, np.zeros_like(days), 'o--', color='#a04d10', label='24 hour schedule')
    ax.plot(days, -3.93 * days, 'o-', color='#26718f', label='Fixed sky direction: sidereal recurrence')
    ax.set(xlim=(-.2, 10.2), ylim=(-47, 8), xlabel='Number of sidereal recurrences', ylabel='Shift from 24 h\nschedule (min)', title='Daily sky transit is a different clock from pulse spacing')
    ax.legend(loc='lower left', fontsize=9, frameon=False)
    ax.annotate('39.3 min earlier', xy=(10, -39.3), xytext=(7.7, -18), arrowprops={'arrowstyle': '->', 'color': '#415367'}, ha='center', fontsize=10)
    fig.suptitle('Two clocks in the pulsar discovery', fontsize=16)
    fig.savefig(Path(__file__).stem + '.png', dpi=110, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
