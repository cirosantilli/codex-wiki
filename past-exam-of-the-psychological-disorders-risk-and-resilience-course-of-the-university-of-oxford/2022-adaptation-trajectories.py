#!/usr/bin/env python3
"""Illustrative trajectories, not fitted classes or observed data.

Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7. Writes PNG into CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    time = np.linspace(-2.0, 6.0, 641)
    after = np.maximum(time, 0.0)
    stable = np.full_like(time, .15)
    recovery = np.where(time < 0, .15, .15 + .65 * np.exp(-after / 1.25))
    persistent = np.full_like(time, .72)
    delayed = np.where(time <= 0, .15, .15 + .58 * (1 - np.exp(-after / 2.5))**2)
    assert np.all((recovery >= .15) & (recovery <= .8))
    assert np.allclose(recovery[time < 0], stable[time < 0])
    assert recovery[-1] < .16
    assert delayed[-1] > .6
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, ax = plt.subplots(figsize=(8.0, 4.0), dpi=100)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.axvline(0, color='#87939d', lw=1.2, ls='--', zorder=0)
    for values, label, color, style in [
        (persistent, 'Persistent distress', '#b24827', '-.'),
        (recovery, 'Disruption and recovery', '#2879a5', '-'),
        (delayed, 'Delayed deterioration', '#9a6300', '--'),
        (stable, 'Stable low symptoms', '#337d64', '-')]:
        ax.plot(time, values, label=label, color=color, lw=2.3, ls=style)
    ax.text(-.06, .93, 'Adverse event', ha='right', va='top',
            transform=ax.get_xaxis_transform(), color='#455968', fontsize=10)
    ax.set(xlim=(-2, 6), ylim=(0, 1), xlabel='Time relative to event (arbitrary units)',
           ylabel='Symptom burden (arbitrary units)')
    ax.set_xticks([-2, 0, 2, 4, 6])
    ax.set_yticks([.15, .72], ['Lower', 'Higher'])
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(loc='upper right', frameon=False, fontsize=10, ncol=2)
    ax.set_title('A trajectory needs a baseline and repeated follow-up',
                 fontweight='bold', fontsize=14, pad=13, color='#19364b')
    fig.text(.5, .025, 'Constructed schematic: no participant data, fitted classes or prevalence estimates',
             ha='center', fontsize=9.5, color='#455e70')
    fig.subplots_adjust(left=.11, right=.98, top=.85, bottom=.19)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100,
                facecolor='white', transparent=False,
                metadata={'Software': 'Original codex-wiki matplotlib generator'})
    plt.close(fig)


if __name__ == '__main__':
    main()
