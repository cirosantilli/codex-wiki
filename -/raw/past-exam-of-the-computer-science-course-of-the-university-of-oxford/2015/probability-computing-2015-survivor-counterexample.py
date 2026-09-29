#!/usr/bin/env python3
"""Exact expectations and the false Q2(c) bound; no simulation.

Tested: Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Writes an opaque PNG in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

rounds = np.arange(2, 7)
actual = np.array([2.0 ** (1 - int(j)) for j in rounds])
printed = np.array([2.0 ** (1 - 2 ** (int(j) - 2)) for j in rounds])
fig, ax = plt.subplots(figsize=(8.0, 4.4), dpi=120, facecolor='white')
ax.set_facecolor('white')
ax.plot(rounds, actual, 'o-', color='#17689b', linewidth=2.2,
        label=r'Exact expectation $x_j=2^{1-j}$')
ax.plot(rounds, printed, 's--', color='#b44338', linewidth=1.9,
        label=r'Printed proposed bound $2\,2^{-2^{j-2}}$')
ax.set_yscale('log', base=2)
ax.set_xticks(rounds)
ax.set_xlabel('Rounds completed, j')
ax.set_ylabel('Expected surviving balls / proposed bound')
ax.set_ylim(2 ** -16, 2)
ax.set_yticks([2.0 ** -k for k in (0, 2, 4, 6, 8, 10, 12, 14, 16)])
ax.set_yticklabels(['1', '1/4', '1/16', '1/64', '1/256', '1/1024',
                    '1/4096', '1/16384', '1/65536'])
ax.set_title('Two balls, two bins: rare collisions survive', pad=12)
ax.grid(axis='y', alpha=.23)
ax.annotate('j = 5: exact 1/16', xy=(5, 1/16), xytext=(4.45, .43),
            color='#17689b', arrowprops={'arrowstyle': '->', 'color': '#17689b'})
ax.annotate('j = 5: proposed 1/128', xy=(5, 1/128), xytext=(3.65, 1/650),
            color='#b44338', arrowprops={'arrowstyle': '->', 'color': '#b44338'})
ax.legend(loc='lower left', fontsize=9, framealpha=1)
fig.text(.5, .022, 'Both balls survive j rounds with probability 2⁻ʲ; otherwise neither survives.',
         ha='center', fontsize=9)
fig.tight_layout(rect=(0, .055, 1, 1))
fig.savefig('probability-computing-2015-survivor-counterexample.png', facecolor='white',
            transparent=False, metadata={'Software': 'Matplotlib'})
plt.close(fig)
