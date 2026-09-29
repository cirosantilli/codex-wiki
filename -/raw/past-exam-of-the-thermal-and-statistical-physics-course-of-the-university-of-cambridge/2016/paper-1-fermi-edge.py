#!/usr/bin/env python3
"""Original educational diagram. Tested with Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7. Run from mirrored _media directory; PNG basename goes to cwd.
All plotted parameter choices are illustrative and do not assert provided exam data.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})

e=np.linspace(-7,7,1000);fig,ax=plt.subplots(figsize=(6.8,3.8))
ax.plot([-7,0,0,7],[1,1,0,0],color='.4',ls='--',label='T = 0')
for tr in [.3,.7,1.2]:ax.plot(e,1/(np.exp(e/tr)+1),label='T / Tref = '+str(tr))
ax.set(xlim=(-7,7),ylim=(-.03,1.03),xlabel='(energy - chemical potential) / (kB Tref)',ylabel='Single-state occupation',title='Thermal rounding of a Fermi edge');ax.legend(fontsize=9);ax.grid(alpha=.2);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight')
