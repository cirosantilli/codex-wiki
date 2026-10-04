"""Spherical-collapse sketch; Python 3.14, NumPy and Matplotlib root dependencies.
Writes paper-45-collapse.png to the caller's current working directory.
The virialized plateau is schematic, not a pressureless-shell solution.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

th = np.linspace(0, 2*np.pi, 850)
t = (th-np.sin(th))/np.pi
radius = (1-np.cos(th))/2
stop = 3*np.pi/2
vtime = (stop-np.sin(stop))/np.pi
fig, ax = plt.subplots(figsize=(7.6, 4.5), dpi=130, facecolor='white')
ax.set_facecolor('white')
ax.plot(t, radius, '--', color='#b34a35', lw=1.7, label='Formal cold top-hat collapse')
mask = th <= stop
ax.plot(t[mask], radius[mask], color='#166a8f', lw=2.5, label='Expansion, contraction, schematic virialization')
ax.plot([vtime, 2.55], [.5, .5], color='#166a8f', lw=2.5)
ax.scatter([1, 2], [1, 0], color=['#166a8f', '#b34a35'], s=28, zorder=5)
ax.axhline(.5, color='#777777', lw=.7, ls=':')
ax.annotate('Turnaround', (1, 1), xytext=(1.18, 1.05), arrowprops={'arrowstyle':'->', 'color':'#444444'}, fontsize=10)
ax.annotate('Virial radius $R_m/2$', (2.25, .5), xytext=(1.78, .76), arrowprops={'arrowstyle':'->', 'color':'#444444'}, fontsize=10)
ax.annotate('Formal collapse\n$t_c=2t_m$', (2, 0), xytext=(1.02, .15), arrowprops={'arrowstyle':'->', 'color':'#b34a35'}, fontsize=9, color='#943d2d')
ax.text(.08, 1.11, 'Plateau onset is schematic; relaxation replaces point collapse.', fontsize=9, color='#444444')
ax.set(xlim=(0, 2.6), ylim=(0, 1.18), xlabel='Time $t/t_m$', ylabel='Physical radius $R/R_m$', title='Spherical proto-cluster: turnaround and virialization')
ax.set_xticks([0, 1, 2]); ax.set_yticks([0, .5, 1]); ax.set_yticklabels(['0', '1/2', '1'])
ax.grid(alpha=.18); ax.legend(loc='lower left', bbox_to_anchor=(0, -.32), fontsize=9, frameon=False)
fig.subplots_adjust(bottom=.25, top=.88, left=.1, right=.97)
fig.savefig('paper-45-collapse.png', facecolor='white', transparent=False)
plt.close(fig)
