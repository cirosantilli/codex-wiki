"""Continuum Turing-instability parameter region; outputs only to caller CWD."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6.6, 4.2), dpi=140, facecolor='white')
b = np.linspace(.06, 1, 500)
c = 3 + 2*np.sqrt(2)
d = c/b
ax.fill_between(b, d, 45, where=d<45, color='#b9dbc9', label='Diffusion-driven instability')
ax.plot(b, d, color='#146749', lw=2, label='Neutral threshold bd = 3 + 2√2')
ax.axvline(1, ls='--', color='#9c443d')
ax.text(1.035, 27, 'Reaction kinetics\nnot asymptotically\nstable', fontsize=9)
ax.text(.43, 32, 'Stable uniform kinetics,\nunstable spatial modes', ha='center', fontsize=10)
ax.text(.7, 3, 'No diffusion-driven instability', ha='center', fontsize=9)
ax.set(xlim=(0, 1.35), ylim=(0, 45), xlabel='Reaction parameter b', ylabel='Diffusivity ratio d', title='Quadratic activator–inhibitor instability')
ax.legend(loc='upper right', fontsize=8)
ax.grid(alpha=.2)
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-3-turing-region.png', facecolor='white', transparent=False)
