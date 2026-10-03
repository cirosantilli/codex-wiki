"""Logarithmic-potential rotation curve. Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7.
Writes only its PNG basename in the caller's cwd. Caller supplies MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

r = np.linspace(0.02, 5, 250)
fig, ax = plt.subplots(figsize=(6.6, 3.6), dpi=100, facecolor='white')
ax.plot(r, np.ones_like(r), lw=2.5, color='#236e96')
ax.plot(0, 1, 'o', ms=7, mfc='white', mec='#236e96', mew=2, clip_on=False)
ax.set(xlim=(0, 5), ylim=(0, 1.45), xlabel=r'Radius $R/R_*$ (arbitrary reference scale)', ylabel=r'Circular speed $v_c/|v_0|$', title='Singular logarithmic galaxy: flat rotation curve')
ax.text(2.8, 1.08, r'$v_c=|v_0|$ for $R>0$', color='#236e96')
ax.annotate('No orbit at the singular center', xy=(0, 1), xytext=(0.55, 0.45), arrowprops={'arrowstyle':'->', 'color':'#555'}, fontsize=9)
ax.grid(alpha=0.2)
fig.tight_layout()
fig.savefig(Path('paper-59-rotation-curve.png'), facecolor='white', transparent=False)
plt.close(fig)
