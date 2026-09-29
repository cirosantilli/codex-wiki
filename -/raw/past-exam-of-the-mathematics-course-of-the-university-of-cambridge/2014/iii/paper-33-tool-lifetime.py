"""Render fitted parallel tool-lifetime lines; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Write the PNG basename to the caller's current directory. Any caller-provided
MPLCONFIGDIR is honored; this script creates no other output directories.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

speed = np.linspace(500, 1000, 200)
intercepts = [35.891690, 35.058282, 48.499350, 52.430811]
fig, ax = plt.subplots(figsize=(8, 4.6), dpi=120, facecolor='white')
ax.set_facecolor('white')
for j, (a, color, style) in enumerate(zip(intercepts, ['#1f77b4', '#d55e00', '#009e73', '#7b3294'], ['-', '--', '-.', ':']), 1):
    ax.plot(speed, a - 0.024585 * speed, color=color, linestyle=style,
            linewidth=2.2, label=f'Type {j}')
ax.set(xlabel='Lathe speed (revolutions per minute)', ylabel='Fitted mean lifetime (hours)',
       title='Parallel fitted tool-lifetime lines', xlim=(500, 1000))
ax.grid(alpha=0.2)
ax.legend(loc='upper right', framealpha=1, facecolor='white')
fig.text(0.5, 0.02, 'Illustrative speed interval; observed speeds were not supplied.',
         ha='center', fontsize=9)
fig.subplots_adjust(left=0.09, right=0.98, top=0.88, bottom=0.15)
fig.savefig('paper-33-tool-lifetime.png', dpi=120, facecolor='white', transparent=False)
plt.close(fig)
