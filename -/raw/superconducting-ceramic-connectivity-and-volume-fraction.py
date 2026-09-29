"""Chosen connectivity counterexample; Python 3.14, numpy 2.3.5, matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig = plt.figure(figsize=(10.6, 6.6), dpi=110, facecolor='white')
grid = fig.add_gridspec(2, 2, height_ratios=[1, 1.45], hspace=.63, wspace=.25)
blue, orange = '#176a9a', '#bd5424'
fraction = .08
for idx, name in enumerate(['Isolated islands: b = 0', 'Spanning filament: b = 1']):
    ax = fig.add_subplot(grid[0, idx])
    ax.set(xlim=(-.12, 1.12), ylim=(-.05, 1.05), aspect='equal')
    ax.axis('off')
    ax.add_patch(Rectangle((0, 0), 1, 1, fc='#eeeeee', ec='#555555'))
    if idx == 0:
        for x in [.17, .39, .61, .83]:
            for y in [.30, .70]:
                ax.add_patch(Rectangle((x-.05, y-.05), .10, .10, fc=blue))
    else:
        ax.add_patch(Rectangle((0, .46), 1, fraction, fc=blue))
    for x in [0, 1]:
        ax.plot([x, x], [0, 1], lw=4, color=orange)
    ax.set_title(name, fontsize=12, weight='bold')
    ax.text(.5, -.10, 'Same superconducting volume fraction: f = 0.08', ha='center', va='top', fontsize=10)
ax = fig.add_subplot(grid[1, :])
floor = 1e-4
for threshold, color, style in [(.08, blue, '-'), (.60, orange, '--')]:
    # Deliberately imposed connectivity b(f); not a random-network calculation.
    ax.plot([0, threshold, threshold, 1], [1, 1, floor, floor], style, color=color, lw=2.4,
            label=fr'Chosen $f_c={threshold:.2f}$; ideal connected short')
ax.axhline(floor, color='#777777', ls=':', lw=1.4)
ax.text(.98, 1.6*floor, 'Chosen readout floor: 100 µΩ', ha='right', va='bottom', fontsize=10)
ax.set(xlim=(0, 1), ylim=(6e-5, 2), yscale='log', xlabel='Superconducting volume fraction f', ylabel='Apparent resistance (Ω)')
ax.set_title('Chosen connectivity sequences; normal path Rₙ = 1 Ω', fontsize=12, weight='bold')
ax.legend(loc='upper right', fontsize=10)
ax.grid(which='major', alpha=.18)
fig.suptitle('Connectivity controls a transport short; volume fraction alone does not', fontsize=15, weight='bold', y=.98)
fig.text(.5, .015, 'Original model, not historical data. Ideal zeros are clipped to the floor. No magnetic shielding curve is implied.', ha='center', fontsize=10, color='#555555')
fig.subplots_adjust(left=.10, right=.97, top=.88, bottom=.12)
fig.savefig(Path(__file__).stem + '.png', dpi=110, facecolor='white')
