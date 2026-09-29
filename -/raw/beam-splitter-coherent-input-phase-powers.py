"""Original coherent beam splitter power curves.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
Power normalization: |a_j|^2 = P; S = [[1,i],[i,1]] / sqrt(2).
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
delta = np.linspace(-np.pi, np.pi, 801)
# Compute fields first; these are not independently split input powers.
a2 = np.exp(1j * delta)
b1 = (1 + 1j * a2) / np.sqrt(2)
b2 = (1j + a2) / np.sqrt(2)
p1, p2 = np.abs(b1)**2, np.abs(b2)**2
assert np.allclose(p1 + p2, 2, atol=2e-15)
fig, ax = plt.subplots(figsize=(9, 5), dpi=100, facecolor='white')
ax.plot(delta, p1, color='#1767a0', lw=2.8, label=r'$P_1/P=1-\sin\delta$')
ax.plot(delta, p2, color='#b84827', lw=2.8, label=r'$P_2/P=1+\sin\delta$')
ax.axhline(2, color='#555e65', ls='--', lw=1.5, label=r'Total $(P_1+P_2)/P=2$')
for d in [-np.pi/2, 0, np.pi/2]:
    ax.axvline(d, color='#c3cbd0', lw=1, zorder=0)
    ax.scatter([d], [1-np.sin(d)], s=52, color='#1767a0', zorder=4)
    ax.scatter([d], [1+np.sin(d)], s=52, facecolors='white', edgecolors='#b84827',
               linewidths=2, zorder=5)
ax.set(xlim=(-np.pi, np.pi), ylim=(-.12, 2.24),
       xlabel=r'Relative input phase $\delta=\arg a_2-\arg a_1$',
       ylabel=r'Output power / one input power $P$')
ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
              [r'$-\pi$', r'$-\pi/2$', '$0$', r'$+\pi/2$', r'$+\pi$'])
ax.set_yticks([0, .5, 1, 1.5, 2])
ax.grid(axis='y', color='#e3e8eb', lw=.8)
ax.spines[['top', 'right']].set_visible(False)
ax.legend(loc='upper center', bbox_to_anchor=(.5, 1.015), ncol=3,
          frameon=False, fontsize=10)
fig.suptitle('Two equal coherent inputs redistribute their combined power',
             fontsize=15, y=.96)
fig.text(.5, .02, r'$a_1=\sqrt{P}$, $a_2=\sqrt{P}e^{i\delta}$; '
         r'$b_1=(a_1+ia_2)/\sqrt{2}$, $b_2=(ia_1+a_2)/\sqrt{2}$'
         '\nIdeal lossless model; calculated curves, not measured data.',
         ha='center', fontsize=11)
fig.subplots_adjust(left=.1, right=.97, top=.84, bottom=.23)
fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
plt.close(fig)
